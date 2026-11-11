#!/usr/bin/env python3
"""Generate plugins/ from upstream/SKILL.md (Robert C. Martin's ub-mode). Do not edit plugins/ by hand."""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
UPSTREAM = REPO / "upstream/SKILL.md"
VERSION = "0.1.0"
BLOB = "9ac940b23b61d77e8e5192721d7b6066357f892c"
COMMIT = "3da62bf3fcfd2034de41f30d920d2739e566171f"

MIT = """MIT License

Copyright (c) 2026 Robert C. Martin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

raw = UPSTREAM.read_text(encoding="utf-8")
_, upstream_front, upstream_body = raw.split("---", 2)

# Parse sections: title -> (level, stage, verbatim text including heading).
sections, stage, current = {}, None, None
lines = upstream_body.splitlines()
for line in lines:
    m = re.match(r"^(#{1,3}) (.+)$", line)
    if m:
        level, title = len(m.group(1)), m.group(2).strip()
        if level == 1 or title == "Architecture":
            stage = title if level == 1 else stage
            current = None
            continue
        current = title
        sections[title] = {"level": level, "stage": stage, "lines": [line]}
        continue
    if current:
        sections[current]["lines"].append(line)


def verbatim(title):
    text = "\n".join(sections[title]["lines"]).strip("\n")
    return text


ARCH = {"Model the Domain", "Boundary Discipline", "Type System Discipline",
        "Make Operations Idempotent", "Separate Before Serializing Shared State"}

STAGE_ZH = {
    "First Make it Work": "先让它能工作（First Make it Work）",
    "Then Make it Right": "再让它正确（Then Make it Right）",
    "Practice": "实践（Practice）",
}

ZH = {
    "Laziness Protocol": ("懒惰协议", [
        "一个决定只存在于一个地方。",
        "交付能解决问题的最小改动。"]),
    "Foundational Thinking": ("基础思维", [
        "先把数据形状弄对，再写逻辑。",
        "先做对后面每个阶段都有帮助的事。",
        "如果并发写入者会造成影响，就不要共享状态。"]),
    "TDD": ("TDD", [
        "修改代码之前，先写会失败的测试。",
        "确认它因为你预期的原因而失败。",
        "做出能让它通过的最小改动。",
        "如果写不出诚实的测试，就不要写一个糟糕的测试。"]),
    "Redesign From First Principles": ("从第一性原理重新设计", [
        "不要把新需求硬接到旧设计上。",
        "问自己：如果它从一开始就存在，你会构建什么；把这个问题想透，然后分块交付。"]),
    "Attack the Premise": ("质疑前提", [
        "当两个共享同一前提的修复在同一道关卡失败时，用一句话写下这个前提，并清点哪些参与者承担着这种失衡。",
        "移除这项分配。",
        "做完这一步之前，不要开始下一个修复。"]),
    "Subtract Before You Add": ("先减后加", [
        "在添加任何东西之前，先去掉复杂性。"]),
    "Outcome-Oriented Execution": ("结果导向执行", [
        "瞄准你能检验的最终状态。",
        "中途出现断裂是允许的，前提是你计划过它，并且能撤销它。"]),
    "Build the Lever": ("打造杠杆", [
        "如果这项工作无法一眼看清，就构建能完成它的工具。",
        "先手工完成一个单元，再让工具的结果与这个单元一致。"]),
    "Model the Domain": ("为领域建模", [
        "把领域放进一个让非法状态不可能出现的结构里。",
        "维护一份领域术语表。",
        "如果代码已经清晰且局部，就不要动它。"]),
    "Boundary Discipline": ("边界纪律", [
        "在数据进入的地方检查它。",
        "在内部，信任它。",
        "把业务逻辑放在纯函数里。"]),
    "Type System Discipline": ("类型系统纪律", [
        "让非法值无法被写出来。",
        "外部数据在进入的地方解析一次。",
        "不要压制编译器。"]),
    "Make Operations Idempotent": ("让操作幂等", [
        "运行两次，或在中途崩溃后再次运行，最终都处于同一状态。"]),
    "Separate Before Serializing Shared State": ("先分离，再串行化共享状态", [
        "如果它们不需要同一个可变的东西，就给每个参与者各自一份。",
        "如果需要，就只允许一个写入者，并在结构上强制这一点。"]),
    "Fix Root Causes": ("修复根因", [
        "复现它。",
        "修复原因。",
        "只是掩盖崩溃的守卫不是修复。"]),
    "Sequence work into verifiable units": ("把工作排成可验证的单元", [
        "完成一个小单元并检查它。",
        "然后再开始下一个。"]),
    "Test Behavior, Not Implementation": ("测试行为，而非实现", [
        "测试以使用者调用代码的方式调用它，并检查使用者会看到的结果。",
        "如果每个函数都什么也不返回时测试仍然会通过，就扔掉这个测试。"]),
    "Crapper": ("Crapper", [
        "使用 crapper 工具",
        "通过拆分、测试或两者兼用，把每个函数的 CRAP 降到 10 以下。",
        "考虑 case 语句是否值得削减。"]),
    "Dryer": ("Dryer", [
        "使用 dryer 工具消除评分在 0.8 或以上的重复。"]),
    "Mutator": ("Mutator", [
        "使用 mutator 工具",
        "覆盖未被覆盖的部分。",
        "杀死存活的变异体。",
        "删除死代码。"]),
    "Refactoring": ("重构", [
        "钉住代码现在的行为。",
        "改变结构。",
        "证明行为没有改变。"]),
    "Keep a Log": ("保持日志", [
        "记录你采取的每一个行动，以及采取它的原因。",
        "完成时汇报这份日志。"]),
    "Guard the Context Window": ("守护上下文窗口", [
        "保持主线程精简。",
        "把大块内容送到别处，只保留摘要。"]),
    "Worktree Cleanup": ("Worktree 清理", [
        "找出可以安全删除的内容，确认仍在使用的东西都不需要它，然后回收磁盘空间。",
        "未提交的工作等待决定。"]),
    "Commit and Push": ("提交与推送", [
        "经常提交，提交要小且有序。",
        "每次提交都说明原因、改了什么，以及你如何证明它。",
        "最后推送到主线。"]),
}

missing = set(ZH) ^ set(sections)
assert not missing, f"section mismatch: {missing}"
for title, (_, items) in ZH.items():
    bullets = [l for l in sections[title]["lines"] if l.startswith("* ")]
    assert len(bullets) == len(items), f"bullet count differs: {title}"


def zh_heading(title):
    name = ZH[title][0]
    return name if name == title else f"{name}（{title}）"


def zh_section(title):
    level = "###" if sections[title]["level"] == 3 else "##"
    body = "\n".join(f"* {item}" for item in ZH[title][1])
    return f"{level} {zh_heading(title)}\n\n{body}"


def en_sections(titles):
    out, arch_open = [], False
    for t in titles:
        if t in ARCH and not arch_open:
            out.append("## Architecture")
            arch_open = True
        out.append(verbatim(t))
    return "\n\n".join(out)


def zh_sections(titles):
    out, arch_open = [], False
    for t in titles:
        if t in ARCH and not arch_open:
            out.append("## 架构（Architecture）")
            arch_open = True
        out.append(zh_section(t))
    return "\n\n".join(out)


GATES_EN = {
    "ub-crap": """## Running crapper (local addition, not part of ub-mode)

