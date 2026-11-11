---
name: ub-root-cause
description: "Reproduce, fix the cause rather than hide the crash, and attack the shared premise when two fixes fail the same gate. Fix Root Causes, Attack the Premise from Robert C. Martin's ub-mode, verbatim. Use only when explicitly invoked."
disable-model-invocation: true
license: MIT
metadata:
  language: en
  translation_of: ub-root-cause-cn
  version: "0.1.0"
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
