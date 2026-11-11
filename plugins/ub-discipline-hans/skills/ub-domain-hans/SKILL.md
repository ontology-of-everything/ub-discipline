---
name: ub-domain-hans
description: "为领域建模、边界纪律、类型系统纪律。仅显式调用。"
disable-model-invocation: true
license: MIT
metadata:
  language: zh-CN
  translation_of: ub-domain
  version: "1.0.0"
---

# ub-domain-hans

## 架构

### 为领域建模

* 把领域放进一个让非法状态不可能出现的结构里。
* 维护一份领域术语表。
* 如果代码已经清晰且局部，就不要动它。

### 边界纪律

* 在数据进入的地方检查它。
* 在内部，信任它。
* 把业务逻辑放在纯函数里。

### 类型系统纪律

* 让非法值无法被写出来。
* 外部数据在进入的地方解析一次。
* 不要压制编译器。
