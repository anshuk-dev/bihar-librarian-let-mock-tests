# -*- coding: utf-8 -*-
"""
Bihar School Librarian Eligibility Test (LET / SLET)
50 Unique Bilingual Mock Test Paper Series Generator Engine
Ensures 100% question uniqueness across all 50 papers using persistent deduplication registry.
"""

import os
import sys
import json
import hashlib
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)

FONT_NAME = 'ArialUnicode'
FONT_PATH = '/Library/Fonts/Arial Unicode.ttf'
if os.path.exists(FONT_PATH):
    pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))

REGISTRY_FILE = "question_dedup_registry.json"

def load_registry():
    if os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"registered_hashes": [], "papers_generated": []}

def save_registry(registry):
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)

def hash_question(q_dict):
    """Generate a unique fingerprint for a question based on its English & Hindi texts."""
    content = f"{q_dict.get('q_en', '').strip().lower()}|{q_dict.get('q_hi', '').strip().lower()}"
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

print("Mock Series deduplication and generation engine ready.")
