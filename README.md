# ub-discipline

Robert C. Martin's [ub-mode](https://github.com/unclebob/ub-mode), split into atomic skills you combine per task. The English plugin quotes the rules verbatim. `ub-discipline-cn` translates them line by line. This is not an official release.

中文版安装 `ub-discipline-cn`。

## Install

Install the plugin, not a single skill. The MIT `LICENSE` is at the plugin root and does not travel with one skill.

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

Guard the Context Window and Worktree Cleanup are only in `ub-mode`. Chinese skill names add `-cn`.

## Combine

```text
New project        $ub-foundation $ub-domain $ub-tdd $ub-crap
Feature evolution  $ub-redesign $ub-lazy $ub-tdd $ub-dry
Bug fix            $ub-root-cause $ub-tdd $ub-lazy
Legacy upkeep      $ub-refactor $ub-tdd $ub-mutate
Migration          $ub-execute $ub-state
Wrap-up            $ub-ship
```

## Source and license

- Content: [unclebob/ub-mode](https://github.com/unclebob/ub-mode), `SKILL.md`, blob `9ac940b`, MIT, Copyright (c) 2026 Robert C. Martin.
- Shape: one explicit-only command per skill, following the `bro` skill in Lauren Tan's pstack. No pstack text is used.
- Gate tools: [crapper](https://github.com/unclebob/crapper), [dryer](https://github.com/unclebob/dryer), [mutator](https://github.com/unclebob/mutator). Install them separately. They support Clojure, Java, Go, TypeScript, Rust, and Python. Sections marked "local addition" only say how to run them.

Each plugin's `LICENSE` repeats this notice.
