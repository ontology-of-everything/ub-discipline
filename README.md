# ub-discipline

Robert C. Martin's [ub-mode](https://github.com/unclebob/ub-mode), split into atomic skills you combine per task. Rule text is quoted verbatim (English plugin) or translated line by line (`ub-discipline-cn`). Not an official release.

中文：安装 `ub-discipline-cn`；规则逐条直译自原文。

## Source and license

Everything about origin and license lives here and in each plugin's `LICENSE`.

- Content: [unclebob/ub-mode](https://github.com/unclebob/ub-mode), `SKILL.md`, blob `9ac940b`, MIT, Copyright (c) 2026 Robert C. Martin.
- Shape: one explicit-only command per skill follows the `bro` skill in Lauren Tan's pstack. No pstack text is used.
- Gate tools: [crapper](https://github.com/unclebob/crapper), [dryer](https://github.com/unclebob/dryer), [mutator](https://github.com/unclebob/mutator). Install separately; they support Clojure, Java, Go, TypeScript, Rust, and Python. Sections marked "local addition" only explain how to run them.

Install the plugin, not single skills, so the LICENSE travels with the text.

```bash
claude plugin marketplace add ontology-of-everything/ub-discipline
claude plugin install ub-discipline@ub-discipline
claude plugin install ub-discipline-cn@ub-discipline
```

## Skills

| Skill | ub-mode sections |
| --- | --- |
| `ub-mode` | All |
| `ub-lazy` | Laziness Protocol, Subtract Before You Add |
| `ub-foundation` | Foundational Thinking |
| `ub-redesign` | Redesign From First Principles |
| `ub-domain` | Model the Domain, Boundary Discipline, Type System Discipline |
| `ub-state` | Make Operations Idempotent, Separate Before Serializing Shared State |
| `ub-tdd` | TDD, Test Behavior, Not Implementation |
| `ub-root-cause` | Fix Root Causes, Attack the Premise |
| `ub-execute` | Outcome-Oriented Execution, Build the Lever, Sequence work into verifiable units |
| `ub-refactor` | Refactoring |
| `ub-crap` / `ub-dry` / `ub-mutate` | Crapper / Dryer / Mutator |
| `ub-ship` | Keep a Log, Commit and Push |

Guard the Context Window and Worktree Cleanup appear only in `ub-mode`. Chinese skills add `-cn`.

## Combine

```text
New project        $ub-foundation $ub-domain $ub-tdd $ub-crap
Feature evolution  $ub-redesign $ub-lazy $ub-tdd $ub-dry
Bug fix            $ub-root-cause $ub-tdd $ub-lazy
Legacy upkeep      $ub-refactor $ub-tdd $ub-mutate
Migration          $ub-execute $ub-state
Wrap-up            $ub-ship
```
