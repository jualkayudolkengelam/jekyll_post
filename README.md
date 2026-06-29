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

## Agent Workflow

Setiap post dihasilkan oleh pipeline 4 agen AI yang berjalan secara berurutan:

```
Input (Nama Kota)
     ↓
[Research] → data.json (riset kota: sejarah, ekonomi, wisata, kuliner, dll.)
     ↓
[Writer]   → draft.md (isi TEMPLATE dengan data riset)
     ↓
[Editor]   → polished.md (validasi YAML + perbaikan bahasa)
     ↓
[Reviewer] → APPROVED / REJECT → Commit & Push
```

### Research Agent
| Aspek | Detail |
|-------|--------|
| **Tugas** | Mengumpulkan data akurat tentang kota target: luas wilayah, populasi, kecamatan, sejarah, ekonomi, wisata, kuliner |
| **System Prompt** | *"Anda adalah Research Agent. Cari data akurat tentang [KOTA]. Output JSON terstruktur — semua field untuk template post-with-city."* |
| **Output** | `data/{kota}.json` (JSON valid) |

### Writer Agent
| Aspek | Detail |
|-------|--------|
| **Tugas** | Mengonversi JSON riset ke dalam template, mengisi semua field YAML (tagline, deskripsi, overview, tentang_kota_1..4, keunggulan, aplikasi, studi kasus, testimoni, FAQ, dll.) |
| **System Prompt** | *"Anda adalah Writer Agent. Isi SEMUA field YAML di template menggunakan data JSON. Ikuti struktur nested list dengan indentasi presisi. Gunakan <strong> di list_item sesuai template."* |
| **Output** | `draft/{kota}.md` |

### Editor Agent
| Aspek | Detail |
|-------|--------|
| **Tugas** | Memvalidasi sintaks YAML, memperbaiki bahasa menjadi persuasif & natural, memastikan tidak ada placeholder tersisa |
| **System Prompt** | *"Anda adalah Editor Agent. Validasi YAML: quotes lengkap, indentasi konsisten, tidak ada trailing whitespace. Bahasa: natural Bahasa Indonesia, tidak terasa AI. Completeness: tidak ada placeholder 'tulis...' atau 'isi...'."* |
| **Output** | `draft/{kota}-edited.md` |

### Reviewer Agent
| Aspek | Detail |
|-------|--------|
| **Tugas** | Verifikasi akhir: bandingkan dengan template, cek path gambar, cek layout. Beri APPROVED atau rejection notes |
| **System Prompt** | *"Anda adalah Reviewer Agent. Bandingkan hasil dengan TEMPLATE—tidak ada section hilang. Path gambar benar. Layout: node--post-with-city. Jika OK → APPROVED; jika tidak → kembali ke Editor."* |
| **Output** | `APPROVED` + final `.md` atau `REJECT` + catatan |

## Keuntungan Multi-Agent
- **Efisien token**: setiap agen hanya konsumsi token untuk tugas spesifik, bukan seluruh pipeline
- **Skalabel**: satu Research Agent bisa riset 3 kota paralel sementara Writer Agent nulis kota lain
- **Traceable**: setiap langkah tercatat sebagai commit terpisah
- **Cross-AI**: bisa dijalankan dari Hermes, Claude Code CLI, GitHub Actions, atau Python langsung

## Repository Structure

```
jekyll_post/
├── jekyll-post-with-city/       # Skill utama
│   ├── SKILL.md                  # Dokumentasi skill
│   ├── entrypoint.py             # Entrypoint generik (cross-LLM)
│   ├── scripts/                  # Skrip agen
│   │   ├── research_agent.py
│   │   ├── writer_agent.py
│   │   ├── editor_agent.py
│   │   └── reviewer_agent.py
│   ├── templates/
│   │   └── TEMPLATE--post-with-city.md
│   └── references/
│       └── ...
├── README.md
└── LICENSE
```

## License

MIT
