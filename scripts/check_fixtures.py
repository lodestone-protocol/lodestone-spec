#!/usr/bin/env python3
"""Golden Fixture corpus integrity check (P3-T1).

Asserts, from the lodestone-spec repository root:
  (a) every fixtures/*.md has a matching fixtures/*.json and vice versa
      (MANIFEST.md itself is not a fixture);
  (b) the number of MANIFEST.md table rows equals the number of fixture
      groups (one .md + one .json per group);
  (c) the "N/14" coverage figure declared at the bottom of MANIFEST.md
      equals the number of distinct diagnostic codes actually exercised by
      the corpus (the canonical 14 codes of spec/v1.3.md §11 / registry).
Exit code 0 when all assertions hold; 1 otherwise.
"""

import json
import os
import re
import sys

CANONICAL_CODES = {
    "E-MISSING-ID", "E-META-SYNTAX", "E-META-FIELD", "E-DUP-ID",
    "E-REF-NOT-FOUND", "E-CYCLE", "W-VERSION-MISMATCH", "W-DOC-META",
    "W-CYCLE-DECLARED", "W-REDUNDANT-EDGE", "W-META-PLACEMENT",
    "W-REDUNDANT-META", "W-UPSTREAM-PENDING", "W-NFC-VIOLATION",
}

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
FIX = os.path.join(ROOT, "fixtures")
MANIFEST = os.path.join(FIX, "MANIFEST.md")
ERRORS = []


def err(msg: str) -> None:
    ERRORS.append(msg)


def main() -> int:
    if not os.path.isdir(FIX):
        err(f"fixtures/ directory missing under {ROOT}")
        return 1

    mds = sorted(f for f in os.listdir(FIX) if f.endswith(".md") and f != "MANIFEST.md")
    jsons = sorted(f for f in os.listdir(FIX) if f.endswith(".json"))
    md_stems = {os.path.splitext(f)[0] for f in mds}
    json_stems = {os.path.splitext(f)[0] for f in jsons}

    # (a) pairwise completeness in both directions.
    for stem in sorted(md_stems ^ json_stems):
        side = ".md" if stem in md_stems else ".json"
        err(f"orphan fixture (no matching {side}): {stem}")

    # (b) MANIFEST table rows == fixture groups. Every fixture row's first
    # cell is exactly the fixture stem, so compare the first-column set with
    # the corpus group set in both directions.
    groups = md_stems & json_stems
    listed = set()
    for line in open(MANIFEST, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if cols and cols[0] in groups:
            listed.add(cols[0])
    if listed != groups:
        missing = sorted(groups - listed)
        extra = sorted(listed - groups)
        if missing:
            err(f"fixtures missing from MANIFEST: {missing}")
        if extra:
            err(f"MANIFEST lists unknown fixtures: {extra}")

    # (c) declared coverage vs exercised diagnostic codes.
    exercised = set()
    for f in jsons:
        with open(os.path.join(FIX, f), encoding="utf-8") as fh:
            data = json.load(fh)
        for entry in data.get("diagnostics", []):
            code = entry.get("code")
            if code:
                exercised.add(code)
    unknown = exercised - CANONICAL_CODES
    if unknown:
        err(f"expected outputs exercise non-canonical codes: {sorted(unknown)}")

    text = open(MANIFEST, encoding="utf-8").read()
    matches = re.findall(r"(\d+)\s*/\s*14", text)
    if not matches:
        err("MANIFEST bottom does not declare an 'N/14' coverage figure")
    else:
        declared = int(matches[-1])
        if declared != len(exercised):
            err(f"MANIFEST declares {declared}/14 coverage but corpus exercises {len(exercised)} codes")

    if ERRORS:
        print("fixtures check FAILED:")
        for e in ERRORS:
            print("  -", e)
        return 1
    print(
        f"fixtures check OK: {len(groups)} groups, "
        f"{len(exercised)}/14 codes exercised, MANIFEST in sync"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
