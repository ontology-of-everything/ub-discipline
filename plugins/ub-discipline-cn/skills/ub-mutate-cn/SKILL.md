---
name: ub-mutate-cn
description: "运行 mutator，覆盖未被覆盖的部分，杀死存活的变异体，并删除死代码。译自 Robert C. Martin 的 ub-mode：Mutator。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-mutate
  version: "0.1.0"
---

# ub-mutate-cn

把以下规则用于当前任务。规则逐条直译自 Robert C. Martin 的 ub-mode 中“再让它正确（Then Make it Right）”部分。

## Mutator

* 使用 mutator 工具
* 覆盖未被覆盖的部分。
* 杀死存活的变异体。
* 删除死代码。

## 运行 mutator（本地补充，不属于 ub-mode 原文）

* mutator 支持 Clojure、Java、Go、TypeScript、Rust 和 Python：<https://github.com/unclebob/mutator>。它要求 crapper 签出在相邻的 `../crapper`。
* 从正在修改的文件开始：`<mutator-checkout>/mutator path/to/file`，或用 `--changed` 检查 git 新增和修改。首次对整棵目录树运行时，会执行所有被覆盖的变异体。
* 退出码 0：执行的变异体全部被杀死。退出码 2：基线测试失败，先修复它。退出码 3：有变异体存活。
* mutator 未安装或不支持项目语言时，说明该检查未执行，不得报告为通过。
