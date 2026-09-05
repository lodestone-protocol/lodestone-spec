# 跨文档机制示例（cross/）
```
mddag index fixtures/v2/cross -o fixtures/v2/cross/.lodestone
```
- `.lodestone` = 库层快照（git 可提交、AI 零成本读取），mddag 语料格式，可被重解析（自举）
- 每个会话投影为 L1 磁石 + 出边磁力线（跨文档 `[label](path#slug)`）
- 库层校验：path 存在 / 目标 slug 存在 / 跨文档循环（E-CYCLE-CROSS）
- 入边派生不落盘（出边 ⇔ 入边双射，极致节能）
- `mddag index <dir> --check`：过期检测（字节级一致性）
