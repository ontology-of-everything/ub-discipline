---
name: ub-mutate
description: "Run mutator to cover the uncovered, kill surviving mutants, and delete dead code. Mutator from Robert C. Martin's ub-mode, verbatim. Use only when explicitly invoked."
disable-model-invocation: true
license: MIT
metadata:
  language: en
  translation_of: ub-mutate-cn
  version: "0.1.0"
---

# ub-mutate

Apply these rules to the current task. They are quoted verbatim from "Then Make it Right" in Robert C. Martin's ub-mode.

## Mutator

* Use the mutator tool
* Cover the uncovered.
* Kill the survivors.
* Delete dead code.

## Running mutator (local addition, not part of ub-mode)

* mutator tests Clojure, Java, Go, TypeScript, Rust, and Python: <https://github.com/unclebob/mutator>. It needs crapper checked out next to it, at `../crapper`.
* Start with the file you are working on: `<mutator-checkout>/mutator path/to/file`, or `--changed` for git additions and edits. A first run over a whole tree executes every covered mutant.
* Exit 0: every executed mutant was killed. Exit 2: the baseline tests fail; fix them first. Exit 3: a mutant survived.
* If mutator is missing or does not support the project's language, say the check did not run. Do not report it as passed.
