# 窗口机制示例（library/）
```
mddag library fixtures/v2/library --keep 2
```
- keep=2：s1 窗口外（隐性分支，按需回忆）；s2/s3 窗口内完整 L0
- keep 是注入参数（示例 12），零硬编码
- strip：窗口外会话剔除磁力线（边退出全局图），审计留痕