* crapper scores Clojure, Java, Go, TypeScript, Rust, and Python: <https://github.com/unclebob/crapper>.
* From the project root, run `<crapper-checkout>/crapper --changed` to score the functions in git additions and edits. Drop `--changed` to score the whole tree.
* The table lists the worst score first; every function at 10 or above still needs work. `--threshold 10` makes the run exit 2 when the worst score is above 10.
* Without a coverage report, `--no-coverage` scores complexity only; report CRAP as not measured.
* If crapper is missing or does not support the project's language, say the check did not run. Do not report it as passed.""",
    "ub-dry": """## Running dryer (local addition, not part of ub-mode)

* dryer compares Clojure, Java, Go, TypeScript, Rust, and Python: <https://github.com/unclebob/dryer>.
* From the project root, run `<dryer-checkout>/dryer --changed --threshold 0.8`. ub-mode sets 0.8; dryer's own default is 0.82.
* dryer skips forms shorter than four lines unless `--min-lines` says otherwise.
* If dryer is missing or does not support the project's language, say the check did not run. Do not report it as passed.""",
    "ub-mutate": """## Running mutator (local addition, not part of ub-mode)

* mutator tests Clojure, Java, Go, TypeScript, Rust, and Python: <https://github.com/unclebob/mutator>. It needs crapper checked out next to it, at `../crapper`.
* Start with the file you are working on: `<mutator-checkout>/mutator path/to/file`, or `--changed` for git additions and edits. A first run over a whole tree executes every covered mutant.
* Exit 0: every executed mutant was killed. Exit 2: the baseline tests fail; fix them first. Exit 3: a mutant survived.
* If mutator is missing or does not support the project's language, say the check did not run. Do not report it as passed.""",
    "ub-ship": """## Pushing (local addition, not part of ub-mode)

* Repository rules and the user's authorization decide whether, when, and where to push.""",
}

