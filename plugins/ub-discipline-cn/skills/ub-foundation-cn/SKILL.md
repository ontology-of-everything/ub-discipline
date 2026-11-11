---
name: ub-foundation-cn
description: "写逻辑之前先把数据形状弄对，先做对后续每个阶段都有帮助的事，并发写入者会造成影响时不共享状态。译自 Robert C. Martin 的 ub-mode：基础思维。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-foundation
  version: "0.1.0"
---

# ub-foundation-cn

把以下规则用于当前任务。规则逐条直译自 Robert C. Martin 的 ub-mode 中“先让它能工作（First Make it Work）”部分。

## 基础思维（Foundational Thinking）

* 先把数据形状弄对，再写逻辑。
* 先做对后面每个阶段都有帮助的事。
* 如果并发写入者会造成影响，就不要共享状态。
