# -*- coding: utf-8 -*-
"""
Assembles pool_lis_u3.py from build_u3 modules.
Unit 3: Information Sources, Systems & Library Management (Q41 to Q60).
"""

import build_u3_q41_q45 as m41
import build_u3_q42_part2 as m42
import build_u3_q43 as m43
import build_u3_q44 as m44
import build_u3_q45 as m45
import build_u3_q46_q50 as m46
import build_u3_q47 as m47
import build_u3_q48 as m48
import build_u3_q49 as m49
import build_u3_q50 as m50
import build_u3_q51_q55 as m51
import build_u3_q52 as m52
import build_u3_q53 as m53
import build_u3_q54 as m54
import build_u3_q55 as m55
import build_u3_q56 as m56
import build_u3_q57 as m57
import build_u3_q58 as m58
import build_u3_q59 as m59
import build_u3_q60 as m60

q42_full = m41.q42_pool + m42.q42_pool_part2

pools = {
    41: m41.q41_pool,
    42: q42_full,
    43: m43.q43_pool,
    44: m44.q44_pool,
    45: m45.q45_pool,
    46: m46.q46_pool,
    47: m47.q47_pool,
    48: m48.q48_pool,
    49: m49.q49_pool,
    50: m50.q50_pool,
    51: m51.q51_pool,
    52: m52.q52_pool,
    53: m53.q53_pool,
    54: m54.q54_pool,
    55: m55.q55_pool,
    56: m56.q56_pool,
    57: m57.q57_pool,
    58: m58.q58_pool,
    59: m59.q59_pool,
    60: m60.q60_pool
}

for q_num, p in pools.items():
    assert len(p) == 48, f"Pool Q{q_num} has {len(p)} items, expected 48"

with open("pool_lis_u3.py", "w", encoding="utf-8") as f:
    f.write('''# -*- coding: utf-8 -*-
"""
Pool module for Part 1: Unit 3 Information Sources, Systems & Library Management (Q41 to Q60).
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
U_EN = "Unit 3: Information Sources, Systems and Library Management"
U_HI = "इकाई 3: सूचना स्रोत, प्रणालियाँ एवं पुस्तकालय प्रबंधन"

''')

    for q_num in range(41, 61):
        f.write(f"pool_q{q_num} = [\n")
        for item in pools[q_num]:
            f.write(f"    {repr(item)},\n")
        f.write("]\n\n")

    f.write('''def get_u3_questions(idx):
    """
    Returns 20 questions for Unit 3 (Q41 to Q60) for a given paper index (0 <= idx < 48).
    """
    assert 0 <= idx < 48, "idx must be between 0 and 47"
    questions = []
    pools = [
        (41, pool_q41), (42, pool_q42), (43, pool_q43), (44, pool_q44), (45, pool_q45),
        (46, pool_q46), (47, pool_q47), (48, pool_q48), (49, pool_q49), (50, pool_q50),
        (51, pool_q51), (52, pool_q52), (53, pool_q53), (54, pool_q54), (55, pool_q55),
        (56, pool_q56), (57, pool_q57), (58, pool_q58), (59, pool_q59), (60, pool_q60)
    ]
    for q_num, pool in pools:
        item = pool[idx]
        ans_idx = (q_num + idx) % 4
        q = make_question(
            q_num, SEC_EN, SEC_HI, U_EN, U_HI,
            item[0], item[1], item[2], item[3],
            item[4], item[5], item[6], item[7],
            ans_idx
        )
        questions.append(q)
    return questions
''')

print("Assembled pool_lis_u3.py successfully!")
