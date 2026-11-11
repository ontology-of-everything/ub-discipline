---
name: ub-crap
description: "Run crapper and bring every function under CRAP 10 by splitting it, testing it, or both. Crapper from Robert C. Martin's ub-mode, verbatim. Use only when explicitly invoked."
disable-model-invocation: true
license: MIT
metadata:
  language: en
  translation_of: ub-crap-cn
  version: "0.1.0"
---

# ub-crap

Apply these rules to the current task. They are quoted verbatim from "Then Make it Right" in Robert C. Martin's ub-mode.

## Crapper

* Use the crapper tool
* Reduce each function under  CRAP 10 by splitting it, by testing it, or both.
* Consider whether case statements are worth reducing.

## Running crapper (local addition, not part of ub-mode)

* crapper scores Clojure, Java, Go, TypeScript, Rust, and Python: <https://github.com/unclebob/crapper>.
* From the project root, run `<crapper-checkout>/crapper --changed` to score the functions in git additions and edits. Drop `--changed` to score the whole tree.
* The table lists the worst score first; every function at 10 or above still needs work. `--threshold 10` makes the run exit 2 when the worst score is above 10.
* Without a coverage report, `--no-coverage` scores complexity only; report CRAP as not measured.
* If crapper is missing or does not support the project's language, say the check did not run. Do not report it as passed.
