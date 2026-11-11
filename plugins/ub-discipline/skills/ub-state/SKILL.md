---
name: ub-state
description: "Make operations end in the same state after a rerun or crash, and separate shared mutable state or allow one enforced writer. Make Operations Idempotent, Separate Before Serializing Shared State from Robert C. Martin's ub-mode, verbatim. Use only when explicitly invoked."
disable-model-invocation: true
license: MIT
metadata:
  language: en
  translation_of: ub-state-cn
  version: "0.1.0"
---

# ub-state

Apply these rules to the current task. They are quoted verbatim from "First Make it Work" in Robert C. Martin's ub-mode.

## Architecture

### Make Operations Idempotent

* Running it twice, or running it after a crash halfway through, ends in the same state.

### Separate Before Serializing Shared State

* If they do not need the same mutable thing, give each its own.
* If they do, allow one writer, and enforce that in the structure.
