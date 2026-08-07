#!/usr/bin/env python3
"""Migrate security-policy-templates from NIST CSF v1.1 codes to v2.0.

Addresses issues #53, #58, #55, #59, #46. Runs in-place with a dry-run
option. Uses the official NIST CSF 1.1→2.0 subcategory mapping."""

import sys, os, re, json

# --- CSF 1.1 → 2.0 category-level mapping (for References lines) ---
CATEGORY_MAP = {
    # ID.GV → GV (Govern) — split into policy, risk, oversight
    'ID.GV': 'GV.PO',
    # ID.SC → GV.SC (supply chain moved to Govern)
    'ID.SC': 'GV.SC',
    # ID.BE → GV.OC (business environment → organizational context)
    'ID.BE': 'GV.OC',
    # PR.AC → PR.AA (access control → identity management/auth/access)
    'PR.AC': 'PR.AA',
    # PR.IP → PR.PS (information protection → platform security)
    'PR.IP': 'PR.PS',
    # PR.PT → PR.PS (protective technology → platform security; some → PR.AA)
    'PR.PT': 'PR.PS',
    # PR.MA → PR.IR (maintenance → infrastructure resilience)
    'PR.MA': 'PR.IR',
    # RS.RP / RS.AN / RS.MI → RS.MA (response planning/analysis → incident mgmt)
    'RS.RP': 'RS.MA',
    'RS.AN': 'RS.MA',
    'RS.MI': 'RS.MA',
    # RC.IM (author typo) → ID.IM (Improvement)
    'RC.IM': 'ID.IM',
}

