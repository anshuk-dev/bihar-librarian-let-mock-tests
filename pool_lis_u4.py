# -*- coding: utf-8 -*-
"""
Unit 4: Information Services, Retrieval & Consortia (Q61 to Q80)
20 slots x 48 items = 960 unique questions.
"""

import build_u4_q61_q65
import build_u4_q62
import build_u4_q63
import build_u4_q64
import build_u4_q65
import build_u4_q66
import build_u4_q67
import build_u4_q68
import build_u4_q69
import build_u4_q70
import build_u4_q71
import build_u4_q72
import build_u4_q73
import build_u4_q74
import build_u4_q75
import build_u4_q76
import build_u4_q77
import build_u4_q78
import build_u4_q79
import build_u4_q80

u4_slots = [
    build_u4_q61_q65.q61_pool,
    build_u4_q62.q62_pool,
    build_u4_q63.q63_pool,
    build_u4_q64.q64_pool,
    build_u4_q65.q65_pool,
    build_u4_q66.q66_pool,
    build_u4_q67.q67_pool,
    build_u4_q68.q68_pool,
    build_u4_q69.q69_pool,
    build_u4_q70.q70_pool,
    build_u4_q71.q71_pool,
    build_u4_q72.q72_pool,
    build_u4_q73.q73_pool,
    build_u4_q74.q74_pool,
    build_u4_q75.q75_pool,
    build_u4_q76.q76_pool,
    build_u4_q77.q77_pool,
    build_u4_q78.q78_pool,
    build_u4_q79.q79_pool,
    build_u4_q80.q80_pool,
]

def get_u4_questions(idx):
    """
    Returns the 20 questions for Unit 4 (Q61 to Q80) for paper index idx (0 <= idx < 48).
    idx = paper_num - 3
    """
    sec_en = "Part 1: Library & Information Science"
    sec_hi = "भाग 1: पुस्तकालय एवं सूचना विज्ञान"
    u_en = "Unit 4: Information Services, Retrieval & Consortia"
    u_hi = "इकाई 4: सूचना सेवाएं, पुनर्प्राप्ति एवं कंसोर्टिया"
    
    questions = []
    letters = ['A', 'B', 'C', 'D']
    for slot_idx, slot_pool in enumerate(u4_slots):
        q_num = 61 + slot_idx
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
