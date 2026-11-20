# -*- coding: utf-8 -*-
"""
Assemble Unit 4: pool_lis_u4.py
Slots Q61 to Q80 (20 slots x 48 items = 960 questions)
"""

import hashlib
import json
import build_u4_q61_q65
pool_q61 = build_u4_q61_q65.q61_pool

# Q62 to Q80
slot_pools = [pool_q61]
for q in range(62, 81):
    mod = __import__(f"build_u4_q{q}")
    pools = [getattr(mod, k) for k in dir(mod) if k.startswith("pool_") or k.startswith("q")]
    slot_pools.append(pools[0])

print(f"Total slots loaded: {len(slot_pools)}")
for i, p in enumerate(slot_pools):
    q_num = 61 + i
    assert len(p) == 48, f"Slot Q{q_num} has {len(p)} items, expected 48"
print("All 20 slots have exactly 48 items!")

# Write pool_lis_u4.py
with open("pool_lis_u4.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nUnit 4: Information Services, Retrieval & Consortia (Q61 to Q80)\n')
    f.write('20 slots x 48 items = 960 unique questions.\n"""\n\n')
    f.write("import build_u4_q61_q65\n")
    for q in range(62, 81):
        f.write(f"import build_u4_q{q}\n")
    f.write("\n")
    f.write("u4_slots = [\n")
    f.write("    build_u4_q61_q65.q61_pool,\n")
    for q in range(62, 81):
        f.write(f"    build_u4_q{q}.q{q}_pool,\n")
    f.write("]\n\n")
    f.write("""def get_u4_questions(idx):
    \"\"\"
    Returns the 20 questions for Unit 4 (Q61 to Q80) for paper index idx (0 <= idx < 48).
    idx = paper_num - 3
    \"\"\"
    questions = []
    letters = ['A', 'B', 'C', 'D']
    for slot_idx, slot_pool in enumerate(u4_slots):
        q_num = 61 + slot_idx
        item = slot_pool[idx]
        q_en, q_hi, correct_en, correct_hi, wrong_en, wrong_hi, exp_en, exp_hi = item
        
        # Rotating balanced answer key: (q_num + idx) % 4
        ans_idx = (q_num + idx) % 4
        correct_letter = letters[ans_idx]
        
        opts_en = list(wrong_en)
        opts_en.insert(ans_idx, correct_en)
        
        opts_hi = list(wrong_hi)
        opts_hi.insert(ans_idx, correct_hi)
        
        q_data = {
            "q_num": q_num,
            "unit": "Unit 4: Information Services, Retrieval & Consortia",
            "question_en": q_en,
            "question_hi": q_hi,
            "options_en": {
                "A": opts_en[0],
                "B": opts_en[1],
                "C": opts_en[2],
                "D": opts_en[3]
            },
            "options_hi": {
                "A": opts_hi[0],
                "B": opts_hi[1],
                "C": opts_hi[2],
                "D": opts_hi[3]
            },
            "correct_option": correct_letter,
            "solution_en": f"Correct Option: {correct_letter}\\n{exp_en}",
            "solution_hi": f"सही विकल्प: {correct_letter}\\n{exp_hi}"
        }
        questions.append(q_data)
    return questions
""")

print("Successfully written pool_lis_u4.py!")

# Verify pool_lis_u4.py by running checks
import pool_lis_u4
total_hashes = set()
for idx in range(48):
    qs = pool_lis_u4.get_u4_questions(idx)
    assert len(qs) == 20
    for q in qs:
        norm = q["question_en"].strip().lower()
        h = hashlib.sha256(norm.encode("utf-8")).hexdigest()
        assert h not in total_hashes, f"Duplicate hash found in U4: {q['question_en'][:40]}"
        total_hashes.add(h)

print(f"Verified Unit 4! Total unique questions: {len(total_hashes)} (expected 960)")

# Check collisions with deduplication registry
with open("question_dedup_registry.json") as f:
    reg = json.load(f)
reg_hashes = set(reg["registered_hashes"])
collision = total_hashes.intersection(reg_hashes)
print(f"Collisions with Papers 01 & 02 registry: {len(collision)}")
assert len(collision) == 0, f"Found collisions: {collision}"
print("Unit 4 has ZERO collisions with existing registry!")
