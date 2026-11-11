---
name: ub-state-hans
description: "让操作幂等、先分离，再串行化共享状态。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-state
  version: "1.0.0"
---

# ub-state-hans

## 架构

### 让操作幂等

* 运行两次，或在中途崩溃后再次运行，最终都处于同一状态。

### 先分离，再串行化共享状态

* 如果它们不需要同一个可变的东西，就给每个参与者各自一份。
* 如果需要，就只允许一个写入者，并在结构上强制这一点。
