---
name: ub-tdd
description: "TDD, Test Behavior, Not Implementation. Quoted verbatim from Robert C. Martin's ub-mode. Explicit invocation only."
disable-model-invocation: true
license: MIT
metadata:
  language: en
  translation_of: ub-tdd-hans
  version: "1.0.0"
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
