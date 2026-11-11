---
name: ub-state-cn
description: "让操作在重复运行或中途崩溃后都结束于同一状态；分离共享的可变状态，或只允许一个受结构约束的写入者。译自 Robert C. Martin 的 ub-mode：让操作幂等、先分离，再串行化共享状态。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-state
  version: "0.1.0"
---

# ub-state-cn

把以下规则用于当前任务。规则逐条直译自 Robert C. Martin 的 ub-mode 中“先让它能工作（First Make it Work）”部分。

## 架构（Architecture）

### 让操作幂等（Make Operations Idempotent）

* 运行两次，或在中途崩溃后再次运行，最终都处于同一状态。

### 先分离，再串行化共享状态（Separate Before Serializing Shared State）

* 如果它们不需要同一个可变的东西，就给每个参与者各自一份。
* 如果需要，就只允许一个写入者，并在结构上强制这一点。
