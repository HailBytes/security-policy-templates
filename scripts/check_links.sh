#!/usr/bin/env bash
# check_links.sh — Verify that relative markdown links (and image paths) in
# every *.md file resolve to a file that actually exists in the repo.
#
# External links (http/https/mailto) and pure anchors (#section) are skipped;
# this only guards against local links rotting as files are moved or renamed.
#
# Usage: ./scripts/check_links.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

broken=0

while IFS= read -r -d '' file; do
  dir="$(dirname "$file")"

  while IFS= read -r link; do
    target="${link%%#*}"
    [[ -z "$target" ]] && continue

    case "$target" in
      http://*|https://*|mailto:*) continue ;;
    esac

    resolved="$(realpath -m "${dir}/${target}" 2>/dev/null || true)"
    if [[ -z "$resolved" || ! -e "$resolved" ]]; then
      echo "BROKEN: $file -> $link"
      broken=1
    fi
  done < <(grep -oP '(?<=\]\()[^)]+(?=\))' "$file" || true)
done < <(find . -path ./.git -prune -o -name "*.md" -print0)

if [[ $broken -ne 0 ]]; then
  echo "One or more internal markdown links are broken."
  exit 1
fi

echo "All internal markdown links resolve correctly."
