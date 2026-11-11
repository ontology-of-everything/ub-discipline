---
name: ub-crap-cn
description: "运行 crapper，通过拆分、测试或两者兼用，把每个函数的 CRAP 降到 10 以下。译自 Robert C. Martin 的 ub-mode：Crapper。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-crap
  version: "0.1.0"
---

# ub-crap-cn

把以下规则用于当前任务。规则逐条直译自 Robert C. Martin 的 ub-mode 中“再让它正确（Then Make it Right）”部分。

## Crapper

* 使用 crapper 工具
* 通过拆分、测试或两者兼用，把每个函数的 CRAP 降到 10 以下。
* 考虑 case 语句是否值得削减。

## 运行 crapper（本地补充，不属于 ub-mode 原文）

* crapper 支持 Clojure、Java、Go、TypeScript、Rust 和 Python：<https://github.com/unclebob/crapper>。
* 在项目根目录运行 `<crapper-checkout>/crapper --changed`，为 git 新增和修改的函数打分；去掉 `--changed` 则检查整棵目录树。
* 结果表按分数从高到低排列；分数为 10 或以上的函数仍需处理。加上 `--threshold 10`，最高分超过 10 时以退出码 2 结束。
* 没有覆盖率报告时，`--no-coverage` 只计算复杂度；此时报告 CRAP 未测量。
* crapper 未安装或不支持项目语言时，说明该检查未执行，不得报告为通过。
