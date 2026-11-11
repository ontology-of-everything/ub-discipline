---
name: ub-domain-cn
description: "为领域建模，让非法状态不可能出现；在数据进入处检查、在内部信任它；不压制编译器。译自 Robert C. Martin 的 ub-mode：为领域建模、边界纪律、类型系统纪律。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-domain
  version: "0.1.0"
---

# ub-domain-cn

把以下规则用于当前任务。规则逐条直译自 Robert C. Martin 的 ub-mode 中“先让它能工作（First Make it Work）”部分。

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
