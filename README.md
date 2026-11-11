# ub-discipline

Robert C. Martin's [ub-mode](https://github.com/unclebob/ub-mode), split into atomic skills you combine per task. The English plugin quotes the rules verbatim. `ub-discipline-hans` is the Simplified Chinese edition. This is not an official release.

中文版安装 `ub-discipline-hans`。

## Why it is split

ub-mode applies its whole list to every change. The list holds rules that apply in different situations. A bug fix needs the smallest edit. A requirement that no longer fits the design needs a redesign, delivered in pieces. New code can start with a failing test. Untested code needs its current behavior pinned before the structure changes.

One discipline is one command. Combine the commands for the task: a new project, a feature change, a bug fix, legacy upkeep, or a migration. `ub-mode` stays for the full list.

原文把整份清单用在每一次改动上。清单里的规则适用的情况不同：修缺陷要最小改动；需求已经装不进旧设计时，要按第一性原理重做并分块交付；新代码可以先写失败的测试；没有测试的代码要先钉住现有行为。

一项纪律一个命令。按任务组合：新项目、功能改动、修缺陷、遗留代码维护、迁移。需要整份清单时用 `ub-mode`。

## Install

Install the plugin, not a single skill. The MIT `LICENSE` is at the plugin root and does not travel with one skill.

```bash
claude plugin marketplace add ontology-of-everything/ub-discipline
claude plugin install ub-discipline@ub-discipline
claude plugin install ub-discipline-hans@ub-discipline
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
| `ub-ship` | Keep a Log, Commit and Push |

Guard the Context Window and Worktree Cleanup are only in `ub-mode`. Chinese skill names add `-hans`.

## Combine

```text
New project        $ub-foundation $ub-domain $ub-tdd
Feature evolution  $ub-redesign $ub-lazy $ub-tdd
Bug fix            $ub-root-cause $ub-tdd $ub-lazy
Legacy upkeep      $ub-refactor $ub-tdd
Migration          $ub-execute $ub-state
Wrap-up            $ub-ship
```

## Source and license

- Content: [unclebob/ub-mode](https://github.com/unclebob/ub-mode), `SKILL.md`, blob `9ac940b`, MIT, Copyright (c) 2026 Robert C. Martin.
- Shape: one explicit-only command per skill, following the `bro` skill in Lauren Tan's pstack. No pstack text is used.
- Crapper, Dryer, and Mutator from the original skill are omitted. They require those tools.

Each plugin's `LICENSE` repeats this notice.
