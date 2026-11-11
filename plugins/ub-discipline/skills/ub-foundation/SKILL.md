---
name: ub-foundation
description: "Get the data shape right before writing logic, do first what helps every later phase, and do not share state a concurrent writer would touch. Foundational Thinking from Robert C. Martin's ub-mode, verbatim. Use only when explicitly invoked."
disable-model-invocation: true
license: MIT
metadata:
  language: en
  translation_of: ub-foundation-cn
  version: "0.1.0"
---

# ub-foundation

Apply these rules to the current task. They are quoted verbatim from "First Make it Work" in Robert C. Martin's ub-mode.

## Foundational Thinking

* Get the data shape right before you write the logic.
* Do first whatever helps every later phase.
* If a concurrent writer would matter, do not share state.
