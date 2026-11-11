---
name: ub-root-cause
description: "Fix Root Causes, Attack the Premise. Quoted verbatim from Robert C. Martin's ub-mode. Explicit invocation only."
disable-model-invocation: true
license: MIT
metadata:
  language: en
  translation_of: ub-root-cause-hans
  version: "1.0.0"
---

# ub-root-cause

Apply these rules to the current task. They are quoted verbatim from "Then Make it Right" and "First Make it Work" in Robert C. Martin's ub-mode.

## Fix Root Causes

* Reproduce it.
* Fix the cause.
* A guard that only hides the crash is not a fix.

## Attack the Premise

* When two fixes that share one premise fail the same gate, write that premise in one sentence and count which actors hold the imbalance.
* Remove the assignment.
* Do not start another fix until you have done that.
