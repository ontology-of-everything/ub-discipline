---
name: ub-dry-cn
description: "运行 dryer，消除评分在 0.8 或以上的重复。译自 Robert C. Martin 的 ub-mode：Dryer。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-dry
  version: "0.1.0"
---

# ub-dry-cn

把以下规则用于当前任务。规则逐条直译自 Robert C. Martin 的 ub-mode 中“再让它正确（Then Make it Right）”部分。

## Dryer

* 使用 dryer 工具消除评分在 0.8 或以上的重复。

## 运行 dryer（本地补充，不属于 ub-mode 原文）

* dryer 支持 Clojure、Java、Go、TypeScript、Rust 和 Python：<https://github.com/unclebob/dryer>。
* 在项目根目录运行 `<dryer-checkout>/dryer --changed --threshold 0.8`。ub-mode 规定 0.8；dryer 自身默认值是 0.82。
* 除非用 `--min-lines` 另行指定，dryer 会跳过少于四行的代码块。
* dryer 未安装或不支持项目语言时，说明该检查未执行，不得报告为通过。
