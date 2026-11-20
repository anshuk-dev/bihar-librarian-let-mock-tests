# -*- coding: utf-8 -*-
"""
Full Series Generator for Bihar School Librarian Eligibility Test (LET)
Automates the creation of all 50 Bilingual Mock Test Papers (7,500 Unique Questions).
"""

import os
import sys
import json
import hashlib
import random
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

class NumberedBilingualCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont(FONT_NAME, 8)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header (page 2 onwards)
        if self._pageNumber > 1:
            self.drawString(36, 814, f"बिहार विद्यालय पुस्तकालय पात्रता परीक्षा (LET) — द्विभाषी मॉडल पेपर")
            self.drawRightString(559, 814, "BSEB 150 MCQs BILINGUAL SET")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(36, 808, 559, 808)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(36, 32, 559, 32)
        self.setFont(FONT_NAME, 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(36, 20, "Bihar State Librarian Eligibility Test (LET/SLET) | 100% Unique Authentic Set")
        self.drawRightString(559, 20, f"Page / पृष्ठ {self._pageNumber} of {page_count}")
        self.restoreState()


def load_registry():
    if os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"registered_hashes": [], "papers_generated": [], "total_unique_questions_registered": 0}

def save_registry(registry):
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)

def hash_q(q):
    txt = f"{q.get('q_en', '').strip().lower()}|{q.get('q_hi', '').strip().lower()}"
    return hashlib.sha256(txt.encode('utf-8')).hexdigest()

print("Full series engine initialized.")
