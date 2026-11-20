# -*- coding: utf-8 -*-
"""
Assemble pool_gs_bihar.py from the 10 slot modules.
"""

import json
import hashlib
import build_pool_bihar_q101
import build_pool_bihar_q102
import build_pool_bihar_q103
import build_pool_bihar_q104
import build_pool_bihar_q105
import build_pool_bihar_q106
import build_pool_bihar_q107
import build_pool_bihar_q108
import build_pool_bihar_q109
import build_pool_bihar_q110

pools = [
    build_pool_bihar_q101.q101_pool,
    build_pool_bihar_q102.q102_pool,
    build_pool_bihar_q103.q103_pool,
    build_pool_bihar_q104.q104_pool,
    build_pool_bihar_q105.q105_pool,
    build_pool_bihar_q106.q106_pool,
    build_pool_bihar_q107.q107_pool,
    build_pool_bihar_q108.q108_pool,
    build_pool_bihar_q109.q109_pool,
    build_pool_bihar_q110.q110_pool,
]

for i, p in enumerate(pools):
    assert len(p) == 48, f"Pool Q{101+i} has {len(p)} items, expected 48"

# Write pool_gs_bihar.py
with open("pool_gs_bihar.py", "w", encoding="utf-8") as f:
    f.write('''# -*- coding: utf-8 -*-
"""
Pool module for General Studies: Bihar GK & General Awareness (Q101 to Q110).
Provides 10 authentic, unique bilingual questions per paper across 48 papers.
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

SEC_EN = "Part 2: General Knowledge & General Studies"
SEC_HI = "भाग 2: सामान्य ज्ञान एवं सामान्य अध्ययन"
U_EN = "Bihar General Knowledge & State Awareness"
U_HI = "बिहार सामान्य ज्ञान एवं राज्य जागरूकता"

''')

    for i in range(10):
        q_num = 101 + i
        f.write(f"pool_q{q_num} = " + repr(pools[i]) + "\n\n")

    f.write('''def get_bihar_questions(idx):
    # idx: 0 to 47
    qs = []
''')
    for i in range(10):
        q_num = 101 + i
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

print("pool_gs_bihar.py generated successfully!")
