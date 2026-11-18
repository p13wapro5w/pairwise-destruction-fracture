# pairwise-destruction-fracture

木箱被打碎后碎片悬空、二次爆炸、支撑结构不塌：断裂用均匀网格；碎片质量按体积但不按材质；冲击力只作用于命中刚体；支撑图没更新；碎片间碰撞滤波错；静止碎片不睡眠；断裂面法线重复；预碎片和运行时断裂混用；破坏事件在主线程同步；网络回放碎片不同步。physics/destruction_fracture.py 是核心，tests/test_destruction_fracture.py 15个红。要修的是：材质感知断裂；质量体积密度；冲击传播；支撑图重建；碎片碰撞滤波；睡眠阈值；断裂面去重；统一碎片路径；异步破坏队列；确定性碎片。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：游戏开发；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
