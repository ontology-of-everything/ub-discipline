---
name: ub-domain
description: "Model the domain so illegal states are impossible, check data where it enters and trust it inside, and do not silence the compiler. Model the Domain, Boundary Discipline, Type System Discipline from Robert C. Martin's ub-mode, verbatim. Use only when explicitly invoked."
disable-model-invocation: true
license: MIT
metadata:
  language: en
  translation_of: ub-domain-cn
  version: "0.1.0"
---

# ub-domain

Apply these rules to the current task. They are quoted verbatim from "First Make it Work" in Robert C. Martin's ub-mode.

## Architecture

### Model the Domain

* Put the domain in a structure that makes the illegal states impossible.
* Maintain a glossary of domain terms.
* If the code is already clear and local, leave it.

### Boundary Discipline

* Check the data where it enters.
* Inside, trust it.
* Keep the business logic in a pure function.

### Type System Discipline

* Make the illegal value impossible to write.
* Parse outside data once, where it comes in.
* Do not silence the compiler.
