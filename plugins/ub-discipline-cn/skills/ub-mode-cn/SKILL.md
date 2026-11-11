---
name: ub-mode-cn
description: "编写或修改代码时遵循精简原则。每次改动都依次遵循：先让它能工作，再让它正确，再遵循实践。在用户运行 /ub-mode-cn 或要求使用精简原则时使用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-mode
  version: "0.1.0"
---

# ub-mode

每次被要求做出改动时，遵循：
* 先让它能工作。
* 再让它正确。
* 遵循实践

# 先让它能工作（First Make it Work）

## 懒惰协议（Laziness Protocol）

* 一个决定只存在于一个地方。
* 交付能解决问题的最小改动。

## 基础思维（Foundational Thinking）

* 先把数据形状弄对，再写逻辑。
* 先做对后面每个阶段都有帮助的事。
* 如果并发写入者会造成影响，就不要共享状态。

## TDD

* 修改代码之前，先写会失败的测试。
* 确认它因为你预期的原因而失败。
* 做出能让它通过的最小改动。
* 如果写不出诚实的测试，就不要写一个糟糕的测试。

## 从第一性原理重新设计（Redesign From First Principles）

* 不要把新需求硬接到旧设计上。
* 问自己：如果它从一开始就存在，你会构建什么；把这个问题想透，然后分块交付。

## 质疑前提（Attack the Premise）

* 当两个共享同一前提的修复在同一道关卡失败时，用一句话写下这个前提，并清点哪些参与者承担着这种失衡。
* 移除这项分配。
* 做完这一步之前，不要开始下一个修复。

## 先减后加（Subtract Before You Add）

* 在添加任何东西之前，先去掉复杂性。

## 结果导向执行（Outcome-Oriented Execution）

* 瞄准你能检验的最终状态。
* 中途出现断裂是允许的，前提是你计划过它，并且能撤销它。

## 打造杠杆（Build the Lever）

* 如果这项工作无法一眼看清，就构建能完成它的工具。
* 先手工完成一个单元，再让工具的结果与这个单元一致。

## 架构（Architecture）

### 为领域建模（Model the Domain）

* 把领域放进一个让非法状态不可能出现的结构里。
* 维护一份领域术语表。
* 如果代码已经清晰且局部，就不要动它。

### 边界纪律（Boundary Discipline）

* 在数据进入的地方检查它。
* 在内部，信任它。
* 把业务逻辑放在纯函数里。

### 类型系统纪律（Type System Discipline）

* 让非法值无法被写出来。
* 外部数据在进入的地方解析一次。
* 不要压制编译器。

### 让操作幂等（Make Operations Idempotent）

* 运行两次，或在中途崩溃后再次运行，最终都处于同一状态。

### 先分离，再串行化共享状态（Separate Before Serializing Shared State）

* 如果它们不需要同一个可变的东西，就给每个参与者各自一份。
* 如果需要，就只允许一个写入者，并在结构上强制这一点。

# 再让它正确（Then Make it Right）

## 修复根因（Fix Root Causes）

* 复现它。
* 修复原因。
* 只是掩盖崩溃的守卫不是修复。

## 把工作排成可验证的单元（Sequence work into verifiable units）

* 完成一个小单元并检查它。
* 然后再开始下一个。

## 测试行为，而非实现（Test Behavior, Not Implementation）

* 测试以使用者调用代码的方式调用它，并检查使用者会看到的结果。
* 如果每个函数都什么也不返回时测试仍然会通过，就扔掉这个测试。

## Crapper

* 使用 crapper 工具
* 通过拆分、测试或两者兼用，把每个函数的 CRAP 降到 10 以下。
* 考虑 case 语句是否值得削减。

## Dryer

* 使用 dryer 工具消除评分在 0.8 或以上的重复。

## Mutator

* 使用 mutator 工具
* 覆盖未被覆盖的部分。
* 杀死存活的变异体。
* 删除死代码。

## 重构（Refactoring）

* 钉住代码现在的行为。
* 改变结构。
* 证明行为没有改变。

# 实践（Practice）

## 保持日志（Keep a Log）

* 记录你采取的每一个行动，以及采取它的原因。
* 完成时汇报这份日志。

## 守护上下文窗口（Guard the Context Window）

* 保持主线程精简。
* 把大块内容送到别处，只保留摘要。

## Worktree 清理（Worktree Cleanup）

* 找出可以安全删除的内容，确认仍在使用的东西都不需要它，然后回收磁盘空间。
* 未提交的工作等待决定。

## 提交与推送（Commit and Push）

* 经常提交，提交要小且有序。
* 每次提交都说明原因、改了什么，以及你如何证明它。
* 最后推送到主线。
