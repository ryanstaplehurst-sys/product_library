"""Rebuild every library from sources/. Run from the repo root."""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCES = REPO / "sources"


def main() -> int:
    failures = []
    for src in sorted(SOURCES.glob("*.py")):
        if src.name.startswith("__"):
            continue
        result = subprocess.run([sys.executable, str(src)], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout.rstrip())
        else:
            print(f"FAILED: {src.name}\n{result.stderr}")
            failures.append(src.name)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
