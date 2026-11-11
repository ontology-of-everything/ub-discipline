---
name: ub-dry
description: "Run dryer and eliminate duplication that ranks 0.8 or above. Dryer from Robert C. Martin's ub-mode, verbatim. Use only when explicitly invoked."
disable-model-invocation: true
license: MIT
metadata:
  language: en
  translation_of: ub-dry-cn
  version: "0.1.0"
---

# ub-dry

Apply these rules to the current task. They are quoted verbatim from "Then Make it Right" in Robert C. Martin's ub-mode.

## Dryer

* Use the dryer tool to eliminate duplication that rank 0.8 or above.

## Running dryer (local addition, not part of ub-mode)

* dryer compares Clojure, Java, Go, TypeScript, Rust, and Python: <https://github.com/unclebob/dryer>.
* From the project root, run `<dryer-checkout>/dryer --changed --threshold 0.8`. ub-mode sets 0.8; dryer's own default is 0.82.
* dryer skips forms shorter than four lines unless `--min-lines` says otherwise.
* If dryer is missing or does not support the project's language, say the check did not run. Do not report it as passed.
