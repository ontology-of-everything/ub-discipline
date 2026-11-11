---
name: ub-tdd
description: "Write the failing test first, see it fail for the expected reason, make the smallest passing change, and test behavior, not implementation. TDD, Test Behavior, Not Implementation from Robert C. Martin's ub-mode, verbatim. Use only when explicitly invoked."
disable-model-invocation: true
license: MIT
metadata:
  language: en
  translation_of: ub-tdd-cn
  version: "0.1.0"
---

# ub-tdd

Apply these rules to the current task. They are quoted verbatim from "First Make it Work" and "Then Make it Right" in Robert C. Martin's ub-mode.

## TDD

* Write the failing test before you change the code.
* See it fail for the reason you expect.
* Make the smallest change that makes it pass.
* If an honest test is impractical, do not write a bad one.

## Test Behavior, Not Implementation

* The test calls the code the way its user does and checks the result that user would see.
* If the test would still pass when every function returned nothing, throw it out.
