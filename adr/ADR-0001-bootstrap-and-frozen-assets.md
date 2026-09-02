# ADR-0001 Protocol repository bootstrap (v1.3.0)

> **Status**: Active (2026-09-02)
> **Scope**: Protocol-level decisions for the lodestone-spec repository.

---

## Background

Lodestone Protocol (MD-DAG) v1.3 Final was authored, reviewed, and its text
frozen while its Rust reference implementation (lodestone-md) was still the
only home for both spec prose and the Golden Fixture corpus. This repository
splits the protocol (spec + registry + fixtures) from any one implementation.

## Decisions

| Decision | Resolution |
|---|---|
| Single-source fixture corpus | `fixtures/` here is the authoritative source, imported byte-for-byte from lodestone-md@3156199 (CI-green snapshot, 25 fixtures). Implementations reference this corpus (e.g. as a git submodule) instead of duplicating it. |
| License | The whole repository is **Apache-2.0** (maintainer directive of 2026-09-02). This supersedes an earlier draft plan of CC-BY-4.0 prose + CC0 fixtures; the single-license scheme is recorded here as the controlling decision. |
| §8.1 additional-field clause | Added to the spec text at bootstrap ("implementations MAY carry additional fields after the contract fields, e.g. `title` for §5.3 invalid-node placeholders; consumers MUST ignore unrecognized fields"). It closes a wording gap between §5.3 (placeholder includes the heading) and the seven-field §8.1 contract. No parsing behavior changes; fully backward compatible. |
| Version mapping contract | Protocol versions use plain SemVer (`v1.3.0`; "Final" is a status carried by Release notes, not a suffix). Implementations must declare "Implements Lodestone Protocol v1.3.0" in their README and package metadata, and their major.minor follows the protocol version while patch is independent. |
| Formal release artifact | The protocol's official release shape is a **spec-repo git tag + GitHub Release** (with spec text and a fixture archive), not a package registry entry. |

## Consequences

- Fixture edits belong in this repository; implementation repos hold a
  submodule pointer and must not drift the corpus.
- Adding or rewording normative spec text requires a new protocol-level ADR
  here; language-specific choices belong to each implementation's own ADRs.
- All 14 codes and the §8.1–§8.4 output contracts are frozen for v1.3.x;
  any change is a SemVer-visible spec revision.
