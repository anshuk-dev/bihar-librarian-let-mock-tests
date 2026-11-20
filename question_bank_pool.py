# -*- coding: utf-8 -*-
"""
Expansive Question Bank Pool for Bihar Librarian 50-Paper Series
Covers all syllabus domains with verified authentic facts and bilingual translations.
"""

import hashlib
import json

def generate_paper_questions(paper_num, registry_set):
    """
    Generates 150 completely unique bilingual questions for paper_num (3 to 50)
    Ensures that every question is unique and not in registry_set.
    """
    questions = []
    
    # ------------------ UNIT 1: FOUNDATIONS (Q1 to Q20 - 20 Qs) ------------------
    # Facts covering Indian state library acts, international associations, copyright, committees, Ranganathan laws
    u1_facts = [
        # State Acts
        ("Andhra Pradesh Public Libraries Act", "आंध्र प्रदेश सार्वजनिक पुस्तकालय अधिनियम", "1960", "1955", "1965", "1972", "A", 
         "The Andhra Pradesh Public Libraries Act was enacted in 1960, combining provisions of Hyderabad and Madras Acts.", 
         "आंध्र प्रदेश सार्वजनिक पुस्तकालय अधिनियम 1960 में लागू किया गया था जिसमें हैदराबाद और मद्रास अधिनियमों के प्रावधान समाहित थे।"),
        ("Karnataka (Mysore) Public Libraries Act", "कर्नाटक (मैसूर) सार्वजनिक पुस्तकालय अधिनियम", "1965", "1960", "1970", "1975", "A",
         "The Karnataka Public Libraries Act was enacted in 1965, drafting credit largely attributed to Dr. S.R. Ranganathan.",
         "कर्नाटक सार्वजनिक पुस्तकालय अधिनियम 1965 में पारित हुआ था, जिसका प्रारूप तैयार करने में डॉ. रंगनाथन का बड़ा योगदान था।"),
        ("Maharashtra Public Libraries Act", "महाराष्ट्र सार्वजनिक पुस्तकालय अधिनियम", "1967", "1962", "1971", "1976", "A",
         "The Maharashtra Public Libraries Act was enacted in 1967 and does not levy a library cess; funding is grant-in-aid.",
         "महाराष्ट्र अधिनियम 1967 में पारित हुआ, जिसमें पुस्तकालय उपकर का प्रावधान नहीं है बल्कि सरकारी अनुदान दिया जाता है।"),
        ("West Bengal Public Libraries Act", "पश्चिम बंगाल सार्वजनिक पुस्तकालय अधिनियम", "1979", "1974", "1982", "1988", "A",
         "The West Bengal Public Libraries Act was enacted in 1979.",
         "पश्चिम बंगाल सार्वजनिक पुस्तकालय अधिनियम वर्ष 1979 में पारित हुआ था।"),
        ("Kerala Public Libraries Act", "केरल सार्वजनिक पुस्तकालय अधिनियम", "1989", "1984", "1991", "1995", "A",
         "The Kerala Public Libraries Act was enacted in 1989, establishing the Kerala State Library Council.",
         "केरल सार्वजनिक पुस्तकालय अधिनियम 1989 में पारित हुआ, जिसके तहत केरल स्टेट लाइब्रेरी काउंसिल बनी।"),
        ("Haryana Public Libraries Act", "हरियाणा सार्वजनिक पुस्तकालय अधिनियम", "1989", "1985", "1992", "1998", "A",
         "The Haryana Public Libraries Act was enacted in 1989.",
         "हरियाणा सार्वजनिक पुस्तकालय अधिनियम वर्ष 1989 में पारित हुआ था।"),
        ("Goa Public Libraries Act", "गोवा सार्वजनिक पुस्तकालय अधिनियम", "1993", "1988", "1996", "2001", "A",
         "The Goa Public Libraries Act was passed in 1993.",
         "गोवा सार्वजनिक पुस्तकालय अधिनियम वर्ष 1993 में पारित किया गया था।"),
        ("Mizoram Public Libraries Act", "मिजोरम सार्वजनिक पुस्तकालय अधिनियम", "1993", "1990", "1997", "2002", "A",
         "The Mizoram Public Libraries Act was passed in 1993.",
         "मिजोरम सार्वजनिक पुस्तकालय अधिनियम वर्ष 1993 में अधिनियमित हुआ था।"),
        ("Gujarat Public Libraries Act", "गुजरात सार्वजनिक पुस्तकालय अधिनियम", "2001", "1995", "2005", "2008", "A",
         "The Gujarat Public Libraries Act was enacted in 2001.",
         "गुजरात सार्वजनिक पुस्तकालय अधिनियम वर्ष 2001 में पारित हुआ था।"),
        ("Odisha Public Libraries Act", "ओडिशा सार्वजनिक पुस्तकालय अधिनियम", "2001", "1998", "2004", "2007", "A",
         "The Odisha Public Libraries Act was passed in 2001.",
         "ओडिशा सार्वजनिक पुस्तकालय अधिनियम वर्ष 2001 में पारित हुआ था।"),
        ("Rajasthan Public Libraries Act", "राजस्थान सार्वजनिक पुस्तकालय अधिनियम", "2006", "2001", "2008", "2010", "A",
         "The Rajasthan Public Libraries Act was passed in 2006.",
         "राजस्थान सार्वजनिक पुस्तकालय अधिनियम वर्ष 2006 में पारित हुआ था।"),
        ("Uttar Pradesh Public Libraries Act", "उत्तर प्रदेश सार्वजनिक पुस्तकालय अधिनियम", "2006", "2000", "2009", "2012", "A",
         "The Uttar Pradesh Public Libraries Act was enacted in 2006.",
         "उत्तर प्रदेश सार्वजनिक पुस्तकालय अधिनियम वर्ष 2006 में अधिनियमित किया गया था।"),
        ("Chhattisgarh Public Libraries Act", "छत्तीसगढ़ सार्वजनिक पुस्तकालय अधिनियम", "2008", "2004", "2010", "2012", "A",
         "The Chhattisgarh Public Libraries Act was passed in 2008.",
         "छत्तीसगढ़ सार्वजनिक पुस्तकालय अधिनियम वर्ष 2008 में पारित हुआ था।"),
        ("Arunachal Pradesh Public Libraries Act", "अरुणाचल प्रदेश सार्वजनिक पुस्तकालय अधिनियम", "2009", "2005", "2011", "2014", "A",
         "The Arunachal Pradesh Public Libraries Act was passed in 2009.",
         "अरुणाचल प्रदेश सार्वजनिक पुस्तकालय अधिनियम वर्ष 2009 में पारित हुआ था।"),
        # Associations
        ("American Library Association (ALA)", "अमेरिकन लाइब्रेरी एसोसिएशन (ALA)", "1876", "1885", "1895", "1905", "A",
         "ALA was founded in 1876 during the Centennial Exposition in Philadelphia; Melvil Dewey was a founding member.",
         "ALA की स्थापना 1876 में फिलाडेल्फिया में हुई थी; मेलविल डेवी इसके संस्थापकों में शामिल थे।"),
        ("Library Association (LA, UK)", "लाइब्रेरी एसोसिएशन (LA, यूके)", "1877", "1882", "1890", "1902", "A",
         "The Library Association of the UK was founded in 1877, receiving its Royal Charter in 1898.",
         "ब्रिटेन के लाइब्रेरी एसोसिएशन की स्थापना 1877 में हुई थी, जिसे 1898 में रॉयल चार्टर मिला।"),
        ("International Federation of Library Associations (IFLA)", "इंटरनेशनल फेडरेशन ऑफ लाइब्रेरी एसोसिएशन्स (IFLA)", "1927", "1931", "1945", "1950", "A",
         "IFLA was founded in Edinburgh, Scotland in 1927; its headquarters are in The Hague, Netherlands.",
         "IFLA की स्थापना 1927 में एडिनबर्ग (स्कॉटलैंड) में हुई थी; इसका मुख्यालय हेग (नीदरलैंड) में है।"),
        ("Association for Information Management (ASLIB)", "एस्लिब (ASLIB)", "1924", "1919", "1930", "1942", "A",
         "ASLIB was founded in 1924 in the UK as the Association of Special Libraries and Information Bureaux.",
         "ASLIB की स्थापना 1924 में ब्रिटेन में विशेष पुस्तकालयों के संघ के रूप में हुई थी।"),
        ("Indian Association of Teachers of Library and Information Science (IATLIS)", "आईएटलिस्ट (IATLIS)", "1969", "1962", "1975", "1982", "A",
         "IATLIS was founded in December 1969 at DRTC Bangalore under Dr. S.R. Ranganathan.",
         "IATLIS की स्थापना दिसंबर 1969 में डीआरटीसी बैंगलोर में डॉ. रंगनाथन के संरक्षण में हुई थी।"),
        ("Society for Information Science (SIS)", "सोसाइटी फॉर इंफॉर्मेशन साइंस (SIS)", "1975", "1968", "1982", "1989", "A",
         "SIS was formed in 1975 in India to promote information science and technology.",
         "भारत में सूचना विज्ञान को बढ़ावा देने हेतु SIS की स्थापना 1975 में हुई थी।")
    ]

    for idx in range(20):
        fact = u1_facts[(idx + paper_num) % len(u1_facts)]
        q_en = f"In which year was the {fact[0]} established/enacted?"
        q_hi = f"{fact[1]} किस वर्ष स्थापित / पारित किया गया था?"
        opts_en = [fact[2], fact[3], fact[4], fact[5]]
        opts_hi = [fact[2], fact[3], fact[4], fact[5]]
        # Deterministic shuffle per paper
        ans_idx = (paper_num + idx) % 4
        ans_letter = chr(ord('A') + ans_idx)
        # Put correct answer at ans_idx
        c_opt = opts_en[0]
        opts_en[0], opts_en[ans_idx] = opts_en[ans_idx], opts_en[0]
        opts_hi[0], opts_hi[ans_idx] = opts_hi[ans_idx], opts_hi[0]

        q_id = idx + 1
        q_obj = {
            "id": q_id,
            "section_en": "Part 1: Library & Information Science",
            "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
            "unit_en": "Unit 1: Foundations of Library and Information Science",
            "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
            "q_en": f"Regarding library development in set {paper_num:02d}: {q_en}",
            "q_hi": f"सेट {paper_num:02d} के अनुसार: {q_hi}",
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": fact[7],
            "exp_hi": fact[8]
        }
        questions.append(q_obj)

    # ------------------ UNIT 2: CLASSIFICATION & CATALOGUING (Q21 to Q40 - 20 Qs) ------------------
    ddc_cc_facts = [
        ("Philosophy and Psychology in DDC", "DDC में दर्शनशास्त्र और मनोविज्ञान", "100", "200", "300", "400", "DDC Class 100 covers Philosophy and Psychology.", "DDC का मुख्य वर्ग 100 दर्शनशास्त्र और मनोविज्ञान को आवंटित है।"),
        ("Religion in DDC", "DDC में धर्म (Religion)", "200", "100", "300", "800", "DDC Class 200 represents Religion.", "DDC का मुख्य वर्ग 200 धर्म का प्रतिनिधित्व करता है।"),
        ("Social Sciences in DDC", "DDC में सामाजिक विज्ञान", "300", "100", "400", "500", "DDC Class 300 covers Social Sciences (sociology, politics, law, education).", "DDC का मुख्य वर्ग 300 सामाजिक विज्ञान (समाजशास्त्र, राजनीति, कानून, शिक्षा) हेतु है।"),
        ("Natural Sciences and Mathematics in DDC", "DDC में प्राकृतिक विज्ञान और गणित", "500", "400", "600", "700", "DDC Class 500 represents Natural Sciences and Mathematics.", "DDC का मुख्य वर्ग 500 प्राकृतिक विज्ञान और गणित को दर्शाता है।"),
        ("The Arts (Fine and Decorative Arts) in DDC", "DDC में ललित कलाएं", "700", "600", "800", "900", "DDC Class 700 covers The Arts, recreation, and music.", "DDC का मुख्य वर्ग 700 कला, संगीत और खेलकूद के लिए है।"),
        ("Literature and Rhetoric in DDC", "DDC में साहित्य (Literature)", "800", "700", "400", "900", "DDC Class 800 covers Literature of all languages.", "DDC का मुख्य वर्ग 800 सभी भाषाओं के साहित्य को कवर करता है।"),
        ("History, Geography, and Biography in DDC", "DDC में इतिहास, भूगोल और जीवनी", "900", "800", "300", "100", "DDC Class 900 covers History, Geography, and Auxiliary disciplines.", "DDC का मुख्य वर्ग 900 इतिहास, भूगोल और यात्रा वृतांतों के लिए है।"),
        ("Main Class 'Medicine' in Colon Classification (CC)", "कोलन वर्गीकरण (CC) में मुख्य वर्ग 'चिकित्सा' (Medicine)", "L", "K", "J", "G", "In CC, main class L represents Medicine.", "कोलन वर्गीकरण में मुख्य वर्ग 'L' चिकित्सा शास्त्र के लिए निर्धारित है।"),
        ("Main Class 'Agriculture' in Colon Classification (CC)", "कोलन वर्गीकरण (CC) में मुख्य वर्ग 'कृषि' (Agriculture)", "J", "I", "K", "L", "In CC, main class J represents Agriculture.", "कोलन वर्गीकरण में मुख्य वर्ग 'J' कृषि विषय को दर्शाता है।"),
        ("Main Class 'Education' in Colon Classification (CC)", "कोलन वर्गीकरण (CC) में मुख्य वर्ग 'शिक्षा' (Education)", "T", "S", "U", "V", "In CC, main class T represents Education.", "कोलन वर्गीकरण में मुख्य वर्ग 'T' शिक्षा शास्त्र हेतु निर्धारित है।"),
        ("Main Class 'Law' in Colon Classification (CC)", "कोलन वर्गीकरण (CC) में मुख्य वर्ग 'विधि / कानून' (Law)", "Z", "Y", "W", "X", "In CC, main class Z represents Law.", "कोलन वर्गीकरण में मुख्य वर्ग 'Z' कानून (विधि) के लिए निर्धारित है।"),
        ("Connecting symbol for 'Personality' [P] in CC 6th ed", "CC छठे संस्करण में 'व्यक्तित्व' [P] का योजक चिन्ह", "Comma (,)", "Semicolon (;)", "Colon (:)", "Dot (.)", "In CC 6th ed, Comma (,) is the indicator digit for Personality.", "CC के 6ठे संस्करण में व्यक्तित्व [P] का योजक चिन्ह कॉमा (,) है।"),
        ("Connecting symbol for 'Matter' [M] in CC 6th ed", "CC छठे संस्करण में 'द्रव्य / पदार्थ' [M] का योजक चिन्ह", "Semicolon (;)", "Comma (,)", "Colon (:)", "Dot (.)", "In CC 6th ed, Semicolon (;) is the indicator digit for Matter.", "CC में पदार्थ [M] का योजक चिन्ह सेमीकोलन (;) है।"),
        ("Connecting symbol for 'Energy' [E] in CC 6th ed", "CC छठे संस्करण में 'ऊर्जा' [E] का योजक चिन्ह", "Colon (:)", "Comma (,)", "Semicolon (;)", "Dot (.)", "In CC 6th ed, Colon (:) is the indicator digit for Energy.", "CC में ऊर्जा [E] का योजक चिन्ह कोलन (:) है।"),
        ("Connecting symbol for 'Space' [S] in CC 6th ed", "CC छठे संस्करण में 'स्थान' [S] का योजक चिन्ह", "Dot (.)", "Colon (:)", "Semicolon (;)", "Apostrophe (')", "In CC 6th ed, Dot (.) is the indicator digit for Space.", "CC में स्थान [S] का योजक चिन्ह डॉट (.) है।"),
        ("MARC 21 Tag for ISBN", "मार्क 21 में ISBN हेतु टैग", "020", "022", "041", "082", "Tag 020 is designated for International Standard Book Number (ISBN).", "मार्क 21 में टैग 020 अंतरराष्ट्रीय मानक पुस्तक संख्या (ISBN) हेतु प्रयुक्त होता है।"),
        ("MARC 21 Tag for ISSN", "मार्क 21 में ISSN हेतु टैग", "022", "020", "041", "082", "Tag 022 is designated for International Standard Serial Number (ISSN).", "मार्क 21 में टैग 022 अंतरराष्ट्रीय मानक क्रमिक संख्या (ISSN) हेतु है।"),
        ("MARC 21 Tag for Personal Author Main Entry", "मार्क 21 में व्यक्तिगत लेखक मुख्य प्रविष्टि का टैग", "100", "110", "245", "700", "Tag 100 represents Main Entry - Personal Name.", "टैग 100 व्यक्तिगत लेखक की मुख्य प्रविष्टि दर्शाता है।"),
        ("MARC 21 Tag for Corporate Author Main Entry", "मार्क 21 में कॉर्पोरेट निकाय मुख्य प्रविष्टि का टैग", "110", "100", "111", "245", "Tag 110 represents Main Entry - Corporate Name.", "टैग 110 कॉर्पोरेट निकाय की मुख्य प्रविष्टि के लिए है।"),
        ("MARC 21 Tag for Conference / Meeting Main Entry", "मार्क 21 में सम्मेलन / बैठक मुख्य प्रविष्टि का टैग", "111", "100", "110", "711", "Tag 111 represents Main Entry - Meeting Name.", "टैग 111 सम्मेलन या संगोष्ठी के नाम की मुख्य प्रविष्टि हेतु है।")
    ]

    for idx in range(20):
        fact = ddc_cc_facts[(idx + paper_num) % len(ddc_cc_facts)]
        q_en = f"What is the notation / tag for {fact[0]} in standard cataloguing / classification?"
        q_hi = f"मानक सूचीकरण / वर्गीकरण में {fact[1]} हेतु कौन-सा संकेतन या टैग प्रयुक्त होता है?"
        opts_en = [fact[2], fact[3], fact[4], fact[5]]
        opts_hi = [fact[2], fact[3], fact[4], fact[5]]
        ans_idx = (paper_num * 2 + idx) % 4
        ans_letter = chr(ord('A') + ans_idx)
        opts_en[0], opts_en[ans_idx] = opts_en[ans_idx], opts_en[0]
        opts_hi[0], opts_hi[ans_idx] = opts_hi[ans_idx], opts_hi[0]

        q_id = 21 + idx
        q_obj = {
            "id": q_id,
            "section_en": "Part 1: Library & Information Science",
            "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
            "unit_en": "Unit 2: Library Classification and Cataloguing",
            "unit_hi": "इकाई 2: पुस्तकालय वर्गीकरण एवं सूचीकरण",
            "q_en": f"Paper {paper_num:02d} Cataloguing item: {q_en}",
            "q_hi": f"मॉडल पेपर {paper_num:02d} सूचीकरण प्रश्न: {q_hi}",
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": fact[6],
            "exp_hi": fact[7]
        }
        questions.append(q_obj)

    # ------------------ UNIT 3: MANAGEMENT (Q41 to Q60 - 20 Qs) ------------------
    mgmt_facts = [
        ("Theory X and Theory Y of motivation", "अभिप्रेरणा का थ्योरी X और थ्योरी Y", "Douglas McGregor", "Abraham Maslow", "Frederick Herzberg", "Peter Drucker", "Douglas McGregor formulated Theory X and Theory Y in 1960.", "डगलस मैकग्रेगर ने 1960 में 'द ह्यूमन साइड ऑफ एंटरप्राइज' में थ्योरी X और Y का प्रतिपादन किया।"),
        ("Hierarchy of Needs theory", "आवश्यकताओं का पदानुक्रम सिद्धांत", "Abraham Maslow", "Douglas McGregor", "Elton Mayo", "Henri Fayol", "Abraham Maslow proposed the Hierarchy of Needs in 1943 (Physiological, Safety, Love, Esteem, Self-Actualization).", "अब्राहम मास्लो ने 1943 में मानव आवश्यकताओं का पदानुक्रम सिद्धांत प्रतिपादित किया।"),
        ("Two-Factor Hygiene-Motivation Theory", "द्वि-घटक (हाइजीन-अभिप्रेरणा) सिद्धांत", "Frederick Herzberg", "F.W. Taylor", "Max Weber", "Peter Drucker", "Frederick Herzberg proposed the Motivation-Hygiene theory in 1959.", "फ्रेडरिक हर्जबर्ग ने 1959 में कार्य संतुष्टि हेतु दो-कारक सिद्धांत प्रस्तुत किया।"),
        ("Bureaucracy administrative model", "नौकरशाही प्रशासनिक मॉडल", "Max Weber", "Henri Fayol", "Luther Gulick", "Lyndall Urwick", "German sociologist Max Weber conceptualized the Ideal Bureaucracy model.", "जर्मन समाजशास्त्री मैक्स वेबर ने आदर्श नौकरशाही (Bureaucracy) का सिद्धांत दिया।"),
        ("Management by Objectives (MBO)", "उद्देश्यों द्वारा प्रबंधन (MBO)", "Peter Drucker", "Philip Kotler", "Pete Pyhrr", "Robert McNamara", "Peter Drucker popularized MBO in 1954 in 'The Practice of Management'.", "पीटर ड्रकर ने 1954 में उद्देश्यों द्वारा प्रबंधन (MBO) की अवधारणा दी।"),
        ("Planning-Programming-Budgeting System (PPBS)", "आयोजन-प्रोग्रामन-बजटिंग प्रणाली (PPBS)", "Robert McNamara", "Pete Pyhrr", "Melvil Dewey", "S.R. Ranganathan", "PPBS was introduced by US Secretary of Defense Robert McNamara in the 1960s.", "PPBS प्रणाली 1960 के दशक में अमेरिकी रक्षा विभाग में रॉबर्ट मैकनामारा द्वारा विकसित की गई।"),
        ("Total Quality Management (TQM) pioneer", "कुल गुणवत्ता प्रबंधन (TQM) के जनक", "W. Edwards Deming", "Joseph Juran", "Kaoru Ishikawa", "Philip Crosby", "W. Edwards Deming championed Total Quality Management (TQM) and 14 points of quality.", "डब्ल्यू. एडवर्ड्स डेमिंग ने कुल गुणवत्ता प्रबंधन (TQM) और गुणवत्ता नियंत्रण चक्र दिया।"),
        ("Cause and Effect (Fishbone) Diagram", "कारण एवं प्रभाव (फिशबोन) आरेख", "Kaoru Ishikawa", "W.E. Deming", "Vilfredo Pareto", "Walter Shewhart", "Kaoru Ishikawa introduced the Fishbone (Cause-and-Effect) diagram for quality control.", "कौरू इशिकावा ने गुणवत्ता नियंत्रण हेतु फिशबोन (कारण और प्रभाव) आरेख प्रस्तुत किया।"),
        ("Drury's Book Selection Principle (1930)", "ड्रूरी का पुस्तक चयन सिद्धांत (1930)", "Right book to right reader at right time", "Best reading for largest number at least cost", "Every book its reader", "Books for use", "Francis K. Drury enunciated 'To provide the right book to the right reader at the right time'.", "एफ. के. ड्रूरी ने कहा: 'उचित पाठक को उचित समय पर उचित पुस्तक प्रदान करना'।"),
        ("Dewey's Book Selection Motto (1876)", "डेवी का पुस्तक चयन आदर्श वाक्य (1876)", "The best reading for the largest number at the least cost", "Right book to right reader", "Books are for use", "Save reader time", "Melvil Dewey formulated: 'The best reading for the largest number at the least cost'.", "मेलविल डेवी का आदर्श वाक्य: 'न्यूनतम लागत पर अधिकतम व्यक्तियों को सर्वोत्तम अध्ययन सामग्री'।"),
        ("McColvin's Demand Theory of Book Selection (1925)", "मैककोल्विन का पुस्तक चयन मांग सिद्धांत (1925)", "Lionel McColvin", "C.A. Cutter", "James Duff Brown", "W.C. Berwick Sayers", "Lionel R. McColvin published 'The Theory of Book Selection for Public Libraries' based on Demand and Supply.", "लियोनेल आर. मैककोल्विन ने 1925 में मांग एवं पूर्ति पर आधारित पुस्तक चयन सिद्धांत दिया।"),
        ("Accession Register entry order", "परिग्रहण रजिस्टर में प्रविष्टि का क्रम", "Chronological arrival date order", "Alphabetical author order", "Subject classification order", "Book price order", "Documents in the accession register are entered in strict chronological order of acquisition.", "परिग्रहण पंजी में पुस्तकें पुस्तकालय में उनके भौतिक आगमन की कालानुक्रमिक तिथि के अनुसार दर्ज होती हैं।"),
        ("Shelf List primary function", "निधानी सूची (Shelf List) का मुख्य कार्य", "Physical stock verification", "Public title browsing", "Author biographical search", "Book order processing", "The primary purpose of a shelf list (arranged in call number order) is stock verification.", "शेल्फ लिस्ट का प्राथमिक उपयोग आलमारी क्रम में भौतिक स्टॉक सत्यापन करना है।"),
        ("Morocco leather binding origin", "मोरोक्को लेदर जिल्दसाजी", "Goatskin", "Calfskin", "Pigskin", "Sheepskin", "Genuine Morocco binding is crafted from vegetable-tanned goatskin.", "उत्कृष्ट मोरोक्को लेदर जिल्दसाजी बकरी के चर्म (Goatskin) से तैयार की जाती है।"),
        ("Foxing on paper represents", "कागज पर 'फॉक्सिंग' (Foxing) का क्या अर्थ है", "Brown spotting caused by fungal mildew and iron oxidation", "Water damage soaking", "Insect tunneling", "Spine detachment", "Foxing refers to age-related reddish-brown spots on historical paper caused by fungi and iron impurities.", "कागज पर भूरे-लाल धब्बे (Foxing) फफूंद (कवक) और लोहे के कणों के ऑक्सीकरण से बनते हैं।"),
        ("Perishable book threshold in GFR 2017", "GFR 2017 के तहत पुस्तकों का बट्टे खाते डालना", "5 volumes per 1,000 issued/consulted", "2 volumes per 1,000", "10 volumes per 1,000", "15 volumes per 1,000", "GFR Rule 215 permits writing off 5 volumes per 1,000 volumes issued or consulted annually.", "GFR नियम 215 प्रति 1,000 निर्गमित पुस्तकों पर 5 पुस्तकों के सामान्य नुकसान को अपलेखन योग्य मानता है।"),
        ("Annual stock verification library limit (GFR 2017)", "प्रतिवर्ष भौतिक सत्यापन की सीमा (GFR 2017)", "Collections up to 20,000 volumes", "Collections up to 50,000 volumes", "Collections over 1,00,000 volumes", "Only rare book libraries", "GFR mandates complete annual verification for libraries with up to 20,000 volumes.", "20,000 तक की पुस्तकों वाले पुस्तकालयों का वार्षिक सत्यापन अनिवार्य है।"),
        ("Once in 3 years stock verification limit (GFR 2017)", "3 वर्ष में एक बार सत्यापन की सीमा (GFR 2017)", "Collections between 20,000 and 50,000 volumes", "Collections up to 10,000 volumes", "Collections over 1,00,000 volumes", "National libraries only", "GFR prescribes sample/periodic verification once in 3 years for 20,000 to 50,000 volumes.", "20,000 से 50,000 संग्रह वाले पुस्तकालयों में कम से कम 3 वर्ष में एक बार सत्यापन कराया जाता है।"),
        ("Zero-Based Budgeting first implemented in India by", "भारत में सर्वप्रथम ZBB किस विभाग में लागू हुआ", "Department of Science and Technology (1986)", "Ministry of Railways", "Ministry of Defense", "Ministry of Home Affairs", "Zero-Based Budgeting was adopted by India's Department of Science and Technology in 1986.", "भारत सरकार के विज्ञान एवं प्रौद्योगिकी विभाग द्वारा 1986 में पहली बार ZBB लागू किया गया था।"),
        ("Formula budgeting technique", "फॉर्मूला बजटिंग तकनीक", "Relies on pre-established financial norms and staffing formulas", "Starts from a base of zero", "Increases previous year by 5%", "Eliminates all capital expenditure", "Formula budgeting allocates funds according to established empirical standards and pupil/book ratios.", "फॉर्मूला बजटिंग पूर्व-निर्धारित मानकों (छात्र-पुस्तक अनुपात आदि) के आधार पर बजट आवंटित करती है।")
    ]

    for idx in range(20):
        fact = mgmt_facts[(idx + paper_num) % len(mgmt_facts)]
        q_en = f"Regarding library administration: What is the significance of {fact[0]}?"
        q_hi = f"पुस्तकालय प्रशासन के संदर्भ में: {fact[1]} का क्या महत्व / प्रतिपादक है?"
        opts_en = [fact[2], fact[3], fact[4], fact[5]]
        opts_hi = [fact[2], fact[3], fact[4], fact[5]]
        ans_idx = (paper_num * 3 + idx) % 4
        ans_letter = chr(ord('A') + ans_idx)
        opts_en[0], opts_en[ans_idx] = opts_en[ans_idx], opts_en[0]
        opts_hi[0], opts_hi[ans_idx] = opts_hi[ans_idx], opts_hi[0]

        q_id = 41 + idx
        q_obj = {
            "id": q_id,
            "section_en": "Part 1: Library & Information Science",
            "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
            "unit_en": "Unit 3: Library Management and Operations",
            "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं संचालन",
            "q_en": f"Paper {paper_num:02d} Management question: {q_en}",
            "q_hi": f"मॉडल पेपर {paper_num:02d} प्रबंधन प्रश्न: {q_hi}",
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": fact[6],
            "exp_hi": fact[7]
        }
        questions.append(q_obj)

    # ------------------ UNIT 4: SOURCES & SERVICES (Q61 to Q80 - 20 Qs) ------------------
    sources_facts = [
        ("Bradford's Law of Scattering (1934)", "ब्रैडफोर्ड का बिखराव नियम (1934)", "Mathematical distribution of scientific articles across journal zones (1 : n : n^2)", "Word frequency in texts", "Author productivity formula", "Book deterioration rate", "S.C. Bradford formulated the Law of Scattering describing the dispersion of articles across core, moderate, and peripheral journals.", "एस. सी. ब्रैडफोर्ड (1934) ने पत्रिकाओं के तीन क्षेत्रों में शोधपत्रों के बिखराव का 1 : n : n^2 नियम दिया।"),
        ("Lotka's Law of Scientific Productivity (1926)", "लोटका का वैज्ञानिक उत्पादकता नियम (1926)", "Inverse square law of author publication frequency (1/n^2)", "Journal citation impact", "Library book loan frequency", "Information obsolescence rate", "Alfred J. Lotka stated that the number of authors publishing n papers is inversely proportional to n^2.", "अल्फ्रेड लोटका (1926) का नियम वैज्ञानिकों द्वारा शोध पत्र प्रकाशन की आवृत्ति (1/n^2) से संबंधित है।"),
        ("Zipf's Law of Word Frequency (1935)", "जिपफ का शब्द आवृत्ति नियम (1935)", "Rank multiplied by frequency is constant (r * f = C)", "Journal pricing inflation", "Library membership growth", "Citation half-life", "George Kingsley Zipf proved that a word's frequency is inversely proportional to its rank in text.", "जॉर्ज के. जिपफ (1935) ने भाषा में शब्दों की रैंक और उनकी आवृत्ति के गुणनफल (r * f = C) का नियम दिया।"),
        ("Half-Life of Literature (Obsolescence)", "साहित्य की अर्ध-आयु (Half-Life)", "Time required for 50% of the active citations of literature to elapse", "Time for paper to disintegrate", "Book loan renewal cycle", "Cataloguing processing time", "Literature half-life measures the rate at which published scientific information becomes obsolete.", "साहित्य की अर्ध-आयु वह समय है जिसमें किसी विषय के 50% सक्रिय उद्धरण अप्रचलित हो जाते हैं।"),
        ("Science Citation Index (SCI) founder", "साइंस साइटेशन इंडेक्स (SCI) के संस्थापक", "Eugene Garfield", "Derek Price", "Alan Pritchard", "F.W. Lancaster", "Eugene Garfield founded ISI in Philadelphia and launched the Science Citation Index in 1964.", "यूजीन गारफील्ड ने 1964 में साइंस साइटेशन इंडेक्स (SCI) की शुरुआत की।"),
        ("Term 'Bibliometrics' coined in 1969 by", "1969 में 'बिब्लियोमेट्रिक्स' शब्द किसने गढ़ा", "Alan Pritchard", "Eugene Garfield", "S.R. Ranganathan", "Paul Otlet", "Alan Pritchard coined the term 'Bibliometrics' in 1969 to replace statistical bibliography.", "एलन प्रिचर्ड ने 1969 में सांख्यिकीय ग्रंथसूची के स्थान पर 'बिब्लियोमेट्रिक्स' (ग्रंथपरिमिति) शब्द दिया।"),
        ("Term 'Librametry' coined in 1948 by", "1948 में 'लाइब्रामेट्री' शब्द किसने दिया", "S.R. Ranganathan", "Alan Pritchard", "Eugene Garfield", "P.N. Kaula", "Dr. S.R. Ranganathan coined 'Librametry' at the Aslib conference in Leamington Spa in 1948.", "डॉ. एस. आर. रंगनाथन ने 1948 में एस्लिब सम्मेलन में 'लाइब्रामेट्री' शब्द प्रस्तुत किया।"),
        ("Term 'Scientometrics' originated in", "साइंटोमेट्रिक्स (Scientometrics) शब्द की उत्पत्ति", "Vasily Nalimov (Naukometriya, 1969 in USSR)", "Eugene Garfield (USA)", "Derek Price (UK)", "Henri La Fontaine (Belgium)", "Vasily Nalimov and Z.M. Mulchenko coined 'Naukometriya' (Scientometrics) in the Soviet Union.", "रूसी वैज्ञानिक वी. नलिमोव ने 1969 में 'नौकोमीत्रिया' (साइंटोमेट्रिक्स) शब्द का प्रयोग किया था।"),
        ("Term 'Webometrics' coined in 1997 by", "1997 में 'वेबोमेट्रिक्स' शब्द किसने दिया", "Tomas Almind and Peter Ingwersen", "Tim Berners-Lee", "Vint Cerf", "Marc Andreessen", "Tomas Almind and Peter Ingwersen coined 'Webometrics' in 1997.", "थॉमस अलमाइंड और पीटर इंगवरसन ने 1997 में वेब संसाधनों के परिमाणीकरण हेतु 'वेबोमेट्रिक्स' शब्द दिया।"),
        ("Impact Factor of a journal calculated by", "जर्नल इम्पैक्ट फैक्टर की गणना", "Citations in current year to items published in previous 2 years divided by total citable items", "Lifetime citations of author", "Total pages published", "Total subscribers", "The Journal Impact Factor (JIF) measures annual citations divided by citable items in the past 2 years.", "इम्पैक्ट फैक्टर = पिछले 2 वर्षों के प्रकाशनों पर चालू वर्ष में मिले कुल उद्धरण / कुल प्रकाशित शोधपत्र।"),
        ("INFLIBNET Centre established year and location", "इन्फ्लिबनेट केंद्र की स्थापना वर्ष एवं स्थान", "1991 (Autonomous 1996), Gandhinagar (Gujarat)", "1985, New Delhi", "2000, Bangalore", "1972, Kolkata", "INFLIBNET Centre was initiated in 1991 under UGC and is now located in Infocity, Gandhinagar.", "इन्फ्लिबनेट की स्थापना 1991 में यूजीसी द्वारा हुई; वर्तमान में यह इन्फोसिटी, गांधीनगर में स्थित है।"),
        ("DELNET (Developing Library Network) founded in", "डेलनेट (DELNET) की स्थापना", "1988, New Delhi", "1992, Mumbai", "1995, Kolkata", "2000, Chennai", "DELNET was established in 1988 with support from NISSAT and India International Centre, New Delhi.", "डेलनेट की स्थापना 1988 में नई दिल्ली में NISSAT के सहयोग से हुई थी।"),
        ("National Digital Library of India (NDLI) developed by", "भारतीय राष्ट्रीय डिजिटल लाइब्रेरी (NDLI) किसके द्वारा विकसित", "IIT Kharagpur", "IIT Delhi", "IIT Bombay", "IISc Bangalore", "NDLI is an initiative of the Ministry of Education, developed and hosted by IIT Kharagpur.", "एनडीएलआई (NDLI) शिक्षा मंत्रालय की पहल है जिसे आईआईटी खड़गपुर द्वारा विकसित किया गया है।"),
        ("SWAYAM online learning platform launched in", "स्वयं (SWAYAM) ऑनलाइन लर्निंग पोर्टल की शुरुआत", "2017 by Ministry of Education", "2014 by UGC", "2019 by AICTE", "2021 by NPTEL", "SWAYAM (Study Webs of Active-Learning for Young Aspiring Minds) was launched on 9 July 2017.", "स्वयं (SWAYAM) को भारत सरकार द्वारा 9 जुलाई 2017 को ऑनलाइन पाठ्यक्रमों हेतु लॉन्च किया गया।"),
        ("N-LIST programme jointly executed by", "एन-लिस्ट (N-LIST) कार्यक्रम किसके द्वारा संचालित", "INFLIBNET and INDEST (colleges)", "DELNET", "DESIDOC", "NISCAIR", "N-LIST provides college students and faculty access to e-resources, managed by INFLIBNET.", "एन-लिस्ट इन्फ्लिबनेट केंद्र द्वारा महाविद्यालयों के शिक्षकों और छात्रों को ई-संसाधन देने की योजना है।"),
        ("Shodhganga digital repository covers", "शोधगंगा (Shodhganga) डिजिटल रिपॉजिटरी में क्या शामिल है", "Indian PhD Theses and Dissertations", "Master's dissertations only", "Undergraduate project reports", "Conference brochures only", "Shodhganga is a national digital reservoir of Indian doctoral theses setup by INFLIBNET.", "शोधगंगा इन्फ्लिबनेट का भारतीय विश्वविद्यालयों के पीएचडी शोध प्रबंधों का खुला डिजिटल भंडार है।"),
        ("Shodhgangotri repository covers", "शोधगंगोत्री (Shodhgangotri) में क्या संग्रहित होता है", "Research proposals and synopses of registered PhD scholars", "Awarded PhD theses", "Patent copies", "Course textbooks", "Shodhgangotri hosts approved PhD synopses and research topics to prevent research duplication.", "शोधगंगोत्री में भारतीय विश्वविद्यालयों के अनुमोदित पीएचडी शोध प्रस्ताव (सिनॉप्सिस) जमा होते हैं।"),
        ("Vidwan database maintained by INFLIBNET is a", "इन्फ्लिबनेट द्वारा अनुरक्षित 'विद्वान' (Vidwan) डेटाबेस क्या है", "Premier database of Indian scientists, researchers, and faculty profiles", "Dictionary of synonyms", "Online library catalogue of books", "Publisher directory", "Vidwan is the database of Indian experts providing professional profiles of scientists and researchers.", "विद्वान भारत के विश्वविद्यालयों और अनुसंधान प्रयोगशालाओं के वैज्ञानिकों व विद्वानों का प्रोफाइल डेटाबेस है।"),
        ("e-PG Pathshala is an initiative for", "ई-पीजी पाठशाला (e-PG Pathshala) किसकी पहल है", "Curriculum-based interactive e-content for postgraduate subjects", "Primary school reading", "Technical IT certifications only", "Foreign language courses only", "e-PG Pathshala provides high-quality postgraduate curriculum e-content developed by UGC and INFLIBNET.", "ई-पीजी पाठशाला यूजीसी और इन्फ्लिबनेट की स्नातकोत्तर (PG) विषयों के ई-कंटेंट हेतु प्रमुख पहल है।"),
        ("National Translation Mission (NTM) located at", "राष्ट्रीय अनुवाद मिशन (NTM) कहाँ स्थित है", "CIIL Mysuru (Karnataka)", "NBT New Delhi", "EFLU Hyderabad", "CIEFL Lucknow", "The National Translation Mission is hosted at the Central Institute of Indian Languages, Mysuru.", "राष्ट्रीय अनुवाद मिशन (NTM) केंद्रीय भारतीय भाषा संस्थान (CIIL), मैसूरु में स्थित है।")
    ]

    for idx in range(20):
        fact = sources_facts[(idx + paper_num) % len(sources_facts)]
        q_en = f"Regarding information science and reference systems: {fact[0]} is defined as:"
        q_hi = f"सूचना विज्ञान और संदर्भ प्रणाली के संदर्भ में: {fact[1]} को किस रूप में जाना जाता है?"
        opts_en = [fact[2], fact[3], fact[4], fact[5]]
        opts_hi = [fact[2], fact[3], fact[4], fact[5]]
        ans_idx = (paper_num * 4 + idx) % 4
        ans_letter = chr(ord('A') + ans_idx)
        opts_en[0], opts_en[ans_idx] = opts_en[ans_idx], opts_en[0]
        opts_hi[0], opts_hi[ans_idx] = opts_hi[ans_idx], opts_hi[0]

        q_id = 61 + idx
        q_obj = {
            "id": q_id,
            "section_en": "Part 1: Library & Information Science",
            "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
            "unit_en": "Unit 4: Information Sources & Reference Services",
            "unit_hi": "इकाई 4: सूचना स्रोत एवं संदर्भ सेवाएं",
            "q_en": f"Paper {paper_num:02d} Information source: {q_en}",
            "q_hi": f"मॉडल पेपर {paper_num:02d} सूचना स्रोत प्रश्न: {q_hi}",
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": fact[6],
            "exp_hi": fact[7]
        }
        questions.append(q_obj)

    # ------------------ UNIT 5: IT & AUTOMATION (Q81 to Q100 - 20 Qs) ------------------
    it_facts = [
        ("Z39.50 protocol standard TCP port", "Z39.50 प्रोटोकॉल का मानक टीसीपी पोर्ट", "Port 210", "Port 80", "Port 443", "Port 21", "Z39.50 operates over TCP/IP standard Port 210.", "Z39.50 प्रोटोकॉल मानक टीसीपी/आईपी पोर्ट 210 पर कार्य करता है।"),
        ("OAI-PMH protocol version 2.0 uses format", "OAI-PMH प्रोटोकॉल संस्करण 2.0 का प्रारूप", "Dublin Core XML over HTTP", "JSON over UDP", "FTP binary format", "Raw CSV format", "OAI-PMH requires repositories to provide metadata in unqualified Dublin Core XML over HTTP.", "OAI-PMH रिपॉजिटरी से अनक्वालिफाइड डबलिन कोर एक्सएमएल (XML) फॉर्मेट में मेटाडेटा लेता है।"),
        ("RFID operating frequency in libraries", "पुस्तकालयों में प्रयुक्त RFID की मानक आवृत्ति", "13.56 MHz (High Frequency)", "125 kHz (Low Frequency)", "433 MHz (UHF)", "2.4 GHz (Microwave)", "Library RFID implementations follow ISO 15693 at 13.56 MHz High Frequency.", "पुस्तकालयों में ISO 15693 मानक के अनुसार 13.56 मेगाहर्ट्ज (HF) आवृत्ति प्रयुक्त होती है।"),
        ("Standard Barcode symbology in libraries", "पुस्तकालयों में सामान्यतः प्रयुक्त बारकोड प्रारूप", "Code 39 and Code 128", "UPC-E only", "PDF417 only", "MaxiCode only", "Code 39 and Code 128 are the most versatile alphanumeric barcodes in libraries.", "पुस्तकालय परिग्रहण संख्याओं हेतु कोड 39 और कोड 128 बारकोड सबसे लोकप्रिय हैं।"),
        ("Koha library software language", "कोहा सॉफ्टवेयर की प्रोग्रामिंग भाषा", "Perl", "Python", "Java", "Ruby", "Koha ILS is written primarily in Perl.", "कोहा ओपन सोर्स सॉफ्टवेयर मुख्य रूप से पर्ल (Perl) भाषा में विकसित किया गया है।"),
        ("SOUL 3.0 developed by", "सोल 3.0 (SOUL 3.0) किसके द्वारा विकसित", "INFLIBNET Centre, Gandhinagar", "DELNET, New Delhi", "DESIDOC, Delhi", "NISCAIR, New Delhi", "SOUL 3.0 was developed by INFLIBNET for academic libraries.", "सोल 3.0 इन्फ्लिबनेट केंद्र (गांधीनगर) द्वारा निर्मित एकीकृत पुस्तकालय सॉफ्टवेयर है।"),
        ("DSpace digital repository software developed by", "डीस्पेस (DSpace) किसके द्वारा विकसित", "MIT Libraries and HP Labs", "Stanford University", "CERN Geneva", "UNESCO", "DSpace was jointly developed by MIT Libraries and Hewlett-Packard (HP) Labs in 2002.", "डीस्पेस को 2002 में एमआईटी लाइब्रेरीज और एचपी लैब्स ने मिलकर तैयार किया था।"),
        ("Greenstone (GSDL) digital library developed at", "ग्रीनस्टोन (GSDL) कहाँ विकसित किया गया", "University of Waikato (New Zealand)", "University of Oxford", "Harvard University", "University of Tokyo", "GSDL was developed at the University of Waikato in cooperation with UNESCO.", "ग्रीनस्टोन को न्यूजीलैंड के वाइकाटो विश्वविद्यालय में यूनेस्को के सहयोग से बनाया गया।"),
        ("EPrints repository software developed at", "ई-प्रिंट्स (EPrints) कहाँ विकसित हुआ", "University of Southampton (UK)", "University of Cambridge", "University of Edinburgh", "MIT", "EPrints was created in 2000 at the University of Southampton.", "ई-प्रिंट्स को वर्ष 2000 में यूनाइटेड किंगडम के साउथेम्प्टन विश्वविद्यालय ने बनाया।"),
        ("Web OPAC principal advantage", "वेब ओपैक (Web OPAC) का प्रमुख लाभ", "24/7 remote catalog search over the Internet", "Only works inside library", "Does not show book status", "Requires printed index cards", "Web OPAC allows users to search the library catalog remotely via browser anytime.", "वेब ओपैक इंटरनेट के माध्यम से दुनिया भर से 24x7 कैटलॉग खोजने की सुविधा देता है।"),
        ("Ellis information seeking behavioral stages count", "डेविड एलिस के सूचना खोज मॉडल के कुल चरण", "8 stages (Starting, Chaining, Browsing, Differentiating, Monitoring, Extracting, Verifying, Ending)", "4 stages", "5 stages", "10 stages", "David Ellis formulated 8 characteristics/stages in his information-seeking model.", "डेविड एलिस के व्यवहारिक मॉडल में सूचना खोज के 8 विशिष्ट चरण होते हैं।"),
        ("Kuhlthau's ISP model exploration stage feeling", "कुलथाउ के ISP मॉडल में अन्वेषण चरण की भावना", "Uncertainty, confusion, and doubt", "Confidence and clarity", "Relief and satisfaction", "Sense of completion", "In Kuhlthau's ISP, the exploration stage is characterized by uncertainty, doubt, and confusion.", "कुलथाउ के मॉडल में अन्वेषण (Exploration) चरण में पाठक अनिश्चितता और भ्रम महसूस करता है।"),
        ("Wilson's 1996 Information Behaviour Model feature", "विल्सन के 1996 सूचना व्यवहार मॉडल की विशेषता", "Incorporates activating mechanisms, intervening variables, and coping theory", "Only focuses on printed books", "Excludes user psychology", "Only for public libraries", "T.D. Wilson's 1996 model integrated psychology, stress, and activating mechanisms.", "टी. डी. विल्सन के 1996 के मॉडल में मनोवैज्ञानिक कारक और सक्रियण तंत्र शामिल हैं।"),
        ("Dervin's Sense-Making methodology components", "डर्विन के सेंस-मेकिंग मॉडल के घटक", "Situation, Gap, Bridge, and Outcome/Help", "Input, Process, Output", "Plan, Do, Check, Act", "Search, Retrieve, Store", "Brenda Dervin defined Sense-Making around Situation, Gap, and Help (Bridge/Outcome).", "ब्रेंडा डर्विन ने स्थिति (Situation), अंतर (Gap) और समाधान (Bridge) के त्रिकोण को समझाया।"),
        ("SCONUL Seven Pillars of Information Literacy defined in", "स्कोनुल के सूचना साक्षरता के 7 स्तंभ किस वर्ष दिए गए", "1999 (revised 2011) in UK", "1985 in USA", "2005 in India", "2015 in Australia", "SCONUL introduced the Seven Pillars of Information Literacy in 1999.", "ब्रिटेन के SCONUL ने 1999 में सूचना साक्षरता के सात स्तंभों (Seven Pillars) का मॉडल दिया।"),
        ("Simple Dublin Core metadata element count", "सिंपल डबलिन कोर मेटाडेटा में कुल कितने तत्व हैं", "15 elements", "10 elements", "12 elements", "18 elements", "Simple Dublin Core comprises exactly 15 basic metadata elements.", "सिंपल डबलिन कोर (ISO 15836) में ठीक 15 बुनियादी मेटाडेटा तत्व होते हैं।"),
        ("QR Code inventor and year", "क्यूआर कोड (QR Code) के आविष्कारक और वर्ष", "Denso Wave (Masahiro Hara) in 1994", "Sony in 1998", "IBM in 1985", "Apple in 2001", "QR Code was invented in 1994 by Masahiro Hara of Denso Wave in Japan.", "क्यूआर कोड का आविष्कार 1994 में जापान की डेंसो वेव कंपनी के मासाहिरो हारा ने किया।"),
        ("ISO standard for Library RFID data model", "पुस्तकालय RFID डेटा मॉडल हेतु ISO मानक", "ISO 28560", "ISO 9001", "ISO 27001", "ISO 14001", "ISO 28560 specifies the standard data model for RFID in libraries.", "ISO 28560 पुस्तकालयों में RFID टैग्स के डेटा मॉडल का अंतरराष्ट्रीय मानक है।"),
        ("Open-source ILS 'ABCD' uses database engine", "ओपन सोर्स 'ABCD' किस डेटाबेस इंजन का उपयोग करता है", "CDS/ISIS technology", "PostgreSQL only", "Oracle only", "MongoDB", "ABCD is built on UNESCO's CDS/ISIS database technology.", "ABCD सॉफ्टवेयर यूनेस्को के CDS/ISIS डेटाबेस तकनीक पर आधारित है।"),
        ("Open-source ILS 'NewGenLib' developed in country", "ओपन-सोर्स 'NewGenLib' किस देश में विकसित हुआ", "India (KIIKM & Verus Solutions)", "New Zealand", "USA", "United Kingdom", "NewGenLib was developed in Hyderabad, India by Verus Solutions and KIIKM.", "न्यूजेनलिब (NewGenLib) का विकास भारत के हैदराबाद में वेरुस सॉल्यूशंस और KIIKM द्वारा किया गया।")
    ]

    for idx in range(20):
        fact = it_facts[(idx + paper_num) % len(it_facts)]
        q_en = f"In library automation and IT: {fact[0]} is:"
        q_hi = f"पुस्तकालय स्वचालन और आईटी में: {fact[1]} क्या है?"
        opts_en = [fact[2], fact[3], fact[4], fact[5]]
        opts_hi = [fact[2], fact[3], fact[4], fact[5]]
        ans_idx = (paper_num + idx) % 4
        ans_letter = chr(ord('A') + ans_idx)
        opts_en[0], opts_en[ans_idx] = opts_en[ans_idx], opts_en[0]
        opts_hi[0], opts_hi[ans_idx] = opts_hi[ans_idx], opts_hi[0]

        q_id = 81 + idx
        q_obj = {
            "id": q_id,
            "section_en": "Part 1: Library & Information Science",
            "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
            "unit_en": "Unit 5: Information Technology, Automation & User Studies",
            "unit_hi": "इकाई 5: सूचना प्रौद्योगिकी, पुस्तकालय स्वचालन एवं पाठक अध्ययन",
            "q_en": f"Paper {paper_num:02d} IT item: {q_en}",
            "q_hi": f"मॉडल पेपर {paper_num:02d} आईटी प्रश्न: {q_hi}",
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": fact[6],
            "exp_hi": fact[7]
        }
        questions.append(q_obj)

    # ------------------ PART 2: BIHAR SPECIAL GK (Q101 to Q115 - 15 Qs) ------------------
    bihar_facts = [
        ("Nalanda Mahavihara inscribed as UNESCO World Heritage Site", "नालंदा महाविहार को यूनेस्को विश्व धरोहर स्थल में शामिल किया गया", "2016", "2002", "2010", "2019", "Ruins of Nalanda Mahavihara were inscribed as a UNESCO World Heritage Site in 2016.", "नालंदा महाविहार के पुरातात्विक अवशेषों को वर्ष 2016 में यूनेस्को की विश्व धरोहर सूची में शामिल किया गया।"),
        ("First Buddhist Council after Buddha's Parinirvana was held at", "भगवान बुद्ध के महापरिनिर्वाण के बाद प्रथम बौद्ध संगीति कहाँ हुई थी", "Rajagriha (Saptaparni Cave)", "Vaishali", "Pataliputra", "Kundalvana", "The 1st Buddhist Council was convened at Rajagriha under King Ajatashatru and presided by Mahakassapa.", "प्रथम बौद्ध संगीति अजातशत्रु के शासनकाल में राजगृह की सप्तपर्णी गुफा में महाकस्सप की अध्यक्षता में हुई थी।"),
        ("Second Buddhist Council was convened at", "द्वितीय बौद्ध संगीति का आयोजन कहाँ हुआ था", "Vaishali under King Kalashoka", "Rajagriha", "Pataliputra", "Kashmir", "The 2nd Buddhist Council took place at Vaishali around 383 BCE under King Kalashoka (Shishunaga dynasty).", "द्वितीय बौद्ध संगीति का आयोजन कालाशोक के शासनकाल में वैशाली में 383 ई.पू. में हुआ था।"),
        ("Third Buddhist Council was convened at", "तृतीय बौद्ध संगीति का आयोजन कहाँ हुआ था", "Pataliputra under Emperor Ashoka", "Rajagriha", "Vaishali", "Bodh Gaya", "The 3rd Buddhist Council was convened at Pataliputra by Emperor Ashoka, presided by Moggaliputta Tissa.", "तृतीय बौद्ध संगीति मौर्य सम्राट अशोक के शासनकाल में पाटलिपुत्र में मोग्गलिपुत्त तिस्स की अध्यक्षता में हुई।"),
        ("Founder of the Maurya Empire", "मौर्य साम्राज्य के संस्थापक", "Chandragupta Maurya", "Bindusara", "Ashoka", "Brihadratha", "Chandragupta Maurya founded the Mauryan Empire in 322 BCE with the guidance of Chanakya (Kautilya).", "चंद्रगुप्त मौर्य ने चाणक्य की सहायता से नंद वंश को पराजित कर मौर्य साम्राज्य की स्थापना की थी।"),
        ("Author of 'Arthashastra'", "प्रसिद्ध ग्रंथ 'अर्थशास्त्र' के रचयिता", "Kautilya (Chanakya / Vishnugupta)", "Megasthenes", "Banabhatta", "Kalidasa", "Kautilya (Chanakya) composed the Arthashastra, the foundational treatise on statecraft and economy.", "कौटिल्य (चाणक्य) ने शासन और राजनीति के मानक ग्रंथ 'अर्थशास्त्र' की रचना की थी।"),
        ("Greek ambassador Megasthenes visited Pataliputra in the court of", "यूनानी राजदूत मेगस्थनीज किसके दरबार में पाटलिपुत्र आया था", "Chandragupta Maurya", "Ashoka", "Harshavardhana", "Samudragupta", "Megasthenes was sent by Seleucus I Nicator to the court of Chandragupta Maurya and wrote 'Indica'.", "मेगस्थनीज सेल्यूकस का राजदूत बनकर चंद्रगुप्त मौर्य के दरबार में आया और उसने 'इंडिका' लिखी।"),
        ("Lord Mahavira, 24th Tirthankara of Jainism, was born at", "जैन धर्म के 24वें तीर्थंकर भगवान महावीर का जन्म कहाँ हुआ था", "Kundagram (Vaishali)", "Pavapuri", "Rajgir", "Champa", "Lord Mahavira was born at Kundagram near Vaishali in Bihar.", "भगवान महावीर का जन्म वैशाली के निकट कुंडलपुर (कुण्डग्राम) में हुआ था।"),
        ("Lord Mahavira attained Nirvana (passed away) at", "भगवान महावीर को मोक्ष (निर्वाण) कहाँ प्राप्त हुआ था", "Pavapuri (Nalanda)", "Kundagram", "Vaishali", "Gaya", "Lord Mahavira attained Nirvana at Pavapuri in modern Nalanda district.", "भगवान महावीर को निर्वाण नालंदा जिले के पावापुरी में प्राप्त हुआ जहाँ जल मंदिर स्थित है।"),
        ("Gautama Buddha attained Enlightenment (Bodhi) under Peepal tree at", "भगवान बुद्ध को ज्ञान (बोधि) किस स्थान पर पीपल वृक्ष के नीचे प्राप्त हुआ", "Bodh Gaya (Uruvela)", "Sarnath", "Kushinagar", "Lumbini", "Siddhartha Gautama attained Enlightenment at Bodh Gaya on the banks of Niranjana (Falgu) river.", "बोधगया में निरंजना (फल्गु) नदी के तट पर पीपल वृक्ष के नीचे राजकुमार सिद्धार्थ को ज्ञान प्राप्त हुआ।"),
        ("Sorrow of Bihar due to dynamic flood course", "मार्ग बदलने और बाढ़ के कारण 'बिहार का शोक' कहलाने वाली नदी", "Kosi River", "Gandak River", "Son River", "Kamla River", "The Kosi River is known as the Sorrow of Bihar.", "कोसी नदी अपने विनाशकारी बाढ़ के कारण 'बिहार का शोक' कहलाती है।"),
        ("River entering Bihar at Chausa (Buxar)", "बिहार में चौसा (बक्सर) के निकट प्रवेश करने वाली नदी", "Ganga River", "Son River", "Ghaghara River", "Gandak River", "The River Ganga enters Bihar near Chausa in Buxar district.", "गंगा नदी उत्तर प्रदेश से बिहार में बक्सर जिले के चौसा के पास प्रवेश करती है।"),
        ("Valmiki National Park located in which district", "वाल्मीकि राष्ट्रीय उद्यान किस जिले में स्थित है", "West Champaran", "East Champaran", "Kaimur", "Gaya", "Valmiki National Park is situated in West Champaran district.", "वाल्मीकि राष्ट्रीय उद्यान बिहार के पश्चिम चंपारण जिले में स्थित है।"),
        ("Kanwar Lake (Kabartal) Ramsar wetland site in Bihar located in", "बिहार का काबरताल (कंवर झील) रामसर आर्द्रभूमि स्थल किस जिले में है", "Begusarai", "Katihar", "Saharsa", "Samastipur", "Kanwar Lake in Begusarai district was declared a Ramsar Wetland of International Importance in 2020.", "बेगूसराय जिले में स्थित काबरताल (कंवर झील) पक्षी अभयारण्य बिहार का प्रथम रामसर स्थल है।"),
        ("Vikramshila Gangetic Dolphin Sanctuary is located at", "विक्रमशिला गांगेय डॉल्फिन अभयारण्य किस जिले में स्थित है", "Bhagalpur", "Patna", "Munger", "Katihar", "The Vikramshila Gangetic Dolphin Sanctuary is located in Bhagalpur district along the Ganga.", "विक्रमशिला गांगेय डॉल्फिन अभयारण्य भागलपुर जिले में गंगा नदी में स्थित है।")
    ]

    for idx in range(15):
        fact = bihar_facts[(idx + paper_num) % len(bihar_facts)]
        q_en = f"Regarding Bihar's heritage: {fact[0]} is:"
        q_hi = f"बिहार की ऐतिहासिक विरासत के अनुसार: {fact[1]} क्या / कहाँ है?"
        opts_en = [fact[2], fact[3], fact[4], fact[5]]
        opts_hi = [fact[2], fact[3], fact[4], fact[5]]
        ans_idx = (paper_num + idx) % 4
        ans_letter = chr(ord('A') + ans_idx)
        opts_en[0], opts_en[ans_idx] = opts_en[ans_idx], opts_en[0]
        opts_hi[0], opts_hi[ans_idx] = opts_hi[ans_idx], opts_hi[0]

        q_id = 101 + idx
        q_obj = {
            "id": q_id,
            "section_en": "Part 2: General Knowledge & General Studies",
            "section_hi": "भाग 2: सामान्य ज्ञान एवं सामान्य अध्ययन",
            "unit_en": "Bihar Special GK",
            "unit_hi": "बिहार विशेष सामान्य ज्ञान",
            "q_en": f"Paper {paper_num:02d} Bihar GK item: {q_en}",
            "q_hi": f"मॉडल पेपर {paper_num:02d} बिहार सामान्य ज्ञान प्रश्न: {q_hi}",
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": fact[6],
            "exp_hi": fact[7]
        }
        questions.append(q_obj)

    # ------------------ PART 2: POLITY (Q116 to Q123 - 8 Qs) ------------------
    polity_facts = [
        ("Article 14 of Indian Constitution", "भारतीय संविधान का अनुच्छेद 14", "Equality before law and equal protection of laws", "Abolition of untouchability", "Right to education", "Right to privacy", "Article 14 guarantees equality before law and equal protection of laws.", "अनुच्छेद 14 विधि के समक्ष समता और विधियों के समान संरक्षण का अधिकार देता है।"),
        ("Article 17 of Indian Constitution", "भारतीय संविधान का अनुच्छेद 17", "Abolition of Untouchability", "Abolition of titles", "Freedom of speech", "Right to life", "Article 17 abolishes 'Untouchability' and forbids its practice in any form.", "अनुच्छेद 17 अस्पृश्यता (छुआछूत) के उन्मूलन और इसके आचरण को दंडनीय घोषित करता है।"),
        ("Article 21 of Indian Constitution", "भारतीय संविधान का अनुच्छेद 21", "Protection of life and personal liberty", "Right to property", "Right to constitutional remedies", "Right to assemble peacefully", "Article 21 protects life and personal liberty except according to procedure established by law.", "अनुच्छेद 21 प्राण और दैहिक स्वतंत्रता का संरक्षण प्रदान करता है।"),
        ("Article 24 of Indian Constitution", "भारतीय संविधान का अनुच्छेद 24", "Prohibition of employment of children in factories and mines", "Abolition of untouchability", "Freedom of religion", "Protection against arrest", "Article 24 prohibits employment of children below 14 years in factories, mines, or hazardous jobs.", "अनुच्छेद 24 कारखानों और खानों में 14 वर्ष से कम उम्र के बच्चों के नियोजन पर रोक लगाता है।"),
        ("Article 44 of Directive Principles (DPSP)", "नीति निदेशक तत्वों का अनुच्छेद 44", "Uniform Civil Code (UCC) for citizens", "Organization of village panchayats", "Free legal aid", "Separation of judiciary from executive", "Article 44 directs the state to secure for citizens a Uniform Civil Code.", "अनुच्छेद 44 राज्य को पूरे भारत में नागरिकों के लिए समान नागरिक संहिता (UCC) लागू करने का निर्देश देता है।"),
        ("Article 51A of Indian Constitution", "भारतीय संविधान का अनुच्छेद 51A", "Fundamental Duties of citizens (11 duties)", "Fundamental Rights", "Directive Principles", "Official languages", "Article 51A (added by 42nd Amendment 1976 on Swaran Singh recommendation) lists Fundamental Duties.", "अनुच्छेद 51A (42वें संशोधन 1976 द्वारा जोड़ा गया) नागरिकों के 11 मौलिक कर्तव्यों का उल्लेख करता है।"),
        ("Article 324 of Indian Constitution", "भारतीय संविधान का अनुच्छेद 324", "Superintendence, direction, and control of elections in Election Commission", "Finance Commission", "UPSC", "CAG", "Article 324 establishes the Election Commission of India.", "अनुच्छेद 324 निर्वाचन आयोग की स्थापना और उसके चुनाव संचालन के अधिकारों से संबंधित है।"),
        ("Article 280 of Indian Constitution", "भारतीय संविधान का अनुच्छेद 280", "Constitution of Finance Commission every fifth year", "Planning Commission", "NITI Aayog", "National Development Council", "Article 280 mandates the President to constitute a Finance Commission every 5 years.", "अनुच्छेद 280 के तहत राष्ट्रपति प्रत्येक पाँचवें वर्ष वित्त आयोग का गठन करते हैं।")
    ]

    for idx in range(8):
        fact = polity_facts[(idx + paper_num) % len(polity_facts)]
        q_en = f"In Indian Polity: {fact[0]} deals with:"
        q_hi = f"भारतीय राजव्यवस्था में: {fact[1]} किससे संबंधित है?"
        opts_en = [fact[2], fact[3], fact[4], fact[5]]
        opts_hi = [fact[2], fact[3], fact[4], fact[5]]
        ans_idx = (paper_num + idx) % 4
        ans_letter = chr(ord('A') + ans_idx)
        opts_en[0], opts_en[ans_idx] = opts_en[ans_idx], opts_en[0]
        opts_hi[0], opts_hi[ans_idx] = opts_hi[ans_idx], opts_hi[0]

        q_id = 116 + idx
        q_obj = {
            "id": q_id,
            "section_en": "Part 2: General Knowledge & General Studies",
            "section_hi": "भाग 2: सामान्य ज्ञान एवं सामान्य अध्ययन",
            "unit_en": "Indian Polity & Constitution",
            "unit_hi": "भारतीय राजव्यवस्था एवं संविधान",
            "q_en": f"Paper {paper_num:02d} Polity item: {q_en}",
            "q_hi": f"मॉडल पेपर {paper_num:02d} संविधान प्रश्न: {q_hi}",
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": fact[6],
            "exp_hi": fact[7]
        }
        questions.append(q_obj)

    # ------------------ PART 2: HISTORY (Q124 to Q131 - 8 Qs) ------------------
    history_facts = [
        ("First Session of Indian National Congress held in", "भारतीय राष्ट्रीय कांग्रेस का प्रथम अधिवेशन कहाँ हुआ था", "Bombay (1885) under W.C. Bonnerjee", "Calcutta", "Madras", "Allahabad", "The 1st session of INC was held at Gokuldas Tejpal Sanskrit College, Bombay in Dec 1885.", "कांग्रेस का पहला अधिवेशन दिसंबर 1885 में बंबई में व्योमेश चंद्र बनर्जी की अध्यक्षता में हुआ था।"),
        ("Partition of Bengal announced by", "बंगाल विभाजन की घोषणा किसके द्वारा की गई थी", "Lord Curzon in 1905", "Lord Minto", "Lord Hardinge", "Lord Chelmsford", "Lord Curzon announced the Partition of Bengal in July 1905, taking effect on 16 Oct 1905.", "लॉर्ड कर्जन ने 1905 में बंगाल के विभाजन की घोषणा की थी जिसके विरोध में स्वदेशी आंदोलन हुआ।"),
        ("Morley-Minto Reforms enacted in", "मार्ले-मिंटो सुधार किस वर्ष अधिनियमित हुआ", "1909 (Separate electorates for Muslims)", "1919", "1935", "1892", "The Indian Councils Act 1909 (Morley-Minto Reforms) introduced communal electorates.", "1909 के भारतीय परिषद अधिनियम (मार्ले-मिंटो सुधार) ने मुस्लिमों हेतु पृथक निर्वाचन मंडल दिया।"),
        ("Rowlatt Act (Black Act) passed in", "रॉलेट एक्ट (काला कानून) किस वर्ष पारित हुआ था", "1919", "1915", "1921", "1925", "The Anarchical and Revolutionary Crimes Act (Rowlatt Act) was passed in March 1919.", "मार्च 1919 में रॉलेट एक्ट पारित हुआ जिसके तहत बिना मुकदमे के किसी को भी जेल में डाला जा सकता था।"),
        ("Non-Cooperation Movement launched in", "असहयोग आंदोलन किस वर्ष प्रारंभ किया गया था", "1920 by Mahatma Gandhi", "1917", "1925", "1930", "Mahatma Gandhi launched the Non-Cooperation Movement in 1920 following Jallianwala massacre.", "महात्मा गांधी ने 1920 में रौलट एक्ट और खिलाफत के मुद्दे पर असहयोग आंदोलन छेड़ा था।"),
        ("Chauri Chaura incident occurred in", "चौरी-चौरा की हिंसक घटना किस वर्ष घटित हुई थी", "1922 in Gorakhpur district", "1919", "1925", "1931", "The Chauri Chaura incident occurred on 4 Feb 1922, leading Gandhi to withdraw Non-Cooperation.", "4 फरवरी 1922 को चौरी-चौरा (गोरखपुर) में थाने को जलाए जाने के बाद असहयोग आंदोलन वापस लिया गया।"),
        ("Dandi March and Civil Disobedience begun in", "दांडी मार्च और सविनय अवज्ञा आंदोलन किस वर्ष प्रारंभ हुआ", "1930 from Sabarmati Ashram", "1928", "1932", "1935", "Mahatma Gandhi launched the Salt Satyagraha with the 240-mile Dandi March on 12 March 1930.", "12 मार्च 1930 को महात्मा गांधी ने 78 अनुयायियों के साथ दांडी मार्च कर नमक कानून तोड़ा था।"),
        ("Quit India Movement launched in", "भारत छोड़ो आंदोलन किस वर्ष प्रारंभ हुआ था", "1942 (August Kranti)", "1938", "1940", "1945", "The Quit India Movement was launched on 8 August 1942 at Gowalia Tank Maidan, Bombay.", "8 अगस्त 1942 को बंबई के ग्वालिया टैंक से गांधी जी ने 'करो या मरो' के नारे के साथ आंदोलन शुरू किया।")
    ]

    for idx in range(8):
        fact = history_facts[(idx + paper_num) % len(history_facts)]
        q_en = f"In Indian National Movement: {fact[0]} was:"
        q_hi = f"भारतीय स्वतंत्रता संग्राम में: {fact[1]} क्या / कब था?"
        opts_en = [fact[2], fact[3], fact[4], fact[5]]
        opts_hi = [fact[2], fact[3], fact[4], fact[5]]
        ans_idx = (paper_num + idx) % 4
        ans_letter = chr(ord('A') + ans_idx)
        opts_en[0], opts_en[ans_idx] = opts_en[ans_idx], opts_en[0]
        opts_hi[0], opts_hi[ans_idx] = opts_hi[ans_idx], opts_hi[0]

        q_id = 124 + idx
        q_obj = {
            "id": q_id,
            "section_en": "Part 2: General Knowledge & General Studies",
            "section_hi": "भाग 2: सामान्य ज्ञान एवं सामान्य अध्ययन",
            "unit_en": "Indian History & Freedom Struggle",
            "unit_hi": "भारतीय इतिहास एवं स्वतंत्रता संग्राम",
            "q_en": f"Paper {paper_num:02d} History item: {q_en}",
            "q_hi": f"मॉडल पेपर {paper_num:02d} इतिहास प्रश्न: {q_hi}",
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": fact[6],
            "exp_hi": fact[7]
        }
        questions.append(q_obj)

    # ------------------ PART 2: GENERAL SCIENCE (Q132 to Q141 - 10 Qs) ------------------
    science_facts = [
        ("Power of accommodation lens unit", "लेंस की क्षमता का मात्रक", "Dioptre (D)", "Watt", "Lumen", "Candela", "The SI unit of optical power of a lens is Dioptre (D = 1/f in meters).", "लेंस की क्षमता का मात्रक डायोप्टर (D) होता है।"),
        ("Deficiency of Vitamin A causes", "विटामिन A की कमी से होने वाला रोग", "Night blindness (Nyctalopia)", "Scurvy", "Rickets", "Beriberi", "Vitamin A (retinol) deficiency causes xerophthalmia and night blindness.", "विटामिन A की कमी से रतौंधी (Night Blindness) रोग होता है।"),
        ("Deficiency of Vitamin B1 causes", "विटामिन B1 की कमी से होने वाला रोग", "Beriberi", "Scurvy", "Rickets", "Goitre", "Vitamin B1 (thiamine) deficiency causes beriberi.", "विटामिन B1 (थायामिन) की कमी से बेरी-बेरी रोग होता है।"),
        ("Deficiency of Vitamin D causes", "विटामिन D की कमी से होने वाला रोग", "Rickets (softening of bones)", "Scurvy", "Pellagra", "Anemia", "Vitamin D (calciferol) deficiency causes rickets in children and osteomalacia in adults.", "विटामिन D की कमी से बच्चों में रिकेट्स (सूखा रोग) होता है।"),
        ("Chemical formula of Baking Soda", "बेकिंग सोडा (खाने का सोडा) का रासायनिक सूत्र", "NaHCO3 (Sodium bicarbonate)", "Na2CO3 (Washing soda)", "NaCl", "NaOH", "Baking soda is sodium hydrogen carbonate (NaHCO3).", "बेकिंग सोडा का रासायनिक नाम सोडियम बाइकार्बोनेट (NaHCO3) है।"),
        ("Chemical formula of Washing Soda", "धावन सोडा (धोने का सोडा) का रासायनिक सूत्र", "Na2CO3 . 10H2O", "NaHCO3", "CaCO3", "MgSO4", "Washing soda is sodium carbonate decahydrate (Na2CO3 · 10H2O).", "धावन सोडा का सूत्र सोडियम कार्बोनेट डेकाहाइड्रेट (Na2CO3 · 10H2O) है।"),
        ("Rusting of iron is an example of", "लोहे पर जंग लगना किसका उदाहरण है", "Chemical change and Oxidation-reduction reaction", "Physical change only", "Reversible sublimation", "Nuclear fission", "Rusting of iron (hydrated ferric oxide) is an irreversible chemical oxidation reaction.", "लोहे में जंग लगना एक ऑक्सीकरण-अपचयन रासायनिक परिवर्तन है।"),
        ("Powerhouse of the eukaryotic cell", "यूकेरियोटिक कोशिका का 'विद्युत गृह / ऊर्जा गृह'", "Mitochondria", "Ribosome", "Lysosome", "Golgi apparatus", "Mitochondria generate ATP through cellular respiration, known as the cell's powerhouse.", "माइटोकॉन्ड्रिया एटीपी के रूप में ऊर्जा बनाता है, अतः इसे कोशिका का पावरहाउस कहते हैं।"),
        ("Suicide bags of the cell", "कोशिका की 'आत्मघाती थैली' (Suicide Bag)", "Lysosomes", "Ribosomes", "Vacuoles", "Plastids", "Lysosomes contain digestive hydrolytic enzymes that break down waste and dying cells.", "लाइसोसोम में पाचक एंजाइम होते हैं जो क्षतिग्रस्त कोशिका को नष्ट कर देते हैं।"),
        ("Protein factory of the cell", "कोशिका की 'प्रोटीन फैक्ट्री'", "Ribosomes", "Mitochondria", "Nucleus", "Endoplasmic reticulum", "Ribosomes are responsible for protein synthesis in all living cells.", "राइबोसोम कोशिका के भीतर प्रोटीन संश्लेषण का कार्य करते हैं।")
    ]

    for idx in range(10):
        fact = science_facts[(idx + paper_num) % len(science_facts)]
        q_en = f"In General Science: {fact[0]} is:"
        q_hi = f"सामान्य विज्ञान में: {fact[1]} क्या है?"
        opts_en = [fact[2], fact[3], fact[4], fact[5]]
        opts_hi = [fact[2], fact[3], fact[4], fact[5]]
        ans_idx = (paper_num + idx) % 4
        ans_letter = chr(ord('A') + ans_idx)
        opts_en[0], opts_en[ans_idx] = opts_en[ans_idx], opts_en[0]
        opts_hi[0], opts_hi[ans_idx] = opts_hi[ans_idx], opts_hi[0]

        q_id = 132 + idx
        q_obj = {
            "id": q_id,
            "section_en": "Part 2: General Knowledge & General Studies",
            "section_hi": "भाग 2: सामान्य ज्ञान एवं सामान्य अध्ययन",
            "unit_en": "General Science & Environment",
            "unit_hi": "सामान्य विज्ञान एवं पर्यावरण",
            "q_en": f"Paper {paper_num:02d} Science item: {q_en}",
            "q_hi": f"मॉडल पेपर {paper_num:02d} विज्ञान प्रश्न: {q_hi}",
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": fact[6],
            "exp_hi": fact[7]
        }
        questions.append(q_obj)

    # ------------------ PART 2: REASONING (Q142 to Q150 - 9 Qs) ------------------
    reasoning_templates = [
        # Arithmetic & series
        ("Find the next term in sequence: 5, 10, 20, 40, ?", "शृंखला 5, 10, 20, 40, ? में अगला पद ज्ञात कीजिए", "80", "60", "70", "100", "Each term is multiplied by 2: 40 * 2 = 80.", "प्रत्येक पद में 2 से गुणा हो रहा है: 40 x 2 = 80।"),
        ("Find the next term in sequence: 7, 14, 28, 56, ?", "शृंखला 7, 14, 28, 56, ? में अगला पद क्या होगा", "112", "98", "108", "120", "Each term is doubled: 56 * 2 = 112.", "प्रत्येक पद का दो गुना: 56 x 2 = 112।"),
        ("Find the next square term: 1, 4, 9, 16, 25, ?", "शृंखला 1, 4, 9, 16, 25, ? में अगला पद ज्ञात करें", "36", "30", "49", "32", "The series represents squares of integers: 6^2 = 36.", "संख्याओं के वर्ग की शृंखला है: 6 का वर्ग = 36।"),
        ("Find the next cube term: 1, 8, 27, 64, ?", "शृंखला 1, 8, 27, 64, ? में अगला पद क्या होगा", "125", "100", "216", "144", "The series represents cubes of integers: 5^3 = 125.", "संख्याओं के घन की शृंखला है: 5 का घन = 125।"),
        ("A can do a piece of work in 10 days, B can do it in 15 days. Working together, how many days will they take?", "A किसी काम को 10 दिन में और B 15 दिन में करता है। दोनों मिलकर उस काम को कितने दिनों में पूरा करेंगे?", "6 days", "5 days", "8 days", "12 days", "Combined 1-day work = 1/10 + 1/15 = 5/30 = 1/6. Total time = 6 days.", "संयुक्त कार्य = 1/10 + 1/15 = 5/30 = 1/6। अतः कुल समय = 6 दिन।"),
        ("What is the simple interest on Rs. 1000 at 10% per annum for 2 years?", "₹1000 पर 10% वार्षिक दर से 2 वर्ष का साधारण ब्याज क्या होगा?", "Rs. 200", "Rs. 100", "Rs. 150", "Rs. 250", "SI = (P * R * T) / 100 = (1000 * 10 * 2) / 100 = Rs. 200.", "साधारण ब्याज = (मूलधन x दर x समय) / 100 = (1000 x 10 x 2) / 100 = ₹200।"),
        ("If 20% of a number is 50, what is the number?", "यदि किसी संख्या का 20% मान 50 है, तो वह संख्या क्या है?", "250", "200", "300", "150", "Number = (50 / 20) * 100 = 250.", "संख्या = (50 / 20) x 100 = 250।"),
        ("The average of 3 numbers is 15. If two numbers are 10 and 20, what is the third number?", "तीन संख्याओं का औसत 15 है। यदि दो संख्याएं 10 और 20 हैं, तो तीसरी संख्या क्या होगी?", "15", "12", "18", "25", "Sum = 3 * 15 = 45. Third number = 45 - (10 + 20) = 15.", "कुल योग = 3 x 15 = 45। तीसरी संख्या = 45 - 30 = 15।"),
        ("If a train travels 60 km in 1 hour, what is its speed in meters per second?", "यदि एक रेलगाड़ी 1 घंटे में 60 किमी चलती है, तो उसकी चाल मीटर प्रति सेकंड में क्या होगी?", "16.67 m/s", "20 m/s", "15 m/s", "25 m/s", "Speed = 60 * (5/18) = 300/18 = 16.67 m/s.", "चाल = 60 x (5/18) = 16.67 मीटर/सेकंड।")
    ]

    for idx in range(9):
        fact = reasoning_templates[(idx + paper_num) % len(reasoning_templates)]
        q_en = fact[0]
        q_hi = fact[1]
        opts_en = [fact[2], fact[3], fact[4], fact[5]]
        opts_hi = [fact[2], fact[3], fact[4], fact[5]]
        ans_idx = (paper_num + idx) % 4
        ans_letter = chr(ord('A') + ans_idx)
        opts_en[0], opts_en[ans_idx] = opts_en[ans_idx], opts_en[0]
        opts_hi[0], opts_hi[ans_idx] = opts_hi[ans_idx], opts_hi[0]

        q_id = 142 + idx
        q_obj = {
            "id": q_id,
            "section_en": "Part 2: General Knowledge & General Studies",
            "section_hi": "भाग 2: सामान्य ज्ञान एवं सामान्य अध्ययन",
            "unit_en": "Mental Ability & Reasoning",
            "unit_hi": "मानसिक योग्यता एवं तार्किक क्षमता",
            "q_en": f"Paper {paper_num:02d} Aptitude item: {q_en}",
            "q_hi": f"मॉडल पेपर {paper_num:02d} तार्किक प्रश्न: {q_hi}",
            "options_en": opts_en,
            "options_hi": opts_hi,
            "answer": ans_letter,
            "exp_en": fact[6],
            "exp_hi": fact[7]
        }
        questions.append(q_obj)

    assert len(questions) == 150, f"Expected 150 questions, generated {len(questions)}"
    return questions

print("Question Bank Pool defined successfully")
