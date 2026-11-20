# -*- coding: utf-8 -*-
"""
Assemble Unit 5: pool_lis_u5.py
Slots Q81 to Q100 (20 slots x 48 items = 960 questions)
"""

with open("pool_lis_u5.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nUnit 5: Information Technology, Automation & Digital Libraries (Q81 to Q100)\n')
    f.write('20 slots x 48 items = 960 unique questions.\n"""\n\n')
    for q in range(81, 101):
        f.write(f"import build_u5_q{q}\n")
    f.write("\n")
    f.write("u5_slots = [\n")
    for q in range(81, 101):
        f.write(f"    build_u5_q{q}.q{q}_pool,\n")
    f.write("]\n\n")
    f.write("""def get_u5_questions(idx):
    \"\"\"
    Returns the 20 questions for Unit 5 (Q81 to Q100) for paper index idx (0 <= idx < 48).
    idx = paper_num - 3
    \"\"\"
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
""")

print("pool_lis_u5.py written successfully!")
