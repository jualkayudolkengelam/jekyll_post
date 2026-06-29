# Template Structure — TEMPLATE--post-with-city.md

## Template Model (Current: Empty-Field)

Two generations of template:

### Gen 1: Instruction Placeholder Model (deprecated)
Fields used natural-language instructions as placeholder values:
```yaml
judul: "tulis judul yang menarik tentang..."
keunggulan_durabilitas: "berikan 3 poin keunggulan..."
```
Scripts had to parse these instructions as both placeholder and prompt, leading to brittle regex-based extraction and inconsistent results.

### Gen 2: Empty-Field Model (current)
All writable fields use empty string `""` as their value:
```yaml
judul: ""
keunggulan_durabilitas: ""
studi_kasus_proyek: ""
```
**Rationale**: The scripts (research_agent → writer_agent → editor_agent → reviewer_agent) each know what content to generate for their stage. Empty fields remove ambiguity — the script fills every `""` field unconditionally, and the instruction text lives in the script code, not in the template.

**Key changes (710 → 943 lines)**:
- All frontmatter placeholders replaced with `""`
- Expanded field sets for completeness (all known sections represented)
- Consistent indentation (2-space key, 4-space list item)
- No duplicate keys (old template had `keunggulan_durabilitas` and `keunggulan_nilai` appearing twice — once as instruction, once as content block)
- Single `studi_kasus_proyek` field (was split across multiple keys)

## Frontmatter Layout

Template frontmatter is structured as:
1. **Identity fields**: `title`, `layout`, `permalink`, etc.
2. **Location fields**: `city`, `province`, `map_embed_url`, etc.
3. **Product fields**: `nama_kayu`, `jenis_kayu`, `keunggulan` sections
4. **SEO/social fields**: `deskripsi`, `keywords`, `og_image`, etc.
5. **Content sections**: `artikel_*`, `studi_kasus_proyek`, `testimoni`, `faq`
6. **Meta fields**: `date`, `last_modified`, `tags`, `categories`, etc.

## How Script Agents Use the Template

Pipeline: **research** → **writer** → **editor** → **reviewer**

1. **Research agent**: Reads template frontmatter keys, researches content for each section, stores results in structured data
2. **Writer agent**: Takes research data, fills template fields by replacing `""` with generated content using YAML-aware parsing
3. **Editor agent**: Post-processes the filled template for consistency, grammar, SEO
4. **Reviewer agent**: Validates all fields are filled, checks formatting, flags issues

Each agent reads/writes the same `.md` file sequentially.