# --- CSF 1.1 → 2.0 subcategory code mapping (for inline citations) ---
# Source: NIST CSWP 29 (CSF 2.0, Feb 2024) subcategory mapping notes.
SUBCATEGORY_MAP = {
    # ID.GV (governance) → GV
    'ID.GV-01': 'GV.PO-01',   # policy established
    'ID.GV-02': 'GV.RR-02',   # roles/authorities determined
    'ID.GV-03': 'GV.OC-03',   # legal/regulatory understood
    'ID.GV-04': 'GV.RM-03',   # risk mgmt integrated
    'ID.GV-1': 'GV.PO-01',
    'ID.GV-2': 'GV.RR-02',
    'ID.GV-3': 'GV.OC-03',
    'ID.GV-4': 'GV.RM-03',
    # ID.BE → GV.OC (organizational context)
    'ID.BE-01': 'GV.OC-05',
    'ID.BE-02': 'GV.OC-01',
    'ID.BE-03': 'GV.OC-01',
    'ID.BE-04': 'GV.OC-04',
    'ID.BE-05': 'GV.OC-04',
    'ID.BE-1': 'GV.OC-05',
    'ID.BE-2': 'GV.OC-01',
    'ID.BE-3': 'GV.OC-01',
    'ID.BE-4': 'GV.OC-04',
    'ID.BE-5': 'GV.OC-04',
    # ID.SC → GV.SC (supply chain → Govern)
    'ID.SC-01': 'GV.SC-01',
    'ID.SC-02': 'GV.SC-03',
    'ID.SC-03': 'GV.SC-05',
    'ID.SC-04': 'GV.SC-07',
    'ID.SC-05': 'GV.SC-08',
    'ID.SC-1': 'GV.SC-01',
    'ID.SC-2': 'GV.SC-03',
    'ID.SC-3': 'GV.SC-05',
    'ID.SC-4': 'GV.SC-07',
    'ID.SC-5': 'GV.SC-08',
    # PR.AC → PR.AA (identity/access)
    'PR.AC-01': 'PR.AA-01',
    'PR.AC-02': 'PR.AA-06',
    'PR.AC-03': 'PR.AA-03',
    'PR.AC-04': 'PR.AA-05',
    'PR.AC-05': 'PR.IR-01',
    'PR.AC-06': 'PR.AA-02',
    'PR.AC-07': 'PR.AA-03',
    'PR.AC-1': 'PR.AA-01',
    'PR.AC-2': 'PR.AA-06',
    'PR.AC-3': 'PR.AA-03',
    'PR.AC-4': 'PR.AA-05',
    'PR.AC-5': 'PR.IR-01',
    'PR.AC-6': 'PR.AA-02',
    'PR.AC-7': 'PR.AA-03',
    # PR.IP → PR.PS / PR.DS / PR.IR / GV / ID / RS / RC / GV.RR
    'PR.IP-01': 'PR.PS-01',   # baseline configuration
    'PR.IP-02': 'PR.PS-02',   # development lifecycle → software maintenance
    'PR.IP-03': 'PR.PS-01',   # config change control → configuration mgmt
    'PR.IP-04': 'PR.DS-11',   # backups → data security (backups)
    'PR.IP-05': 'PR.IR-02',   # physical environment → environmental protection
    'PR.IP-06': 'PR.DS-09',   # data destruction → data security
    'PR.IP-07': 'PR.PS-04',   # protection processes → log records
    'PR.IP-08': 'PR.PS-05',   # effectiveness testing → unauthorized software
    'PR.IP-09': 'RS.MA-01',   # response plans → incident mgmt
    'PR.IP-10': 'ID.IM-02',   # recovery plans → improvement
    'PR.IP-11': 'GV.RR-04',   # cyber safety/HR → roles/responsibilities
    'PR.IP-12': 'ID.RA-01',   # vulnerability mgmt → risk assessment
    'PR.IP-1': 'PR.PS-01',
    'PR.IP-2': 'PR.PS-02',
    'PR.IP-3': 'PR.PS-01',
    'PR.IP-4': 'PR.DS-11',
    'PR.IP-5': 'PR.IR-02',
    'PR.IP-6': 'PR.DS-09',
    'PR.IP-7': 'PR.PS-04',
    'PR.IP-8': 'PR.PS-05',
    'PR.IP-9': 'RS.MA-01',
    'PR.IP-10': 'ID.IM-02',
    'PR.IP-11': 'GV.RR-04',
    'PR.IP-12': 'ID.RA-01',
    # PR.PT → PR.PS / PR.DS / PR.AA / PR.IR
    'PR.PT-01': 'PR.PS-04',   # audit logs → log records
    'PR.PT-02': 'PR.DS-01',   # data in transit → data-at-rest/in-transit protection
    'PR.PT-03': 'PR.PS-01',   # hardware → configuration mgmt
    'PR.PT-04': 'PR.AA-07',   # remote access → identity/access
    'PR.PT-05': 'PR.IR-04',   # maintenance → resilience
    'PR.PT-1': 'PR.PS-04',
    'PR.PT-2': 'PR.DS-01',
    'PR.PT-3': 'PR.PS-01',
    'PR.PT-4': 'PR.AA-07',
    'PR.PT-5': 'PR.IR-04',
    # PR.MA → PR.PS / ID.AM
    'PR.MA-01': 'PR.PS-03',   # maintenance → hardware maintenance
    'PR.MA-02': 'PR.PS-02',   # remote maintenance → software maintenance
    'PR.MA-1': 'PR.PS-03',
    'PR.MA-2': 'PR.PS-02',
    # DE.AE / DE.CM subcategory renumbering + merges (verified from CSWP 29)
    'DE.AE-1': 'DE.AE-01',   # survives
    'DE.AE-2': 'DE.AE-02',   # survives
    'DE.AE-3': 'DE.AE-03',   # survives
    'DE.AE-4': 'DE.AE-04',   # survives
    'DE.AE-5': 'DE.AE-08',   # → declared incident criteria
    'DE.AE-6': 'DE.AE-06',   # survives (formerly DE.DP-04)
    'DE.CM-1': 'DE.CM-01',   # survives
    'DE.CM-2': 'DE.CM-02',   # survives
    'DE.CM-3': 'DE.CM-01',   # merged into network monitoring
    'DE.CM-4': 'DE.CM-09',   # merged into computing monitoring
    'DE.CM-5': 'DE.CM-09',   # merged into computing monitoring
    'DE.CM-6': 'DE.CM-06',   # survives (formerly DE.CM-07 partial)
    'DE.CM-7': 'DE.CM-01',   # merged
    'DE.CM-8': 'ID.RA-01',   # moved to risk assessment
    'DE.DP-4': 'DE.AE-06',   # moved to anomaly events
    # RS.RP → RS.MA (response planning → incident management)
    'RS.RP-1': 'RS.MA-01',
    'RS.RP-01': 'RS.MA-01',
    'RS.MI-1': 'RS.MA-01',   # RS.MI (mishandled variant) → incident mgmt
    'RS.MI-2': 'RS.MA-02',
    'RS.MI-3': 'RS.MA-03',
    'RS.MI-01': 'RS.MA-01',
    'RS.MI-02': 'RS.MA-02',
    'RS.MI-03': 'RS.MA-03',
    # RS.AN → RS.MA / ID.RA (analysis merged into incident mgmt)
    'RS.AN-1': 'RS.MA-02',
    'RS.AN-2': 'RS.MA-03',
    'RS.AN-3': 'RS.MA-03',
    'RS.AN-4': 'RS.MA-03',
    'RS.AN-5': 'ID.RA-08',
    'RS.AN-01': 'RS.MA-02',
    'RS.AN-02': 'RS.MA-03',
    'RS.AN-03': 'RS.MA-03',
    'RS.AN-04': 'RS.MA-03',
    'RS.AN-05': 'ID.RA-08',
    # RS.CO → PR.AT / RS.CO (survivors) / RS.MA
    'RS.CO-1': 'PR.AT-01',
    'RS.CO-2': 'RS.CO-02',
    'RS.CO-3': 'RS.CO-03',
    'RS.CO-4': 'RS.MA-04',
    'RS.CO-01': 'PR.AT-01',
    'RS.CO-02': 'RS.CO-02',
    'RS.CO-03': 'RS.CO-03',
    'RS.CO-04': 'RS.MA-04',
    # RC.RP/RC.CO survive; pad single digits
    'RC.RP-1': 'RC.RP-01',
    'RC.RP-2': 'RC.RP-02',
    'RC.RP-3': 'RC.RP-03',
    'RC.RP-4': 'RC.RP-04',
    'RC.RP-5': 'RC.RP-05',
    'RC.CO-1': 'RC.CO-01',
    'RC.CO-2': 'RC.CO-02',
    'RC.CO-3': 'RC.CO-03',
    # ID.RA / ID.AM / PR.DS / PR.AT / PR.IR / GV.* / DE.AE / DE.CM zero-pad
    'ID.AM-1': 'ID.AM-01', 'ID.AM-2': 'ID.AM-02', 'ID.AM-3': 'ID.AM-03',
    'ID.AM-4': 'ID.AM-04', 'ID.AM-5': 'ID.AM-05', 'ID.AM-6': 'ID.AM-06',
    'ID.AM-7': 'ID.AM-07', 'ID.AM-8': 'ID.AM-08',
    'ID.RA-1': 'ID.RA-01', 'ID.RA-2': 'ID.RA-02', 'ID.RA-3': 'ID.RA-03',
    'ID.RA-4': 'ID.RA-04', 'ID.RA-5': 'ID.RA-05', 'ID.RA-6': 'ID.RA-06',
    'PR.DS-1': 'PR.DS-01', 'PR.DS-2': 'PR.DS-02', 'PR.DS-3': 'PR.DS-03',
    'PR.DS-4': 'PR.DS-04', 'PR.DS-5': 'PR.DS-05', 'PR.DS-6': 'PR.DS-06',
    'PR.DS-7': 'PR.DS-07', 'PR.DS-8': 'PR.DS-08', 'PR.DS-9': 'PR.DS-09',
    'PR.DS-10': 'PR.DS-10', 'PR.DS-11': 'PR.DS-11',
    'PR.AT-1': 'PR.AT-01', 'PR.AT-2': 'PR.AT-02', 'PR.AT-3': 'PR.AT-03',
    'PR.AT-4': 'PR.AT-04', 'PR.AT-5': 'PR.AT-05',
    'PR.AA-1': 'PR.AA-01', 'PR.AA-2': 'PR.AA-02', 'PR.AA-3': 'PR.AA-03',
    'PR.AA-4': 'PR.AA-04', 'PR.AA-5': 'PR.AA-05', 'PR.AA-6': 'PR.AA-06',
    'PR.AA-7': 'PR.AA-07',
    'PR.PS-1': 'PR.PS-01', 'PR.PS-2': 'PR.PS-02', 'PR.PS-3': 'PR.PS-03',
    'PR.PS-4': 'PR.PS-04', 'PR.PS-5': 'PR.PS-05', 'PR.PS-6': 'PR.PS-06',
    'PR.IR-1': 'PR.IR-01', 'PR.IR-2': 'PR.IR-02', 'PR.IR-3': 'PR.IR-03',
    'PR.IR-4': 'PR.IR-04',
    'GV.OC-1': 'GV.OC-01', 'GV.OC-2': 'GV.OC-02', 'GV.OC-3': 'GV.OC-03',
    'GV.OC-4': 'GV.OC-04', 'GV.OC-5': 'GV.OC-05',
    'GV.RM-1': 'GV.RM-01', 'GV.RM-2': 'GV.RM-02', 'GV.RM-3': 'GV.RM-03',
    'GV.RM-4': 'GV.RM-04', 'GV.RM-5': 'GV.RM-05', 'GV.RM-6': 'GV.RM-06',
    'GV.PO-1': 'GV.PO-01', 'GV.PO-2': 'GV.PO-02', 'GV.PO-3': 'GV.PO-03',
    'GV.SC-1': 'GV.SC-01', 'GV.SC-2': 'GV.SC-02', 'GV.SC-3': 'GV.SC-03',
    'GV.SC-4': 'GV.SC-04', 'GV.SC-5': 'GV.SC-05', 'GV.SC-6': 'GV.SC-06',
    'GV.SC-7': 'GV.SC-07', 'GV.SC-8': 'GV.SC-08', 'GV.SC-9': 'GV.SC-09',
    'GV.SC-10': 'GV.SC-10',
    'GV.RR-1': 'GV.RR-01', 'GV.RR-2': 'GV.RR-02', 'GV.RR-3': 'GV.RR-03',
    'GV.RR-4': 'GV.RR-04',
    'DE.AE-01': 'DE.AE-01', 'DE.AE-02': 'DE.AE-02', 'DE.AE-03': 'DE.AE-03',
    'DE.CM-01': 'DE.CM-01', 'DE.CM-02': 'DE.CM-02', 'DE.CM-06': 'DE.CM-06',
    'DE.CM-09': 'DE.CM-09',
    # RC.IM / RS.IM are author typos for ID.IM (Improvement) / RS.MA
    'RC.IM-1': 'ID.IM-01',
    'RC.IM-2': 'ID.IM-01',
    'RC.IM-01': 'ID.IM-01',
    'RC.IM-02': 'ID.IM-01',
    'RS.IM-1': 'RS.MA-01',
    'RS.IM-2': 'RS.MA-02',
    'RS.IM-01': 'RS.MA-01',
    'RS.IM-02': 'RS.MA-02',
    # Bare category codes (References lines)
    'RS.RP': 'RS.MA',
    'RS.AN': 'RS.MA',
    'RS.MI': 'RS.MA',
    'RS.IM': 'RS.MA',
    'RC.IM': 'ID.IM',
    # Category-level fallbacks (References lines)
    'ID.GV': 'GV.PO',
    'ID.SC': 'GV.SC',
    'ID.BE': 'GV.OC',
    'PR.AC': 'PR.AA',
    'PR.IP': 'PR.PS',
    'PR.PT': 'PR.PS',
    'PR.MA': 'PR.IR',
}

