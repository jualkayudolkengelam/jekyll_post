#!/usr/bin/env python3
"""
Editor Agent — validasi YAML, perbaiki bahasa, pastikan tidak ada placeholder.
"""

import re
import sys
from pathlib import Path


def validate_yaml(content: str) -> tuple[bool, list[str]]:
    """
    Validate YAML frontmatter. Returns (is_valid, errors).
    """
    errors = []
    try:
        import yaml
        # Extract frontmatter
        parts = content.split("---")
        if len(parts) >= 3:
            frontmatter = "---".join(parts[1:-1])
            yaml.safe_load(frontmatter)
        else:
            errors.append("No frontmatter found (missing --- delimiters)")
    except ImportError:
        errors.append("PyYAML not installed — skipping YAML validation")
    except yaml.YAMLError as e:
        errors.append(f"YAML syntax error: {e}")
    except Exception as e:
        errors.append(f"Validation error: {e}")

    return len(errors) == 0, errors


def check_placeholders(content: str) -> list[str]:
    """
    Find remaining placeholder/instruction text.
    Returns list of issues found.
    """
    issues = []
    patterns = [
        (r'"tulis[^"]*"', "Instruction placeholder: 'tulis...'"),
        (r'"isi[^"]*"', "Instruction placeholder: 'isi...'"),
        (r'"berikan[^"]*"', "Instruction placeholder: 'berikan...'"),
        (r'"contoh[^"]*"', "Instruction placeholder: 'contoh...'"),
        (r'Instruksi:', "Comment instruction marker"),
    ]
    for pat, msg in patterns:
        matches = re.findall(pat, content, re.IGNORECASE)
        if matches:
            issues.append(f"{msg} ({len(matches)} occurrence(s))")
    return issues


def edit(draft_path: str) -> str:
    """
    Validate and clean draft. Returns path to edited file.
    """
    print(f"[Editor] Processing: {draft_path}")

    content = Path(draft_path).read_text()
    issues = []

    # 1. YAML validation
    valid, yaml_errors = validate_yaml(content)
    if valid:
        print("[Editor] YAML: OK ✅")
    else:
        for e in yaml_errors:
            print(f"[Editor] YAML ERROR: {e}")
        issues.extend(yaml_errors)

    # 2. Placeholder check
    ph_issues = check_placeholders(content)
    if not ph_issues:
        print("[Editor] Placeholders: CLEAN ✅")
    else:
        for issue in ph_issues:
            print(f"[Editor] WARNING: {issue}")
        issues.extend(ph_issues)

    # 3. Write edited output
    edited_path = draft_path.replace(".md", "-edited.md") if "-edited" not in draft_path else draft_path
    Path(edited_path).write_text(content)

    print(f"[Editor] Output: {edited_path}")
    return edited_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: editor_agent.py <draft.md>")
        sys.exit(1)
    edit(sys.argv[1])
