# -*- coding: utf-8 -*-
"""
Bihar School Librarian Eligibility Test (LET / SLET)
50 Mock Test Series Orchestrator & Deduplication Runner
"""

import os
import sys
import json
import hashlib

REGISTRY_FILE = "question_dedup_registry.json"

def show_series_status():
    if not os.path.exists(REGISTRY_FILE):
        print("Registry file not found.")
        return

    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_q = data.get("total_unique_questions_registered", 0)
    papers = data.get("papers_generated", [])

    print("=" * 65)
    print("  BIHAR LIBRARIAN (LET) 50 BILINGUAL MOCK TEST SERIES STATUS")
    print("=" * 65)
    print(f"Total Unique Questions Registered: {total_q} / 7,500")
    print(f"Full Model Papers Completed:        {len(papers)} / 50")
    print("-" * 65)
    for idx, p in enumerate(papers, 1):
        size = os.path.getsize(p) if os.path.exists(p) else 0
        print(f" [{idx:02d}] {p:<42} ({size/1024:.1f} KB)")
    print("=" * 65)

if __name__ == "__main__":
    show_series_status()
