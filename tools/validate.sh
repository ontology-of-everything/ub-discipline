#!/usr/bin/env bash
# Regenerate into a temp copy, require no drift, then check upstream fidelity and plugin manifests.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
BLOB=9ac940b23b61d77e8e5192721d7b6066357f892c
[[ "$(git hash-object "$ROOT/upstream/SKILL.md")" == "$BLOB" ]] || { echo "FAIL: upstream/SKILL.md is not blob $BLOB" >&2; exit 1; }
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/tools" "$TMP/upstream"; cp "$ROOT/tools/sync.py" "$TMP/tools/"; cp "$ROOT/upstream/SKILL.md" "$TMP/upstream/"
python3 "$TMP/tools/sync.py" >/dev/null
diff -r "$TMP/plugins" "$ROOT/plugins" >/dev/null || { echo "FAIL: plugins/ differs from tools/sync.py output; run tools/sync.py" >&2; exit 1; }
python3 - "$ROOT" <<'PY'
import sys
from pathlib import Path
root = Path(sys.argv[1])
omit = {"Crapper", "Dryer", "Mutator"}
skills = root / "plugins/ub-discipline/skills"
up_lines = set((root/"upstream/SKILL.md").read_text().split("---", 2)[2].splitlines())
full = (skills/"ub-mode/SKILL.md").read_text().split("---", 2)[2]
for title in omit:
    assert f"## {title}" not in full, f"ub-mode still contains {title}"
for name in ("ub-crap", "ub-dry", "ub-mutate"):
    assert not (skills/name).exists(), f"tool skill still present: {name}"
for p in skills.glob("ub-*/SKILL.md"):
    for line in p.read_text().split("---", 2)[2].splitlines():
        if line.startswith("### ") or line.startswith("## "):
            if line == "## Architecture":
                continue
            assert line in up_lines, f"{p.parent.name}: not verbatim: {line}"
        elif line.startswith("* "):
            assert line in up_lines, f"{p.parent.name}: not verbatim: {line}"
print("OK: upstream fidelity")
PY
if command -v claude >/dev/null; then
  for d in "$ROOT" "$ROOT/plugins/ub-discipline" "$ROOT/plugins/ub-discipline-hans"; do claude plugin validate "$d" >/dev/null; done
  echo "OK: plugin manifests"
fi
echo "OK: ub-discipline checks passed"
