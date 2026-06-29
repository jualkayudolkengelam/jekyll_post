# jekyll_post — Hermes Skills for Jekyll Content Automation

A collection of Hermes skills to generate Jekyll posts automatically using a multi-agent workflow (Research → Writer → Editor → Reviewer).

## Available Skills

| Skill | Description |
|-------|-------------|
| `jekyll-post-with-city` | Generate Jekyll post for a city using `TEMPLATE--post-with-city.md` — research city data, fill all frontmatter sections, auto-validate YAML. |

## Installation

```bash
hermes skill install github.com/jualkayudolkengelam/jekyll_post#jekyll-post-with-city
```

## Usage

```bash
hermes skill run jekyll-post-with-city --param city="Maros" --output _post_with_city/2026-06-29-jual-kayu-dolken-maros.md
```

Or directly from Python (cross-AI compatible):

```bash
python3 jekyll-post-with-city/entrypoint.py \
  --city "Maros" \
  --template "TEMPLATES/TEMPLATE--post-with-city.md" \
  --output "_post_with_city/2026-06-29-jual-kayu-dolken-maros.md"
```

## License

MIT
