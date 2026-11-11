---
name: ub-root-cause-cn
description: "先复现，修复原因而不掩盖崩溃；两个修复在同一关卡失败时，质疑它们共享的前提。译自 Robert C. Martin 的 ub-mode：修复根因、质疑前提。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-root-cause
  version: "0.1.0"
---

# ub-root-cause-cn

把以下规则用于当前任务。规则逐条直译自 Robert C. Martin 的 ub-mode 中“再让它正确（Then Make it Right）”和“先让它能工作（First Make it Work）”部分。

## 修复根因（Fix Root Causes）

* 复现它。
* 修复原因。
* 只是掩盖崩溃的守卫不是修复。

## 质疑前提（Attack the Premise）

* 当两个共享同一前提的修复在同一道关卡失败时，用一句话写下这个前提，并清点哪些参与者承担着这种失衡。
* 移除这项分配。
* 做完这一步之前，不要开始下一个修复。
