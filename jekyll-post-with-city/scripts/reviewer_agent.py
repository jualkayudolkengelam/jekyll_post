#!/usr/bin/env python3
"""
Reviewer Agent — final QA sebelum commit.
Returns: True (APPROVED) or False (REJECTED).
"""

import re
import sys
from pathlib import Path


def review(final_path: str, template_path: str = None) -> bool:
    """
    Run final checks. Returns True if all pass, False otherwise.
    """
    print(f"[Reviewer] Checking: {final_path}")

    content = Path(final_path).read_text()

    checks = {
        "layout_correct": ("layout: node--post-with-city", "layout node--post-with-city"),
        "images_section": ("images:", "images frontmatter"),
        "images_alt_section": ("images_alt:", "images_alt frontmatter"),
        "no_placeholder_tulis": (None, "no 'tulis...' placeholder"),
        "no_placeholder_isi": (None, "no 'isi...' placeholder"),
        "no_placeholder_berikan": (None, "no 'berikan...' placeholder"),
        "telepon_present": ("081311400177", "telepon 081311400177"),
        "whatsapp_present": ("081311400177", "whatsapp 081311400177"),
    }

    all_pass = True

    for key, (pattern, desc) in checks.items():
        if pattern is None:
            # Negative checks
            fail = re.search(r'\b(tulis|isi|berikan)\.{3}\b', content, re.IGNORECASE)
            passed = fail is None
        else:
            passed = pattern in content

        status = "✅" if passed else "❌"
        print(f"  {status} {desc}")
        if not passed:
            all_pass = False

    # Check template sections exist (if template provided)
    if template_path and Path(template_path).exists():
        template = Path(template_path).read_text()
        # Extract section headers from template
        template_sections = re.findall(r'# SECTION ([^(]+)', template)
        for sec in template_sections:
            sec_clean = sec.strip()
            if sec_clean:
                found = sec_clean in content
                status = "✅" if found else "❌"
                print(f"  {status} Section: {sec_clean}")
                if not found:
                    all_pass = False

    if all_pass:
        print("\n[Reviewer] ✅ APPROVED")
    else:
        print("\n[Reviewer] ❌ REJECTED — fix issues above")

    return all_pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: reviewer_agent.py <final.md> [template.md]")
        sys.exit(1)

    final_path = sys.argv[1]
    template_path = sys.argv[2] if len(sys.argv) > 2 else None

    ok = review(final_path, template_path)
    sys.exit(0 if ok else 1)