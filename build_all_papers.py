# -*- coding: utf-8 -*-
"""
Master Generation Script: Renders all 48 remaining mock test booklets (Paper 03 to Paper 50).
Combined with Papers 01 & 02, this completes all 50 Mock Papers (7,500 unique questions).
"""

import os
import sys
import json
import time
import hashlib
from pypdf import PdfReader

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
import batch_paper_builder
import generate_bilingual_pdf as p1
import generate_bilingual_pdf_02 as p2

def get_question_hash(q):
    txt = f"{q.get('q_en', '').strip().lower()}|{q.get('q_hi', '').strip().lower()}"
    return hashlib.sha256(txt.encode('utf-8')).hexdigest()

REGISTRY_FILE = "question_dedup_registry.json"

# Initialize with Paper 01 and Paper 02 questions
qs1 = p1.BILINGUAL_QUESTIONS + p1.BILINGUAL_U2_U3 + p1.BILINGUAL_U4_U5 + p1.BILINGUAL_PART2_GS
qs2 = p2.PAPER02_U1_U3_QUESTIONS + p2.PAPER02_U4_U5_QUESTIONS + p2.BILINGUAL_MOCK02_PART2_GS

registered_hashes = set()
for q in qs1:
    registered_hashes.add(get_question_hash(q))
for q in qs2:
    registered_hashes.add(get_question_hash(q))

assert len(registered_hashes) == 300, f"Expected 300 hashes for Papers 1 & 2, got {len(registered_hashes)}"

papers_generated = [
    "Bihar_Librarian_Bilingual_Mock_01.pdf",
    "Bihar_Librarian_Bilingual_Mock_02.pdf"
]

print(f"Starting Master Generation Loop. Papers 1 & 2 registered: {len(registered_hashes)} hashes.")

start_total_time = time.time()

for paper_num in range(3, 51):
    idx = paper_num - 3 # 0 to 47
    pdf_filename = f"Bihar_Librarian_Bilingual_Mock_{paper_num:02d}.pdf"
    
    t0 = time.time()
    
    # 1. Assemble all 150 questions
    all_questions = []
    all_questions.extend(pool_lis_u1.get_u1_questions(idx))
    all_questions.extend(pool_lis_u2.get_u2_questions(idx))
    all_questions.extend(pool_lis_u3.get_u3_questions(idx))
    all_questions.extend(pool_lis_u4.get_u4_questions(idx))
    all_questions.extend(pool_lis_u5.get_u5_questions(idx))
    all_questions.extend(pool_gs_bihar.get_bihar_questions(idx))
    all_questions.extend(pool_gs_polity.get_polity_questions(idx))
    all_questions.extend(pool_gs_history.get_history_questions(idx))
    all_questions.extend(pool_gs_science.get_science_questions(idx))
    all_questions.extend(pool_gs_reasoning.get_reasoning_questions(idx))
    
    assert len(all_questions) == 150, f"Paper {paper_num:02d} has {len(all_questions)} questions, expected 150"
    
    # 2. Verify and register hashes
    for q in all_questions:
        qh = get_question_hash(q)
        assert qh not in registered_hashes, f"Duplicate detected in Paper {paper_num:02d} Q{q['id']}: {q['q_en'][:50]}"
        registered_hashes.add(qh)
    
    if pdf_filename not in papers_generated:
        papers_generated.append(pdf_filename)
    
    # 3. Render PDF
    batch_paper_builder.render_paper_pdf(paper_num, all_questions, pdf_filename)
    
    t1 = time.time()
    file_size_kb = os.path.getsize(pdf_filename) / 1024
    reader = PdfReader(pdf_filename)
    num_pages = len(reader.pages)
    
    print(f"[{paper_num:02d}/50] Rendered {pdf_filename} | {num_pages} pages | {file_size_kb:.1f} KB | Time: {t1-t0:.2f}s | Total Qs: {len(registered_hashes)}")

# 4. Save final registry
reg = {
    "total_unique_questions_registered": len(registered_hashes),
    "papers_generated": papers_generated,
    "registered_hashes": list(registered_hashes)
}

with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
    json.dump(reg, f, indent=2, ensure_ascii=False)

total_elapsed = time.time() - start_total_time
print(f"\n=======================================================")
print(f"ALL 50 MOCK PAPERS SUCCESSFULLY GENERATED & VERIFIED!")
print(f"Total time elapsed: {total_elapsed:.2f} seconds")
print(f"Total unique questions registered: {len(registered_hashes)} / 7500")
print(f"=======================================================")
