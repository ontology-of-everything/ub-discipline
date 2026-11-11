---
name: ub-tdd-cn
description: "先写会失败的测试，确认它因预期原因失败，做最小改动让它通过，并测试行为而非实现。译自 Robert C. Martin 的 ub-mode：TDD、测试行为，而非实现。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-tdd
  version: "0.1.0"
---

# ub-tdd-cn

把以下规则用于当前任务。规则逐条直译自 Robert C. Martin 的 ub-mode 中“先让它能工作（First Make it Work）”和“再让它正确（Then Make it Right）”部分。

## TDD

* 修改代码之前，先写会失败的测试。
* 确认它因为你预期的原因而失败。
* 做出能让它通过的最小改动。
* 如果写不出诚实的测试，就不要写一个糟糕的测试。

## 测试行为，而非实现（Test Behavior, Not Implementation）

* 测试以使用者调用代码的方式调用它，并检查使用者会看到的结果。
* 如果每个函数都什么也不返回时测试仍然会通过，就扔掉这个测试。