GATES_ZH = {
    "ub-crap": """## 运行 crapper（本地补充，不属于 ub-mode 原文）

* crapper 支持 Clojure、Java、Go、TypeScript、Rust 和 Python：<https://github.com/unclebob/crapper>。
* 在项目根目录运行 `<crapper-checkout>/crapper --changed`，为 git 新增和修改的函数打分；去掉 `--changed` 则检查整棵目录树。
* 结果表按分数从高到低排列；分数为 10 或以上的函数仍需处理。加上 `--threshold 10`，最高分超过 10 时以退出码 2 结束。
* 没有覆盖率报告时，`--no-coverage` 只计算复杂度；此时报告 CRAP 未测量。
* crapper 未安装或不支持项目语言时，说明该检查未执行，不得报告为通过。""",
    "ub-dry": """## 运行 dryer（本地补充，不属于 ub-mode 原文）

* dryer 支持 Clojure、Java、Go、TypeScript、Rust 和 Python：<https://github.com/unclebob/dryer>。
* 在项目根目录运行 `<dryer-checkout>/dryer --changed --threshold 0.8`。ub-mode 规定 0.8；dryer 自身默认值是 0.82。
* 除非用 `--min-lines` 另行指定，dryer 会跳过少于四行的代码块。
* dryer 未安装或不支持项目语言时，说明该检查未执行，不得报告为通过。""",
    "ub-mutate": """## 运行 mutator（本地补充，不属于 ub-mode 原文）

* mutator 支持 Clojure、Java、Go、TypeScript、Rust 和 Python：<https://github.com/unclebob/mutator>。它要求 crapper 签出在相邻的 `../crapper`。
* 从正在修改的文件开始：`<mutator-checkout>/mutator path/to/file`，或用 `--changed` 检查 git 新增和修改。首次对整棵目录树运行时，会执行所有被覆盖的变异体。
* 退出码 0：执行的变异体全部被杀死。退出码 2：基线测试失败，先修复它。退出码 3：有变异体存活。
* mutator 未安装或不支持项目语言时，说明该检查未执行，不得报告为通过。""",
    "ub-ship": """## 推送（本地补充，不属于 ub-mode 原文）

* 是否推送、何时推送、推送到哪里，由仓库规则和用户授权决定。""",
}

