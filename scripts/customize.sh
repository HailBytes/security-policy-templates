#!/usr/bin/env bash
# customize.sh — Replace placeholder values across all policy templates
#
# Usage:
#   ./scripts/customize.sh [OPTIONS]
#
# Options:
#   --company      "Acme Corp"            [Company Name]
#   --date         "2025-01-15"           [Date]           (YYYY-MM-DD)
#   --it-contact   "it@example.com"       [IT Contact]
#   --sec-officer  "Jane Smith, CISO"     [Security Officer]
#   --review-date  "2026-01-15"           [Review Date]    (YYYY-MM-DD)
#   --department   "Information Security" [Department]
#   --industry     "Healthcare"           [Industry]
#   --output-dir   "./customized"         Directory to write customized files to
#                                         (default: overwrites files in place)
#   --dry-run                             Preview replacements without writing files
#   --help                                Show this help message
#
# Examples:
#   # Preview changes without writing:
#   ./scripts/customize.sh --company "Acme Corp" --dry-run
#
#   # Customize all templates and write to ./customized directory:
#   ./scripts/customize.sh \
#     --company "Acme Corp" \
#     --date "2025-01-15" \
#     --it-contact "John Doe / it@acme.com" \
#     --sec-officer "Jane Smith, CISO" \
#     --review-date "2026-01-15" \
#     --department "Information Technology" \
#     --industry "Finance" \
#     --output-dir "./customized"
#
#   # Overwrite files in place (make sure you have a git backup!):
#   ./scripts/customize.sh \
#     --company "Acme Corp" \
#     --date "2025-01-15" \
#     --it-contact "it@acme.com" \
#     --sec-officer "Jane Smith"

set -euo pipefail

# ─── Defaults ────────────────────────────────────────────────────────────────
COMPANY=""
DATE=""
IT_CONTACT=""
SEC_OFFICER=""
REVIEW_DATE=""
DEPARTMENT=""
INDUSTRY=""
OUTPUT_DIR=""
DRY_RUN=false

# ─── Colours ─────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RESET='\033[0m'

# ─── Help ─────────────────────────────────────────────────────────────────────
usage() {
  sed -n '/^# Usage:/,/^[^#]/p' "$0" | grep '^#' | sed 's/^# \?//'
  exit 0
}

# ─── Argument parsing ────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --company)      COMPANY="$2";      shift 2 ;;
    --date)         DATE="$2";         shift 2 ;;
    --it-contact)   IT_CONTACT="$2";   shift 2 ;;
    --sec-officer)  SEC_OFFICER="$2";  shift 2 ;;
    --review-date)  REVIEW_DATE="$2";  shift 2 ;;
    --department)   DEPARTMENT="$2";   shift 2 ;;
    --industry)     INDUSTRY="$2";     shift 2 ;;
    --output-dir)   OUTPUT_DIR="$2";   shift 2 ;;
    --dry-run)      DRY_RUN=true;      shift   ;;
    --help|-h)      usage ;;
    *) echo -e "${RED}Unknown option: $1${RESET}" >&2; usage ;;
  esac
done

# ─── Locate repo root ─────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# ─── Validate inputs ─────────────────────────────────────────────────────────
if [[ -z "$COMPANY" && -z "$DATE" && -z "$IT_CONTACT" && -z "$SEC_OFFICER" && \
      -z "$REVIEW_DATE" && -z "$DEPARTMENT" && -z "$INDUSTRY" ]]; then
  echo -e "${YELLOW}Warning: No replacement values provided. Nothing to do.${RESET}"
  echo "Run with --help to see usage."
  exit 0
fi

