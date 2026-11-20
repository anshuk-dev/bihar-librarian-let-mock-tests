# -*- coding: utf-8 -*-
"""
Bilingual Question Dataset for Bihar Librarian LET Mock Paper 02 (Units 1 to 3)
Contains 60 brand-new, authentic previous-year style MCQs in both English and Hindi.
Units covered:
- Unit 1: Foundations of LIS (Q1 to Q20)
- Unit 2: Knowledge Organization, Classification & Cataloguing (Q21 to Q40)
- Unit 3: Library Management & Operations (Q41 to Q60)
"""

PAPER02_U1_U3_QUESTIONS = [
    # =========================================================================
    # UNIT 1: FOUNDATIONS OF LIBRARY AND INFORMATION SCIENCE (Q1 to Q20)
    # =========================================================================
    {
        "id": 1,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "Who is credited with pioneering the modern public library movement in India by establishing a state-wide network of free public libraries in the princely state of Baroda in 1910?",
        "q_hi": "वर्ष 1910 में बड़ौदा रियासत में निःशुल्क सार्वजनिक पुस्तकालयों का राज्यव्यापी नेटवर्क स्थापित कर भारत में आधुनिक सार्वजनिक पुस्तकालय आंदोलन का सूत्रपात करने का श्रेय किसे दिया जाता है?",
        "options_en": [
            "Maharaja Sayajirao Gaekwad III",
            "Maharaja Fatehsinghrao Gaekwad",
            "Sir Asutosh Mukherjee",
            "Nizam Mir Osman Ali Khan"
        ],
        "options_hi": [
            "महाराजा सयाजीराव गायकवाड़ तृतीय",
            "महाराजा फतेहसिंहराव गायकवाड़",
            "सर आशुतोष मुखर्जी",
            "निज़ाम मीर उस्मान अली खान"
        ],
        "answer": "A",
        "exp_en": "Maharaja Sayajirao Gaekwad III of Baroda pioneered the public library movement in India in 1910 by introducing a free compulsory primary education scheme complemented by a comprehensive state-wide network of free public libraries.",
        "exp_hi": "बड़ौदा के महाराजा सयाजीराव गायकवाड़ तृतीय ने 1910 में अनिवार्य प्राथमिक शिक्षा के साथ-साथ राज्यव्यापी निःशुल्क सार्वजनिक पुस्तकालय नेटवर्क की शुरुआत कर भारत में आधुनिक पुस्तकालय आंदोलन की मजबूत नींव रखी थी।"
    },
    {
        "id": 2,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "Whom did Maharaja Sayajirao Gaekwad III invite from the United States in 1910 to plan, organize, and direct the library system in the state of Baroda?",
        "q_hi": "1910 में बड़ौदा राज्य में पुस्तकालय प्रणाली की योजना, संगठन और निर्देशन के लिए महाराजा सयाजीराव गायकवाड़ तृतीय ने संयुक्त राज्य अमेरिका से किसे आमंत्रित किया था?",
        "options_en": [
            "Melvil Dewey",
            "William Alanson Borden",
            "Charles Ammi Cutter",
            "Asa Don Dickinson"
        ],
        "options_hi": [
            "मेलविल डेवी",
            "विलियम एलेनसन बोर्डन",
            "चार्ल्स एमी कटर",
            "असा डॉन डिकिन्सन"
        ],
        "answer": "B",
        "exp_en": "William Alanson Borden, an American librarian and pupil of Melvil Dewey, was invited and appointed as the Director of the State Library Department in Baroda in 1910 to design a state-wide public library network.",
        "exp_hi": "मेलविल डेवी के शिष्य और अमेरिकी पुस्तकालयाध्यक्ष विलियम एलेनसन बोर्डन (W.A. Borden) को 1910 में बड़ौदा के राज्य पुस्तकालय विभाग का निदेशक नियुक्त किया गया था।"
    },
    {
        "id": 3,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "In which year was the first formal library training class in India initiated by William Alanson Borden in the princely state of Baroda?",
        "q_hi": "भारत में पहली औपचारिक पुस्तकालय प्रशिक्षण कक्षा किस वर्ष विलियम एलेनसन बोर्डन द्वारा बड़ौदा रियासत में शुरू की गई थी?",
        "options_en": [
            "1908",
            "1910",
            "1911",
            "1915"
        ],
        "options_hi": [
            "1908",
            "1910",
            "1911",
            "1915"
        ],
        "answer": "C",
        "exp_en": "The first formal training class for librarians in India was initiated by W.A. Borden in Baroda in 1911 to train personnel to manage the newly established public libraries across the state.",
        "exp_hi": "भारत में पुस्तकालयाध्यक्षों के लिए पहली औपचारिक प्रशिक्षण कक्षा 1911 में डब्लू. ए. बोर्डन द्वारा बड़ौदा में शुरू की गई थी ताकि राज्य भर के पुस्तकालयों के कुशल संचालन हेतु पेशेवर तैयार किए जा सकें।"
    },
    {
        "id": 4,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "Which was the first library journal published in India, launched in 1912 under the patronage of the Baroda State Library Department?",
        "q_hi": "भारत में प्रकाशित होने वाली पहली पुस्तकालय पत्रिका कौन-सी थी, जिसे 1912 में बड़ौदा राज्य पुस्तकालय विभाग के संरक्षण में शुरू किया गया था?",
        "options_en": [
            "Indian Library Journal",
            "Library Miscellany",
            "Granthagar Bandhu",
            "Modern Librarian"
        ],
        "options_hi": [
            "इंडियन लाइब्रेरी जर्नल",
            "लाइब्रेरी मिसेलनी (Library Miscellany)",
            "ग्रंथागार बंधु",
            "मॉडर्न लाइब्रेरियन"
        ],
        "answer": "B",
        "exp_en": "'Library Miscellany' was the first library periodical published in India, launched in August 1912 from Baroda in three languages: English, Gujarati, and Marathi.",
        "exp_hi": "'लाइब्रेरी मिसेलनी' (Library Miscellany) भारत की पहली पुस्तकालय विज्ञान पत्रिका थी, जो अगस्त 1912 में बड़ौदा से तीन भाषाओं (अंग्रेजी, गुजराती और मराठी) में प्रकाशित की गई थी।"
    },
    {
        "id": 5,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "Under whose initiative was the Imperial Library Act passed in 1902, amalgamating the Calcutta Public Library with the Imperial Library?",
        "q_hi": "1902 में कलकत्ता पब्लिक लाइब्रेरी को इम्पीरियल लाइब्रेरी में समाहित करने वाला 'इम्पीरियल लाइब्रेरी अधिनियम' किसकी पहल पर पारित किया गया था?",
        "options_en": [
            "Lord Ripon",
            "Lord Curzon",
            "Lord Dalhousie",
            "Lord Minto"
        ],
        "options_hi": [
            "लॉर्ड रिपन",
            "लॉर्ड कर्जन",
            "लॉर्ड डलहौजी",
            "लॉर्ड मिंटो"
        ],
        "answer": "B",
        "exp_en": "Lord Curzon, the then Viceroy of India, took the initiative to amalgamate the Calcutta Public Library (founded 1836) with the Imperial Library (formed 1891) through the Imperial Library Act of 1902, which opened to the public on 30 January 1903 at Metcalfe Hall.",
        "exp_hi": "भारत के तत्कालीन वायसराय लॉर्ड कर्जन की पहल पर 1902 में इम्पीरियल लाइब्रेरी अधिनियम पारित कर कलकत्ता पब्लिक लाइब्रेरी (1836) और इम्पीरियल लाइब्रेरी (1891) का विलय किया गया, जिसे 30 जनवरी 1903 को मेटकाफ हॉल में आम जनता के लिए खोला गया।"
    },
    {
        "id": 6,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "Who was appointed as the first Librarian of the Imperial Library of India in Calcutta in 1901?",
        "q_hi": "1901 में कलकत्ता में इम्पीरियल लाइब्रेरी ऑफ इंडिया के पहले पुस्तकालयाध्यक्ष के रूप में किसे नियुक्त किया गया था?",
        "options_en": [
            "Harinath De",
            "John Macfarlane",
            "J.A. Chapman",
            "B.S. Kesavan"
        ],
        "options_hi": [
            "हरिनाथ डे",
            "जॉन मैकफर्लेन",
            "जे. ए. चैपमैन",
            "बी. एस. केशवन"
        ],
        "answer": "B",
        "exp_en": "John Macfarlane, an Assistant Librarian from the British Museum in London, was appointed as the first Librarian of the Imperial Library in Calcutta in 1901.",
        "exp_hi": "ब्रिटिश म्यूजियम, लंदन के सहायक पुस्तकालयाध्यक्ष जॉन मैकफर्लेन (John Macfarlane) को 1901 में कलकत्ता में इम्पीरियल लाइब्रेरी का प्रथम पुस्तकालयाध्यक्ष नियुक्त किया गया था।"
    },
    {
        "id": 7,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "On which date was the National Library of India formally opened to the general public at the Belvedere Estate, Kolkata, by Union Education Minister Maulana Abul Kalam Azad?",
        "q_hi": "केंद्रीय शिक्षा मंत्री मौलाना अबुल कलाम आजाद द्वारा बेलवेडियर एस्टेट, कोलकाता में भारतीय राष्ट्रीय पुस्तकालय को औपचारिक रूप से आम जनता के लिए किस तिथि को खोला गया था?",
        "options_en": [
            "15 August 1947",
            "26 January 1950",
            "1 February 1953",
            "14 November 1954"
        ],
        "options_hi": [
            "15 अगस्त 1947",
            "26 जनवरी 1950",
            "1 फरवरी 1953",
            "14 नवंबर 1954"
        ],
        "answer": "C",
        "exp_en": "On 1 February 1953, the National Library of India at Belvedere House, Alipore, Kolkata, was formally opened to the nation by Maulana Abul Kalam Azad, having been declared an institution of national importance under the Imperial Library (Change of Name) Act 1948.",
        "exp_hi": "1 फरवरी 1953 को केंद्रीय शिक्षा मंत्री मौलाना अबुल कलाम आजाद द्वारा बेलवेडियर हाउस, अलीपुर, कोलकाता में राष्ट्रीय पुस्तकालय का औपचारिक उद्घाटन कर इसे राष्ट्र को समर्पित किया गया था।"
    },
    {
        "id": 8,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "Who was appointed as the first Librarian of the National Library of independent India and is celebrated as the 'Father of the Indian National Bibliography (INB)'?",
        "q_hi": "स्वतंत्र भारत के राष्ट्रीय पुस्तकालय के पहले पुस्तकालयाध्यक्ष के रूप में किसे नियुक्त किया गया था, जिन्हें 'भारतीय राष्ट्रीय ग्रंथसूची (INB) का जनक' भी माना जाता है?",
        "options_en": [
            "Dr. S.R. Ranganathan",
            "B.S. Kesavan",
            "Khan Bahadur K.M. Asadullah",
            "D.N. Marshall"
        ],
        "options_hi": [
            "डॉ. एस. आर. रंगनाथन",
            "बी. एस. केशवन",
            "खान बहादुर के. एम. असदुल्लाह",
            "डी. एन. मार्शल"
        ],
        "answer": "B",
        "exp_en": "Bellary Shamanna Kesavan (B.S. Kesavan) was appointed as the first Librarian of the National Library of independent India in 1948 and served as the first General Editor of the Indian National Bibliography (INB).",
        "exp_hi": "बेल्लारी शमन्ना केशवन (बी. एस. केशवन) स्वतंत्र भारत के राष्ट्रीय पुस्तकालय के प्रथम लाइब्रेरियन बने तथा उन्हें 'भारतीय राष्ट्रीय ग्रंथसूची (INB)' के प्रथम प्रधान संपादक के रूप में इसका जनक कहा जाता है।"
    },
    {
        "id": 9,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "The 'Advisory Committee for Libraries' was appointed by the Ministry of Education, Government of India, in 1957 under the chairmanship of:",
        "q_hi": "भारत सरकार के शिक्षा मंत्रालय द्वारा 1957 में 'पुस्तकालय सलाहकार समिति' किसकी अध्यक्षता में गठित की गई थी?",
        "options_en": [
            "Dr. S.R. Ranganathan",
            "K.P. Sinha",
            "Dr. D.S. Kothari",
            "Prof. S. Radhakrishnan"
        ],
        "options_hi": [
            "डॉ. एस. आर. रंगनाथन",
            "के. पी. सिन्हा",
            "डॉ. डी. एस. कोठारी",
            "प्रो. एस. राधाकृष्णन"
        ],
        "answer": "B",
        "exp_en": "The Advisory Committee for Libraries was constituted in 1957 by the Government of India under the chairmanship of K.P. Sinha (Director of Public Instruction, Bihar). It submitted its comprehensive report in 1959.",
        "exp_hi": "भारत सरकार के शिक्षा मंत्रालय द्वारा 1957 में के. पी. सिन्हा (बिहार के तत्कालीन जन शिक्षा निदेशक) की अध्यक्षता में पुस्तकालय सलाहकार समिति (सिन्हा समिति) का गठन किया गया था, जिसने 1959 में रिपोर्ट सौंपी।"
    },
    {
        "id": 10,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "What specific library cess rate was recommended by the K.P. Sinha Committee (Advisory Committee for Libraries 1957-1959) on house and property tax?",
        "q_hi": "के. पी. सिन्हा समिति (पुस्तकालय सलाहकार समिति 1957-1959) ने गृह एवं संपत्ति कर पर कितने पुस्तकालय उपकर (Cess) लगाने की सिफारिश की थी?",
        "options_en": [
            "2 paise per rupee",
            "6 paise per rupee",
            "10 paise per rupee",
            "15 paise per rupee"
        ],
        "options_hi": [
            "2 पैसे प्रति रुपया",
            "6 पैसे प्रति रुपया",
            "10 पैसे प्रति रुपया",
            "15 पैसे प्रति रुपया"
        ],
        "answer": "B",
        "exp_en": "The K.P. Sinha Committee recommended that state governments should levy a library cess at the rate of 6 paise per rupee of property/house tax in all civic and panchayat areas to finance public library networks.",
        "exp_hi": "सिन्हा समिति ने सिफारिश की थी कि राज्य सरकारों को सार्वजनिक पुस्तकालयों के वित्तपोषण हेतु सभी नगरपालिकाओं और पंचायत क्षेत्रों में गृह/संपत्ति कर पर 6 पैसे प्रति रुपये की दर से पुस्तकालय उपकर लगाना चाहिए।"
    },
    {
        "id": 11,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "In 1985, the Government of India constituted the 'Committee on National Policy on Library and Information Systems' (CONLIS) under the chairmanship of:",
        "q_hi": "1985 में भारत सरकार ने 'राष्ट्रीय पुस्तकालय एवं सूचना प्रणाली नीति समिति' (CONLIS) का गठन किसकी अध्यक्षता में किया था?",
        "options_en": [
            "Prof. D.P. Chattopadhyaya",
            "Prof. Yash Pal",
            "Dr. V.A. Kamath",
            "Prof. P.N. Kaula"
        ],
        "options_hi": [
            "प्रो. डी. पी. चट्टोपाध्याय",
            "प्रो. यश पाल",
            "डॉ. वी. ए. कामथ",
            "प्रो. पी. एन. कौला"
        ],
        "answer": "A",
        "exp_en": "The Department of Culture, Ministry of Human Resource Development, appointed the Committee on National Policy on Library and Information Systems (CONLIS) in October 1985 under the chairmanship of Prof. D.P. Chattopadhyaya; it submitted its report in May 1986.",
        "exp_hi": "मानव संसाधन विकास मंत्रालय के संस्कृति विभाग ने अक्टूबर 1985 में प्रो. डी. पी. चट्टोपाध्याय की अध्यक्षता में CONLIS समिति गठित की, जिसने मई 1986 में अपनी रिपोर्ट केंद्र सरकार को प्रस्तुत की।"
    },
    {
        "id": 12,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "The Chattopadhyaya Committee (CONLIS, 1986) recommended that what percentage of the total education budget of the Central and State Governments should be allocated to library development?",
        "q_hi": "चट्टोपाध्याय समिति (CONLIS, 1986) ने केंद्र और राज्य सरकारों के कुल शिक्षा बजट का कितना प्रतिशत पुस्तकालय विकास के लिए आवंटित करने की सिफारिश की थी?",
        "options_en": [
            "1% to 2%",
            "6% to 10%",
            "15% to 20%",
            "25%"
        ],
        "options_hi": [
            "1% से 2%",
            "6% से 10%",
            "15% से 20%",
            "25%"
        ],
        "answer": "B",
        "exp_en": "The Chattopadhyaya Committee explicitly recommended that 6% to 10% of the total education budget of the Central and State Governments should be devoted to the development and maintenance of libraries.",
        "exp_hi": "चट्टोपाध्याय समिति ने स्पष्ट सिफारिश की थी कि केंद्र और राज्य सरकारों के कुल शिक्षा बजट का 6% से 10% हिस्सा पुस्तकालयों के विकास और रखरखाव के लिए निर्धारित किया जाना चाहिए।"
    },
    {
        "id": 13,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "In which year was the National Knowledge Commission (NKC) constituted under the chairmanship of Sam Pitroda to advise the Prime Minister on knowledge-related institutions including libraries?",
        "q_hi": "सैम पित्रोदा की अध्यक्षता में राष्ट्रीय ज्ञान आयोग (NKC) का गठन किस वर्ष किया गया था ताकि पुस्तकालयों सहित ज्ञान संस्थानों के आधुनिकीकरण हेतु प्रधानमंत्री को सलाह दी जा सके?",
        "options_en": [
            "2002",
            "2005",
            "2008",
            "2011"
        ],
        "options_hi": [
            "2002",
            "2005",
            "2008",
            "2011"
        ],
        "answer": "B",
        "exp_en": "The National Knowledge Commission (NKC) was constituted on 13 June 2005 by Prime Minister Dr. Manmohan Singh, chaired by Sam Pitroda, which functioned through 2009 and produced landmark recommendations on libraries.",
        "exp_hi": "राष्ट्रीय ज्ञान आयोग (NKC) का गठन 13 जून 2005 को प्रधानमंत्री डॉ. मनमोहन सिंह द्वारा सैम पित्रोदा की अध्यक्षता में किया गया था, जिसने पुस्तकालयों के आधुनिकीकरण पर ऐतिहासिक सिफारिशें दीं।"
    },
    {
        "id": 14,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "Who served as the Chairperson of the dedicated 'Working Group on Libraries' constituted by the National Knowledge Commission (NKC) in 2006?",
        "q_hi": "राष्ट्रीय ज्ञान आयोग (NKC) द्वारा 2006 में गठित समर्पित 'पुस्तकालय कार्य समूह' की अध्यक्षा के रूप में किसने कार्य किया था?",
        "options_en": [
            "Kalpana Dasgupta",
            "Dr. S.R. Ranganathan",
            "B.S. Kesavan",
            "Subbiah Arunachalam"
        ],
        "options_hi": [
            "कल्पना दासगुप्ता",
            "डॉ. एस. आर. रंगनाथन",
            "बी. एस. केशवन",
            "सुब्बैया अरुणाचलम"
        ],
        "answer": "A",
        "exp_en": "The NKC Working Group on Libraries was headed by Mrs. Kalpana Dasgupta (former Director of Central Secretariat Library and former President of ILA), whose recommendations led to the creation of the National Mission on Libraries (NML).",
        "exp_hi": "राष्ट्रीय ज्ञान आयोग के पुस्तकालय कार्य समूह की अध्यक्षा श्रीमती कल्पना दासगुप्ता (केंद्रीय सचिवालय पुस्तकालय की पूर्व निदेशक) थीं, जिनकी सिफारिशों के परिणामस्वरूप राष्ट्रीय पुस्तकालय मिशन (NML) का गठन हुआ।"
    },
    {
        "id": 15,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "When and by whom was the Special Libraries Association (SLA) founded in the United States?",
        "q_hi": "संयुक्त राज्य अमेरिका में स्पेशल लाइब्रेरीज एसोसिएशन (SLA) की स्थापना कब और किसके द्वारा की गई थी?",
        "options_en": [
            "1876 by Melvil Dewey",
            "1909 by John Cotton Dana",
            "1924 by A.S. Nitin",
            "1933 by S.R. Ranganathan"
        ],
        "options_hi": [
            "1876 में मेलविल डेवी द्वारा",
            "1909 में जॉन कॉटन डाना द्वारा",
            "1924 में ए. एस. नितिन द्वारा",
            "1933 में एस. आर. रंगनाथन द्वारा"
        ],
        "answer": "B",
        "exp_en": "The Special Libraries Association (SLA) was founded in 1909 at Bretton Woods, New Hampshire, by John Cotton Dana, who also served as its first president with the motto 'Putting Knowledge to Work'.",
        "exp_hi": "स्पेशल लाइब्रेरीज एसोसिएशन (SLA) की स्थापना 1909 में न्यू हैम्पशायर में जॉन कॉटन डाना (John Cotton Dana) द्वारा की गई थी। इसका आदर्श वाक्य 'पुटिंग नॉलेज टू वर्क' (Putting Knowledge to Work) है।"
    },
    {
        "id": 16,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "The Chartered Institute of Library and Information Professionals (CILIP) in the United Kingdom was formed in 2002 by the unification of which two historic bodies?",
        "q_hi": "यूनाइटेड किंगडम में चार्टर्ड इंस्टीट्यूट ऑफ लाइब्रेरी एंड इंफॉर्मेशन प्रोफेशनल्स (CILIP) का गठन 2002 में किन दो ऐतिहासिक संस्थाओं के विलय से हुआ था?",
        "options_en": [
            "Library Association (LA) and Aslib",
            "Library Association (LA) and Institute of Information Scientists (IIS)",
            "Aslib and SCONUL",
            "British Library Association and FID"
        ],
        "options_hi": [
            "लाइब्रेरी एसोसिएशन (LA) और एस्लिब (Aslib)",
            "लाइब्रेरी एसोसिएशन (LA) और इंस्टीट्यूट ऑफ इंफॉर्मेशन साइंटिस्ट्स (IIS)",
            "एस्लिब (Aslib) और स्कोनुल (SCONUL)",
            "ब्रिटिश लाइब्रेरी एसोसिएशन और एफआईडी (FID)"
        ],
        "answer": "B",
        "exp_en": "CILIP was formed in April 2002 in the UK through the merger of the Library Association (LA, founded in 1877) and the Institute of Information Scientists (IIS, founded in 1958).",
        "exp_hi": "CILIP का गठन अप्रैल 2002 में यूनाइटेड किंगडम के 'लाइब्रेरी एसोसिएशन' (LA, 1877) और 'इंस्टीट्यूट ऑफ इंफॉर्मेशन साइंटिस्ट्स' (IIS, 1958) के ऐतिहासिक विलय द्वारा हुआ था।"
    },
    {
        "id": 17,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "The International Federation for Information and Documentation (FID), originally founded in 1895 as the Institut International de Bibliographie (IIB) by Paul Otlet and Henri La Fontaine, was officially dissolved in which year?",
        "q_hi": "1895 में पॉल ऑटलेट और हेनरी ला फॉन्टेन द्वारा 'इंस्टीट्यूट इंटरनेशनल डी बिब्लियोग्राफी' (IIB) के रूप में स्थापित इंटरनेशनल फेडरेशन फॉर इंफॉर्मेशन एंड डॉक्यूमेंटेशन (FID) आधिकारिक रूप से किस वर्ष भंग कर दिया गया था?",
        "options_en": [
            "1991",
            "1998",
            "2002",
            "2006"
        ],
        "options_hi": [
            "1991",
            "1998",
            "2002",
            "2006"
        ],
        "answer": "C",
        "exp_en": "FID (headquartered in The Hague) was officially dissolved in 2002 after 107 years of historic bibliographic service due to insurmountable financial constraints.",
        "exp_hi": "हेग (नीदरलैंड) में स्थित FID को गंभीर वित्तीय संकट के कारण 107 वर्षों की ऐतिहासिक सेवाओं के पश्चात आधिकारिक रूप से वर्ष 2002 में भंग कर दिया गया था।"
    },
    {
        "id": 18,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "Which landmark international meeting held in December 2001 (released in February 2002) officially defined and launched the worldwide movement for 'Open Access' to peer-reviewed research literature?",
        "q_hi": "दिसंबर 2001 में आयोजित (फरवरी 2002 में जारी) किस ऐतिहासिक अंतरराष्ट्रीय सम्मेलन ने सहकर्मी-समीक्षित शोध साहित्य के लिए 'मुक्त अभिगम' (Open Access) आंदोलन को आधिकारिक रूप से परिभाषित और शुरू किया?",
        "options_en": [
            "Paris Declaration",
            "Budapest Open Access Initiative (BOAI)",
            "Helsinki Guidelines",
            "Geneva Convention"
        ],
        "options_hi": [
            "पेरिस घोषणा",
            "बुडापेस्ट ओपन एक्सेस इनिशिएटिव (BOAI)",
            "हेलसिंकी दिशानिर्देश",
            "जिनेवा कन्वेंशन"
        ],
        "answer": "B",
        "exp_en": "The Budapest Open Access Initiative (BOAI) was convened by the Open Society Institute (OSI) in December 2001 and released on 14 February 2002, formally defining the term 'Open Access' and recommending dual strategies: self-archiving and open access journals.",
        "exp_hi": "ओपन सोसाइटी इंस्टीट्यूट द्वारा आयोजित 'बुडापेस्ट ओपन एक्सेस इनिशिएटिव' (BOAI) फरवरी 2002 में जारी किया गया था, जिसने शोध साहित्य के लिए 'मुक्त अभिगम' (Open Access) शब्द और इसके दो प्रमुख मार्गों को औपचारिक रूप से परिभाषित किया।"
    },
    {
        "id": 19,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "In Open Access terminology, author self-archiving of pre-print or post-print articles in an institutional or subject repository is universally known as:",
        "q_hi": "मुक्त अभिगम (Open Access) शब्दावली में, लेखकों द्वारा संस्थागत या विषयगत रिपॉजिटरी में प्री-प्रिंट या पोस्ट-प्रिंट लेखों के स्व-अभिलेखागार (Self-archiving) को किस रूप में जाना जाता है?",
        "options_en": [
            "Gold Open Access",
            "Green Open Access",
            "Diamond Open Access",
            "Bronze Open Access"
        ],
        "options_hi": [
            "गोल्ड ओपन एक्सेस",
            "ग्रीन ओपन एक्सेस",
            "डायमंड ओपन एक्सेस",
            "ब्रॉन्ज ओपन एक्सेस"
        ],
        "answer": "B",
        "exp_en": "'Green Open Access' refers to author self-archiving where manuscripts (pre-prints/post-prints) are deposited into an institutional repository or open archive. 'Gold Open Access' refers to publishing directly in peer-reviewed open access journals.",
        "exp_hi": "'ग्रीन ओपन एक्सेस' (Green OA) का तात्पर्य लेखक द्वारा अपने शोधपत्रों को किसी संस्थागत या विषयगत डिजिटल रिपॉजिटरी में स्वयं आर्काइव (अपलोड) करने से है, जबकि 'गोल्ड ओपन एक्सेस' में लेख सीधे खुली पत्रिकाओं में प्रकाशित होते हैं।"
    },
    {
        "id": 20,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 1: Foundations of Library and Information Science",
        "unit_hi": "इकाई 1: पुस्तकालय एवं सूचना विज्ञान के आधार",
        "q_en": "Which Creative Commons tool allows creators to waive all copyright and related rights in their work, dedicating it completely to the worldwide public domain?",
        "q_hi": "कौन-सा क्रिएटिव कॉमन्स (Creative Commons) साधन रचनाकारों को अपनी रचना पर सभी कॉपीराइट और संबंधित अधिकारों को त्यागकर उसे पूरी तरह से वैश्विक सार्वजनिक डोमेन (Public Domain) में समर्पित करने की अनुमति देता है?",
        "options_en": [
            "CC BY",
            "CC BY-SA",
            "CC0 (CC Zero)",
            "CC BY-NC-ND"
        ],
        "options_hi": [
            "CC BY",
            "CC BY-SA",
            "CC0 (CC Zero / क्रिएटिव कॉमन्स ज़ीरो)",
            "CC BY-NC-ND"
        ],
        "answer": "C",
        "exp_en": "CC0 (Creative Commons Zero) is a public domain dedication tool that enables copyright holders to opt out of copyright altogether and dedicate their works to the public domain with 'No Rights Reserved'.",
        "exp_hi": "CC0 (क्रिएटिव कॉमन्स ज़ीरो) एक पब्लिक डोमेन साधन है जो कॉपीराइट धारकों को सभी अधिकार त्यागकर अपनी कृति को 'कोई अधिकार सुरक्षित नहीं' के साथ दुनिया भर के सार्वजनिक डोमेन में रखने की अनुमति देता है।"
    },

    # =========================================================================
    # UNIT 2: KNOWLEDGE ORGANIZATION, CLASSIFICATION & CATALOGUING (Q21 to Q40)
    # =========================================================================
    {
        "id": 21,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "In the Dewey Decimal Classification (DDC), which main class number is assigned to 'Language' (Linguistics)?",
        "q_hi": "डेवी दशमलव वर्गीकरण (DDC) में 'भाषा' (Language / भाषाविज्ञान) विषय के लिए कौन-सा मुख्य वर्ग अंक निर्धारित है?",
        "options_en": [
            "300",
            "400",
            "800",
            "900"
        ],
        "options_hi": [
            "300",
            "400",
            "800",
            "900"
        ],
        "answer": "B",
        "exp_en": "In DDC, Main Class 400 is assigned to Language (Linguistics), while Class 800 is assigned to Literature. (300 is Social sciences and 900 is History & geography).",
        "exp_hi": "DDC में मुख्य वर्ग 400 'भाषा' (भाषाविज्ञान) के लिए निर्धारित है, जबकि वर्ग 800 'साहित्य' के लिए निर्धारित है (300 सामाजिक विज्ञान और 900 इतिहास व भूगोल है)।"
    },
    {
        "id": 22,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "Which main class in the Dewey Decimal Classification (DDC) represents 'Technology (Applied Sciences)'?",
        "q_hi": "डेवी दशमलव वर्गीकरण (DDC) में कौन-सा मुख्य वर्ग 'प्रौद्योगिकी (अनुप्रयुक्त विज्ञान)' [Technology / Applied Sciences] का प्रतिनिधित्व करता है?",
        "options_en": [
            "500",
            "600",
            "700",
            "200"
        ],
        "options_hi": [
            "500",
            "600",
            "700",
            "200"
        ],
        "answer": "B",
        "exp_en": "Class 500 represents Natural Sciences and Mathematics, whereas Class 600 is allocated to Technology (Applied Sciences), covering engineering, medicine, agriculture, and manufacturing.",
        "exp_hi": "DDC में वर्ग 500 प्राकृतिक विज्ञान और गणित का प्रतिनिधित्व करता है, जबकि वर्ग 600 प्रौद्योगिकी (अनुप्रयुक्त विज्ञान) जैसे चिकित्सा, इंजीनियरिंग, कृषि आदि के लिए आवंटित है।"
    },
    {
        "id": 23,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "In Table 1 (Standard Subdivisions) of the Dewey Decimal Classification, which notation represents 'Dictionaries, encyclopedias, and concordances'?",
        "q_hi": "डेवी दशमलव वर्गीकरण की तालिका 1 (मानक उप-विभाजन) में 'शब्दकोश, विश्वकोश और अनुक्रमणिका' (Dictionaries, encyclopedias, concordances) के लिए कौन-सा संकेतन प्रयुक्त होता है?",
        "options_en": [
            "-01",
            "-02",
            "-03",
            "-05"
        ],
        "options_hi": [
            "-01",
            "-02",
            "-03",
            "-05"
        ],
        "answer": "C",
        "exp_en": "In DDC Table 1, the notation -03 is designated for 'Dictionaries, encyclopedias, concordances'. (-01 is Philosophy and theory, -02 is Miscellany, and -05 is Serial publications).",
        "exp_hi": "DDC की तालिका 1 में -03 का प्रयोग 'शब्दकोश, विश्वकोश और अनुक्रमणिका' के लिए किया जाता है (-01 दर्शन व सिद्धांत, -02 प्रकीर्ण, और -05 क्रमिक प्रकाशन हैं)।"
    },
    {
        "id": 24,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "In DDC Table 1 (Standard Subdivisions), which notation is designated for 'Serial publications (Periodicals)'?",
        "q_hi": "DDC की तालिका 1 (मानक उप-विभाजन) में 'क्रमिक प्रकाशन (सामयिकी/पत्रिकाएँ)' के लिए कौन-सा संकेतन निर्धारित है?",
        "options_en": [
            "-03",
            "-05",
            "-07",
            "-09"
        ],
        "options_hi": [
            "-03",
            "-05",
            "-07",
            "-09"
        ],
        "answer": "B",
        "exp_en": "In DDC Table 1, -05 is assigned to 'Serial publications' (journals, periodicals, magazines), while -07 is Education/Research and -09 is History/Geography.",
        "exp_hi": "DDC तालिका 1 में संकेतन -05 का उपयोग 'क्रमिक प्रकाशनों' (जर्नल, सामयिकी और पत्रिकाओं) को दर्शाने के लिए किया जाता है।"
    },
    {
        "id": 25,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "The 7th edition of Colon Classification (CC 7) published in 1987 was posthumously revised and edited by which eminent disciple of Dr. S.R. Ranganathan?",
        "q_hi": "1987 में प्रकाशित द्विबिंदु वर्गीकरण (Colon Classification) के 7वें संस्करण (CC 7) का संपादन एवं संशोधन डॉ. एस. आर. रंगनाथन के किस प्रख्यात शिष्य द्वारा किया गया था?",
        "options_en": [
            "P.N. Kaula",
            "M.A. Gopinath",
            "A. Neelameghan",
            "S. Parthasarathy"
        ],
        "options_hi": [
            "पी. एन. कौला",
            "एम. ए. गोपीनाथ (M.A. Gopinath)",
            "ए. नीलमेघन",
            "एस. पार्थसारथी"
        ],
        "answer": "B",
        "exp_en": "Colon Classification 7th edition was published posthumously in 1987, thoroughly edited and revised by Dr. M.A. Gopinath of the Documentation Research and Training Centre (DRTC), Bangalore.",
        "exp_hi": "द्विबिंदु वर्गीकरण का 7वाँ संस्करण 1987 में डॉ. रंगनाथन के देहांत के पश्चात डीआरटीसी (DRTC) बैंगलोर के डॉ. एम. ए. गोपीनाथ द्वारा संपादित और प्रकाशित किया गया था।"
    },
    {
        "id": 26,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "In the 7th edition of Colon Classification (CC 7), the fundamental category 'Matter' [M] was expanded and classified into which three distinct varieties?",
        "q_hi": "द्विबिंदु वर्गीकरण के 7वें संस्करण (CC 7) में मूल श्रेणी 'पदार्थ' (Matter) [M] को किन तीन विशिष्ट किस्मों में विस्तारित और वर्गीकृत किया गया था?",
        "options_en": [
            "Matter-Material, Matter-Property, and Matter-Method",
            "Matter-Energy, Matter-Space, and Matter-Time",
            "Matter-Form, Matter-Substance, and Matter-Quality",
            "Matter-Static, Matter-Dynamic, and Matter-Kinetic"
        ],
        "options_hi": [
            "मैटर-मटेरियल (द्रव्य), मैटर-प्रॉपर्टी (गुणधर्म) और मैटर-मेथड (विधि)",
            "मैटर-एनर्जी, मैटर-स्पेस और मैटर-टाइम",
            "मैटर-फॉर्म, मैटर-सबस्टेंस और मैटर-क्वालिटी",
            "मैटर-स्टैटिक, मैटर-डायनामिक और मैटर-काइनेटिक"
        ],
        "answer": "A",
        "exp_en": "In CC 7, Ranganathan and Gopinath expanded the fundamental category 'Matter' into three manifestations: Matter-Material [MM] (indicator ;), Matter-Property [MP] (indicator ;), and Matter-Method [MMt].",
        "exp_hi": "CC के 7वें संस्करण में 'पदार्थ' (Matter) को तीन किस्मों में विभाजित किया गया: मैटर-मटेरियल [MM] (द्रव्य/सामग्री), मैटर-प्रॉपर्टी [MP] (गुणधर्म/विशेषता) और मैटर-मेथड [MMt] (विधि/कार्यप्रणाली)।"
    },
    {
        "id": 27,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "In the Universal Decimal Classification (UDC), which symbol is used to enclose the 'Common Auxiliaries of Place'?",
        "q_hi": "यूनिवर्सल डेसिमल क्लासिफिकेशन (UDC) में 'स्थान के सामान्य सहायक' (Common Auxiliaries of Place) को दर्शाने के लिए किस प्रतीक का प्रयोग किया जाता है?",
        "options_en": [
            "Parentheses (1/9)",
            "Quotation marks \"...\"",
            "Equals sign =...",
            "Hyphen -..."
        ],
        "options_hi": [
            "कोष्ठक (1/9) [Parentheses]",
            "उद्धरण चिह्न \"...\" [Double Quotes]",
            "बराबर चिह्न =... [Equals Sign]",
            "हाइफ़न -... [Hyphen]"
        ],
        "answer": "A",
        "exp_en": "In UDC, Common Auxiliaries of Place are indicated by round brackets/parentheses enclosing the geographic number (1/9). For example, (540) represents India.",
        "exp_hi": "UDC में स्थान के सामान्य सहायकों को गोल कोष्ठक (1/9) द्वारा दर्शाया जाता है; उदाहरण के लिए, भारत का स्थान संकेतन (540) है।"
    },
    {
        "id": 28,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "In the Universal Decimal Classification (UDC), which punctuation mark serves as the indicator digit for 'Common Auxiliaries of Time'?",
        "q_hi": "यूनिवर्सल डेसिमल क्लासिफिकेशन (UDC) में 'समय के सामान्य सहायक' (Common Auxiliaries of Time) के लिए सूचक अंक के रूप में किस विराम चिह्न का उपयोग किया जाता है?",
        "options_en": [
            "Slash /",
            "Quotation marks \"...\"",
            "Colon :",
            "Plus sign +"
        ],
        "options_hi": [
            "स्लैश /",
            "दोहरे उद्धरण चिह्न \"...\" (Double Quotes)",
            "कोलन :",
            "धन चिह्न +"
        ],
        "answer": "B",
        "exp_en": "In UDC, Common Auxiliaries of Time are enclosed within double quotation marks \"...\". For example, \"19\" denotes the 20th century, and \"1947\" denotes the year 1947.",
        "exp_hi": "UDC में समय (Time) के सामान्य सहायकों को दोहरे उद्धरण चिह्नों \"...\" के अंदर लिखा जाता है, जैसे \"19\" 20वीं शताब्दी को और \"1947\" वर्ष 1947 को दर्शाता है।"
    },
    {
        "id": 29,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "Under AACR-2 (Rule 21.1B2), a corporate body is recognized as the heading/author of a publication under which of the following prescribed categories?",
        "q_hi": "AACR-2 (नियम 21.1B2) के अनुसार, किसी निकाय (कॉर्पोरेट बॉडी) को निम्नलिखित में से किस श्रेणी के प्रकाशनों के लिए मुख्य शीर्षक/लेखक के रूप में मान्यता दी जाती है?",
        "options_en": [
            "Works of an administrative nature dealing with the corporate body itself",
            "Fictional novels written by an individual employee",
            "Commercial advertising brochures for external goods",
            "Any general textbook sponsored by an institution"
        ],
        "options_hi": [
            "स्वयं कॉर्पोरेट निकाय की आंतरिक नीतियों, वित्त या प्रशासन से संबंधित प्रशासनिक प्रकृति की कृतियाँ",
            "किसी व्यक्तिगत कर्मचारी द्वारा लिखे गए काल्पनिक उपन्यास",
            "बाहरी सामानों के व्यावसायिक विज्ञापन ब्रोशर",
            "संस्थान द्वारा प्रायोजित कोई भी सामान्य पाठ्यपुस्तक"
        ],
        "answer": "A",
        "exp_en": "AACR-2 Rule 21.1B2 limits corporate authorship to specific defined categories, the primary one being works of an administrative nature dealing with the corporate body itself, its internal policies, operations, or finances.",
        "exp_hi": "AACR-2 के नियम 21.1B2 के अनुसार किसी निकाय के नाम के अंतर्गत प्रविष्टि तभी की जाती है जब कृति स्वयं उस निकाय की आंतरिक नीतियों, प्रशासन, वित्तीय रिपोर्ट या कार्यवाही से संबंधित प्रशासनिक प्रकृति की हो।"
    },
    {
        "id": 30,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "In AACR-2, what is the primary purpose of assigning a 'Uniform Title' as prescribed in Chapter 25?",
        "q_hi": "AACR-2 में 'समान शीर्षक' (Uniform Title - अध्याय 25) प्रदान करने का प्राथमिक उद्देश्य क्या है?",
        "options_en": [
            "To replace an author's real name with an official pseudonym",
            "To bring together all catalogue entries for the same work when published under varying titles or translations",
            "To assign an automated call number to rare books",
            "To reduce the number of subject access points"
        ],
        "options_hi": [
            "लेखक के वास्तविक नाम को आधिकारिक छद्म नाम से बदलना",
            "विभिन्न शीर्षकों या अनुवादों के तहत प्रकाशित एक ही कृति की सभी सूची प्रविष्टियों को एक साथ लाना",
            "दुर्लभ पुस्तकों को एक स्वचालित कॉल नंबर प्रदान करना",
            "विषय प्रविष्टि बिंदुओं की संख्या को कम करना"
        ],
        "answer": "B",
        "exp_en": "According to Chapter 25 of AACR-2, the purpose of a Uniform Title is to bring together all catalogue entries for the same work when its manifestations have appeared under varying titles (e.g., sacred scriptures like Bible, Mahabharata, or anonymous classics).",
        "exp_hi": "AACR-2 के अध्याय 25 के तहत समान शीर्षक (Uniform Title) का उद्देश्य विभिन्न शीर्षकों, भाषा-संस्करणों या अनुवादों में प्रकाशित एक ही कृति (जैसे रामायण, कुरान, शेक्सपियर के नाटक) की सभी प्रविष्टियों को एक जगह संगठित करना है।"
    },
    {
        "id": 31,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "Which international cataloguing standard was released in 2010 by the Joint Steering Committee as the modern successor to AACR-2?",
        "q_hi": "एंग्लो-अमेरिकन कैटलॉगिंग रूल्स (AACR-2) के आधुनिक उत्तराधिकारी के रूप में 2010 में संयुक्त संचालन समिति द्वारा किस अंतरराष्ट्रीय मानक को जारी किया गया था?",
        "options_en": [
            "ISBD",
            "CCF",
            "RDA (Resource Description and Access)",
            "Dublin Core"
        ],
        "options_hi": [
            "ISBD",
            "CCF",
            "RDA (Resource Description and Access / संसाधन विवरण एवं पहुँच)",
            "डबलिन कोर"
        ],
        "answer": "C",
        "exp_en": "RDA (Resource Description and Access) was released in 2010 by the Joint Steering Committee (JSC) to replace AACR-2, designed to provide a comprehensive, web-compatible cataloguing framework based on FRBR.",
        "exp_hi": "RDA (रिसोर्स डिस्क्रिप्शन एंड एक्सेस) को 2010 में AACR-2 के उत्तराधिकारी के रूप में जारी किया गया था, जो एफआरबीआर (FRBR) वैचारिक मॉडल पर आधारित वेब-अनुकूल अंतरराष्ट्रीय कैटलॉगिंग मानक है।"
    },
    {
        "id": 32,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "Which traditional cataloguing convention of AACR-2 was completely eliminated in RDA in order to record all contributing authors fully?",
        "q_hi": "सभी योगदानकर्ता लेखकों को पूर्ण रूप से दर्ज करने के लिए AACR-2 के किस पारंपरिक नियम को RDA में पूरी तरह समाप्त कर दिया गया?",
        "options_en": [
            "Principle of uniform titles",
            "'Rule of Three' (which restricted entries to the first author followed by 'et al.')",
            "Use of capital letters in titles",
            "Recording of publisher names and dates"
        ],
        "options_hi": [
            "समान शीर्षक का सिद्धांत",
            "'तीन का नियम' (Rule of Three - जिसके तहत तीन से अधिक लेखक होने पर केवल प्रथम लेखक लिखकर 'et al.' लगाया जाता था)",
            "शीर्षकों में बड़े अक्षरों का प्रयोग",
            "प्रकाशक के नाम और तिथियों को दर्ज करना"
        ],
        "answer": "B",
        "exp_en": "RDA discarded AACR-2's restrictive 'Rule of Three', enabling libraries to transcribe all collaborating authors, editors, and creators without using Latin truncations like '[et al.]'.",
        "exp_hi": "RDA ने AACR-2 के संकुचित 'तीन के नियम' (Rule of Three) को पूरी तरह समाप्त कर दिया, जिससे अब बिना '[et al.]' का प्रयोग किए सभी सह-लेखकों और योगदानकर्ताओं के नाम प्रविष्ट किए जा सकते हैं।"
    },
    {
        "id": 33,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "The FRBR (Functional Requirements for Bibliographic Records) model, approved by IFLA in 1998, is structurally built on which conceptual database modeling approach?",
        "q_hi": "1998 में IFLA द्वारा स्वीकृत FRBR (Functional Requirements for Bibliographic Records) मॉडल संरचनात्मक रूप से किस वैचारिक डेटाबेस मॉडलिंग पद्धति पर निर्मित है?",
        "options_en": [
            "Hierarchical Classification Model",
            "Entity-Relationship (E-R) Model",
            "Network Topological Model",
            "Vector Space Retrieval Model"
        ],
        "options_hi": [
            "पदानुक्रमित वर्गीकरण मॉडल",
            "इकाई-संबंध (Entity-Relationship / E-R) मॉडल",
            "नेटवर्क टोपोलॉजिकल मॉडल",
            "वेक्टर स्पेस पुनर्प्राप्ति मॉडल"
        ],
        "answer": "B",
        "exp_en": "FRBR was formulated by an IFLA Study Group using an Entity-Relationship (E-R) model, structuring bibliographic information into entities, relationships, and attributes.",
        "exp_hi": "FRBR मॉडल को IFLA अध्ययन समूह द्वारा एंटिटी-रिलेशनशिप (E-R / इकाई-संबंध) पद्धति पर विकसित किया गया था, जो ग्रंथपरक जगत को इकाइयों, संबंधों और विशेषताओं में संरचित करता है।"
    },
    {
        "id": 34,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "In the FRBR conceptual framework, what are the four 'Group 1' entities that represent products of intellectual or artistic endeavor?",
        "q_hi": "FRBR वैचारिक ढांचे में बौद्धिक या कलात्मक प्रयास के उत्पादों का प्रतिनिधित्व करने वाली चार 'समूह 1' (Group 1) इकाइयाँ कौन-सी हैं?",
        "options_en": [
            "Person, Corporate Body, Family, Concept",
            "Work, Expression, Manifestation, Item (WEMI)",
            "Concept, Object, Event, Place",
            "Title, Author, Subject, Publisher"
        ],
        "options_hi": [
            "व्यक्ति, कॉर्पोरेट निकाय, परिवार, अवधारणा",
            "वर्क (Work), एक्सप्रेशन (Expression), मैनिफेस्टेशन (Manifestation), आइटम (Item) [WEMI]",
            "संकल्पना, वस्तु, घटना, स्थान",
            "शीर्षक, लेखक, विषय, प्रकाशक"
        ],
        "answer": "B",
        "exp_en": "FRBR Group 1 entities represent products of intellectual endeavor: Work (distinct intellectual creation), Expression (realization of a work), Manifestation (physical embodiment), and Item (single physical exemplar) — known by the acronym WEMI.",
        "exp_hi": "FRBR समूह 1 की चार इकाइयाँ हैं: वर्क (कृति/रचना), एक्सप्रेशन (अभिव्यक्ति), मैनिफेस्टेशन (प्रकटीकरण), और आइटम (भौतिक प्रति/वस्तु) — जिसे संक्षेप में WEMI कहा जाता है।"
    },
    {
        "id": 35,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "Which of the following correctly identifies the four fundamental 'User Tasks' defined in the FRBR model?",
        "q_hi": "निम्नलिखित में से कौन FRBR मॉडल में परिभाषित चार मौलिक 'उपयोगकर्ता कार्यों' (User Tasks) की सही पहचान करता है?",
        "options_en": [
            "Read, Write, Edit, Publish",
            "Find, Identify, Select, Obtain (FISO)",
            "Acquire, Process, Preserve, Disseminate",
            "Classify, Catalogue, Index, Abstract"
        ],
        "options_hi": [
            "पढ़ना, लिखना, संपादन, प्रकाशन",
            "खोजना (Find), पहचानना (Identify), चयन करना (Select), प्राप्त करना (Obtain) [FISO]",
            "अधिग्रहण, प्रसंस्करण, संरक्षण, प्रसार",
            "वर्गीकरण, प्रसूचीकरण, अनुक्रमण, सार-निर्माण"
        ],
        "answer": "B",
        "exp_en": "The four core user tasks defined in FRBR are: Find (to locate resources), Identify (to confirm that document corresponds to user needs), Select (to choose appropriate entity), and Obtain (to acquire or access the entity) — acronym FISO.",
        "exp_hi": "FRBR मॉडल में उपयोगकर्ताओं की आवश्यकताओं के अनुरूप चार मुख्य कार्य परिभाषित किए गए हैं: खोजना (Find), पहचानना (Identify), चयन करना (Select), और प्राप्त करना (Obtain) — संक्षेप में FISO।"
    },
    {
        "id": 36,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "In the International Standard Bibliographic Description (ISBD), which area is designated as 'Area 3'?",
        "q_hi": "अंतर्राष्ट्रीय मानक ग्रंथपरक विवरण (ISBD) के 8 क्षेत्रों में से 'क्षेत्र 3' (Area 3) के रूप में किसे नामित किया गया है?",
        "options_en": [
            "Edition Area",
            "Material (or type of publication) Specific Details Area",
            "Publication, Distribution, etc., Area",
            "Series Area"
        ],
        "options_hi": [
            "संस्करण क्षेत्र (Edition Area)",
            "सामग्री (या प्रकाशन के प्रकार) विशिष्ट विवरण क्षेत्र (Material Specific Details Area)",
            "प्रकाशन, वितरण आदि क्षेत्र (Publication, Distribution Area)",
            "ग्रंथमाला (सीरीज) क्षेत्र (Series Area)"
        ],
        "answer": "B",
        "exp_en": "In ISBD's 8 descriptive areas, Area 3 is the 'Material (or type of publication) Specific Details Area' (used for cartographic scales, serial numbering, or digital file characteristics).",
        "exp_hi": "ISBD के 8 क्षेत्रों में से क्षेत्र 3 'सामग्री (या प्रकाशन के प्रकार) विशिष्ट विवरण क्षेत्र' है, जिसका उपयोग मानचित्रों के पैमाने, पत्रिकाओं की अंक संख्या या डिजिटल विशेषताओं के लिए किया जाता है।"
    },
    {
        "id": 37,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "The Common Communication Format (CCF) was developed by UNESCO in 1984 based structurally on which international record-structure standard?",
        "q_hi": "यूनेस्को द्वारा 1984 में विकसित कॉमन कम्युनिकेशन फॉर्मेट (CCF) संरचनात्मक रूप से किस अंतर्राष्ट्रीय रिकॉर्ड-संरचना मानक पर आधारित था?",
        "options_en": [
            "ISO 2709",
            "ISO 9001",
            "ISO 3297",
            "ISO 2108"
        ],
        "options_hi": [
            "आईएसओ 2709 (ISO 2709)",
            "आईएसओ 9001 (ISO 9001)",
            "आईएसओ 3297 (ISO 3297)",
            "आईएसओ 2108 (ISO 2108)"
        ],
        "answer": "A",
        "exp_en": "CCF was developed by UNESCO under the UNISIST program conforming to ISO 2709 (the international standard for format exchange of bibliographic information on magnetic media).",
        "exp_hi": "CCF को यूनेस्को द्वारा यूनिसिस्ट (UNISIST) कार्यक्रम के अंतर्गत तैयार किया गया था, जो ग्रंथपरक सूचनाओं के विनिमय के अंतरराष्ट्रीय मानक आईएसओ 2709 (ISO 2709) पर आधारित है।"
    },
    {
        "id": 38,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "On which date did the International Standard Book Number (ISBN) officially expand from a 10-digit to a 13-digit standard, and which GS1 Bookland prefixes were introduced?",
        "q_hi": "अंतर्राष्ट्रीय मानक पुस्तक संख्या (ISBN) को आधिकारिक तौर पर 10 अंकों से 13 अंकों के मानक में किस तिथि को विस्तारित किया गया, और कौन-से GS1 बुकलैंड उपसर्ग जोड़े गए?",
        "options_en": [
            "1 January 2005; Prefixes 900 and 901",
            "1 January 2007; Prefixes 978 and 979",
            "1 January 2010; Prefixes 980 and 981",
            "1 January 2015; Prefixes 998 and 999"
        ],
        "options_hi": [
            "1 जनवरी 2005; उपसर्ग 900 और 901",
            "1 जनवरी 2007; उपसर्ग 978 और 979",
            "1 जनवरी 2010; उपसर्ग 980 और 981",
            "1 जनवरी 2015; उपसर्ग 998 और 999"
        ],
        "answer": "B",
        "exp_en": "On 1 January 2007, the ISBN system was expanded globally from 10 digits to 13 digits to harmonize with EAN-13 barcodes, utilizing GS1 Bookland prefixes 978 and 979.",
        "exp_hi": "1 जनवरी 2007 को वैश्विक स्तर पर ISBN को 10 अंकों से बढ़ाकर 13 अंकों का कर दिया गया, ताकि इसे EAN-13 बारकोड प्रणाली के अनुकूल बनाया जा सके और इसमें 978 तथा 979 के उपसर्ग जोड़े गए।"
    },
    {
        "id": 39,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "In the 13-digit ISBN structure, the final check digit is computed using which mathematical algorithm?",
        "q_hi": "13-अंकीय ISBN संरचना में अंतिम जाँच अंक (Check Digit) की गणना किस गणितीय एल्गोरिदम द्वारा की जाती है?",
        "options_en": [
            "Modulo 11 with weights 10 down to 2",
            "Modulo 10 with alternating weights of 1 and 3",
            "Modulo 10 with progressive weights 1 to 12",
            "Modulo 7 with prime multipliers"
        ],
        "options_hi": [
            "मॉड्यूलो 11 (10 से 2 तक के घटते भार के साथ)",
            "मॉड्यूलो 10 (1 और 3 के वैकल्पिक भार के साथ)",
            "मॉड्यूलो 10 (1 से 12 तक के प्रगतिशील भार के साथ)",
            "मॉड्यूलो 7 (अभाज्य गुणकों के साथ)"
        ],
        "answer": "B",
        "exp_en": "Unlike the 10-digit ISBN which utilized Modulo 11, the 13-digit ISBN calculates its check digit using the EAN-13 Modulo 10 algorithm with alternating weights of 1 and 3.",
        "exp_hi": "10 अंकों वाले पुराने ISBN में प्रयुक्त मॉड्यूलो 11 के विपरीत, 13 अंकों वाले नए ISBN में अंतिम चेक डिजिट की गणना मॉड्यूलो 10 (Modulo 10) और 1 तथा 3 के वैकल्पिक भार (weights 1 and 3) द्वारा की जाती है।"
    },
    {
        "id": 40,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 2: Knowledge Organization, Information Processing and Retrieval",
        "unit_hi": "इकाई 2: ज्ञान संगठन, सूचना प्रसंस्करण एवं पुनर्प्राप्ति",
        "q_en": "The International Standard Serial Number (ISSN) consists of 8 digits. In India, which institution acts as the National Centre for assigning ISSN to serials?",
        "q_hi": "अंतर्राष्ट्रीय मानक क्रमिक संख्या (ISSN) में 8 अंक होते हैं। भारत में क्रमिक प्रकाशनों (पत्रिकाओं) को ISSN आवंटित करने के लिए कौन-सा संस्थान राष्ट्रीय केंद्र के रूप में कार्य करता है?",
        "options_en": [
            "National Library of India, Kolkata",
            "Raja Rammohun Roy National Agency, New Delhi",
            "National Science Library, CSIR-NIScPR, New Delhi",
            "Delhi Public Library, Delhi"
        ],
        "options_hi": [
            "भारतीय राष्ट्रीय पुस्तकालय, कोलकाता",
            "राजा राममोहन राय राष्ट्रीय एजेंसी, नई दिल्ली",
            "राष्ट्रीय विज्ञान पुस्तकालय, CSIR-NIScPR, नई दिल्ली",
            "दिल्ली पब्लिक लाइब्रेरी, दिल्ली"
        ],
        "answer": "C",
        "exp_en": "The National Science Library at CSIR-NIScPR (formerly NISCAIR), New Delhi, is the officially designated National Centre responsible for assigning ISSN to serial publications in India.",
        "exp_hi": "भारत में पत्रिकाओं/सामयिकी को ISSN आवंटित करने का अधिकृत राष्ट्रीय केंद्र CSIR-NIScPR (पूर्व में निस्केयर / NISCAIR) की नेशनल साइंस लाइब्रेरी, नई दिल्ली है (जबकि राजा राममोहन राय एजेंसी ISBN देती है)।"
    },

    # =========================================================================
    # UNIT 3: LIBRARY MANAGEMENT AND OPERATIONS (Q41 to Q60)
    # =========================================================================
    {
        "id": 41,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "In his seminal treatise 'The Principles of Scientific Management' (1911), Frederick Winslow Taylor advocated which fundamental operational technique to eliminate wasted motion and optimize labor productivity?",
        "q_hi": "फ्रेडरिक विंसलो टेलर ने अपनी प्रसिद्ध पुस्तक 'द प्रिंसिपल्स ऑफ साइंटिफिक मैनेजमेंट' (1911) में व्यर्थ गतियों को समाप्त करने और श्रम उत्पादकता को अनुकूलित करने के लिए किस परिचालन तकनीक की वकालत की थी?",
        "options_en": [
            "Time and Motion Study",
            "Scalar Chain Principle",
            "Unity of Command",
            "Espirit de Corps"
        ],
        "options_hi": [
            "समय एवं गति अध्ययन (Time and Motion Study)",
            "सोपान श्रृंखला सिद्धांत (Scalar Chain)",
            "आदेश की एकता (Unity of Command)",
            "सहयोग की भावना (Espirit de Corps)"
        ],
        "answer": "A",
        "exp_en": "F.W. Taylor pioneered 'Time and Motion Study' to systematically record, analyze, and time physical movements required to perform a task, establishing standardized workflows in scientific management.",
        "exp_hi": "एफ. डब्ल्यू. टेलर ने कार्यकुशलता बढ़ाने और श्रमिकों की अनावश्यक गतिविधियों को समाप्त करने के लिए 'समय और गति अध्ययन' (Time and Motion Study) की तकनीक विकसित की थी।"
    },
    {
        "id": 42,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "According to F.W. Taylor, what is the core psychological prerequisite necessary for the successful implementation of Scientific Management?",
        "q_hi": "एफ. डब्ल्यू. टेलर के अनुसार, वैज्ञानिक प्रबंधन के सफल क्रियान्वयन के लिए मुख्य मनोवैज्ञानिक पूर्वशर्त कौन-सी है?",
        "options_en": [
            "Total mechanization of all jobs",
            "'Mental Revolution' between workers and management",
            "Abolition of all supervisory personnel",
            "Strict penal punishment for minor operational delays"
        ],
        "options_hi": [
            "सभी नौकरियों का पूर्ण यंत्रीकरण",
            "श्रमिकों और प्रबंधन के बीच 'मानसिक क्रांति' (Mental Revolution)",
            "सभी पर्यवेक्षी कर्मचारियों का उन्मूलन",
            "मामूली परिचालन देरी के लिए सख्त दंडात्मक कार्रवाई"
        ],
        "answer": "B",
        "exp_en": "Taylor emphasized 'Mental Revolution' as the cornerstone of scientific management—a complete change of mental attitude on the part of both workers and management towards mutual cooperation rather than antagonism.",
        "exp_hi": "टेलर ने 'मानसिक क्रांति' (Mental Revolution) को वैज्ञानिक प्रबंधन का मूल आधार बताया, जिसका तात्पर्य श्रमिकों और प्रबंधन दोनों के बीच आपसी संघर्ष के बजाय सहयोग और सद्भाव का पूर्ण दृष्टिकोण विकसित करना है।"
    },
    {
        "id": 43,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "Elton Mayo and his Harvard research team conducted the classic 'Hawthorne Studies' (1924-1932) at the manufacturing plant of which company?",
        "q_hi": "एल्टन मेयो और उनकी हार्वर्ड अनुसंधान टीम ने प्रसिद्ध 'हॉथोर्न अध्ययन' (1924-1932) किस कंपनी के विनिर्माण संयंत्र में आयोजित किए थे?",
        "options_en": [
            "General Motors Corporation",
            "Western Electric Company",
            "Ford Motor Company",
            "Remington Rand Corporation"
        ],
        "options_hi": [
            "जनरल मोटर्स कॉरपोरेशन",
            "वेस्टर्न इलेक्ट्रिक कंपनी (Western Electric Company)",
            "फोर्ड मोटर कंपनी",
            "रेमिंगटन रैंड कॉरपोरेशन"
        ],
        "answer": "B",
        "exp_en": "The Hawthorne Studies were carried out between 1924 and 1932 at the Western Electric Company's Hawthorne Works in Cicero, Illinois, laying the foundation of the Human Relations School of Management.",
        "exp_hi": "हॉथोर्न अध्ययन 1924 से 1932 के मध्य शिकागो के निकट 'वेस्टर्न इलेक्ट्रिक कंपनी' के हॉथोर्न वर्क्स संयंत्र में आयोजित किए गए थे, जिसने प्रबंधन के मानव संबंध संप्रदाय की नींव रखी।"
    },
    {
        "id": 44,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "What does the term 'Hawthorne Effect' refer to in management and behavioral sciences?",
        "q_hi": "प्रबंधन और व्यवहार विज्ञान में 'हॉथोर्न प्रभाव' (Hawthorne Effect) पद का क्या तात्पर्य है?",
        "options_en": [
            "Decline in output caused by mechanical breakdown",
            "The tendency of individuals to alter and improve their productivity when they know they are being observed and valued",
            "The natural fatigue that occurs during night shifts",
            "Direct linear growth of output proportional to monetary bonuses"
        ],
        "options_hi": [
            "यांत्रिक खराबी के कारण उत्पादन में गिरावट",
            "व्यक्तियों द्वारा यह जाने जाने पर कि उनका अवलोकन किया जा रहा है और उन पर ध्यान दिया जा रहा है, अपने व्यवहार और उत्पादकता में सुधार करने की प्रवृत्ति",
            "रात की पाली के दौरान होने वाली प्राकृतिक थकान",
            "मौद्रिक बोनस के अनुपात में उत्पादन की सीधी रैखिक वृद्धि"
        ],
        "answer": "B",
        "exp_en": "The 'Hawthorne Effect' refers to the finding that individuals modify or improve their behavior and productivity in response to the awareness that they are being observed, studied, and receiving attention.",
        "exp_hi": "'हॉथोर्न प्रभाव' उस मनोवैज्ञानिक प्रवृत्ति को दर्शाता है जिसमें कर्मचारी यह महसूस करने पर कि उनका विशेष निरीक्षण किया जा रहा है और उन पर ध्यान दिया जा रहा है, अपनी कार्यकुशलता और उत्पादकता को स्वतः बढ़ा देते हैं।"
    },
    {
        "id": 45,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "Who propounded the classic book selection principle: 'To provide the right book to the right reader at the right time'?",
        "q_hi": "पुस्तक चयन का यह कालजयी सिद्धांत किसने प्रतिपादित किया था: 'सही समय पर सही पाठक को सही पुस्तक प्रदान करना' (To provide the right book to the right reader at the right time)?",
        "options_en": [
            "Melvil Dewey",
            "Francis K.W. Drury",
            "L.R. McColvin",
            "Dr. S.R. Ranganathan"
        ],
        "options_hi": [
            "मेलविल डेवी",
            "फ्रांसिस के. डब्ल्यू. ड्ररी (F.K.W. Drury)",
            "एल. आर. मैककॉल्विन",
            "डॉ. एस. आर. रंगनाथन"
        ],
        "answer": "B",
        "exp_en": "Francis K.W. Drury propounded this principle in his seminal 1930 book 'Book Selection', advocating reader-oriented collection development.",
        "exp_hi": "फ्रांसिस के. डब्ल्यू. ड्ररी (F.K.W. Drury) ने 1930 में अपनी प्रसिद्ध पुस्तक 'बुक सेलेक्शन' में पाठक-केंद्रित पुस्तक चयन हेतु यह अमर सूत्र प्रतिपादित किया था।"
    },
    {
        "id": 46,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "The renowned library motto: 'The best reading for the largest number at the least cost' was formulated in 1876 by:",
        "q_hi": "पुस्तकालय का सुप्रसिद्ध आदर्श वाक्य: 'न्यूनतम लागत पर अधिकतम व्यक्तियों के लिए सर्वोत्तम पठन सामग्री' (The best reading for the largest number at the least cost) 1876 में किसके द्वारा प्रतिपादित किया गया था?",
        "options_en": [
            "Melvil Dewey",
            "C.A. Cutter",
            "W.A. Borden",
            "Nina E. Browne"
        ],
        "options_hi": [
            "मेलविल डेवी",
            "सी. ए. कटर",
            "डब्लू. ए. बोर्डन",
            "नीना ई. ब्राउन"
        ],
        "answer": "A",
        "exp_en": "Melvil Dewey formulated this motto in 1876, which was adopted as the official motto of the American Library Association (ALA) to guide economical and high-impact book acquisition.",
        "exp_hi": "मेलविल डेवी ने 1876 में यह सूत्र दिया था, जिसे बाद में अमेरिकन लाइब्रेरी एसोसिएशन (ALA) के आधिकारिक आदर्श वाक्य के रूप में अपनाया गया।"
    },
    {
        "id": 47,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "In his 1925 work 'The Theory of Book Selection for Public Libraries', Lionel Roy McColvin based his principles of book selection on:",
        "q_hi": "1925 की अपनी कृति 'द थ्योरी ऑफ बुक सेलेक्शन फॉर पब्लिक लाइब्रेरीज' में लियोनेल रॉय मैककॉल्विन ने पुस्तक चयन के सिद्धांतों को किस पर आधारित किया?",
        "options_en": [
            "Historical chronology of world authors",
            "Demand and Supply Theory (Volume and Variety of Demand)",
            "Commercial marketing strategies",
            "Physical durability of leather binding"
        ],
        "options_hi": [
            "विश्व के लेखकों का ऐतिहासिक कालक्रम",
            "माँग एवं आपूर्ति सिद्धांत (माँग का परिमाण एवं विविधता)",
            "व्यावसायिक विपणन रणनीतियाँ",
            "चमड़े की जिल्दसाजी का भौतिक स्थायित्व"
        ],
        "answer": "B",
        "exp_en": "L.R. McColvin propounded the 'Demand Theory' of book selection in 1925, stating that books should be acquired according to the volume and variety of readers' demands, counterbalanced by intrinsic value.",
        "exp_hi": "एल. आर. मैककॉल्विन ने 1925 में पुस्तक चयन का 'माँग एवं आपूर्ति सिद्धांत' (Demand Theory) दिया, जिसके तहत पुस्तकों का अधिग्रहण पाठकों की माँग के परिमाण (Volume) और विविधता (Variety) के आधार पर होना चाहिए।"
    },
    {
        "id": 48,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "In which book published in 1952 did Dr. S.R. Ranganathan demonstrate that the principles of book selection are direct corollaries of the First Three Laws of Library Science?",
        "q_hi": "1952 में प्रकाशित किस पुस्तक में डॉ. एस. आर. रंगनाथन ने प्रदर्शित किया कि पुस्तक चयन के सिद्धांत पुस्तकालय विज्ञान के प्रथम तीन सूत्रों के प्रत्यक्ष उपप्रमेय हैं?",
        "options_en": [
            "Library Book Selection",
            "Prolegomena to Library Classification",
            "Library Administration",
            "Reference Service"
        ],
        "options_hi": [
            "लाइब्रेरी बुक सेलेक्शन (Library Book Selection)",
            "प्रोलिगोमेना टू लाइब्रेरी क्लासिफिकेशन",
            "लाइब्रेरी एडमिनिस्ट्रेशन",
            "रेफरेंस सर्विस"
        ],
        "answer": "A",
        "exp_en": "Dr. S.R. Ranganathan published 'Library Book Selection' in 1952, deriving book selection criteria systematically from the First Three Laws: Books are for use, Every reader his/her book, and Every book its reader.",
        "exp_hi": "डॉ. रंगनाथन ने 1952 में 'लाइब्रेरी बुक सेलेक्शन' पुस्तक प्रकाशित की, जिसमें उन्होंने दिखाया कि प्रथम तीन सूत्र (पुस्तकें उपयोगार्थ हैं, प्रत्येक पाठक को उसकी पुस्तक, प्रत्येक पुस्तक को उसका पाठक) पुस्तक चयन के मुख्य नियामक हैं।"
    },
    {
        "id": 49,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "Which of the following is a universally accepted rule regarding the assignment of an 'Accession Number' in a library?",
        "q_hi": "पुस्तकालय में 'परिग्रहण संख्या' (Accession Number) आवंटित करने के संबंध में निम्नलिखित में से कौन-सा एक सार्वभौमिक नियम है?",
        "options_en": [
            "It changes whenever a damaged book is rebound",
            "It is a unique chronological serial number that is never reassigned to another book, even if the original copy is weeded out or lost",
            "Multiple copies of the same title share the identical accession number",
            "It is determined strictly by the DDC classification number"
        ],
        "options_hi": [
            "क्षतिग्रस्त पुस्तक की पुन: जिल्दसाजी होने पर यह संख्या बदल जाती है",
            "यह एक अद्वितीय कालानुक्रमिक संख्या है जिसे किसी अन्य पुस्तक को कभी पुनः आवंटित नहीं किया जाता, भले ही मूल प्रति निरस्त या खो गई हो",
            "एक ही शीर्षक की कई प्रतियों को एक समान परिग्रहण संख्या दी जाती है",
            "यह DDC वर्गीकरण संख्या द्वारा सख्ती से निर्धारित होती है"
        ],
        "answer": "B",
        "exp_en": "An Accession Number is a permanent, unique sequential serial number assigned to each specific volume as it enters the library; even if the book is subsequently withdrawn, discarded, or lost, that number is never reused.",
        "exp_hi": "परिग्रहण संख्या पुस्तकालय में आने वाले प्रत्येक प्रलेख को दी जाने वाली एक स्थायी और अद्वितीय क्रमिक संख्या है; यदि पुस्तक बाद में खो भी जाती है या निरस्त कर दी जाती है, तो भी वह संख्या किसी अन्य पुस्तक को नहीं दी जाती।"
    },
    {
        "id": 50,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "What is the primary structural difference in arrangement between the Accession Register and the Shelf List in a library?",
        "q_hi": "पुस्तकालय में परिग्रहण पंजिका (Accession Register) और निधानी सूची (Shelf List) के क्रम में प्राथमिक संरचनात्मक अंतर क्या है?",
        "options_en": [
            "Accession Register is alphabetical by author; Shelf List is alphabetical by title",
            "Accession Register is chronological by date of receipt; Shelf List is in the exact classified order of books on the shelves (by Call Number)",
            "Accession Register is arranged by price; Shelf List is arranged by publisher",
            "There is no difference in arrangement between the two records"
        ],
        "options_hi": [
            "परिग्रहण पंजिका लेखक वर्णानुक्रम में होती है; शेल्फ लिस्ट शीर्षक वर्णानुक्रम में होती है",
            "परिग्रहण पंजिका प्राप्ति तिथि के कालक्रमानुसार होती है; शेल्फ लिस्ट अलमारियों पर रखी पुस्तकों के सटीक वर्गीकृत क्रम (क्रमांक / कॉल नंबर) में होती है",
            "परिग्रहण पंजिका मूल्य के अनुसार होती है; शेल्फ लिस्ट प्रकाशक के अनुसार होती है",
            "दोनों रिकॉर्डों की व्यवस्था में कोई अंतर नहीं होता"
        ],
        "answer": "B",
        "exp_en": "The Accession Register records volumes in continuous chronological order of acquisition, whereas the Shelf List arranges entries in the exact classified sequence in which books stand on the physical shelves (by Call Number).",
        "exp_hi": "परिग्रहण पंजिका में पुस्तकों को प्राप्ति की तिथि के अनुसार कालक्रमानुसार दर्ज किया जाता है, जबकि शेल्फ लिस्ट में प्रविष्टियाँ अलमारियों में रखी पुस्तकों के सटीक वर्गीकृत क्रम (कॉल नंबर/वर्गांक) के अनुसार व्यवस्थित होती हैं।"
    },
    {
        "id": 51,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "In library bookbinding, how is a 'Half Leather Binding' constructed?",
        "q_hi": "पुस्तकालय जिल्दसाजी में 'हाफ लेदर बाइंडिंग' (Half Leather Binding) की संरचना किस प्रकार की जाती है?",
        "options_en": [
            "The entire exterior of the book is bound in artificial synthetic leather",
            "Genuine leather covers the spine and four corners, while cloth or paper covers the sides",
            "Only the top edge and bottom edge of the book are bound in leather",
            "The front board is made of leather and the back board is made of cloth"
        ],
        "options_hi": [
            "पुस्तक का पूरा बाहरी भाग कृत्रिम सिंथेटिक चमड़े से मढ़ा होता है",
            "असली चमड़ा पुस्तक की पीठ (स्पाइन) और चारों कोनों को ढकता है, जबकि बाकी तख्ते कपड़े या कागज़ से ढके होते हैं",
            "पुस्तक के केवल ऊपरी और निचले किनारों को चमड़े से बांधा जाता है",
            "सामने का बोर्ड चमड़े से और पीछे का बोर्ड कपड़े से बना होता है"
        ],
        "answer": "B",
        "exp_en": "In 'Half Leather Binding', genuine leather is used on the spine and the four outer corners (the sections enduring greatest mechanical wear), while the sides of the boards are covered with durable cloth or paper.",
        "exp_hi": "'हाफ लेदर बाइंडिंग' में पुस्तक की पीठ (स्पाइन) और चारों कोनों पर असली चमड़ा लगाया जाता है (क्योंकि यहाँ सर्वाधिक घिसाव होता है), तथा बाकी दोनों तख्तों पर टिकाऊ कपड़ा या कागज़ चढ़ाया जाता है।"
    },
    {
        "id": 52,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "In fine library bookbinding, 'Morocco Leather' is manufactured from the hide of which animal and tanned with which vegetable agent?",
        "q_hi": "उत्कृष्ट पुस्तकालय जिल्दसाजी में 'मोरोक्को लेदर' (Morocco Leather) किस पशु की खाल से बनाया जाता है और इसे किस वानस्पतिक पदार्थ से पकाया (टैन) जाता है?",
        "options_en": [
            "Cowhide tanned with mineral chrome",
            "Goatskin tanned with sumac",
            "Pigskin tanned with oak bark",
            "Sheepskin tanned with fish oil"
        ],
        "options_hi": [
            "खनिज क्रोम से पकाई गई गाय की खाल",
            "सुमाक (Sumac) से पकाई गई बकरे/बकरी की खाल (Goatskin)",
            "ओक की छाल से पकाई गई सुअर की खाल",
            "मछली के तेल से पकाई गई भेड़ की खाल"
        ],
        "answer": "B",
        "exp_en": "Morocco leather is prepared from goatskin vegetable-tanned with sumac, known for its fine pebble grain, pliability, and superior longevity in library preservation.",
        "exp_hi": "मोरोक्को लेदर उच्च कोटि की बकरी/बकरे की खाल (Goatskin) से तैयार किया जाता है जिसे 'सुमाक' नामक वानस्पतिक पदार्थ से टैन किया जाता है; यह अपने लचीलेपन, प्राकृतिक दानेदार बनावट और दीर्घायु के लिए प्रसिद्ध है।"
    },
    {
        "id": 53,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "In book anatomy and binding, the strip of open-weave starched cotton gauze glued to the spine of the book block to reinforce the hinge is called:",
        "q_hi": "पुस्तक संरचना और जिल्दसाजी में पुस्तक ब्लॉक की पीठ पर मजबूती देने के लिए चिपकाई जाने वाली स्टार्चयुक्त खुली बुनाई वाली सूती जाली (गॉज) की पट्टी को क्या कहा जाता है?",
        "options_en": [
            "Endpaper",
            "Mull (or Super)",
            "Headband",
            "Slipcase"
        ],
        "options_hi": [
            "एंडपेपर (अंतःपत्र)",
            "मल या सुपर (Mull / Super)",
            "हेडबैंड (Headband)",
            "स्लिपकेस (Slipcase)"
        ],
        "answer": "B",
        "exp_en": "'Mull' (also termed 'super' or 'crash') is a coarse open-weave starched cotton fabric pasted across the sewn spine of a book block to secure the gatherings and reinforce the hinge attaching the cover boards.",
        "exp_hi": "'मल' (Mull) या 'सुपर' स्टार्चयुक्त जालीदार सूती कपड़ा होता है जिसे सिली हुई स्पाइन पर चिपकाया जाता है ताकि कवर और पन्नों के जोड़ को मजबूती मिल सके और जिल्द लंबे समय तक टिकी रहे।"
    },
    {
        "id": 54,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "Which common wingless, silvery biological pest in libraries (Lepisma saccharina) feeds primarily on the starch, glue, and sizing paste used in book bindings?",
        "q_hi": "पुस्तकालयों का कौन-सा सामान्य पंखहीन, चांदी जैसे रंग वाला जैविक कीट (Lepisma saccharina) मुख्य रूप से जिल्दसाजी में प्रयुक्त स्टार्च, सरेस (गोंद) और कागज़ की साइजिंग को खाता है?",
        "options_en": [
            "Termite (White ant)",
            "Silverfish",
            "Book scorpion",
            "Carpet beetle"
        ],
        "options_hi": [
            "दीमक",
            "सिल्वरफिश (Silverfish)",
            "बुक बिच्छू",
            "कालीन भृंग"
        ],
        "answer": "B",
        "exp_en": "Silverfish (Lepisma saccharina) are destructive, wingless nocturnal insects in libraries that thrive in damp areas and feed voraciously on carbohydrate-rich book materials like starch paste, glue, and paper glaze.",
        "exp_hi": "सिल्वरफिश (Silverfish / Lepisma saccharina) एक पंखहीन निशाचर कीट है जो नम और अंधेरे वातावरण में पनपता है तथा जिल्दसाजी में प्रयुक्त स्टार्च, गोंद और कागज़ के लेप को खाकर गंभीर क्षति पहुँचाता है।"
    },
    {
        "id": 55,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "The 'Planning-Programming-Budgeting System' (PPBS) was first introduced in 1961 by which administrative leader in the United States Department of Defense?",
        "q_hi": "'प्लानिंग-प्रोग्रामिंग-बजटिंग सिस्टम' (PPBS) की शुरुआत 1961 में संयुक्त राज्य अमेरिका के रक्षा विभाग में किस प्रशासनिक नेता द्वारा की गई थी?",
        "options_en": [
            "Peter Drucker",
            "Robert McNamara",
            "Peter Pyhrr",
            "Henri Fayol"
        ],
        "options_hi": [
            "पीटर ड्रकर",
            "रॉबर्ट मैकनामारा (Robert McNamara)",
            "पीटर पायर",
            "हेनरी फेयोल"
        ],
        "answer": "B",
        "exp_en": "PPBS was introduced in 1961 by US Secretary of Defense Robert McNamara under the Kennedy administration to integrate strategic long-term planning with budgeting and cost-benefit analysis.",
        "exp_hi": "PPBS को 1961 में अमेरिकी रक्षा सचिव रॉबर्ट मैकनामारा द्वारा अमेरिकी रक्षा विभाग में दीर्घकालिक रणनीतिक योजना और लागत-प्रभावशीलता विश्लेषण को बजट से जोड़ने के लिए लागू किया गया था।"
    },
    {
        "id": 56,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "What is the defining operational characteristic of the PPBS (Planning-Programming-Budgeting System) budgeting methodology?",
        "q_hi": "PPBS (प्लानिंग-प्रोग्रामिंग-बजटिंग सिस्टम) बजट पद्धति की मुख्य परिचालन विशेषता क्या है?",
        "options_en": [
            "It mechanically increases line items by an inflation percentage each year",
            "It establishes clear organizational goals, formulates programs to meet them, and evaluates allocations through cost-benefit analysis",
            "It allocates funds purely based on the historical seniority of department heads",
            "It bases expenditures solely on the number of physical visitors"
        ],
        "options_hi": [
            "यह प्रत्येक वर्ष केवल मुद्रास्फीति दर के आधार पर मदों में यांत्रिक वृद्धि करता है",
            "यह स्पष्ट संगठनात्मक लक्ष्य निर्धारित करता है, उन्हें पूरा करने के लिए कार्यक्रम बनाता है और लागत-लाभ विश्लेषण द्वारा बजट आवंटित करता है",
            "यह विभाग प्रमुखों की वरिष्ठता के आधार पर पूरी तरह धन आवंटित करता है",
            "यह व्यय को केवल भौतिक आगंतुकों की संख्या पर आधारित करता है"
        ],
        "answer": "B",
        "exp_en": "PPBS operates by identifying overarching organizational objectives (Planning), developing discrete operational activities/projects to achieve them (Programming), and funding alternatives based on rigorous cost-benefit evaluations (Budgeting).",
        "exp_hi": "PPBS योजना, कार्यक्रम और बजट को जोड़ता है जहाँ संस्था के प्राथमिक लक्ष्यों की पहचान की जाती है, उन लक्ष्यों को पूरा करने वाले कार्यक्रम तय किए जाते हैं और लागत-लाभ विश्लेषण के आधार पर बजट आवंटित किया जाता है।"
    },
    {
        "id": 57,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "The management technique 'Management by Objectives' (MBO) was propounded by Peter Drucker in 1954 in which classic management treatise?",
        "q_hi": "'उद्देश्यों द्वारा प्रबंधन' (Management by Objectives - MBO) की तकनीक पीटर ड्रकर द्वारा 1954 में अपनी किस प्रसिद्ध पुस्तक में प्रतिपादित की गई थी?",
        "options_en": [
            "The Practice of Management",
            "General and Industrial Management",
            "The Effective Executive",
            "Shop Management"
        ],
        "options_hi": [
            "द प्रैक्टिस ऑफ मैनेजमेंट (The Practice of Management)",
            "जनरल एंड इंडस्ट्रियल मैनेजमेंट",
            "द इफेक्टिव एग्जीक्यूटिव",
            "शॉप मैनेजमेंट"
        ],
        "answer": "A",
        "exp_en": "Peter Drucker propounded the concept of 'Management by Objectives' (MBO) in his 1954 book 'The Practice of Management', emphasizing goal-oriented management.",
        "exp_hi": "पीटर ड्रकर ने 1954 में अपनी कालजयी पुस्तक 'द प्रैक्टिस ऑफ मैनेजमेंट' में 'उद्देश्यों द्वारा प्रबंधन' (MBO) की अवधारणा प्रस्तुत की थी।"
    },
    {
        "id": 58,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "In a library adopting 'Management by Objectives' (MBO), how are operational objectives and performance targets formulated?",
        "q_hi": "'उद्देश्यों द्वारा प्रबंधन' (MBO) अपनाने वाले पुस्तकालय में परिचालन उद्देश्यों और प्रदर्शन लक्ष्यों का निर्धारण कैसे किया जाता है?",
        "options_en": [
            "Unilateral top-down decree issued without subordinate input",
            "Joint participative consultation and agreement between supervisors and subordinate staff",
            "Random assignment determined by computer software",
            "Exclusive prescription by external auditing authorities"
        ],
        "options_hi": [
            "अधीनस्थों के इनपुट के बिना जारी किया गया एकतरफा शीर्ष-स्तरीय आदेश",
            "पर्यवेक्षकों और अधीनस्थ कर्मचारियों के बीच संयुक्त सहभागी परामर्श और आपसी सहमति",
            "कंप्यूटर सॉफ्टवेयर द्वारा निर्धारित यादृच्छिक आवंटन",
            "केवल बाहरी लेखापरीक्षा अधिकारियों द्वारा अनन्य निर्धारण"
        ],
        "answer": "B",
        "exp_en": "The foundational mechanism of MBO is participatory management: supervisors and subordinates jointly identify common goals, define individual areas of responsibility, and use these agreed measures to guide operations.",
        "exp_hi": "MBO का मूल आधार सहभागी प्रबंधन है, जिसमें उच्चाधिकारी और अधीनस्थ कर्मचारी मिलकर लक्ष्यों को तय करते हैं, जिम्मेदारियों का निर्धारण करते हैं और समय-समय पर परिणामों की समीक्षा करते हैं।"
    },
    {
        "id": 59,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "What standard radio frequency is universally utilized for RFID tags in modern library management systems (governed by ISO 15693 / ISO 18000-3)?",
        "q_hi": "आधुनिक पुस्तकालय प्रबंधन प्रणालियों (ISO 15693 / ISO 18000-3 द्वारा शासित) में RFID टैग के लिए सामान्यतः कौन-सी मानक रेडियो आवृत्ति अपनाई जाती है?",
        "options_en": [
            "Low Frequency (LF) 125 kHz",
            "High Frequency (HF) 13.56 MHz",
            "Ultra-High Frequency (UHF) 860-960 MHz",
            "Microwave 2.45 GHz"
        ],
        "options_hi": [
            "लो फ्रीक्वेंसी (LF) 125 kHz",
            "हाई फ्रीक्वेंसी (HF) 13.56 MHz",
            "अल्ट्रा-हाई फ्रीक्वेंसी (UHF) 860-960 MHz",
            "माइक्रोवेव 2.45 GHz"
        ],
        "answer": "B",
        "exp_en": "High Frequency (HF) operating at 13.56 MHz is the globally accepted standard frequency for library RFID applications (ISO 15693 and ISO 18000-3), providing an optimal read distance and minimal interference.",
        "exp_hi": "पुस्तकालयों में RFID टैग के लिए अंतरराष्ट्रीय स्तर पर स्वीकृत मानक आवृत्ति हाई फ्रीक्वेंसी (HF) 13.56 MHz है (ISO 15693 मानक), जो आदर्श स्कैनिंग दूरी और न्यूनतम व्यवधान सुनिश्चित करती है।"
    },
    {
        "id": 60,
        "section_en": "Part 1: Library & Information Science",
        "section_hi": "भाग 1: पुस्तकालय एवं सूचना विज्ञान",
        "unit_en": "Unit 3: Information Sources, Systems and Services / Library Management",
        "unit_hi": "इकाई 3: पुस्तकालय प्रबंधन एवं परिचालन",
        "q_en": "In a library RFID automation system, what component or status setting in the RFID tag triggers the alarm at the exit security gate if a patron attempts to leave with an unborrowed book?",
        "q_hi": "पुस्तकालय RFID स्वचालन प्रणाली में यदि कोई पाठक बिना इश्यू (निर्गमन) कराई गई पुस्तक लेकर बाहर निकलता है, तो निकास द्वार पर अलार्म टैग के किस घटक या स्थिति द्वारा बजता है?",
        "options_en": [
            "The barcode label transparency",
            "The active EAS (Electronic Article Surveillance) bit / AFI byte",
            "The physical weight difference of the paper",
            "The electrostatic voltage on the spine"
        ],
        "options_hi": [
            "बारकोड लेबल की पारदर्शिता",
            "सक्रिय ईएएस (Electronic Article Surveillance - EAS) बिट / AFI बाइट",
            "कागज़ का भौतिक भार अंतर",
            "स्पाइन पर इलेक्ट्रोस्टैटिक वोल्टेज"
        ],
        "answer": "B",
        "exp_en": "In library RFID tags, the EAS (Electronic Article Surveillance) bit or AFI (Application Family Identifier) byte is armed on the shelf and disarmed during legitimate checkout at the circulation desk. If a book passes the exit gate with an armed EAS bit, the gate alarms trigger instantly.",
        "exp_hi": "RFID टैग में EAS (इलेक्ट्रॉनिक आर्टिकल सर्विलांस) बिट या AFI बाइट होता है। सर्कुलेशन काउंटर पर पुस्तक इश्यू होने पर यह बिट निष्क्रिय (disarm) हो जाता है; बिना इश्यू कराई गई पुस्तक के गेट से गुजरने पर सक्रिय EAS बिट तुरंत अलार्म बजा देता है।"
    }
]

if __name__ == "__main__":
    print(f"Total questions in Paper 02 Units 1-3: {len(PAPER02_U1_U3_QUESTIONS)}")
    # Verify validity
    for i, q in enumerate(PAPER02_U1_U3_QUESTIONS):
        assert len(q["options_en"]) == 4, f"Q{q['id']} options_en != 4"
        assert len(q["options_hi"]) == 4, f"Q{q['id']} options_hi != 4"
        assert q["answer"] in ["A", "B", "C", "D"], f"Q{q['id']} invalid answer"
        assert len(q["q_en"]) > 10, f"Q{q['id']} empty q_en"
        assert len(q["q_hi"]) > 10, f"Q{q['id']} empty q_hi"
        assert len(q["exp_en"]) > 10, f"Q{q['id']} empty exp_en"
        assert len(q["exp_hi"]) > 10, f"Q{q['id']} empty exp_hi"
    print("All 60 questions passed structure assertions!")
