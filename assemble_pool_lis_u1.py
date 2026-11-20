# -*- coding: utf-8 -*-
"""
Assemble pool_lis_u1.py from the modular slot scripts.
"""

import json
import hashlib

import build_pool_lis_u1_q1
import build_pool_lis_u1_q2
import build_pool_lis_u1_q3
import build_pool_lis_u1_q4
import build_pool_lis_u1_q5
import build_pool_lis_u1_q6
import build_pool_lis_u1_q7
import build_pool_lis_u1_q8
import build_pool_lis_u1_q9
import build_pool_lis_u1_q10
import build_pool_lis_u1_q11_q15
import build_pool_lis_u1_q16_q20

pools = [
    build_pool_lis_u1_q1.q1_pool,
    build_pool_lis_u1_q2.q2_pool,
    build_pool_lis_u1_q3.q3_pool,
    build_pool_lis_u1_q4.q4_pool,
    build_pool_lis_u1_q5.q5_pool,
    build_pool_lis_u1_q6.q6_items,
    build_pool_lis_u1_q7.q7_pool,
    build_pool_lis_u1_q8.q8_pool,
    build_pool_lis_u1_q9.q9_pool,
    build_pool_lis_u1_q10.q10_pool,
    build_pool_lis_u1_q11_q15.q11_pool,
    build_pool_lis_u1_q11_q15.q12_pool,
    build_pool_lis_u1_q11_q15.q13_pool,
    build_pool_lis_u1_q11_q15.q14_pool,
    build_pool_lis_u1_q11_q15.q15_pool,
    build_pool_lis_u1_q16_q20.q16_pool,
    build_pool_lis_u1_q16_q20.q17_pool,
    build_pool_lis_u1_q16_q20.q18_pool,
    build_pool_lis_u1_q16_q20.q19_pool,
    build_pool_lis_u1_q16_q20.q20_pool,
]

for i, p in enumerate(pools):
    assert len(p) == 48, f"Pool Q{i+1} has {len(p)} items, expected 48"

with open("pool_lis_u1.py", "w", encoding="utf-8") as f:
    f.write('''# -*- coding: utf-8 -*-
"""
Pool module for Part 1: Unit 1 Foundations of LIS (Q1 to Q20).
Provides 20 authentic, unique bilingual questions per paper across 48 papers.
"""

def make_question(q_id, sec_en, sec_hi, u_en, u_hi, q_en, q_hi, c_en, c_hi, w_en, w_hi, exp_en, exp_hi, ans_idx):
    opts_en = list(w_en)
    opts_hi = list(w_hi)
    opts_en.insert(ans_idx, c_en)
    opts_hi.insert(ans_idx, c_hi)
    ans_letter = chr(ord('A') + ans_idx)
    return {
        "id": q_id,
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

SEC_EN = "Part 1: Library & Information Science"
SEC_HI = "भाग 1: पुस्तकालय एवं सूचना विज्ञान"
U_EN = "Unit 1: Foundations of Library and Information Science"
U_HI = "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार"

''')

    for i in range(20):
        q_num = i + 1
        f.write(f"pool_q{q_num} = " + repr(pools[i]) + "\n\n")

    f.write('''def get_u1_questions(idx):
    # idx: 0 to 47
    qs = []
''')
    for i in range(20):
        q_num = i + 1
        f.write(f'''    item = pool_q{q_num}[idx]
    ans_idx = ({q_num} + idx) % 4
    qs.append(make_question(
        {q_num}, SEC_EN, SEC_HI, U_EN, U_HI,
        item[0], item[1], item[2], item[3],
        item[4], item[5], item[6], item[7],
        ans_idx
    ))
''')
    f.write("    return qs\n")

print("pool_lis_u1.py assembled successfully!")
