# -*- coding: utf-8 -*-
import json
import hashlib

def get_hash(text):
    return hashlib.sha256(text.strip().lower().encode('utf-8')).hexdigest()

with open("question_dedup_registry.json", "r", encoding="utf-8") as f:
    reg_data = json.load(f)

hashes_list = reg_data["registered_hashes"]
print(f"Registry has {len(hashes_list)} hashes from Papers 1 & 2.")

seen = {}
for h in hashes_list:
    seen[h] = "Paper 1/2"

import pool_lis_u1
import pool_lis_u2
import pool_lis_u3
import pool_lis_u4
import pool_lis_u5
import pool_gs_bihar
import pool_gs_polity
import pool_gs_history
import pool_gs_science
import pool_gs_reasoning

modules = [
    ("U1", pool_lis_u1.get_u1_questions, 20),
    ("U2", pool_lis_u2.get_u2_questions, 20),
    ("U3", pool_lis_u3.get_u3_questions, 20),
    ("U4", pool_lis_u4.get_u4_questions, 20),
    ("U5", pool_lis_u5.get_u5_questions, 20),
    ("GS Bihar", pool_gs_bihar.get_bihar_questions, 10),
    ("GS Polity", pool_gs_polity.get_polity_questions, 10),
    ("GS History", pool_gs_history.get_history_questions, 10),
    ("GS Science", pool_gs_science.get_science_questions, 10),
    ("GS Reasoning", pool_gs_reasoning.get_reasoning_questions, 10),
]

collisions = 0
for paper_idx in range(48):
    paper_num = paper_idx + 3
    q_count = 0
    for mod_name, get_fn, expected_len in modules:
        qs = get_fn(paper_idx)
        assert len(qs) == expected_len, f"Paper {paper_num} {mod_name} expected {expected_len}, got {len(qs)}"
        q_count += len(qs)
        for q in qs:
            h = get_hash(q["q_en"])
            if h in seen:
                print(f"COLLISION: Paper {paper_num} Q{q['id']} ({mod_name}) matches {seen[h]}")
                print(f"Question text: {q['q_en'][:80]}")
                collisions += 1
            seen[h] = f"Paper {paper_num} Q{q['id']}"
    assert q_count == 150, f"Paper {paper_num} has {q_count} questions instead of 150"

print(f"\n==========================================")
print(f"AUDIT COMPLETED!")
print(f"Total Collisions: {collisions}")
print(f"Total Unique Questions Tracked: {len(seen)}")
assert len(seen) == 7500, f"Expected 7500 unique questions, got {len(seen)}"
assert collisions == 0, f"Expected 0 collisions, got {collisions}"
print(f"SUCCESS: 100% OF 7,500 QUESTIONS ARE UNIQUE WITH ZERO COLLISIONS!")
print(f"==========================================")
