#!/usr/bin/env python3
"""
Writer Agent — isi TEMPLATE--post-with-city.md dengan data riset.
Output: draft markdown dengan semua field frontmatter terisi.
"""

import json
import re
import sys
from pathlib import Path


def fill_template(template: str, data: dict) -> str:
    """
    Replace {key} placeholders in template with values from data dict.
    Supports dot-notation: {key.subkey}
    Supports list indexing: {list.0.field}
    """
    def resolve(d, key):
        parts = key.split(".")
        val = d
        for p in parts:
            if isinstance(val, list) and p.isdigit():
                val = val[int(p)]
            elif isinstance(val, dict):
                val = val.get(p, "")
            else:
                return ""
        return str(val) if val is not None else ""

    def replacer(m):
        return resolve(data, m.group(1).strip())

    return re.sub(r"\{([^}]+)\}", replacer, template)


def write(city: str, data: dict, template_path: str, output_path: str) -> str:
    """
    Fill template with research data and write draft.
    Returns path to draft file.
    """
    print(f"[Writer] Template: {template_path}")
    print(f"[Writer] Output:   {output_path}")

    template = Path(template_path).read_text()
    filled = fill_template(template, data)

    Path(output_path).write_text(filled)
    print(f"[Writer] Draft written — {len(filled)} chars")

    # Check for unfilled placeholders
    unfilled = len(re.findall(r"\{[^}]+\}", filled))
    if unfilled:
        print(f"[Writer] Warning: {unfilled} unfilled placeholder(s) remain")
    else:
        print("[Writer] All placeholders filled ✅")

    return output_path


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: writer_agent.py <city> <data.json> <template.md> [output.md]")
        sys.exit(1)

    city = sys.argv[1]
    data = json.loads(Path(sys.argv[2]).read_text())
    template_path = sys.argv[3]
    output_path = sys.argv[4] if len(sys.argv) > 4 else f"/tmp/{city}-draft.md"

    write(city, data, template_path, output_path)