# Validate date format if provided
validate_date() {
  local val="$1" label="$2"
  if [[ -n "$val" ]] && ! [[ "$val" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    echo -e "${RED}Error: $label must be in YYYY-MM-DD format (got: '$val')${RESET}" >&2
    exit 1
  fi
}
validate_date "$DATE" "--date"
validate_date "$REVIEW_DATE" "--review-date"

# ─── Find target files ───────────────────────────────────────────────────────
# All markdown files in policies/, templates/, industry-variants/, and docs/
mapfile -t TARGET_FILES < <(find "${REPO_ROOT}/policies" \
                                  "${REPO_ROOT}/templates" \
                                  "${REPO_ROOT}/industry-variants" \
                                  "${REPO_ROOT}/docs" \
                              -name "*.md" 2>/dev/null | sort)

if [[ ${#TARGET_FILES[@]} -eq 0 ]]; then
  echo -e "${RED}Error: No markdown files found under ${REPO_ROOT}${RESET}" >&2
  exit 1
fi

echo -e "${CYAN}Security Policy Template Customizer${RESET}"
echo -e "${CYAN}=====================================${RESET}"
echo ""
echo "Repository root : ${REPO_ROOT}"
echo "Files to process: ${#TARGET_FILES[@]}"
[[ -n "$OUTPUT_DIR" ]] && echo "Output directory: ${OUTPUT_DIR}"
$DRY_RUN && echo -e "${YELLOW}DRY RUN — no files will be modified${RESET}"
echo ""

# ─── Build sed expression ────────────────────────────────────────────────────
# Each substitution replaces the placeholder literally (not a regex)
build_sed_args() {
  local args=()

  # Helper: escape special sed characters in replacement string
  escape_replace() {
    printf '%s' "$1" | sed 's/[&/\]/\\&/g'
  }

  [[ -n "$COMPANY" ]]     && args+=(-e "s/\[Company Name\]/$(escape_replace "$COMPANY")/g")
  [[ -n "$DATE" ]]        && args+=(-e "s/\[Date\]/$(escape_replace "$DATE")/g")
  [[ -n "$IT_CONTACT" ]]  && args+=(-e "s/\[IT Contact\]/$(escape_replace "$IT_CONTACT")/g")
  [[ -n "$SEC_OFFICER" ]] && args+=(-e "s/\[Security Officer\]/$(escape_replace "$SEC_OFFICER")/g")
  [[ -n "$REVIEW_DATE" ]] && args+=(-e "s/\[Review Date\]/$(escape_replace "$REVIEW_DATE")/g")
  [[ -n "$DEPARTMENT" ]]  && args+=(-e "s/\[Department\]/$(escape_replace "$DEPARTMENT")/g")
  [[ -n "$INDUSTRY" ]]    && args+=(-e "s/\[Industry\]/$(escape_replace "$INDUSTRY")/g")

  printf '%s\n' "${args[@]}"
}

# Read sed args into array
mapfile -t SED_ARGS < <(build_sed_args)

if [[ ${#SED_ARGS[@]} -eq 0 ]]; then
  echo -e "${YELLOW}No valid replacements configured. Exiting.${RESET}"
  exit 0
fi

echo "Replacements configured:"
[[ -n "$COMPANY" ]]     && echo "  [Company Name]     → $COMPANY"
[[ -n "$DATE" ]]        && echo "  [Date]             → $DATE"
[[ -n "$IT_CONTACT" ]]  && echo "  [IT Contact]       → $IT_CONTACT"
[[ -n "$SEC_OFFICER" ]] && echo "  [Security Officer] → $SEC_OFFICER"
[[ -n "$REVIEW_DATE" ]] && echo "  [Review Date]      → $REVIEW_DATE"
[[ -n "$DEPARTMENT" ]]  && echo "  [Department]       → $DEPARTMENT"
[[ -n "$INDUSTRY" ]]    && echo "  [Industry]         → $INDUSTRY"
echo ""

# ─── Setup output directory ──────────────────────────────────────────────────
if [[ -n "$OUTPUT_DIR" ]]; then
  if $DRY_RUN; then
    echo -e "${YELLOW}[DRY RUN] Would create output directory: ${OUTPUT_DIR}${RESET}"
  else
    mkdir -p "$OUTPUT_DIR"
    echo -e "${GREEN}Output directory created: ${OUTPUT_DIR}${RESET}"
  fi
fi

# ─── Process files ───────────────────────────────────────────────────────────
MODIFIED_COUNT=0
SKIPPED_COUNT=0

for src_file in "${TARGET_FILES[@]}"; do
  rel_path="${src_file#${REPO_ROOT}/}"

  # Check if file contains any of our placeholders
  if ! grep -qE '\[(Company Name|Date|IT Contact|Security Officer|Review Date|Department|Industry)\]' "$src_file" 2>/dev/null; then
    $DRY_RUN && echo "  [skip] $rel_path (no placeholders found)"
    (( SKIPPED_COUNT++ )) || true
    continue
  fi

  if $DRY_RUN; then
    echo -e "  ${CYAN}[would modify]${RESET} $rel_path"
    # Show a preview of what would change
    sed "${SED_ARGS[@]}" "$src_file" | diff --color=never - "$src_file" | grep '^[<>]' | head -10 | \
      sed 's/^< /    + /;s/^> /    - /' || true
    (( MODIFIED_COUNT++ )) || true
    continue
  fi

  if [[ -n "$OUTPUT_DIR" ]]; then
    # Preserve directory structure under output dir
    out_file="${OUTPUT_DIR}/${rel_path}"
    mkdir -p "$(dirname "$out_file")"
    sed "${SED_ARGS[@]}" "$src_file" > "$out_file"
    echo -e "  ${GREEN}[written]${RESET} ${out_file#${REPO_ROOT}/}"
  else
    # Overwrite in place
    # Use a temp file for safety
    tmp_file="$(mktemp)"
    sed "${SED_ARGS[@]}" "$src_file" > "$tmp_file"
    mv "$tmp_file" "$src_file"
    echo -e "  ${GREEN}[modified]${RESET} $rel_path"
  fi

  (( MODIFIED_COUNT++ )) || true
done

# ─── Summary ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${CYAN}─────────────────────────────────────${RESET}"
if $DRY_RUN; then
  echo -e "${YELLOW}DRY RUN complete.${RESET}"
  echo "  Files that would be modified : $MODIFIED_COUNT"
  echo "  Files skipped (no placeholders): $SKIPPED_COUNT"
  echo ""
  echo "Run without --dry-run to apply changes."
else
  echo -e "${GREEN}Customization complete.${RESET}"
  echo "  Files modified : $MODIFIED_COUNT"
  echo "  Files skipped  : $SKIPPED_COUNT"
  if [[ -n "$OUTPUT_DIR" ]]; then
    echo "  Output written to: ${OUTPUT_DIR}"
  fi
  echo ""
  echo -e "${YELLOW}Tip: Review changes with 'git diff' before committing.${RESET}"
fi

# ─── Check for remaining placeholders ────────────────────────────────────────
if ! $DRY_RUN; then
  REMAINING_DIRS=("${REPO_ROOT}/policies" "${REPO_ROOT}/templates" "${REPO_ROOT}/industry-variants")
  [[ -n "$OUTPUT_DIR" ]] && REMAINING_DIRS=("$OUTPUT_DIR")

  remaining=$(grep -rn --include="*.md" \
    -E '\[(Company Name|Date|IT Contact|Security Officer|Review Date|Department|Industry)\]' \
    "${REMAINING_DIRS[@]}" 2>/dev/null || true)

  if [[ -n "$remaining" ]]; then
    echo ""
    echo -e "${YELLOW}Note: Some placeholders remain (values not provided for these):${RESET}"
    echo "$remaining" | head -20 | sed "s|${REPO_ROOT}/||"
    remaining_count=$(echo "$remaining" | wc -l)
    [[ $remaining_count -gt 20 ]] && echo "  ... and $((remaining_count - 20)) more"
  else
    echo -e "${GREEN}All known placeholders have been replaced.${RESET}"
  fi
fi
