# -*- coding: utf-8 -*-
"""
Assembles the complete, clean, 100% authentic pool_lis_u1.py
by splicing the newly authored authentic questions for slots 6, 7, 10-20.
"""

import pool_lis_u1 as orig
import scratch_u1_part1 as p1
import scratch_u1_part2 as p2
import scratch_u1_part3 as p3
import scratch_u1_part4 as p4
import scratch_u1_part5 as p5
import scratch_u1_part6 as p6
import scratch_u1_part7 as p7

new_pools = {}

# Retain original pools 1, 2, 3, 4, 5, 8, 9 unchanged
for i in [1, 2, 3, 4, 5, 8, 9]:
    new_pools[f'pool_q{i}'] = getattr(orig, f'pool_q{i}')

# Splice the new authentic items for other pools
new_pools['pool_q6'] = orig.pool_q6[:10] + p1.slot6_supplement[:38]
new_pools['pool_q7'] = orig.pool_q7[:10] + p1.slot7_supplement[:38]
new_pools['pool_q10'] = orig.pool_q10[:28] + p2.slot10_supplement[:20]
new_pools['pool_q11'] = orig.pool_q11[:10] + p2.slot11_supplement[:38]
new_pools['pool_q12'] = orig.pool_q12[:10] + p3.slot12_supplement[:38]
new_pools['pool_q13'] = orig.pool_q13[:10] + p3.slot13_supplement[:38]
new_pools['pool_q14'] = orig.pool_q14[:10] + p4.slot14_supplement[:38]
new_pools['pool_q15'] = orig.pool_q15[:10] + p4.slot15_supplement[:38]
new_pools['pool_q16'] = orig.pool_q16[:10] + p5.slot16_supplement[:38]
new_pools['pool_q17'] = orig.pool_q17[:10] + p5.slot17_supplement[:38]
new_pools['pool_q18'] = orig.pool_q18[:10] + p6.slot18_supplement[:38]
new_pools['pool_q19'] = orig.pool_q19[:9] + p6.slot19_supplement[:39]
new_pools['pool_q20'] = orig.pool_q20[:10] + p7.slot20_supplement[:38]

# Verify all pools have length 48
for i in range(1, 21):
    pool_name = f'pool_q{i}'
    assert len(new_pools[pool_name]) == 48, f"{pool_name} has {len(new_pools[pool_name])} items, expected 48"
print("All 20 pools verified with exactly 48 items each!")

# Construct output pool_lis_u1.py
with open('pool_lis_u1.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
Pool module for Part 1: Unit 1 Foundations of LIS (Q1 to Q20).
Provides 20 authentic, unique bilingual questions per paper across 48 papers.
Completely free of synthetic templates or comical distractors.
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
    for i in range(1, 21):
        f.write(f"pool_q{i} = " + repr(new_pools[f'pool_q{i}']) + "\n\n")

    f.write('''def get_u1_questions(paper_idx):
    idx = paper_idx % 48
    qs = []
''')
    for i in range(1, 21):
        f.write(f'''    item = pool_q{i}[idx]
    ans_idx = ({i} + idx) % 4
    qs.append(make_question(
        {i}, SEC_EN, SEC_HI, U_EN, U_HI,
        item[0], item[1], item[2], item[3],
        item[4], item[5], item[6], item[7],
        ans_idx
    ))
''')
    f.write('    return qs\n')

print("pool_lis_u1.py written successfully!")
