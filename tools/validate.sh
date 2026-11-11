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
up = (root/"upstream/SKILL.md").read_text().split("---", 2)[2].strip()
full = (root/"plugins/ub-discipline/skills/ub-mode/SKILL.md").read_text().split("---", 2)[2].strip()
assert up == full, "ub-mode body differs from upstream"
lines = set(up.splitlines())
for p in (root/"plugins/ub-discipline/skills").glob("ub-*/SKILL.md"):
    rules = p.read_text().split("---", 2)[2].split("(local addition")[0]
    for l in rules.splitlines():
        if (l.startswith("* ") or l.startswith("##")) and not l.startswith("## Running") and not l.startswith("## Pushing"):
            assert l in lines, f"{p.parent.name}: not verbatim: {l}"
print("OK: upstream fidelity")
PY
if command -v claude >/dev/null; then
  for d in "$ROOT" "$ROOT/plugins/ub-discipline" "$ROOT/plugins/ub-discipline-cn"; do claude plugin validate "$d" >/dev/null; done
  echo "OK: plugin manifests"
fi
echo "OK: ub-discipline checks passed"