# name, sections, en description, zh description, en display, zh display, en prompt, zh prompt
ATOMS = [
    ("ub-lazy", ["Laziness Protocol", "Subtract Before You Add"],
     "Keep one decision in one place, ship the smallest edit that solves the problem, and take complexity out before adding anything.",
     "一个决定只放在一处，交付能解决问题的最小改动，添加任何东西之前先去掉复杂性。",
     "UB · Lazy", "UB · 最小改动",
     "Use $ub-lazy to make the smallest change that solves this.", "使用 $ub-lazy，用最小改动解决这个问题。"),
    ("ub-foundation", ["Foundational Thinking"],
     "Get the data shape right before writing logic, do first what helps every later phase, and do not share state a concurrent writer would touch.",
     "写逻辑之前先把数据形状弄对，先做对后续每个阶段都有帮助的事，并发写入者会造成影响时不共享状态。",
     "UB · Foundation", "UB · 基础思维",
     "Use $ub-foundation to settle the data shape before writing the logic.", "使用 $ub-foundation，写逻辑之前先定数据形状。"),
    ("ub-redesign", ["Redesign From First Principles"],
     "Do not bolt a new requirement onto the old design; design it as if it had been there from the start, and deliver it in pieces.",
     "不把新需求硬接到旧设计上；按它从一开始就存在来设计，并分块交付。",
     "UB · Redesign", "UB · 第一性原理重设计",
     "Use $ub-redesign to fit this requirement into the design.", "使用 $ub-redesign，把这个需求融入设计。"),
    ("ub-domain", ["Model the Domain", "Boundary Discipline", "Type System Discipline"],
     "Model the domain so illegal states are impossible, check data where it enters and trust it inside, and do not silence the compiler.",
     "为领域建模，让非法状态不可能出现；在数据进入处检查、在内部信任它；不压制编译器。",
     "UB · Domain", "UB · 领域、边界与类型",
     "Use $ub-domain to model this domain, its boundaries, and its types.", "使用 $ub-domain，为这个领域的模型、边界和类型做设计。"),
    ("ub-state", ["Make Operations Idempotent", "Separate Before Serializing Shared State"],
     "Make operations end in the same state after a rerun or crash, and separate shared mutable state or allow one enforced writer.",
     "让操作在重复运行或中途崩溃后都结束于同一状态；分离共享的可变状态，或只允许一个受结构约束的写入者。",
     "UB · State", "UB · 幂等与共享状态",
     "Use $ub-state to make this operation idempotent and its shared state safe.", "使用 $ub-state，让这个操作幂等、共享状态安全。"),
    ("ub-tdd", ["TDD", "Test Behavior, Not Implementation"],
     "Write the failing test first, see it fail for the expected reason, make the smallest passing change, and test behavior, not implementation.",
     "先写会失败的测试，确认它因预期原因失败，做最小改动让它通过，并测试行为而非实现。",
     "UB · TDD", "UB · TDD",
     "Use $ub-tdd to drive this change with a failing test first.", "使用 $ub-tdd，先写失败的测试来驱动这次改动。"),
    ("ub-root-cause", ["Fix Root Causes", "Attack the Premise"],
     "Reproduce, fix the cause rather than hide the crash, and attack the shared premise when two fixes fail the same gate.",
     "先复现，修复原因而不掩盖崩溃；两个修复在同一关卡失败时，质疑它们共享的前提。",
     "UB · Root Cause", "UB · 根因与前提",
     "Use $ub-root-cause to reproduce and fix the cause of this defect.", "使用 $ub-root-cause，复现并修复这个缺陷的根因。"),
    ("ub-execute", ["Outcome-Oriented Execution", "Build the Lever", "Sequence work into verifiable units"],
     "Aim at a checkable end state, build the tool when the work is not obvious, and finish and check one small unit before the next.",
     "瞄准可检验的最终状态，工作无法一眼看清时构建工具，完成并检查一个小单元后再开始下一个。",
     "UB · Execute", "UB · 结果、杠杆与小单元",
     "Use $ub-execute to plan and run this multi-step change in verifiable units.", "使用 $ub-execute，把这次多步改动拆成可验证的单元来执行。"),
    ("ub-refactor", ["Refactoring"],
     "Pin what the code does, change the structure, and prove the behavior did not change.",
     "钉住代码现在的行为，改变结构，并证明行为没有改变。",
     "UB · Refactor", "UB · 重构",
     "Use $ub-refactor to restructure this code without changing its behavior.", "使用 $ub-refactor，在不改变行为的前提下重构这段代码。"),
    ("ub-crap", ["Crapper"],
     "Run crapper and bring every function under CRAP 10 by splitting it, testing it, or both.",
     "运行 crapper，通过拆分、测试或两者兼用，把每个函数的 CRAP 降到 10 以下。",
     "UB · Crapper", "UB · CRAP 检查",
     "Use $ub-crap to score the changed functions and reduce any at CRAP 10 or above.", "使用 $ub-crap，为改动的函数打分并降低 CRAP 不低于 10 的函数。"),
    ("ub-dry", ["Dryer"],
     "Run dryer and eliminate duplication that ranks 0.8 or above.",
     "运行 dryer，消除评分在 0.8 或以上的重复。",
     "UB · Dryer", "UB · 重复检查",
     "Use $ub-dry to find and remove duplication in the changed code.", "使用 $ub-dry，找出并消除改动代码中的重复。"),
    ("ub-mutate", ["Mutator"],
     "Run mutator to cover the uncovered, kill surviving mutants, and delete dead code.",
     "运行 mutator，覆盖未被覆盖的部分，杀死存活的变异体，并删除死代码。",
     "UB · Mutator", "UB · 变异测试",
     "Use $ub-mutate to mutation-test the file I am changing.", "使用 $ub-mutate，对我正在修改的文件做变异测试。"),
    ("ub-ship", ["Keep a Log", "Commit and Push"],
     "Log every action with its reason, report the log on completion, and commit often in small ordered commits that say why, what, and how it was proved.",
     "记录每个行动及原因并在完成时汇报；经常提交，提交小而有序，并说明原因、改动和证明方式。",
     "UB · Ship", "UB · 日志与提交",
     "Use $ub-ship to log this work and commit it in small ordered commits.", "使用 $ub-ship，记录这项工作并以小而有序的提交收尾。"),
]


