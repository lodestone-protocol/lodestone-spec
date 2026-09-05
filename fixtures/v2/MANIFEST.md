# v2.0-draft Fixtures

> 纯 markdown 语料（无 JSON 伴随文件）——v2 元数据可见于正文，校验器直接读结构。
> 用途：mddag v2 实现的验收语料 + 协议示例。不冻结（随 spec draft 演进）。

| # | 文件 | 内容 | 期望 |
|---|---|---|---|
| 01 | `01_basic_lodestones.md` | 三磁石 + 状态（converged/aligned/draft）+ 子标题树 | 解析正常 |
| 02 | `02_aligned_compress.md` | aligned 磁石（summary + 全文链接）+ 沉淀区 | 压缩形态合法 |
| 03 | `03_magnetic_lines.md` | 依赖/反驳磁力线 + 沉淀链接过滤 | 磁力线正确 |
| 04 | `04_cycle.md` | aligned 双磁石互引 | E-CYCLE |
| 05 | `05_diagnostics.md` | 重复 slug / 悬空引用 / 无状态 | E-DUP-ID + W-REF-NOT-FOUND + W-STATUS-MISSING |
| 06 | `06_decay.md` → `06_decay_after.md` | decay 前/后：draft 磁石被遗忘，收敛磁石保留 | 审计行存在；重解析合法 |
| 07 | `library/` + `07_window.md` | 三会话库（session/created 元数据）+ 窗口投影 + strip | keep=2 时 s1 折叠、s2/s3 完整；strip 后磁力线 0 |
| 08 | `cross/` + `08_cross_doc.md` | 跨文档：三会话互引 + `.lodestone` 索引快照 | 生成索引与期望一致；目标存在校验；循环检测 |
