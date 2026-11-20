# -*- coding: utf-8 -*-
"""
Unit 5: Information Technology, Automation & Digital Libraries (Q81 to Q100)
20 slots x 48 items = 960 unique questions.
"""

import build_u5_q81
import build_u5_q82
import build_u5_q83
import build_u5_q84
import build_u5_q85
import build_u5_q86
import build_u5_q87
import build_u5_q88
import build_u5_q89
import build_u5_q90
import build_u5_q91
import build_u5_q92
import build_u5_q93
import build_u5_q94
import build_u5_q95
import build_u5_q96
import build_u5_q97
import build_u5_q98
import build_u5_q99
import build_u5_q100

u5_slots = [
    build_u5_q81.q81_pool,
    build_u5_q82.q82_pool,
    build_u5_q83.q83_pool,
    build_u5_q84.q84_pool,
    build_u5_q85.q85_pool,
    build_u5_q86.q86_pool,
    build_u5_q87.q87_pool,
    build_u5_q88.q88_pool,
    build_u5_q89.q89_pool,
    build_u5_q90.q90_pool,
    build_u5_q91.q91_pool,
    build_u5_q92.q92_pool,
    build_u5_q93.q93_pool,
    build_u5_q94.q94_pool,
    build_u5_q95.q95_pool,
    build_u5_q96.q96_pool,
    build_u5_q97.q97_pool,
    build_u5_q98.q98_pool,
    build_u5_q99.q99_pool,
    build_u5_q100.q100_pool,
]

def get_u5_questions(idx):
    """
    Returns the 20 questions for Unit 5 (Q81 to Q100) for paper index idx (0 <= idx < 48).
    idx = paper_num - 3
    """
    sec_en = "Part 1: Library & Information Science"
    sec_hi = "भाग 1: पुस्तकालय एवं सूचना विज्ञान"
    u_en = "Unit 5: Information Technology, Automation & Digital Libraries"
    u_hi = "इकाई 5: सूचना प्रौद्योगिकी, स्वचालन एवं डिजिटल पुस्तकालय"
    
    questions = []
    letters = ['A', 'B', 'C', 'D']
    for slot_idx, slot_pool in enumerate(u5_slots):
        q_num = 81 + slot_idx
        item = slot_pool[idx]
        q_en, q_hi, correct_en, correct_hi, wrong_en, wrong_hi, exp_en, exp_hi = item
        
        # Rotating balanced answer key: (q_num + idx) % 4
        ans_idx = (q_num + idx) % 4
        ans_letter = letters[ans_idx]
        
        opts_en = list(wrong_en)
        opts_en.insert(ans_idx, correct_en)
        
        opts_hi = list(wrong_hi)
        opts_hi.insert(ans_idx, correct_hi)
        
        q_data = {
            "id": q_num,
            "section_en": sec_en,
            "section_hi": sec_hi,
            "unit_en": u_en,
            "unit_hi": u_hi,
            "q_en": q_en,
            "q_hi": q_hi,
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": exp_en,
            "exp_hi": exp_hi
        }
        questions.append(q_data)
    return questions
