#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# inject_version_cell.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

"""
Inject a version/change metadata cell at the top of each converted notebook.

For every .ipynb file found under --notebooks-dir, the script looks up the
corresponding entry in examples.yml (matched by path) and inserts a markdown
cell at position 0 containing:

    **Built for NEST version MAJOR.MINOR.**

    *This example has <last_change>.* (only if last_change != "no change")

Usage:
    python inject_version_cell.py \\
        --notebooks-dir notebooks/notebooks \\
        --examples-yml  nest-simulator/pynest/examples/examples.yml \\
        --nest-version  3.10
"""

import argparse
import sys
from pathlib import Path

import nbformat
import yaml

NO_CHANGE = "no change"


def build_cell_source(nest_version: str, last_change: str) -> str:
    lines = [f"**Built for NEST version {nest_version}.**"]
    if last_change and last_change != NO_CHANGE:
        # last_change is e.g. "changes since version v3.9" or "new since version v3.9"
        lines.append(f"*This example has {last_change}.*")
    return "\n\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Inject version/change cell into converted notebooks")
    parser.add_argument("--notebooks-dir", required=True, help="Directory containing .ipynb files")
    parser.add_argument("--examples-yml", required=True, help="Path to pynest/examples/examples.yml")
    parser.add_argument("--nest-version", required=True, help="NEST MAJOR.MINOR version string, e.g. 3.10")
    args = parser.parse_args()

    notebooks_dir = Path(args.notebooks_dir).resolve()
    examples_yml = Path(args.examples_yml).resolve()

    if not notebooks_dir.is_dir():
        print(f"ERROR: notebooks-dir not found: {notebooks_dir}", file=sys.stderr)
        sys.exit(1)

    if not examples_yml.exists():
        print(f"ERROR: examples-yml not found: {examples_yml}", file=sys.stderr)
        sys.exit(1)

    with examples_yml.open() as f:
        data = yaml.safe_load(f)

    # Build lookup: examples.yml path value -> last_change
    by_path = {e["path"]: e.get("last_change", NO_CHANGE) for e in data["examples"]}

    notebooks = sorted(notebooks_dir.rglob("*.ipynb"))
    if not notebooks:
        print("No .ipynb files found — nothing to do.")
        return

    print(f"Injecting version cell into {len(notebooks)} notebook(s) (NEST {args.nest_version})...")

    for nb_path in notebooks:
        # Map notebook path back to the examples.yml path key:
        #   notebooks/notebooks/pong/run_simulations.ipynb -> pong/run_simulations.py
        rel = nb_path.relative_to(notebooks_dir)
        yml_key = str(rel.with_suffix(".py"))

        last_change = by_path.get(yml_key, NO_CHANGE)
        cell_source = build_cell_source(args.nest_version, last_change)

        nb = nbformat.read(str(nb_path), as_version=4)
        nb.cells.insert(0, nbformat.v4.new_markdown_cell(source=cell_source))
        nbformat.write(nb, str(nb_path))

        tag = f"  [{last_change}]" if last_change != NO_CHANGE else ""
        print(f"  {rel}{tag}")

    print("Done.")


if __name__ == "__main__":
    main()