def frontmatter(name, description, language, pair):
    desc = description.replace('"', '\\"')
    return (f"---\nname: {name}\ndescription: \"{desc}\"\n"
            f"disable-model-invocation: true\nlicense: MIT\nmetadata:\n"
            f"  language: {language}\n  translation_of: {pair}\n  version: \"{VERSION}\"\n---\n")


def openai_yaml(display, short, prompt):
    return (f"interface:\n  display_name: \"{display}\"\n  short_description: \"{short}\"\n"
            f"  default_prompt: \"{prompt}\"\npolicy:\n  allow_implicit_invocation: false\n")


def stages_of(titles):
    seen = []
    for t in titles:
        s = sections[t]["stage"]
        if s not in seen:
            seen.append(s)
    return seen


SOURCE_EN = f"""- Author: Robert C. Martin (Uncle Bob)
- Repository: <https://github.com/unclebob/ub-mode>
- File: `SKILL.md`, Git blob `{BLOB}` (commit `{COMMIT}`, 2026-11-02)
- License: MIT, reproduced below"""

SOURCE_ZH = f"""- 作者：Robert C. Martin（Uncle Bob）
- 仓库：<https://github.com/unclebob/ub-mode>
- 文件：`SKILL.md`，Git blob `{BLOB}`（commit `{COMMIT}`，2026-11-02）
- 许可：MIT，全文见下"""

SHAPE_EN = ("handy-skills splits ub-mode into one explicit command per discipline so you can combine them per task. "
            "The one-command shape follows the `bro` skill in Lauren Tan's pstack; no pstack text is used.")
SHAPE_ZH = ("handy-skills 把 ub-mode 拆成每项纪律一个显式命令，按任务自由组合。"
            "“一个技能对应一个命令”的形状借鉴 Lauren Tan 的 pstack 中的 `bro` 技能，未使用 pstack 的任何文字。")


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip("\n") + "\n", encoding="utf-8")


def gen_atom(name, titles, d_en, d_zh, disp_en, disp_zh, p_en, p_zh):
    en_dir = REPO / "plugins/ub-discipline/skills" / name
    zh_dir = REPO / "plugins/ub-discipline-cn/skills" / f"{name}-cn"
    stages = stages_of(titles)
    stage_en = " and ".join(f'"{s}"' for s in stages)
    stage_zh = "和".join(f"“{STAGE_ZH[s]}”" for s in stages)
    sec_en = ", ".join(titles)

    en_body = (f"# {name}\n\nApply these rules to the current task. They are quoted verbatim from {stage_en} "
               f"in Robert C. Martin's ub-mode.\n\n"
               f"{en_sections(titles)}\n")
    if name in GATES_EN:
        en_body += "\n" + GATES_EN[name] + "\n"
    write(en_dir / "SKILL.md", frontmatter(name, f"{d_en} {sec_en} from Robert C. Martin's ub-mode, verbatim. Use only when explicitly invoked.", "en", f"{name}-cn") + "\n" + en_body)
    write(en_dir / "agents/openai.yaml", openai_yaml(disp_en, d_en.split(",")[0].rstrip("."), p_en))

    zh_body = (f"# {name}-cn\n\n把以下规则用于当前任务。规则逐条直译自 Robert C. Martin 的 ub-mode 中{stage_zh}部分。\n\n{zh_sections(titles)}\n")
    if name in GATES_ZH:
        zh_body += "\n" + GATES_ZH[name] + "\n"
    write(zh_dir / "SKILL.md", frontmatter(f"{name}-cn", f"{d_zh}译自 Robert C. Martin 的 ub-mode：{'、'.join(ZH[t][0] for t in titles)}。仅显式调用。", "zh-CN", name) + "\n" + zh_body)
    write(zh_dir / "agents/openai.yaml", openai_yaml(disp_zh, d_zh.split("，")[0].rstrip("。"), p_zh))
    originals = "\n\n".join(verbatim(t) for t in titles)


