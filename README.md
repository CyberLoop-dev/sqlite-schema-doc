<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0f766e&height=170&section=header&text=SQLite%20Schema%20Doc&fontColor=ffffff&fontSize=34" alt="SQLite Schema Doc banner"/></p>
<p align="center"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=19&duration=2800&pause=900&center=true&vCenter=true&width=620&lines=Document%20a%20SQLite%20database%3BExplore%20tables%20and%20indexes%3BGenerate%20a%20portable%20HTML%20report" alt="Typing title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/sqlite-schema-doc?style=flat-square"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/sqlite-schema-doc?style=flat-square"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/sqlite-schema-doc?style=flat-square"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/sqlite-schema-doc?style=flat-square"/></p>
<p align="center"><img src="assets/mark.svg" width="520" alt="SQLite Schema Doc illustration"/></p>

## 🧭 Overview
SQLite Schema Doc opens a local database in read-only mode and generates a portable HTML data dictionary for tables and views, including columns, indexes, and foreign-key relationships.

## ✨ Features
- 🗃️ List tables and views with their SQL definitions
- 🧱 Document column types, primary keys, and nullability
- 🔗 Show indexes and foreign-key relationships
- 🔒 Open the database read-only; never modify schema or data

## 🖥️ Demo
No hosted demo is provided. Run the project locally using the quick-start command.

## 🚀 Quick Start
Requires Python 3.10 or newer.

```bash
python main.py ./example.db --output schema-report.html
```

Run checks with `python -m unittest discover -s tests -v`.

## 🧰 Tech Stack
- Python standard library
- `argparse` CLI and `unittest`
- Read-only inspection by default

## 🗂️ Folder Structure
```text
.
├── .github/workflows/ci.yml
├── assets/mark.svg
├── tests/test_main.py
├── main.py
├── pyproject.toml
└── README.md
```

## 🗺️ Roadmap
- [ ] Add more edge-case fixtures
- [ ] Improve machine-readable output
- [ ] Keep the core workflow lightweight and local-first

## 🤝 Contributing
Issues and focused pull requests are welcome. Add regression tests for parser and reporting changes.

## 📄 License
MIT License. See [LICENSE](LICENSE).
<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:0f172a&height=100&section=footer" alt="Animated wave footer"/></p>