# Sort by length descending so specific subcategory matches happen before
# generic category-level matches (e.g. PR.AC-01 before PR.AC).
SUBCATEGORY_KEYS = sorted(SUBCATEGORY_MAP.keys(), key=len, reverse=True)

def migrate_file(path, dry_run=True):
    """Apply CSF 1.1→2.0 migrations to a single file."""
    with open(path) as f:
        content = f.read()
    original = content

    # 1. Replace "NIST CSF v1.1" → "NIST CSF 2.0"
    content = content.replace('NIST CSF v1.1', 'NIST CSF 2.0')

    # 2. Replace category-level codes in References lines (the bulk of #53)
    #    Match patterns like "PR.AC (Access Control)" or "PR.AC-1, PR.AT-2"
    #    We do subcategory codes first (longer matches), then category codes.
    #
    # Strategy: replace all known CSF 1.1 codes with their 2.0 equivalents.
    # Use word-boundary matching to avoid partial replacements.
    for old_code in SUBCATEGORY_KEYS:
        new_code = SUBCATEGORY_MAP[old_code]
        # Escape the code for regex (contains dots and dashes, no regex specials)
        # Match only whole codes (preceded by start/space/paren/comma/colon, followed by end/space/comma/paren/newline/dash/dot)
        content = re.sub(
            r'(?<![a-zA-Z0-9])' + re.escape(old_code) + r'(?![a-zA-Z0-9-])',
            new_code,
            content,
        )

    # 3. Fix function-level headers (e.g. "## PROTECT (PR)" → fine, PR is still PR)
    #    But the function descriptor line "**NIST CSF Functions: Protect (PR), Detect (DE)**" — fine

    # 4. Dedupe consecutive duplicate category codes in References lines
    #    (e.g. RS.MA, RS.MA, RS.MA after RS.RP/RS.AN/RS.MI all map to RS.MA)
    content = re.sub(r'((?:[A-Z]{2}\.[A-Z]{2}), )(\1)+', r'\1', content)

    # 4. Fix mapping file specific: ID.SC section header → GV.SC
    content = content.replace('### ID.SC — Supply Chain Risk Management', '### GV.SC — Supply Chain Risk Management')
    content = content.replace('### PR.IP — Information Protection Processes and Procedures', '### PR.PS — Platform Security')
    content = content.replace('### PR.IP — Information Protection', '### PR.PS — Platform Security')

    if content == original:
        return False

    if dry_run:
        changes = []
        for i, (old, new) in enumerate(zip(original.split('\n'), content.split('\n'))):
            if old != new:
                changes.append(f'  L{i+1}: -{old}')
                changes.append(f'        +{new}')
        if changes:
            print(f'{path}:')
            for c in changes[:20]:
                print(c)
            if len(changes) > 20:
                print(f'  ... ({len(changes)} line changes total)')
        return True
    else:
        with open(path, 'w') as f:
            f.write(content)
        return True