def gen_full():
    en_dir, zh_dir = REPO / "plugins/ub-discipline/skills/ub-mode", REPO / "plugins/ub-discipline-cn/skills/ub-mode-cn"
    desc_en = ("Follow the reduced principles when writing or changing code. Every change follows First Make it Work, "
               "then Then Make it Right, then Follow Practice. Use when the user runs /ub-mode or asks for the reduced principles.")
    assert " ".join(desc_en.split()) in " ".join(upstream_front.split())
    write(en_dir / "SKILL.md", frontmatter("ub-mode", desc_en, "en", "ub-mode-cn") + upstream_body.rstrip("\n").lstrip("\n").join(["\n", "\n"]))
    write(en_dir / "agents/openai.yaml", openai_yaml("UB Mode", "Every ub-mode discipline at once, verbatim", "Use $ub-mode to make this change, verify each step, and report the log."))

    parts = ["# ub-mode\n\n每次被要求做出改动时，遵循：\n* 先让它能工作。\n* 再让它正确。\n* 遵循实践"]
    order = [t for t in sections]
    current_stage, arch_open = None, False
    for t in order:
        s = sections[t]["stage"]
        if s != current_stage:
            parts.append(f"# {STAGE_ZH[s]}")
            current_stage = s
        if t in ARCH and not arch_open:
            parts.append("## 架构（Architecture）")
            arch_open = True
        parts.append(zh_section(t))
    desc_zh = "编写或修改代码时遵循精简原则。每次改动都依次遵循：先让它能工作，再让它正确，再遵循实践。在用户运行 /ub-mode-cn 或要求使用精简原则时使用。"
    write(zh_dir / "SKILL.md", frontmatter("ub-mode-cn", desc_zh, "zh-CN", "ub-mode") + "\n" + "\n\n".join(parts) + "\n")
    write(zh_dir / "agents/openai.yaml", openai_yaml("UB Mode · 工程纪律", "一次启用 ub-mode 全部纪律，逐条直译", "使用 $ub-mode-cn 完成这次改动，逐步验证并汇报日志。"))


gen_full()
for atom in ATOMS:
    gen_atom(*atom)

covered = {t for a in ATOMS for t in a[1]}
print("not atomized (kept in ub-mode only):", sorted(set(sections) - covered))
print("generated", 2 * (len(ATOMS) + 1), "packages")


import json
for name, desc, tags in [
    ("ub-discipline", "Robert C. Martin's ub-mode, verbatim: one full skill plus 13 atomic skills you combine per task. Inspired by unclebob/ub-mode; the one-command shape follows the bro skill in Lauren Tan's pstack. Not an official release.", ["ub-mode", "tdd", "refactoring", "quality-gates"]),
    ("ub-discipline-cn", "Robert C. Martin 的 ub-mode 逐条直译：1 个完整版加 13 个可按任务组合的原子技能。灵感来自 unclebob/ub-mode，“一个技能一个命令”借鉴 Lauren Tan 的 pstack 中的 bro 技能。非官方发布。", ["ub-mode", "tdd", "refactoring", "quality-gates", "zh-CN"]),
]:
    d = REPO / "plugins" / name
    write(d / ".claude-plugin/plugin.json", json.dumps({"name": name, "version": VERSION, "description": desc, "author": {"name": "ub-discipline contributors"}, "homepage": "https://github.com/unclebob/ub-mode", "license": "MIT", "keywords": tags, "skills": "./skills/"}, ensure_ascii=False, indent=2))
    how = "unchanged." if name == "ub-discipline" else "translated line by line."
    write(d / "LICENSE", f"Source: https://github.com/unclebob/ub-mode, SKILL.md, Git blob {BLOB} (commit {COMMIT}, 2026-11-02).\nThe rule text in this plugin is that file, {how}\n\n{MIT}")
