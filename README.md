# Lodestone Protocol (alias: MD-DAG)

> **Lodestone Protocol — Markdown-Embedded DAG for conversational knowledge
> convergence / Alias: MD-DAG**
>
> Lodestone（磁石协议）为人机对话的知识脱水与收敛而生长：节点如同磁石吸附
> 有效信息，边作为磁力线登记依赖与分歧，draft → converged → aligned
> 标记观点成型阶段。

This repository is the authoritative home of the **protocol**: the normative
specification text, the error-code registry, and the Golden Fixture corpus.
It is language-agnostic — the protocol is not a library.

## Repository layout

```
spec/v1.3.md          # normative spec text (v1.3.0, frozen line)
registry/errors.md    # the 14 error/warning codes (§11 extraction)
fixtures/             # 25 Golden Fixtures (.md input + .json expected) + MANIFEST
adr/                  # protocol-level architecture decision records
```

## Version mapping contract

- Protocol versions use plain **SemVer**: the current release is **v1.3.0**.
  "Final" is a status carried by Release notes, not a version suffix.
- An implementation's major.minor tracks the protocol version; its patch is
  independent.
- Implementations MUST declare in their README and package metadata:
  **"Implements Lodestone Protocol v1.3.0"**, and their conformance tests MUST
  stay green against this repository's `fixtures/`.

## The three-level read mode (protocol essence)

| Level | Content | Typical use |
|---|---|---|
| L1 skeleton | node table + normalized edges + diagnostics | rebuild global awareness |
| L2 targeted body | one node read by `body_start`/`body_end` | answer a specific question |
| L3 full text | all bytes | recall-complete tasks |

AI agents are the protocol's native consumers (L1 + L2 minimal subset);
humans audit alignment state, warnings, and dispute domains.

## Reference implementations

| Repository | Language | Status |
|---|---|---|
| [lodestone-md](https://github.com/lodestone-protocol/lodestone-md) | Rust | Implements Lodestone Protocol v1.3.0 · 23 tests green · submodule-imports this corpus |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — especially the ADR attribution rule
(spec wording here, implementation choices there, cross-cutting issues start
here).

## License

Apache-2.0
