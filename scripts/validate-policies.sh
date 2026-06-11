#!/usr/bin/env bash
# validate-policies.sh — Check policy files for required structure and content
#
# Exits 0 if all checks pass, 1 if any check fails.
# Usage: ./scripts/validate-policies.sh [--verbose]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

VERBOSE=false
[[ "${1:-}" == "--verbose" ]] && VERBOSE=true

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RESET='\033[0m'

ERRORS=0
WARNINGS=0
FILES_CHECKED=0

log_error()   { echo -e "${RED}  [FAIL]${RESET} $*"; (( ERRORS++ ))   || true; }
log_warn()    { echo -e "${YELLOW}  [WARN]${RESET} $*"; (( WARNINGS++ )) || true; }
log_ok()      { $VERBOSE && echo -e "${GREEN}  [ OK ]${RESET} $*"; }
log_section() { echo -e "\n${CYAN}▸ $*${RESET}"; }

# ─── Required sections every policy must contain ─────────────────────────────
# Each entry is a pipe-separated list of acceptable alternatives (any one suffices).
REQUIRED_SECTIONS=(
  "## Purpose"
  "## Scope"
  "## Enforcement|## Compliance"
  "## References"
  "## Version History"
)

# ─── Collect policy files ────────────────────────────────────────────────────
mapfile -t POLICY_FILES < <(find "${REPO_ROOT}/policies" -name "*.md" | sort)

if [[ ${#POLICY_FILES[@]} -eq 0 ]]; then
  echo -e "${RED}Error: No policy files found under ${REPO_ROOT}/policies${RESET}" >&2
  exit 1
fi

# ─── Check 1: Required sections ──────────────────────────────────────────────
log_section "Checking required sections (${#POLICY_FILES[@]} files)"

has_any_section() {
  local file="$1" candidates="$2"
  IFS='|' read -ra alts <<< "$candidates"
  for alt in "${alts[@]}"; do
    grep -q "^${alt}" "$file" && return 0
  done
  return 1
}

for f in "${POLICY_FILES[@]}"; do
  rel="${f#${REPO_ROOT}/}"
  missing=()
  for section in "${REQUIRED_SECTIONS[@]}"; do
    if ! has_any_section "$f" "$section"; then
      # Use first alternative as the display name
      missing+=("${section%%|*}")
    fi
  done
  if [[ ${#missing[@]} -gt 0 ]]; then
    log_error "${rel}: missing sections: ${missing[*]}"
  else
    log_ok "${rel}: all required sections present"
  fi
  (( FILES_CHECKED++ )) || true
done

# ─── Check 2: NIST CSF citations ─────────────────────────────────────────────
log_section "Checking NIST CSF citations"

for f in "${POLICY_FILES[@]}"; do
  rel="${f#${REPO_ROOT}/}"
  if ! grep -qE '\*\(NIST CSF:' "$f"; then
    log_error "${rel}: no NIST CSF citations found (expected at least one '*(NIST CSF: XX.XX-X)*')"
  else
    citation_count=$(grep -cE '\*\(NIST CSF:' "$f" || true)
    log_ok "${rel}: ${citation_count} NIST CSF citation(s)"
  fi
done

# ─── Check 3: Version History table ──────────────────────────────────────────
log_section "Checking Version History table format"

for f in "${POLICY_FILES[@]}"; do
  rel="${f#${REPO_ROOT}/}"
  if grep -q "^## Version History" "$f"; then
    # Must have a markdown table with Version/Date/Author/Changes headers
    if ! grep -qE '^\| *Version *\|' "$f"; then
      log_error "${rel}: Version History section exists but has no table"
    else
      log_ok "${rel}: Version History table present"
    fi
  fi
done

# ─── Check 4: NIST CSF function declared in header ───────────────────────────
log_section "Checking NIST CSF function header"

for f in "${POLICY_FILES[@]}"; do
  rel="${f#${REPO_ROOT}/}"
  # Expect a line like: **NIST CSF Functions: ...**
  if ! grep -qE '^\*\*NIST CSF Functions?' "$f"; then
    log_warn "${rel}: no '**NIST CSF Functions:**' header line found"
  else
    log_ok "${rel}: NIST CSF function header present"
  fi
done

# ─── Check 5: customize.sh smoke test ────────────────────────────────────────
log_section "Smoke-testing scripts/customize.sh (--dry-run)"

CUSTOMIZE="${REPO_ROOT}/scripts/customize.sh"
if [[ ! -x "$CUSTOMIZE" ]]; then
  log_error "scripts/customize.sh is not executable"
else
  if bash "$CUSTOMIZE" \
      --company "Test Corp" \
      --date "2025-01-01" \
      --it-contact "it@test.com" \
      --sec-officer "Jane Smith" \
      --review-date "2026-01-01" \
      --department "IT" \
      --industry "Technology" \
      --dry-run > /dev/null 2>&1; then
    log_ok "customize.sh --dry-run exited successfully"
  else
    log_error "customize.sh --dry-run failed (exit code $?)"
  fi
fi

# ─── Check 6: Broken internal markdown links ─────────────────────────────────
log_section "Checking internal links"

ALL_MD_FILES=()
while IFS= read -r -d '' file; do
  ALL_MD_FILES+=("$file")
done < <(find "${REPO_ROOT}" -name "*.md" -not -path "*/.git/*" -print0 | sort -z)

for f in "${POLICY_FILES[@]}"; do
  rel="${f#${REPO_ROOT}/}"
  base_dir="$(dirname "$f")"

  # Extract markdown links of the form [text](../some/path.md) — local refs only
  while IFS= read -r link; do
    # Resolve relative to the file's directory
    target="${base_dir}/${link}"
    # Normalise (resolve ../ etc.)
    resolved="$(cd "${base_dir}" && realpath -m "${link}" 2>/dev/null || true)"
    if [[ -n "$resolved" && ! -e "$resolved" ]]; then
      log_warn "${rel}: broken internal link → ${link}"
    fi
  done < <(grep -oE '\]\([^)#]+\.md[^)]*\)' "$f" 2>/dev/null | sed 's/^](\(.*\))$/\1/' || true)
done

# ─── Summary ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${CYAN}─────────────────────────────────────${RESET}"
echo "Files checked : ${FILES_CHECKED}"
echo "Errors        : ${ERRORS}"
echo "Warnings      : ${WARNINGS}"

if [[ $ERRORS -gt 0 ]]; then
  echo -e "\n${RED}Validation FAILED — ${ERRORS} error(s) must be fixed.${RESET}"
  exit 1
elif [[ $WARNINGS -gt 0 ]]; then
  echo -e "\n${YELLOW}Validation passed with ${WARNINGS} warning(s).${RESET}"
  exit 0
else
  echo -e "\n${GREEN}All checks passed.${RESET}"
  exit 0
fi