def main():
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    if dry_run:
        print('=== DRY RUN — no files will be modified ===')

    # Find all policy files
    policy_files = []
    for root, dirs, files in os.walk('policies'):
        for f in sorted(files):
            if f.endswith('.md'):
                policy_files.append(os.path.join(root, f))

    # Also fix CONTRIBUTING.md, docs/framework_mapping.md, mappings/nist-csf.md
    extra_files = ['CONTRIBUTING.md', 'docs/framework_mapping.md', 'mappings/nist-csf.md']

    all_files = sorted(policy_files) + [f for f in extra_files if os.path.exists(f)]

    changed = 0
    for path in all_files:
        if migrate_file(path, dry_run=dry_run):
            changed += 1

    print(f'\n{changed}/{len(all_files)} files would be modified' if dry_run else f'\n{changed}/{len(all_files)} files modified')

    if not dry_run:
        # Also fix customize.sh flags (#46)
        fix_customize_sh(dry_run=dry_run)
        # Fix framework_mapping.md header (#55)
        fix_framework_mapping_header(dry_run=dry_run)


def fix_customize_sh(dry_run=True):
    """Remove the dead --department flag from customize.sh (#46).

    Note: --review-date is KEPT — 5 templates (incident forms, checklists,
    training outline) use [Review Date]. Only [Department] has zero uses.
    """
    path = 'scripts/customize.sh'
    if not os.path.exists(path):
        return
    with open(path) as f:
        content = f.read()
    original = content

    # Remove --department flag only (not --review-date)
    content = re.sub(r'#   --department[^\n]*\n?', '', content)
    content = re.sub(r'#     --department[^\n]*\n?', '', content)
    content = re.sub(r'--department\)[^\n]*\n?', '', content)
    # Remove DEPARTMENT var init, validation refs, sed substitution, summary echo
    content = re.sub(r'^DEPARTMENT=""\n', '', content)
    content = re.sub(r'-z "\$DEPARTMENT" && \\\n', '', content)
    content = re.sub(r'\[\[ -n "\$DEPARTMENT" \]\][^\n]*\n?', '', content)

    # Clean up blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original and not dry_run:
        with open(path, 'w') as f:
            f.write(content)
        print(f'Updated {path}')


def fix_framework_mapping_header(dry_run=True):
    """Update framework_mapping.md header to acknowledge CSF 2.0 (#55)."""
    path = 'docs/framework_mapping.md'
    if not os.path.exists(path):
        return
    with open(path) as f:
        content = f.read()
    original = content

    content = content.replace(
        '**NIST CSF v1.1** — NIST Cybersecurity Framework (already embedded in each template)',
        '**NIST CSF 2.0** — NIST Cybersecurity Framework (already embedded in each template)',
    )

    if content != original and not dry_run:
        with open(path, 'w') as f:
            f.write(content)
        print(f'Updated {path}')


if __name__ == '__main__':
    main()