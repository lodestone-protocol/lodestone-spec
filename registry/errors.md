# Error & Warning Code Registry

> Source of truth: spec/v1.3.md §11. This registry extracts the table for
> machine and validator conformance; it MUST stay in sync with the spec text.
> Conformance language per RFC 2119 / RFC 8174.

## Codes (14)

| Code | Level | Meaning | Deterministic consequence |
|---|---|---|---|
| E-MISSING-ID | error | Node has no usable id | Node invalid |
| E-META-SYNTAX | error | Metadata malformed / JSON parse failure / **duplicate keys** | Node invalid |
| E-META-FIELD | error | Illegal field value | Node valid, field degraded |
| E-DUP-ID | error | Duplicate id among valid nodes | All nodes with that id invalid |
| E-REF-NOT-FOUND | error | Edge references a missing or invalid node | Edge ineffective |
| E-CYCLE | error | Global graph contains a cycle | Cycle edge set ineffective |
| W-VERSION-MISMATCH | warning | Document `version` is not `"1.3"` | Keep parsing |
| W-DOC-META | warning | Document metadata JSON invalid / **duplicate keys** | Ignore it, keep parsing |
| W-CYCLE-DECLARED | warning | Declared normalized edge set contains a cycle | No structural effect |
| W-REDUNDANT-EDGE | warning | Duplicate after normalization | Folded into one edge |
| W-META-PLACEMENT | warning | Suspected metadata in an illegal position/form | Node has no metadata |
| W-REDUNDANT-META | warning | Later mddag comment inside a node ignored | Comment ignored |
| W-UPSTREAM-PENDING | warning | An aligned node has a non-aligned upstream | No structural effect |
| W-NFC-VIOLATION | warning | Heading text is not in NFC form | No structural effect |

## Pinned behaviors referenced by codes

- **E-META-SYNTAX**: duplicate JSON keys in node metadata (spec §5.2).
- **W-DOC-META**: duplicate JSON keys or non-string `version` in document
  metadata (spec §3.1); all failure paths converge on "warn + keep parsing".
- **E-CYCLE**: only the *cycle edge set* (edges on at least one cycle) is
  ineffective; the remaining subgraph is emitted normally (spec §7.3).
- **failure values**: an ineffective edge's `failure` records its single
  primary reason, e.g. `E-REF-NOT-FOUND`, `E-CYCLE`, `W-UPSTREAM-PENDING`
  (spec §8.2).

## Stability

Codes are part of the frozen v1.3 contract. Adding a code requires a spec
revision (SemVer minor bump); renaming or removing a code is a breaking
change (SemVer major bump). Implementations MUST use exactly these strings.
