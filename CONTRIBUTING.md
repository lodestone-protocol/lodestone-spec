# Contributing

Thank you for contributing to the Lodestone Protocol. This repository holds
the protocol: the normative spec text (`spec/`), the error-code registry
(`registry/`), and the authoritative Golden Fixture corpus (`fixtures/`).

## Where a discussion belongs (ADR attribution rule)

| Topic | Where it goes |
|---|---|
| Normative spec text (wording, MUST/SHOULD semantics, contracts, codes) | This repository (`spec/` + protocol-level ADR in `adr/`) |
| A specific language's implementation choices / APIs | That implementation's repository and its own ADRs |
| Something touching both | Open an issue in this repository first; consensus lands in the spec, the implementation records follow-up |

## Frozen assets — read first

The following are frozen for the v1.3 line and are not open to
"supplementary authorization" style edits:

- Syntax identifier `mddag` (prefix `<!-- mddag: `, package/library name).
- The §8.1–§8.4 output contracts, the §3.1 behavior table, and the 14 codes
  in `registry/errors.md`.
- Golden Fixture expected outputs are canonical bytes (`fixtures/*.json`).

Any change to these is a SemVer-visible spec revision requiring a
protocol-level ADR and a maintainer decision.

## Golden Fixture workflow

- Fixture inputs (`fixtures/*.md`) and their expected outputs
  (`fixtures/*.json`) always change **together**, in the same commit, and each
  change is validated against a reference implementation run.
- `MANIFEST.md` maps every fixture to the spec sections it pins; update it
  whenever fixtures change.
- Do not edit expected outputs to make a parser pass — the expected output is
  the contract, not the code.

## License

By contributing you agree that your contributions are licensed under
Apache-2.0, as the repository's LICENSE states.
