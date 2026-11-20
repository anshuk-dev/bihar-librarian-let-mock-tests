# -*- coding: utf-8 -*-
"""
Pool module for General Studies: Mental Ability & Reasoning (Q141 to Q150).
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
U_EN = "Mental Ability & Quantitative Reasoning"
U_HI = "मानसिक योग्यता एवं गणितीय तर्कशक्ति"

def get_reasoning_questions(idx):
    # idx: 0 to 47 (corresponds to Paper 3 to 50)
    qs = []

    # Q141: Arithmetic Number Series (strictly unique start a1 for each idx)
    a1 = 3 + idx * 3
    d1 = 4 + (idx % 7)
    s1 = [a1 + i * d1 for i in range(5)]
    next_s1 = a1 + 5 * d1
    ans_idx = (141 + idx) % 4
    qs.append(make_question(
        141, SEC_EN, SEC_HI, U_EN, U_HI,
        f"Find the next term in the arithmetic sequence: {s1[0]}, {s1[1]}, {s1[2]}, {s1[3]}, {s1[4]}, ?",
        f"समानांतर शृंखला {s1[0]}, {s1[1]}, {s1[2]}, {s1[3]}, {s1[4]}, ? में अगला पद ज्ञात करें:",
        str(next_s1), str(next_s1),
        [str(next_s1 - d1 + 1), str(next_s1 + d1 - 2), str(next_s1 + d1)],
        [str(next_s1 - d1 + 1), str(next_s1 + d1 - 2), str(next_s1 + d1)],
        f"Common difference d = {d1}. Next term = {s1[4]} + {d1} = {next_s1}.",
        f"सार्व अंतर d = {d1} है। अगला पद = {s1[4]} + {d1} = {next_s1} होगा।",
        ans_idx
    ))

    # Q142: Geometric / Squares / Multiplicative Series
    mult = 2 + (idx % 3)
    start_m = 2 + idx
    s2 = [start_m * (mult ** i) for i in range(4)]
    next_s2 = start_m * (mult ** 4)
    ans_idx = (142 + idx) % 4
    qs.append(make_question(
        142, SEC_EN, SEC_HI, U_EN, U_HI,
        f"Find the missing term in the sequence: {s2[0]}, {s2[1]}, {s2[2]}, {s2[3]}, ?",
        f"शृंखला {s2[0]}, {s2[1]}, {s2[2]}, {s2[3]}, ? में अगला पद क्या होगा?",
        str(next_s2), str(next_s2),
        [str(next_s2 - start_m), str(next_s2 + mult * 2), str(next_s2 * 2)],
        [str(next_s2 - start_m), str(next_s2 + mult * 2), str(next_s2 * 2)],
        f"Each successive term is multiplied by {mult}: {s2[3]} * {mult} = {next_s2}.",
        f"प्रत्येक पद पिछले पद का {mult} गुना है: {s2[3]} x {mult} = {next_s2}।",
        ans_idx
    ))

    # Q143: Coding-Decoding (48 distinct words)
    words = [
        ("BOOK", "CPPL", 1), ("READ", "SFBS", 1), ("PAGE", "QBFH", 1), ("DESK", "EFTL", 1),
        ("NOTE", "OPUF", 1), ("EXAM", "FYBN", 1), ("DATA", "EBUB", 1), ("MOCK", "NPDL", 1),
        ("TEXT", "UFYU", 1), ("WORD", "XPSE", 1), ("LIBR", "MJCS", 1), ("CARD", "DBSE", 1),
        ("SHELF", "TIFMG", 1), ("INDEX", "JOEFY", 1), ("STUDY", "TUVZZ", 1), ("LEARN", "MFBSO", 1),
        ("PAPER", "QBQFS", 1), ("TITLE", "UJUMF", 1), ("PRESS", "QSFTT", 1), ("PRINT", "QSJOU", 1),
        ("CLASS", "DMBTT", 1), ("TOPIC", "UPQJD", 1), ("MEDIA", "NFEDB", 1), ("QUERY", "RVFSZ", 1),
        ("ORDER", "PSEFS", 1), ("STAFF", "TUBGG", 1), ("USERS", "VTFST", 1), ("STOCK", "TUPDL", 1),
        ("ENTRY", "FOUAZ", 1), ("ISSUE", "JTTVF", 1), ("STACK", "TUBDL", 1), ("CATAL", "DBUBM", 1),
        ("GUIDE", "HVJEF", 1), ("DRIVE", "ESJWF", 1), ("SHARE", "TIBSF", 1), ("WRITE", "XSJUF", 1),
        ("CHECK", "DIFDL", 1), ("DIGIT", "EJHJU", 1), ("SCALE", "TDBMF", 1), ("MODEL", "NPFEM", 1),
        ("SOLVE", "TPMWF", 1), ("SERVE", "TFSWF", 1), ("TRACK", "USBDL", 1), ("SMART", "TNBSU", 1),
        ("TRAIN", "USBJO", 1), ("TOTAL", "UPUBM", 1), ("VALID", "WBMJE", 1), ("WORLD", "XPSEM", 1)
    ]
    w_info = words[idx]
    ans_idx = (143 + idx) % 4
    qs.append(make_question(
        143, SEC_EN, SEC_HI, U_EN, U_HI,
        f"In a certain code language, if '{w_info[0]}' is coded as '{w_info[1]}', what rule determines the cipher?",
        f"एक निश्चित कूट भाषा में यदि '{w_info[0]}' को '{w_info[1]}' लिखा जाता है, तो कौन सा नियम प्रयुक्त हुआ है?",
        f"Each letter is shifted forward by +{w_info[2]}", f"प्रत्येक अक्षर को +{w_info[2]} स्थान आगे बढ़ाया गया है",
        [f"Each letter shifted backward by -{w_info[2]}", "Vowels are reversed", "First and last letters swapped"],
        [f"प्रत्येक अक्षर को -{w_info[2]} स्थान पीछे किया गया है", "केवल स्वरों को उलटा गया है", "प्रथम एवं अंतिम अक्षर परस्पर बदले गए हैं"],
        f"Every character in '{w_info[0]}' advances by 1 alphabetical position: {w_info[1]}.",
        f"'{w_info[0]}' के प्रत्येक अक्षर में +1 की वृद्धि की गई है: {w_info[1]}।",
        ans_idx
    ))

    # Q144: Blood Relations (48 strictly unique person names and relations)
    names_pool = [
        "Aarav", "Rohan", "Suresh", "Vikram", "Anil", "Deepak", "Manoj", "Pankaj",
        "Rajesh", "Sunil", "Amit", "Alok", "Gaurav", "Harish", "Kunal", "Naveen",
        "Pradeep", "Sachin", "Tarun", "Varun", "Abhishek", "Brijesh", "Chandan", "Dharmendra",
        "Girish", "Hemant", "Jitendra", "Kamal", "Lalit", "Mahesh", "Nilesh", "Omkar",
        "Praveen", "Ramesh", "Sanjay", "Tushar", "Umesh", "Vinod", "Ashok", "Bharat",
        "Chetan", "Devendra", "Eshwar", "Fateh", "Govind", "Hari", "Inder", "Jagdish"
    ]
    person = names_pool[idx]
    ans_idx = (144 + idx) % 4
    if idx % 2 == 0:
        qs.append(make_question(
            144, SEC_EN, SEC_HI, U_EN, U_HI,
            f"Pointing to a photograph of a boy, {person} said, 'He is the son of the only son of my mother.' How is {person} related to the boy in the photograph?",
            f"एक लड़के की तस्वीर की ओर इशारा करते हुए {person} ने कहा, 'वह मेरी माँ के एकमात्र पुत्र का पुत्र है।' {person} उस लड़के से किस प्रकार संबंधित है?",
            "Father", "पिता",
            ["Uncle", "Brother", "Grandfather"], ["चाचा", "भाई", "दादा"],
            f"Mother's only son is {person} himself. The boy is {person}'s son, hence {person} is the Father.",
            f"माँ का एकमात्र पुत्र स्वयं {person} है। अतः वह लड़का {person} का पुत्र है और {person} उसका पिता है।",
            ans_idx
        ))
    else:
        qs.append(make_question(
            144, SEC_EN, SEC_HI, U_EN, U_HI,
            f"Introducing a gentleman, {person} remarked, 'His father is the only son of my grandfather.' How is {person} related to that gentleman?",
            f"एक सज्जन का परिचय कराते हुए {person} ने कहा, 'उसके पिता मेरे दादा के एकमात्र पुत्र हैं।' {person} उस सज्जन से किस प्रकार संबंधित है?",
            "Brother", "भाई",
            ["Father", "Uncle", "Cousin"], ["पिता", "चाचा", "चचेरा भाई"],
            f"Grandfather's only son is {person}'s father. If the gentleman's father is the same person, {person} and the gentleman are Brothers.",
            f"दादा के एकमात्र पुत्र {person} के पिता हैं। अतः वह सज्जन और {person} परस्पर भाई हैं।",
            ans_idx
        ))

    # Q145: Direction Sense Test (strictly unique distances for each idx)
    d_n = 10 + idx
    d_e = 8 + (idx % 5)
    ans_idx = (145 + idx) % 4
    qs.append(make_question(
        145, SEC_EN, SEC_HI, U_EN, U_HI,
        f"A candidate walks {d_n} meters North, then turns right and walks {d_e} meters, and finally turns right and walks {d_n} meters. In which direction is the candidate relative to the starting point?",
        f"एक अभ्यर्थी {d_n} मीटर उत्तर दिशा में चलता है, फिर दाएं मुड़कर {d_e} मीटर चलता है, और अंत में दाएं मुड़कर {d_n} मीटर चलता है। प्रारंभिक बिंदु के सापेक्ष अभ्यर्थी किस दिशा में है?",
        "East", "पूर्व",
        ["North", "West", "South"], ["उत्तर", "पश्चिम", "दक्षिण"],
        f"Moving {d_n}m North and then {d_n}m South cancels the vertical movement. The net displacement is {d_e}m directly East.",
        f"{d_n}मी उत्तर और फिर {d_n}मी दक्षिण चलने से ऊर्ध्वाधर विस्थापन शून्य हो जाता है। अतः शुद्ध विस्थापन ठीक {d_e}मी पूर्व दिशा में है।",
        ans_idx
    ))

    # Q146: Averages (strictly unique values for each idx)
    vals = [20 + idx, 24 + idx, 28 + idx, 32 + idx, 36 + idx]
    avg_val = sum(vals) / len(vals)
    ans_idx = (146 + idx) % 4
    qs.append(make_question(
        146, SEC_EN, SEC_HI, U_EN, U_HI,
        f"Find the arithmetic mean (average) of the five numbers: {vals[0]}, {vals[1]}, {vals[2]}, {vals[3]}, {vals[4]}.",
        f"पाँच संख्याओं {vals[0]}, {vals[1]}, {vals[2]}, {vals[3]}, {vals[4]} का समांतर माध्य (औसत) ज्ञात करें:",
        str(int(avg_val)), str(int(avg_val)),
        [str(int(avg_val - 4)), str(int(avg_val + 4)), str(int(avg_val + 8))],
        [str(int(avg_val - 4)), str(int(avg_val + 4)), str(int(avg_val + 8))],
        f"Sum = {sum(vals)}. Average = {sum(vals)} / 5 = {int(avg_val)}.",
        f"कुल योग = {sum(vals)}। औसत = {sum(vals)} / 5 = {int(avg_val)}।",
        ans_idx
    ))

    # Q147: Percentages, Profit and Loss (strictly unique CP for each idx)
    cp = 400 + idx * 25
    profit_pct = 10 + (idx % 5) * 5
    sp = cp + int(cp * profit_pct / 100)
    ans_idx = (147 + idx) % 4
    qs.append(make_question(
        147, SEC_EN, SEC_HI, U_EN, U_HI,
        f"A library procurement officer purchases reference manuals for Rs. {cp} and supplies them with a margin of {profit_pct}%. What is the invoiced selling price?",
        f"पुस्तकालय क्रय अधिकारी ₹{cp} में संदर्भ ग्रंथ खरीदता है तथा {profit_pct}% के लाभ मार्जिन पर आपूर्ति करता है। इनवॉइस का विक्रय मूल्य क्या होगा?",
        f"Rs. {sp}", f"₹{sp}",
        [f"Rs. {sp - 35}", f"Rs. {sp + 45}", f"Rs. {cp + profit_pct}"],
        [f"₹{sp - 35}", f"₹{sp + 45}", f"₹{cp + profit_pct}"],
        f"SP = CP * (1 + profit%/100) = {cp} * (1 + {profit_pct}/100) = Rs. {sp}.",
        f"विक्रय मूल्य = क्रय मूल्य x (1 + लाभ%/100) = {cp} x (1 + {profit_pct}/100) = ₹{sp}।",
        ans_idx
    ))

    # Q148: Simple Interest (strictly unique principal for each idx)
    p_si = 1500 + idx * 100
    r_si = 5 + (idx % 6)
    t_si = 2 + (idx % 3)
    si_val = int((p_si * r_si * t_si) / 100)
    ans_idx = (148 + idx) % 4
    qs.append(make_question(
        148, SEC_EN, SEC_HI, U_EN, U_HI,
        f"What is the simple interest accrued on an institutional library endowment fund of Rs. {p_si} invested at {r_si}% per annum for {t_si} years?",
        f"₹{p_si} के संस्थागत पुस्तकालय अक्षय निधि पर {r_si}% वार्षिक दर से {t_si} वर्ष में कितना साधारण ब्याज अर्जित होगा?",
        f"Rs. {si_val}", f"₹{si_val}",
        [f"Rs. {si_val - 25}", f"Rs. {si_val + 35}", f"Rs. {si_val + 70}"],
        [f"₹{si_val - 25}", f"₹{si_val + 35}", f"₹{si_val + 70}"],
        f"SI = (P * R * T) / 100 = ({p_si} * {r_si} * {t_si}) / 100 = Rs. {si_val}.",
        f"साधारण ब्याज = (मूलधन x दर x समय) / 100 = ({p_si} x {r_si} x {t_si}) / 100 = ₹{si_val}।",
        ans_idx
    ))

    # Q149: Time and Work (strictly unique worker pairing)
    days_a = 12 + idx
    days_b = 24 + idx * 2
    # Combined = (days_a * days_b) / (days_a + days_b) = (days_a * 2*days_a) / (3*days_a) = 2/3 * days_a
    combined = (days_a * days_b) / (days_a + days_b)
    comb_str = f"{combined:.1f}".rstrip('0').rstrip('.')
    ans_idx = (149 + idx) % 4
    qs.append(make_question(
        149, SEC_EN, SEC_HI, U_EN, U_HI,
        f"Assistant Librarian 'A' can digitize a collection in {days_a} days, while Assistant 'B' takes {days_b} days for the same workload. How many days will they take working collaboratively?",
        f"सहायक पुस्तकालय अध्यक्ष 'A' किसी संग्रह का डिजिटलीकरण {days_a} दिनों में तथा सहायक 'B' {days_b} दिनों में पूरा कर सकता है। दोनों मिलकर इस कार्य को कितने दिनों में समाप्त करेंगे?",
        f"{comb_str} days", f"{comb_str} दिन",
        [f"{days_a - 3} days", f"{days_b - 6} days", f"{int(combined) + 4} days"],
        [f"{days_a - 3} दिन", f"{days_b - 6} दिन", f"{int(combined) + 4} दिन"],
        f"Combined 1-day work = 1/{days_a} + 1/{days_b}. Total days = ({days_a}*{days_b})/({days_a}+{days_b}) = {comb_str} days.",
        f"संयुक्त 1 दिन का कार्य = 1/{days_a} + 1/{days_b}। कुल दिन = ({days_a}x{days_b})/({days_a}+{days_b}) = {comb_str} दिन।",
        ans_idx
    ))

    # Q150: Time, Speed and Distance (strictly unique train speed)
    speed_kmh = 36 + idx * 2
    speed_ms = speed_kmh * 5 / 18
    speed_ms_str = f"{speed_ms:.2f}".rstrip('0').rstrip('.')
    ans_idx = (150 + idx) % 4
    qs.append(make_question(
        150, SEC_EN, SEC_HI, U_EN, U_HI,
        f"A mobile library van travels at a steady speed of {speed_kmh} km/h between rural distribution points. What is its speed in meters per second (m/s)?",
        f"एक सचल पुस्तकालय वाहन ग्रामीण वितरण केंद्रों के मध्य {speed_kmh} किमी/घंटा की स्थिर गति से चलता है। मीटर प्रति सेकंड (m/s) में इसकी चाल क्या होगी?",
        f"{speed_ms_str} m/s", f"{speed_ms_str} मीटर/सेकंड",
        [f"{float(speed_ms_str) - 3:.1f} m/s", f"{float(speed_ms_str) + 4:.1f} m/s", f"{float(speed_ms_str) + 8:.1f} m/s"],
        [f"{float(speed_ms_str) - 3:.1f} मीटर/सेकंड", f"{float(speed_ms_str) + 4:.1f} मीटर/सेकंड", f"{float(speed_ms_str) + 8:.1f} मीटर/सेकंड"],
        f"Speed in m/s = {speed_kmh} * (5/18) = {speed_ms_str} m/s.",
        f"मीटर/सेकंड में चाल = {speed_kmh} x (5/18) = {speed_ms_str} मीटर/सेकंड।",
        ans_idx
    ))

    assert len(qs) == 10, f"Expected 10 questions, got {len(qs)}"
    return qs
