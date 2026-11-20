# -*- coding: utf-8 -*-
"""
Assembles pool_lis_u2.py from build_u2 modules.
Unit 2: Knowledge Organization, Classification & Cataloguing (Q21 to Q40).
"""

import build_u2_q21_q25 as m1
import build_u2_q26_q30 as m2
import build_u2_q31_q35 as m3
import build_u2_q36_q40 as m4

pools = {
    21: m1.q21_pool,
    22: m1.q22_pool,
    23: m1.q23_pool,
    24: m1.q24_pool,
    25: m1.q25_pool,
    26: m2.q26_pool,
    27: m2.q27_pool,
    28: m2.q28_pool,
    29: m2.q29_pool,
    30: m2.q30_pool,
    31: m3.q31_pool,
    32: m3.q32_pool,
    33: m3.q33_pool,
    34: m3.q34_pool,
    35: m3.q35_pool,
    36: m4.q36_pool,
    37: m4.q37_pool,
    38: m4.q38_pool,
    39: m4.q39_pool,
    40: m4.q40_pool
}

for q_num, p in pools.items():
    assert len(p) == 48, f"Pool Q{q_num} has {len(p)} items, expected 48"

with open("pool_lis_u2.py", "w", encoding="utf-8") as f:
    f.write('''# -*- coding: utf-8 -*-
"""
Pool module for Part 1: Unit 2 Knowledge Organization, Classification & Cataloguing (Q21 to Q40).
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
U_EN = "Unit 2: Knowledge Organization, Classification and Cataloguing"
U_HI = "इकाई 2: ज्ञान संगठन, वर्गीकरण एवं सूचीकरण"

''')

    for q_num in range(21, 41):
        f.write(f"pool_q{q_num} = [\n")
        items = pools[q_num]
        for it in items:
            f.write(f"    {repr(it)},\n")
        f.write("]\n\n")

    f.write('''def get_u2_questions(idx):
    # idx: 0 to 47
    qs = []
''')
    for q_num in range(21, 41):
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

print("pool_lis_u2.py assembled successfully!")
