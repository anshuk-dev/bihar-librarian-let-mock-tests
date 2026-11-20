# -*- coding: utf-8 -*-
import os
from pypdf import PdfReader

papers_rows = []
for i in range(1, 51):
    fname = f"Bihar_Librarian_Bilingual_Mock_{i:02d}.pdf"
    size_kb = os.path.getsize(fname) / 1024
    reader = PdfReader(fname)
    pages = len(reader.pages)
    papers_rows.append(f"| **Mock {i:02d}** | [{fname}](./{fname}) | {pages} pages | {size_kb:.1f} KB | 150 Qs | Bilingual (En + Hi) |")

papers_table = "\n".join(papers_rows)

readme_content = f"""# 📚 Bihar Library Eligibility Test (LET / SLET) — 50 Full Bilingual Mock Papers

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Total Questions](https://img.shields.io/badge/Questions-7%2C500_MCQs-blue.svg)](#)
[![Total Papers](https://img.shields.io/badge/Papers-50_Full_Mock_Tests-green.svg)](#)
[![Language](https://img.shields.io/badge/Language-Bilingual_(English_%26_Hindi)-orange.svg)](#)
[![Deduplication](https://img.shields.io/badge/Deduplication-100%25_Unique_(0_Collisions)-purple.svg)](#)

A comprehensive, production-grade repository containing **50 Full-Length Bilingual (English & Hindi) Mock Test Booklets** for the **Bihar Library Eligibility Test (LET / SLET)** conducted by the **Bihar School Examination Board (BSEB)**.

🌐 **Live Web Application (Desktop & Mobile):** [https://anshuk-dev.github.io/bihar-librarian-let-mock-tests/](https://anshuk-dev.github.io/bihar-librarian-let-mock-tests/)

---

## 🌟 Series Highlights

- **50 Complete Mock Papers:** 150 questions per paper = **7,500 total questions**.
- **100% Unique Questions:** Zero duplicate questions across all 50 booklets. Verified via SHA-256 cryptographic deduplication registry (`question_dedup_registry.json`).
- **Strictly Bilingual:** Every question stem, all 4 options (A, B, C, D), and comprehensive explanatory solutions are presented side-by-side in both **English and Hindi**.
- **Complete Solutions & Answer Grid:** Every paper includes a 150-question answer key table followed by full conceptual explanations.
- **Official BSEB Syllabus Alignment:**
  - **Part 1 (Q001–Q100): Library & Information Science (100 Marks)**
    - Unit 1 (Q01–Q20): Foundations of LIS, 5 Laws, Library Legislation, Movement & Associations
    - Unit 2 (Q21–Q40): Knowledge Organization, Classification (DDC/CC/UDC) & Cataloguing (AACR-2/CCC/MARC21/RDA)
    - Unit 3 (Q41–Q60): Information Sources (Primary/Secondary/Tertiary), Reference Services & Library Management (Fayol/Taylor/TQM/Circulation)
    - Unit 4 (Q61–Q80): Information Services (CAS/SDI/DDS), Retrieval, Networks & Consortia (INFLIBNET/DELNET/e-ShodhSindhu)
    - Unit 5 (Q81–Q100): Library Automation, Software (Koha/SOUL/DSpace), Semantic Web, AI & Cybersecurity
  - **Part 2 (Q101–Q150): General Knowledge & General Studies (50 Marks)**
    - Module 1 (Q101–Q110): Bihar Special (History, Geography, Economy, Schemes & Culture)
    - Module 2 (Q111–Q120): Indian Polity, Governance & Constitution
    - Module 3 (Q121–Q130): Modern Indian History & National Freedom Movement
    - Module 4 (Q131–Q140): General Science, Technology & Environment/Ecology
    - Module 5 (Q141–Q150): Logical Reasoning, Numerical Ability & Mental Aptitude
- **Printable PDF Booklets:** Rendered using ReportLab with exact page-budgeting, running headers, and footers (1,740 total pages).

---

## 📱 Web Portal Features (Desktop & Mobile)

The repository includes a responsive web application (`index.html`) optimized for both mobile phones and desktop computers:
1. **Interactive Search & Filter:** Instant filter by paper number, syllabus topics, or paper sets.
2. **View Toggles:** Responsive Card Grid view and Compact List view.
3. **In-Browser PDF Previewer:** View any of the 50 PDF booklets directly inside the browser on desktop or mobile.
4. **Interactive Practice Mode:** Test your knowledge with 10 sample bilingual questions, instant grading, and full explanations.
5. **Dark / Light Theme:** Native dark mode support for comfortable night study.

---

## 📑 Complete Index of All 50 Mock Test Booklets

| Paper # | PDF Download Link | Booklet Pages | File Size | Questions | Format |
| :---: | :--- | :---: | :---: | :---: | :---: |
{papers_table}

---

## 🛠️ Verification & Quality Assurance Audit

To verify zero question collisions and 100% uniqueness:
```bash
python3 full_audit.py
```
Expected output:
```
AUDIT COMPLETED!
Total Collisions: 0
Total Unique Questions Tracked: 7500
SUCCESS: 100% OF 7,500 QUESTIONS ARE UNIQUE WITH ZERO COLLISIONS!
```

---

## 💻 Local Running & Development

To preview the web portal locally on your computer:
```bash
# Clone the repository
git clone https://github.com/anshuk-dev/bihar-librarian-let-mock-tests.git
cd bihar-librarian-let-mock-tests

# Start a local web server
python3 -m http.server 8000
```
Then open `http://localhost:8000` in your web browser.

---

## 📄 License & Attribution

This open educational resource is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. Free to share, print, and use for academic preparation and recruitment examinations.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Generated README.md successfully!")
