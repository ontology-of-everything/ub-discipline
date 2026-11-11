---
name: ub-execute-cn
description: "瞄准可检验的最终状态，工作无法一眼看清时构建工具，完成并检查一个小单元后再开始下一个。译自 Robert C. Martin 的 ub-mode：结果导向执行、打造杠杆、把工作排成可验证的单元。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-execute
  version: "0.1.0"
---

# ub-execute-cn

把以下规则用于当前任务。规则逐条直译自 Robert C. Martin 的 ub-mode 中“先让它能工作（First Make it Work）”和“再让它正确（Then Make it Right）”部分。

## 结果导向执行（Outcome-Oriented Execution）

* 瞄准你能检验的最终状态。
* 中途出现断裂是允许的，前提是你计划过它，并且能撤销它。

## 打造杠杆（Build the Lever）

* 如果这项工作无法一眼看清，就构建能完成它的工具。
* 先手工完成一个单元，再让工具的结果与这个单元一致。

## 把工作排成可验证的单元（Sequence work into verifiable units）

* 完成一个小单元并检查它。
* 然后再开始下一个。
