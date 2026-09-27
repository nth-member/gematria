#!/usr/bin/env python3
"""Build the gematria site's data from the two programs.

    python3 build.py

The programs' folder is named by GEMATRIA, or else by the first line of the local,
untracked file .programs beside this script.

Writes docs/data/tables.json: the programs' own letter table and control-character
names, so the page carries no hand-typed copy of either. Nothing else is published.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOCAL = HERE / ".programs"
SRC = Path(os.path.expanduser(os.environ.get("GEMATRIA")
                              or (LOCAL.read_text().splitlines()[0].strip() if LOCAL.exists() else "")))
if not (SRC / "gematria_names.py").exists():
    sys.exit(f"build.py: the programs are not at {SRC!s:.60}; set GEMATRIA or write their folder in .programs")
sys.path.insert(0, str(SRC))
sys.dont_write_bytecode = True  # import the programs without leaving a __pycache__ beside them
import ascii_name_sum  # noqa: E402
import gematria_names  # noqa: E402

DATA = HERE / "docs" / "data"


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    tables = {
        "values": gematria_names.VALUES,
        "control_names": {str(k): v for k, v in ascii_name_sum.CONTROL_NAMES.items()},
    }
    (DATA / "tables.json").write_text(json.dumps(tables, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("tables: the programs' letter values and control names")


if __name__ == "__main__":
    main()
