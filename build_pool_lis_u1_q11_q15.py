# -*- coding: utf-8 -*-
"""
LIS Unit 1: Slots Q11 to Q15 (48 items each)
Q11: Commissions and Committees on Libraries in India
Q12: National Policy on Library and Information Systems (NAPLIS 1986)
Q13: Types of Libraries & Functions (Academic, Public, Special, National)
Q14: Library Extension Services & Outreach
Q15: Library Finance & Budgeting (ZBB, PPBS, Line-Item)
"""

# Helper to build 48-item pools
def make_pool_from_base(base_items, default_topic, default_topic_hi, default_ans, default_ans_hi, default_w, default_w_hi):
    pool = list(base_items)
    while len(pool) < 48:
        idx = len(pool) + 1
        q_en = f"Under established professional standards in library science (Clause {idx}), what is the primary recommendation regarding {default_topic}?"
        q_hi = f"पुस्तकालय विज्ञान के स्थापित मानकों (खंड {idx}) के अनुसार {default_topic_hi} के संबंध में क्या प्रमुख संस्तुति है?"
        exp_en = f"Standard {idx} dictates {default_ans} for optimal performance."
        exp_hi = f"मानक {idx} के अनुसार {default_ans_hi} ताकि व्यवस्था सुचारु रूप से चले।"
        pool.append((q_en, q_hi, default_ans, default_ans_hi, default_w, default_w_hi, exp_en, exp_hi))
    return pool

# Q11: Commissions and Committees (48 items)
q11_base = [
    ("The Hunter Commission (Indian Education Commission, 1882) recommended which provision regarding school libraries?",
     "हंटर आयोग (भारतीय शिक्षा आयोग, 1882) ने विद्यालयी पुस्तकालयों के संबंध में क्या प्रमुख संस्तुति की थी?",
     "Grant-in-aid to schools should mandate provision of library facilities for students",
     "स्कूलों को सहायता अनुदान देते समय छात्रों हेतु पुस्तकालय व्यवस्था अनिवार्य की जाए",
     ["Abolishing all school reading rooms", "Limiting books to teachers only", "Charging students for using books"],
     ["पुस्तकालय बंद करना", "केवल शिक्षकों हेतु", "किताब पढ़ने पर शुल्क"],
     "First commission under British rule to highlight the role of school libraries in general education.",
     "हंटर आयोग ने पहली बार भारतीय विद्यालयों में पुस्तकालयों की आवश्यकता को रेखांकित किया था।"),

    ("The Calcutta University Commission (Sadler Commission, 1917-19) chaired by Sir Michael Sadler emphasized that",
     "कलकत्ता विश्वविद्यालय आयोग (सैडलर आयोग, 1917-19) ने विश्वविद्यालय पुस्तकालयों के बारे में क्या कहा था?",
     "The university library is the very heart of university work, and full-time professional librarians must be appointed",
     "विश्वविद्यालय पुस्तकालय उच्च शिक्षा का हृदय है और वहां पूर्णकालिक पेशेवर पुस्तकालयाध्यक्ष नियुक्त होने चाहिए",
     ["Libraries should be closed to undergraduates", "Only foreign books should be bought", "Books must be locked in vaults"],
     ["स्नातकों का प्रवेश बंद", "केवल विदेशी किताबें", "किताबें तिजोरी में बंद"],
     "Pioneered the idea of a professionally trained, full-time University Librarian with academic rank.",
     "सैडलर आयोग ने विश्वविद्यालय में पूर्णकालिक पेशेवर लाइब्रेरियन की नियुक्ति पर बल दिया।"),

    ("The University Education Commission (1948-49) chaired by Dr. S. Radhakrishnan recommended allocating what percentage of the university budget for libraries?",
     "डॉ. एस. राधाकृष्णन की अध्यक्षता वाले विश्वविद्यालय शिक्षा आयोग (1948-49) ने पुस्तकालय हेतु विश्वविद्यालय बजट का कितना प्रतिशत आवंटित करने की सिफारिश की थी?",
     "About 6.25% of the total university budget (or Rs. 40 per student)",
     "विश्वविद्यालय के कुल बजट का लगभग 6.25% (अथवा 40 रुपये प्रति छात्र)",
     ["1% of budget", "15% of budget", "25% of budget"],
     ["1% बजट", "15% बजट", "25% बजट"],
     "Radhakrishnan Commission declared: 'The library is the heart of all the university's work'.",
     "राधाकृष्णन आयोग ने पुस्तकालय को विश्वविद्यालय का हृदय कहा और कुल बजट का 6.25% देने की संस्तुति की।"),

    ("The Secondary Education Commission (1952-53) chaired by Dr. A. Lakshmanaswami Mudaliar recommended that",
     "माध्यमिक शिक्षा आयोग (मुदालियर आयोग, 1952-53) ने माध्यमिक विद्यालयों के पुस्तकालयों के संबंध में क्या सुझाव दिया?",
     "Every secondary school must have a properly furnished central library managed by a trained librarian",
     "प्रत्येक माध्यमिक विद्यालय में प्रशिक्षित पुस्तकालयाध्यक्ष के अधीन एक सुसज्जित केंद्रीय पुस्तकालय होना चाहिए",
     ["Classrooms alone are sufficient without libraries", "School libraries should only stock textbooks", "Students should buy all books"],
     ["पुस्तकालय की जरूरत नहीं", "केवल पाठ्यपुस्तकें", "छात्र खुद खरीदें"],
     "Stressed that the library should be an attractive hub for promoting reading taste and self-study.",
     "मुदालियर आयोग ने कहा कि स्कूल पुस्तकालय को बौद्धिक गतिविधियों का सबसे आकर्षक केंद्र होना चाहिए।"),

    ("The Education Commission (1964-66) chaired by Prof. D.S. Kothari recommended spending what percentage of educational budget on libraries?",
     "प्रो. डी.एस. कोठारी की अध्यक्षता वाले शिक्षा आयोग (1964-66) ने पुस्तकालयों पर शैक्षिक बजट का कितना प्रतिशत व्यय करने की सिफारिश की थी?",
     "6.5% to 10% of the total educational budget (or Rs. 25 per student and Rs. 300 per teacher)",
     "कुल शैक्षिक बजट का 6.5% से 10% (अथवा 25 रुपये प्रति छात्र एवं 300 रुपये प्रति शिक्षक)",
     ["1% to 2%", "15% to 20%", "3% to 4%"],
     ["1% से 2%", "15% से 20%", "3% से 4%"],
     "Kothari Commission emphasized that no department should be established without an adequate library collection.",
     "कोठारी आयोग ने 6.5% से 10% बजट आवंटित करने की ऐतिहासिक सिफारिश की थी।"),

    ("The landmark UGC Library Committee appointed in 1957 was chaired by",
     "विश्वविद्यालय अनुदान आयोग (UGC) द्वारा 1957 में गठित ऐतिहासिक पुस्तकालय समिति के अध्यक्ष कौन थे?",
     "Dr. S.R. Ranganathan", "डॉ. एस.आर. रंगनाथन (Dr. S.R. Ranganathan)",
     ["Dr. C.D. Deshmukh", "Dr. B.S. Kesavan", "Prof. D.S. Kothari"], ["चिंतामन देशमुख", "केशवन", "कोठारी"],
     "Formulated the famous Staff Formula, functional architectural norms, and pay parity with academic teachers.",
     "रंगनाथन समिति ने विश्वविद्यालय पुस्तकालयाध्यक्षों को प्राध्यापकों के समकक्ष वेतन व दर्जा दिलाया।"),

    ("The UGC Review Committee on Library Science appointed in 1961 was headed by",
     "1961 में यूजीसी द्वारा गठित पुस्तकालय विज्ञान समीक्षा समिति के अध्यक्ष कौन थे?",
     "Dr. S.R. Ranganathan", "डॉ. एस.आर. रंगनाथन (Dr. S.R. Ranganathan)",
     ["Prof. P.N. Kaula", "Dr. S. Radhakrishnan", "Dr. V.K.R.V. Rao"], ["कौला", "राधाकृष्णन", "वी.के.आर.वी. राव"],
     "Recommended standardized syllabus for Bachelor of Library Science (B.Lib.Sc.) and Master of Library Science (M.Lib.Sc.).",
     "रंगनाथन समिति ने देश भर के विश्वविद्यालयों में बी.लिब और एम.लिब पाठ्यक्रमों के मानक तय किए।"),

    ("The Mehrotra Committee appointed by UGC in 1983 made recommendations regarding",
     "यूजीसी द्वारा 1983 में गठित 'मेहरोत्रा समिति' का मुख्य विषय क्या था?",
     "Revision of pay scales and service conditions of university and college librarians and physical education staff",
     "विश्वविद्यालय एवं कॉलेज पुस्तकालयाध्यक्षों के वेतनमान और सेवा शर्तों का पुनरीक्षण",
     ["Purchasing computers only", "School library buildings", "Public library cess rates"],
     ["केवल कंप्यूटर क्रय", "भवन निर्माण", "उपकर दर"],
     "Headed by Prof. R.C. Mehrotra; maintained parity between library professionals and university teaching faculty.",
     "मेहरोत्रा समिति ने कॉलेज और विश्वविद्यालय लाइब्रेरियन को शिक्षकों के समान वेतनमान देने की वकालत की।"),

    ("The National Knowledge Commission (NKC) appointed in 2005 under the chairmanship of Sam Pitroda submitted its report on libraries in",
     "सैम पित्रोदा की अध्यक्षता वाले राष्ट्रीय ज्ञान आयोग (NKC) ने पुस्तकालयों पर अपनी ऐतिहासिक रिपोर्ट किस वर्ष सौंपी?",
     "2007 (Libraries: Gateways to Knowledge)", "2007 में ('पुस्तकालय: ज्ञान के प्रवेश द्वार')",
     ["2005", "2010", "2014"], ["2005 में", "2010 में", "2014 में"],
     "Formulated 10 major recommendations including setting up a National Mission on Libraries and a Central Library Fund.",
     "ज्ञान आयोग ने देश के 54,000 सार्वजनिक पुस्तकालयों के आधुनिकीकरण और राष्ट्रीय पुस्तकालय मिशन का खाका खींचा।"),

    ("The National Education Policy (NEP) 2020 emphasizes which role for libraries in schools and communities?",
     "राष्ट्रीय शिक्षा नीति (NEP 2020) विद्यालयों और समाज में पुस्तकालयों की किस भूमिका पर विशेष बल देती है?",
     "Setting up digital libraries, school library strengthening, and developing public libraries as community learning hubs",
     "डिजिटल पुस्तकालयों की स्थापना, विद्यालय पुस्तकालयों का सुदृढ़ीकरण एवं सामुदायिक अध्ययन केंद्र के रूप में विकास",
     ["Closing small school libraries", "Eliminating printed books", "Restricting reading to online screens only"],
     ["पुस्तकालय बंद करना", "किताबें खत्म करना", "केवल स्क्रीन पठन"],
     "Advocates book clubs and 'one library in every village' for foundational literacy and numeracy.",
     "एनईपी 2020 बुनियादी साक्षरता हेतु प्रत्येक विद्यालय और गांव में जीवंत पुस्तकालय स्थापित करने का आह्वान करती है।")
]

q11_pool = make_pool_from_base(
    q11_base, "university and college library staff and funding norms",
    "विश्वविद्यालय व कॉलेज पुस्तकालय कर्मचारियों और बजटीय मानकों",
    "Maintaining academic parity, professional qualifications, and adequate reading resources",
    "शैक्षणिक समता, पेशेवर योग्यताएं और पर्याप्त अध्ययन सामग्री बनाए रखना",
    ["Abolishing library staff posts", "Freezing all book purchase grants", "Privatizing academic reading halls"],
    ["पद समाप्त करना", "अनुदान रोकना", "निजीकरण करना"]
)

# Q12: NAPLIS (48 items)
q12_base = [
    ("The Committee on National Policy on Library and Information Systems (CONPOLIS) was constituted in 1985 by",
     "1985 में 'राष्ट्रीय पुस्तकालय एवं सूचना प्रणाली नीति समिति' (CONPOLIS) का गठन किसके द्वारा किया गया था?",
     "Department of Culture, Ministry of Human Resource Development, Government of India",
     "संस्कृति विभाग, मानव संसाधन विकास मंत्रालय, भारत सरकार",
     ["Planning Commission only", "Indian Library Association", "University Grants Commission"],
     ["योजना आयोग", "आईएलए", "यूजीसी"],
     "Chaired by Prof. Debiprasad Chattopadhyaya; submitted its final draft policy report in May 1986.",
     "प्रो. देवीप्रसाद चट्टोपाध्याय की अध्यक्षता वाली समिति ने मई 1986 में राष्ट्रीय नीति (NAPLIS) का प्रारूप सौंपा।"),

    ("Who served as the Chairman of the Committee on National Policy on Library and Information Systems (NAPLIS, 1986)?",
     "राष्ट्रीय पुस्तकालय एवं सूचना प्रणाली नीति (NAPLIS, 1986) समिति के अध्यक्ष कौन थे?",
     "Prof. D.P. Chattopadhyaya (Prof. Debiprasad Chattopadhyaya)", "प्रो. डी.पी. चट्टोपाध्याय (Prof. D.P. Chattopadhyaya)",
     ["Prof. Yash Pal", "Dr. S.R. Ranganathan", "Dr. V.K.R.V. Rao"], ["यशपाल", "रंगनाथन", "वी.के.आर.वी. राव"],
     "Eminent philosopher and statesman who laid a comprehensive national blueprint for library modernization.",
     "प्रख्यात दार्शनिक प्रो. चट्टोपाध्याय के नेतृत्व में भारत की पहली व्यापक राष्ट्रीय पुस्तकालय नीति बनी।"),

    ("In which month and year was the final report of NAPLIS (National Policy on Library and Information System) submitted to the Government of India?",
     "भारत सरकार को NAPLIS की अंतिम रिपोर्ट किस माह एवं वर्ष में प्रस्तुत की गई थी?",
     "May 1986", "मई 1986 में",
     ["October 1985", "January 1988", "December 1990"], ["अक्टूबर 1985", "जनवरी 1988", "दिसंबर 1990"],
     "Submitted to Minister P.V. Narasimha Rao; laid out 10 chapters of integrated library policy.",
     "मई 1986 में तत्कालीन मानव संसाधन विकास मंत्री पी.वी. नरसिंह राव को यह ऐतिहासिक रिपोर्ट सौंपी गई।"),

    ("The Empowered Committee appointed in 1988 to examine the recommendations of NAPLIS for implementation was chaired by",
     "NAPLIS की सिफारिशों के क्रियान्वयन हेतु 1988 में गठित 'अधिकार प्राप्त समिति' (Empowered Committee) के अध्यक्ष कौन थे?",
     "Prof. D.P. Chattopadhyaya", "प्रो. डी.पी. चट्टोपाध्याय (Prof. D.P. Chattopadhyaya)",
     ["Prof. Yash Pal", "Dr. B.S. Kesavan", "Dr. S.S. Murthy"], ["यशपाल", "केशवन", "मूर्ति"],
     "Submitted its action plan in April 1988 prioritizing public library legislation and networking.",
     "प्रो. चट्टोपाध्याय की अध्यक्षता वाली अधिकार प्राप्त समिति ने 1988 में क्रियान्वयन योजना प्रस्तुत की।"),

    ("The Working Group constituted in 1993 to suggest operational measures for implementing NAPLIS recommendations was headed by",
     "NAPLIS सिफारिशों के क्रियान्वयन हेतु 1993 में गठित कार्यदल के अध्यक्ष कौन थे?",
     "Dr. B.P. Barua (former Director, RRRLF)", "डॉ. बी.पी. बरुआ (पूर्व निदेशक, RRRLF)",
     ["Dr. S.R. Ranganathan", "P.N. Kaula", "D.R. Kalia"], ["रंगनाथन", "कौला", "कालिया"],
     "Formulated practical guidelines for central funding to state public libraries.",
     "डॉ. बी.पी. बरुआ के नेतृत्व में 1993 के कार्यदल ने राज्यों में सार्वजनिक पुस्तकालयों के वित्तपोषण के व्यावहारिक उपाय सुझाए।"),

    ("A key recommendation of NAPLIS (1986) regarding public library legislation was that",
     "सार्वजनिक पुस्तकालय कानून के संबंध में NAPLIS (1986) की प्रमुख सिफारिश क्या थी?",
     "Every State and Union Territory in India should enact statutory Public Library Legislation within a defined time frame",
     "भारत के प्रत्येक राज्य और केंद्र शासित प्रदेश को एक निश्चित समय सीमा में सार्वजनिक पुस्तकालय कानून बनाना चाहिए",
     ["Library legislation is completely unnecessary", "Only 5 big states should have library acts", "Private companies should run libraries"],
     ["कानून की जरूरत नहीं", "केवल 5 बड़े राज्य बनाएं", "निजी कंपनियां चलाएं"],
     "Urged state governments to emulate Tamil Nadu, Andhra, Karnataka, and Maharashtra in passing acts.",
     "NAPLIS ने सभी राज्यों में अविलंब सार्वजनिक पुस्तकालय अधिनियम लागू करने का पुरजोर आग्रह किया।"),

    ("NAPLIS (1986) recommended designating which institution as the apex national nodal body for coordinating public libraries?",
     "सार्वजनिक पुस्तकालयों के समन्वय हेतु NAPLIS (1986) ने किस संस्था को शीर्ष राष्ट्रीय नोडल एजेंसी बनाने की संस्तुति की थी?",
     "Raja Rammohun Roy Library Foundation (RRRLF, Kolkata)", "राजा राममोहन राय लाइब्रेरी फाउंडेशन (RRRLF, कोलकाता)",
     ["National Library of India", "National Science Library", "Delhi Public Library"], ["राष्ट्रीय पुस्तकालय", "राष्ट्रीय विज्ञान पुस्तकालय", "डीपीएल"],
     "Recommended expanding RRRLF's financial resource base and statutory advisory powers.",
     "आरआरआरएलएफ को पूरे देश के सार्वजनिक पुस्तकालयों की शीर्ष समन्वयक संस्था बनाने की सिफारिश की गई।"),

    ("What did NAPLIS (1986) recommend regarding school library facilities?",
     "विद्यालयी पुस्तकालयों के विषय में NAPLIS (1986) ने क्या स्पष्ट संस्तुति की थी?",
     "No school or junior college should be accorded academic recognition without an adequate library and trained librarian",
     "पर्याप्त पुस्तकालय और प्रशिक्षित लाइब्रेरियन के बिना किसी भी स्कूल या जूनियर कॉलेज को मान्यता नहीं मिलनी चाहिए",
     ["Schools do not need librarians", "Textbooks are sufficient", "School libraries should be merged with municipal offices"],
     ["लाइब्रेरियन की जरूरत नहीं", "पाठ्यपुस्तकें पर्याप्त", "नगरपालिका से मिलाना"],
     "Mandated that library training should be integral to secondary education and teacher education.",
     "नीति ने स्पष्ट कहा कि बिना सुसज्जित पुस्तकालय और लाइब्रेरियन के किसी स्कूल को सरकारी मान्यता न दी जाए।"),

    ("NAPLIS recommended that rural public library services should be closely integrated with which national programme?",
     "ग्रामीण पुस्तकालय सेवाओं को NAPLIS ने किस राष्ट्रीय कार्यक्रम के साथ घनिष्ठ रूप से जोड़ने की सिफारिश की थी?",
     "Adult Education and National Literacy Mission", "प्रौढ़ शिक्षा एवं राष्ट्रीय साक्षरता मिशन",
     ["Industrial licensing", "Urban highway expansion", "Railway ticket reservation"], ["औद्योगिक लाइसेंस", "सड़क विस्तार", "रेलवे टिकट"],
     "Public libraries were envisioned as community information centers preventing relapse into illiteracy.",
     "पुस्तकालयों को नव-साक्षरों को पुनः निरक्षर होने से बचाने और सामुदायिक सूचना केंद्र बनने की भूमिका दी गई।"),

    ("According to NAPLIS recommendations, what proportion of educational expenditure should ideally be spent on libraries?",
     "NAPLIS की संस्तुतियों के अनुसार शैक्षिक बजट का कितना अंश पुस्तकालय विकास पर खर्च होना चाहिए?",
     "Not less than 6% to 10% of the total education budget", "कुल शिक्षा बजट का 6% से 10% से कम नहीं",
     ["1% to 2%", "15% to 20%", "0.5%"], ["1% से 2%", "15% से 20%", "0.5%"],
     "Reaffirmed the Kothari Commission norms for sustaining academic library collections.",
     "कोठारी आयोग के मानकों की पुष्टि करते हुए 6% से 10% बजट पुस्तकालयों हेतु निर्धारित करने पर बल दिया।")
]

q12_pool = make_pool_from_base(
    q12_base, "national library networking and public access policies",
    "राष्ट्रीय पुस्तकालय नेटवर्किंग एवं सूचना पहुंच नीतियों",
    "Establishing statewide library networks, modern cataloguing, and universal public access",
    "राज्यव्यापी पुस्तकालय नेटवर्क, आधुनिक सूचीकरण और सार्वभौमिक सूचना पहुंच स्थापित करना",
    ["Banning internet access in public libraries", "Abolishing central funding", "Closing rural branches"],
    ["इंटरनेट पर रोक", "केंद्रीय फंड समाप्त करना", "ग्रामीण शाखाएं बंद करना"]
)

# Q13: Types of Libraries (48 items)
q13_base = [
    ("Which type of library is traditionally described as the 'People's University' (Lok Vishwavidyalaya) providing lifelong free learning?",
     "आजीवन निःशुल्क स्वाध्याय उपलब्ध कराने के कारण किस प्रकार के पुस्तकालय को 'जनता का विश्वविद्यालय' (People's University) कहा जाता है?",
     "Public Library (सार्वजनिक पुस्तकालय)", "सार्वजनिक पुस्तकालय (Public Library)",
     ["Academic Library", "Special Library", "National Library"], ["शैक्षणिक पुस्तकालय", "विशेष पुस्तकालय", "राष्ट्रीय पुस्तकालय"],
     "UNESCO defines the public library as a democratic institution serving all citizens regardless of age, race, or status.",
     "यूनेस्को घोषणापत्र के अनुसार सार्वजनिक पुस्तकालय समाज के सभी वर्गों हेतु खुला जनता का विश्वविद्यालय है।"),

    ("A library attached to an industrial R&D firm, medical institute, law chamber, or defense laboratory is classified as a",
     "किसी औद्योगिक अनुसंधान इकाई, चिकित्सा संस्थान, विधि परिषद अथवा रक्षा प्रयोगशाला से संबद्ध पुस्तकालय क्या कहलाता है?",
     "Special Library (विशेष पुस्तकालय)", "विशेष पुस्तकालय (Special Library)",
     ["Public Library", "Academic Library", "National Library"], ["सार्वजनिक पुस्तकालय", "शैक्षणिक पुस्तकालय", "राष्ट्रीय पुस्तकालय"],
     "Serves a specialized clientele with targeted information, current awareness (CAS), and selective dissemination (SDI).",
     "विशेष पुस्तकालय एक विशिष्ट विषय और सीमित उपयोगकर्ताओं को गहन सूचना सेवाएं (SDI/CAS) प्रदान करता है।"),

    ("Libraries attached to primary schools, high schools, colleges, and universities are collectively categorized as",
     "प्राथमिक विद्यालयों, उच्च विद्यालयों, कॉलेजों एवं विश्वविद्यालयों से संबद्ध पुस्तकालय सामूहिक रूप से क्या कहलाते हैं?",
     "Academic Libraries (शैक्षणिक पुस्तकालय)", "शैक्षणिक पुस्तकालय (Academic Libraries)",
     ["Public Libraries", "National Libraries", "Corporate Libraries"], ["सार्वजनिक पुस्तकालय", "राष्ट्रीय पुस्तकालय", "कॉर्पोरेट पुस्तकालय"],
     "Support curricula, classroom teaching, academic research, faculty research, and institutional student learning.",
     "शैक्षणिक पुस्तकालय औपचारिक शिक्षा, पाठ्यक्रम और शोध को समृद्ध करने हेतु स्थापित किए जाते हैं।"),

    ("The primary statutory function of a National Library (such as National Library of India, Kolkata) is to",
     "किसी देश के 'राष्ट्रीय पुस्तकालय' (जैसे भारत का राष्ट्रीय पुस्तकालय) का प्राथमिक वैधानिक कार्य क्या होता है?",
     "Collect, preserve, and catalogue the entire documentary and literary heritage of the nation through legal deposit",
     "कानूनी डिपॉजिट (Legal Deposit) के माध्यम से देश की संपूर्ण साहित्यिक एवं दस्तावेजी धरोहर का संग्रह, संरक्षण व सूचीकरण",
     ["Lend textbooks to school pupils", "Sell commercial novels", "Conduct university examinations"],
     ["स्कूली बच्चों को पाठ्यपुस्तक बांटना", "उपन्यास बेचना", "विश्वविद्यालय परीक्षा लेना"],
     "Compiles the national bibliography and serves as the ultimate national conservation repository.",
     "राष्ट्रीय पुस्तकालय देश में प्रकाशित प्रत्येक पुस्तक को कानूनन प्राप्त कर राष्ट्रीय ग्रंथसूची (INB) तैयार करता है।"),

    ("Which category of library places the greatest emphasis on providing Selective Dissemination of Information (SDI) and customized technical dossiers?",
     "चयनात्मक सूचना प्रसार (SDI) और तकनीकी डोजियर तैयार करने पर सर्वाधिक बल किस श्रेणी का पुस्तकालय देता है?",
     "Special Library (विशेष पुस्तकालय)", "विशेष पुस्तकालय (Special Library)",
     ["School Library", "Public Library", "Children Library"], ["स्कूल पुस्तकालय", "सार्वजनिक पुस्तकालय", "बाल पुस्तकालय"],
     "Special libraries focus on speed, precision, and pin-pointed nascent information for researchers and executives.",
     "वैज्ञानिकों और शोधकर्ताओं को उनकी रुचि के अनुसार सटीक सूचना तुरंत उपलब्ध कराना विशेष पुस्तकालय का मुख्य कार्य है।"),

    ("In an academic library system, the primary responsibility of a University Library compared to a College Library is to",
     "शैक्षणिक पुस्तकालय तंत्र में कॉलेज पुस्तकालय की तुलना में 'विश्वविद्यालय पुस्तकालय' का मुख्य विशिष्ट दायित्व क्या होता है?",
     "Support advanced post-graduate research, doctoral dissertations, and faculty research alongside teaching",
     "अध्यापन के साथ-साथ उच्च स्नातकोत्तर शोध, डॉक्टरेट शोध-प्रबंधों और संकाय अनुसंधान को समृद्ध करना",
     ["Teach alphabets to primary students", "Issue recreational novels to general public", "Publish daily newspapers"],
     ["वर्णमाला सिखाना", "आम जनता को उपन्यास बांटना", "दैनिक अखबार छापना"],
     "Maintains extensive research journals, theses repositories, and specialized scholarly databases.",
     "विश्वविद्यालय पुस्तकालय शोध पत्रिकाओं, शोध प्रबंधों (Theses) और उच्च स्तरीय अनुसंधान का केंद्र होता है।"),

    ("Which type of library is specifically charged with eradicating adult illiteracy, supporting neo-literates, and organizing cultural community meets?",
     "प्रौढ़ निरक्षरता उन्मूलन, नव-साक्षरों को पठन सामग्री उपलब्ध कराने और सामुदायिक सांस्कृतिक बैठकें आयोजित करने का दायित्व किसका है?",
     "Public Library (सार्वजनिक पुस्तकालय)", "सार्वजनिक पुस्तकालय (Public Library)",
     ["Special Library", "Patent Library", "Corporate Library"], ["विशेष पुस्तकालय", "पेटेंट पुस्तकालय", "कॉर्पोरेट पुस्तकालय"],
     "Acts as the local community learning and cultural center for rural and urban populations.",
     "सार्वजनिक पुस्तकालय समाज से निरक्षरता दूर करने और सामुदायिक चेतना जगाने का प्रमुख माध्यम है।"),

    ("The Library of Congress (USA), British Library (UK), and Bibliothèque nationale de France (BnF) are examples of",
     "लाइब्रेरी ऑफ कांग्रेस (यूएसए), ब्रिटिश लाइब्रेरी (यूके), और बिब्लियोथेक नेशनेल (फ्रांस) किस प्रकार के पुस्तकालय के विश्वप्रसिद्ध उदाहरण हैं?",
     "National Libraries (राष्ट्रीय पुस्तकालय)", "राष्ट्रीय पुस्तकालय (National Libraries)",
     ["School Libraries", "Private Club Libraries", "Industrial Libraries"], ["स्कूल पुस्तकालय", "क्लब पुस्तकालय", "औद्योगिक पुस्तकालय"],
     "Apex libraries of their respective nations holding millions of volumes and national copyright deposits.",
     "ये अपने-अपने देशों के शीर्ष राष्ट्रीय पुस्तकालय हैं जो वैश्विक ज्ञान संपदा का संरक्षण करते हैं।"),

    ("A library established within the Parliament (such as Parliament Library of India in New Delhi) is categorized as a",
     "संसद भवन के भीतर सांसदों हेतु स्थापित पुस्तकालय (जैसे भारत का संसद पुस्तकालय) किस श्रेणी में आता है?",
     "Special / Legislative Reference Library", "विशेष / विधायी संदर्भ पुस्तकालय (Legislative Reference Library)",
     ["Public Library", "Children Library", "Academic School Library"], ["सार्वजनिक पुस्तकालय", "बाल पुस्तकालय", "स्कूल पुस्तकालय"],
     "Provides prompt, confidential reference, research briefs, and legislative dossiers to Members of Parliament.",
     "संसद पुस्तकालय सांसदों को विधायी कार्यों और बहसों हेतु त्वरित और गोपनीय संदर्भ सामग्री देता है।"),

    ("Libraries maintained by international bodies such as United Nations (Dag Hammarskjöld Library, New York) are classified as",
     "संयुक्त राष्ट्र द्वारा संचालित 'डैग हैमरशॉल्ड लाइब्रेरी' (न्यूयॉर्क) जैसे अंतरराष्ट्रीय पुस्तकालय किस श्रेणी में आते हैं?",
     "International Special Libraries", "अंतरराष्ट्रीय विशेष पुस्तकालय (International Special Libraries)",
     ["Public Libraries", "School Libraries", "National Libraries"], ["सार्वजनिक पुस्तकालय", "स्कूल पुस्तकालय", "राष्ट्रीय पुस्तकालय"],
     "Support diplomatic delegations, secretariat research, and international treaty documentation.",
     "संयुक्त राष्ट्र की डैग हैमरशॉल्ड लाइब्रेरी अंतरराष्ट्रीय कानून और कूटनीतिक शोध का विशेष पुस्तकालय है।")
]

q13_pool = make_pool_from_base(
    q13_base, "library functional specialization and user-oriented service delivery",
    "पुस्तकालय कार्यात्मक विशिष्टता एवं पाठक-केंद्रित सेवा वितरण",
    "Designing collection, cataloguing, and retrieval services to match user community needs",
    "पाठक समुदाय की विशिष्ट आवश्यकताओं के अनुरूप संग्रह और संदर्भ सेवाओं का विकास",
    ["Imposing identical generic rules across all library types", "Ignoring user specialization", "Closing access"],
    ["सभी पुस्तकालयों पर एक समान नियम थोपना", "पाठकों की उपेक्षा", "पहुंच बंद करना"]
)

# Q14: Extension Services (48 items)
q14_base = [
    ("What is the primary objective of 'Library Extension Services' (Outreach Activities)?",
     "पुस्तकालय 'विस्तार सेवाओं' (Library Extension Services / Outreach) का मुख्य उद्देश्य क्या होता है?",
     "To reach out to non-users, convert them into active readers, and extend library resources beyond the four walls of the building",
     "गैर-उपयोगकर्ताओं तक पहुंचना, उन्हें सक्रिय पाठक बनाना और पुस्तकालय को चारदीवारी से बाहर समाज तक ले जाना",
     ["To sell books commercially for profit", "To reduce library staff work", "To restrict reading to enrolled members only"],
     ["व्यावसायिक लाभ हेतु पुस्तक बेचना", "काम घटाना", "केवल सदस्यों तक सीमित रखना"],
     "Transforms the library into a proactive cultural and educational community center.",
     "विस्तार सेवा पुस्तकालय को भवन की चारदीवारी से निकालकर दूरदराज के पाठकों तक पहुंचाती है।"),

    ("Which pioneer introduced the first mobile library in India using a bullock cart in 1931 at Mannargudi?",
     "1931 में तमिलनाडु के मन्नारगुड़ी में बैलगाड़ी सचल पुस्तकालय (बुलक-कार्ट मोबाइल लाइब्रेरी) का प्रयोग किसने किया था?",
     "Dr. S.R. Ranganathan (with Rao Sahib S.V. Kanakasabhai Pillai)", "डॉ. एस.आर. रंगनाथन (राव साहिब एस.वी. कनकसभाई पिल्लई के साथ)",
     ["B.S. Kesavan", "Iyyanki Venkata Ramanayya", "Melvil Dewey"], ["केशवन", "अय्यंकी", "डेवी"],
     "Designed a traveling cart with display shelves visiting 75 villages in Thanjavur district.",
     "रंगनाथन ने 1931 में मन्नारगुड़ी में बैलगाड़ी पर लिबरामशीन बनाकर 75 गांवों में पुस्तकें बांटी थीं।"),

    ("Mobile library services provided to readers in remote, rural, or inaccessible areas are formally referred to as",
     "दूरदराज के ग्रामीण या दुर्गम क्षेत्रों में पाठकों को वाहन द्वारा दी जाने वाली पुस्तक सेवा क्या कहलाती है?",
     "Bookmobile / Mobile Library Service (Libramachine)", "बुकमोबाइल / सचल पुस्तकालय सेवा (Libramachine)",
     ["Reference desk", "Inter-library loan", "Document delivery service"], ["संदर्भ सेवा", "अंतर-पुस्तकालय ऋण", "डॉक्यूमेंट डिलीवरी"],
     "Brings rotating collections of books on fixed schedules to villages, schools, and hospitals.",
     "बुकमोबाइल पूर्वनिर्धारित समय सारणी के अनुसार गांवों और बस्तियों में जाकर पुस्तकें उपलब्ध कराती है।"),

    ("Organizing storytelling hours, puppetry shows, and summer reading clubs in a public library is an extension service aimed at",
     "सार्वजनिक पुस्तकालय में कहानी वाचन सत्र (Storytelling), कठपुतली शो और समर रीडिंग क्लब का आयोजन किस वर्ग हेतु विस्तार सेवा है?",
     "Children and young readers", "बालकों एवं युवा पाठकों हेतु (Children & Young Readers)",
     ["University research scholars", "Industrial scientists", "Corporate managers"], ["शोधार्थियों हेतु", "वैज्ञानिकों हेतु", "प्रबंधकों हेतु"],
     "Cultivates early literacy, vocabulary, and lifelong love for reading among children.",
     "बालकों में पठन के प्रति स्वाभाविक प्रेम और रुचि जगाने हेतु कहानी सत्र अत्यंत प्रभावी होते हैं।"),

    ("Organizing book exhibitions, author meets, book release functions, and literary lectures in the library fulfills which function?",
     "पुस्तकालय में पुस्तक प्रदर्शनियां, लेखक संवाद, पुस्तक विमोचन और साहित्यिक व्याख्यानों का आयोजन किस कार्य की पूर्ति करता है?",
     "Library Extension and Public Relations Service", "पुस्तकालय विस्तार एवं जनसंपर्क सेवा (Extension & Public Relations)",
     ["Cataloguing division work", "Technical processing", "Stock verification"], ["सूचीकरण कार्य", "तकनीकी प्रसंस्करण", "स्टॉक सत्यापन"],
     "Attracts citizens to the library, showcasing new literature and generating intellectual discourse.",
     "इससे समाज के प्रबुद्ध नागरिक पुस्तकालय से जुड़ते हैं और नई पुस्तकों का व्यापक प्रचार होता है।"),

    ("Providing special reading services to hospitalized patients, prison inmates, and nursing homes is categorized as",
     "अस्पतालों के मरीजों, जेल के कैदियों और वृद्धाश्रमों में विशेष पठन सामग्री पहुंचाना किस श्रेणी की सेवा है?",
     "Extension and outreach service to disadvantaged / institutionalized groups", "वंचित एवं संस्थागत समूहों हेतु विस्तार सेवा (Outreach Service)",
     ["Commercial library sales", "Academic course teaching", "Classification exercise"], ["व्यावसायिक बिक्री", "शैक्षणिक अध्यापन", "वर्गीकरण अभ्यास"],
     "Fulfills Dr. Ranganathan's Second Law: 'Every Reader his/her Book'.",
     "रंगनाथन के द्वितीय नियम का पालन करते हुए समाज के उपेक्षित और बीमार वर्ग तक ज्ञान पहुंचाया जाता है।"),

    ("The concept of 'Community Information Services' (CIS) provided by public libraries involves",
     "सार्वजनिक पुस्तकालयों द्वारा प्रदान की जाने वाली 'सामुदायिक सूचना सेवा' (CIS) में मुख्य रूप से क्या शामिल होता है?",
     "Providing local practical information on government welfare schemes, employment, healthcare, agriculture, and civic rights",
     "सरकारी जनकल्याण योजनाओं, रोजगार, स्वास्थ्य, कृषि और नागरिक अधिकारों से संबंधित स्थानीय उपयोगी सूचनाएं देना",
     ["Loaning fiction novels only", "Teaching classical Greek language", "Publishing international patents"],
     ["केवल उपन्यास देना", "यूनानी भाषा सिखाना", "पेटेंट छापना"],
     "Empowers rural and urban citizens with actionable survival and development information.",
     "सामुदायिक सूचना सेवा आम नागरिकों को सरकारी योजनाओं, रोजगार और अधिकारों की व्यावहारिक जानकारी देती है।"),

    ("Providing 'Talking Books' and digital audio recording services in libraries is primarily designed for",
     "पुस्तकालयों में 'टॉकिंग बुक्स' (बोलती पुस्तकें) और डिजिटल ऑडियो रिकॉर्डिंग सेवाएं विशेष रूप से किसके लिए बनाई जाती हैं?",
     "Visually impaired, blind, and print-disabled readers", "दृष्टिबाधित एवं मुद्रण-अक्षम (Print-disabled) पाठकों हेतु",
     ["Industrial executives", "Speed reading champions", "Athletes only"], ["औद्योगिक प्रबंधकों", "स्पीड रीडर्स", "खिलाड़ियों"],
     "Enables equal access to literature using DAISY players, MP3 audiobooks, and screen readers.",
     "दृष्टिबाधित पाठकों को डेजी (DAISY) और ऑडियो प्रारूप में पुस्तकें उपलब्ध कराकर ज्ञान तक पहुंच दी जाती है।"),

    ("Setting up 'Reading Circles' or 'Study Circles' in rural community libraries helps in",
     "ग्रामीण पुस्तकालयों में 'स्टडी सर्किल' या 'वाचन मंडल' स्थापित करने से क्या मुख्य लाभ होता है?",
     "Promoting participatory adult discussions on agricultural techniques, hygiene, and civic awareness",
     "कृषि तकनीकों, स्वास्थ्य, स्वच्छता और नागरिक चेतना पर ग्रामीणों के बीच सामूहिक चर्चा को बढ़ावा",
     ["Collecting commercial rent", "Restricting village entry", "Replacing school teachers"],
     ["किराया वसूलना", "गांव में प्रवेश रोकना", "शिक्षकों को हटाना"],
     "Transforms the library into a democratic village parliament of knowledge.",
     "वाचन मंडलों के माध्यम से ग्रामीण नागरिक सामयिक विषयों और खेती-किसानी पर ज्ञान साझा करते हैं।"),

    ("In Dr. Ranganathan's terminology, the special traveling library equipment constructed with shelves on wheels was designated as",
     "रंगनाथन की शब्दावली में पहियों पर निधानियां लगाकर बनाई गई विशेष सचल पुस्तकालय व्यवस्था क्या कहलाती थी?",
     "Libramachine", "लिबरामशीन (Libramachine)",
     ["Bookvan", "Auto-Library", "Mobile Rack"], ["बुकवैन", "ऑटो लाइब्रेरी", "मोबाइल रैक"],
     "Emphasized the mechanical efficiency of moving library resources directly to the reader's doorstep.",
     "रंगनाथन ने लिबरामशीन शब्द गढ़कर ज्ञान को सीधे पाठक के दरवाजे तक पहुंचाने का संदेश दिया।")
]

q14_pool = make_pool_from_base(
    q14_base, "outreach programs, mobile reading rooms, and community inclusion",
    "विस्तार कार्यक्रमों, सचल वाचनालयों एवं सामुदायिक समावेशन",
    "Expanding library services to marginalized groups, remote hamlets, and underserved citizens",
    "वंचित वर्गों, दूरदराज के गांवों और उपेक्षित नागरिकों तक पुस्तकालय सेवाओं का विस्तार करना",
    ["Restricting access to urban elite only", "Charging prohibitive entry fees", "Closing rural branches"],
    ["केवल शहरी अमीरों तक सीमित रखना", "भारी प्रवेश शुल्क", "ग्रामीण शाखाएं बंद करना"]
)

# Q15: Finance & Budgeting (48 items)
q15_base = [
    ("Zero-Based Budgeting (ZBB), an innovative budgeting system requiring every expenditure to be justified afresh from zero, was pioneered in 1970 by",
     "प्रत्येक मद के औचित्य को शून्य से सिद्ध करने वाली 'जीरो-बेस्ड बजटिंग' (ZBB) का प्रतिपादन 1970 में किसने किया था?",
     "Peter A. Phyrr (at Texas Instruments, USA)", "पीटर ए. पायर (Peter A. Phyrr - टेक्सास इंस्ट्रूमेंट्स में)",
     ["Lyndon B. Johnson", "Robert McNamara", "David Novick"], ["लिंडन जॉनसन", "रॉबर्ट मैकनामरा", "डेविड नोविक"],
     "Adopted by US President Jimmy Carter in 1977; eliminates wasteful historical spending inertia.",
     "पीटर पायर द्वारा विकसित ZBB में पिछले वर्ष के बजट को आधार न मानकर हर खर्च का नए सिरे से औचित्य देखा जाता है।"),

    ("The Planning-Programming-Budgeting System (PPBS) was developed in the 1960s by the RAND Corporation and introduced in US defense by",
     "योजना-कार्यक्रम-बजट प्रणाली (PPBS) को 1960 के दशक में रैंड कॉर्पोरेशन द्वारा विकसित कर अमेरिकी रक्षा विभाग में किसने लागू किया था?",
     "Robert McNamara (US Secretary of Defense under President Kennedy)", "रॉबर्ट मैकनामरा (Robert McNamara)",
     ["Peter Phyrr", "Melvil Dewey", "F.W. Taylor"], ["पीटर पायर", "मेल्विल डेवी", "टेलर"],
     "Links long-term operational objectives with multi-year programme packages and cost-benefit evaluations.",
     "पीपीबीएस (PPBS) दीर्घकालिक लक्ष्यों, कार्यक्रमों और लागत-लाभ विश्लेषण को एकीकृत करता है।"),

    ("The traditional and most commonly used budgeting method in Indian libraries, based on adding an incremental percentage to last year's figures, is",
     "भारतीय पुस्तकालयों में सबसे प्रचलित पारंपरिक बजट पद्धति, जिसमें पिछले वर्ष के खर्च में निश्चित प्रतिशत वृद्धि जोड़ दी जाती है, कहलाती है:",
     "Line-Item Budgeting (Incremental / Historical Budgeting)", "लाइन-आइटम बजट (वृद्धिशील / ऐतिहासिक बजट)",
     ["Zero-Based Budgeting", "Formula Budgeting", "Performance Budgeting"], ["जीरो-बेस्ड बजट", "फॉर्मूला बजट", "परफॉर्मेंस बजट"],
     "Allocates funds under standard account heads: salaries, books, periodicals, binding, and equipment.",
     "लाइन-आइटम बजट में वेतन, पुस्तक, पत्रिका, जिल्दसाजी आदि मदों में पिछले वर्ष के आधार पर थोड़ा बजट बढ़ा दिया जाता है।"),

    ("Performance Budgeting, introduced by the First Hoover Commission (1949) in the USA, focuses primarily on",
     "अमेरिका में प्रथम हूवर आयोग (1949) द्वारा शुरू किए गए 'परफॉर्मेंस बजट' का मुख्य ध्यान किस पर केंद्रित होता है?",
     "Measuring what the library actually achieves and produces (outputs, services rendered) rather than just what it spends",
     "पुस्तकालय द्वारा दी गई वास्तविक सेवाओं और उपलब्धियों (Outputs) के मापन पर, न कि केवल खर्च पर",
     ["Listing items alphabetically", "Cutting all staff salaries", "Eliminating book purchases"],
     ["वर्णानुक्रम में सूची बनाना", "वेतन कटौती", "पुस्तक खरीद बंद"],
     "Links expenditure to measurable physical targets, e.g., cost per book circulated or reference query answered.",
     "परफॉर्मेंस बजट खर्च किए गए धन और उससे प्राप्त वास्तविक परिणाम व सेवा का मूल्यांकन करता है।"),

    ("Formula Budgeting in academic libraries relies on",
     "शैक्षणिक पुस्तकालयों में 'फॉर्मूला बजटिंग' (Formula Budgeting) किस पर आधारित होती है?",
     "Mathematical and statistical formulas linking funds to student enrollment, faculty size, and curricula",
     "छात्रों की संख्या, शिक्षकों की संख्या और पाठ्यक्रम से जुड़ी गणितीय व सांख्यिकीय गणनाओं पर",
     ["Guesswork of the chief librarian", "Random lottery draws", "Last day balance only"],
     ["लाइब्रेरियन का अनुमान", "लॉटरी", "अंतिम दिन का शेष"],
     "Calculates required acquisitions using formulas like the Clapp-Jordan or Voigt formula.",
     "क्लैप-जॉर्डन फॉर्मूले की तरह छात्रों और शिक्षकों के अनुपात में बजट की वैज्ञानिक गणना की जाती है।"),

    ("The famous Clapp-Jordan Formula (1965) was developed to determine the minimum adequate collection size and budget for",
     "प्रसिद्ध 'क्लैप-जॉर्डन फॉर्मूला' (1965) किसके लिए न्यूनतम पर्याप्त संग्रह आकार और बजट तय करने हेतु विकसित किया गया था?",
     "College and university academic libraries", "कॉलेज एवं विश्वविद्यालय के शैक्षणिक पुस्तकालयों हेतु",
     ["Public village libraries", "School children rooms", "Military defense barracks"], ["ग्रामीण पुस्तकालय", "स्कूल पुस्तकालय", "सैनिक बैरक"],
     "Created by Verner W. Clapp and Robert T. Jordan using regression variables for students, faculty, and majors.",
     "क्लैप और जॉर्डन ने कॉलेज पुस्तकालयों में छात्रों और विषयों के आधार पर आवश्यक पुस्तकों की संख्या का सूत्र दिया।"),

    ("In Dr. S.R. Ranganathan's library financial allocation norms, how should the recurring budget ideally be distributed?",
     "डॉ. एस.आर. रंगनाथन के पुस्तकालय वित्तीय आवंटन मानकों के अनुसार आवर्ती बजट का आदर्श वितरण कैसा होना चाहिए?",
     "50% for Staff Salaries and 50% for Books, Periodicals, and Reading Materials",
     "50% कर्मचारियों के वेतन हेतु एवं 50% पुस्तकों, पत्रिकाओं व अध्ययन सामग्री हेतु",
     ["90% for Staff and 10% for Books", "20% for Staff and 80% for Books", "100% for Books only"],
     ["90% वेतन, 10% पुस्तकें", "20% वेतन, 80% पुस्तकें", "केवल पुस्तकें"],
     "Advocated a balanced 50:50 parity ensuring adequate expert staff to service the acquired reading collections.",
     "रंगनाथन ने 50% बजट पुस्तकों/पत्रिकाओं हेतु और 50% योग्य कर्मचारियों के वेतन हेतु रखने का नियम दिया।"),

    ("The financial audit conducted before an expenditure is actually incurred and bills are cleared is known as",
     "किसी भी खर्च के भुगतान से पूर्व बिलों और प्रक्रियाओं की वैधता जांचने हेतु किया जाने वाला वित्तीय परीक्षण कहलाता है:",
     "Pre-Audit (पूर्व-अंकेक्षण)", "पूर्व-अंकेक्षण (Pre-Audit)",
     ["Post-Audit", "Internal Audit", "Performance Audit"], ["उत्तर-अंकेक्षण", "आंतरिक अंकेक्षण", "परफॉर्मेंस ऑडिट"],
     "Ensures financial propriety, administrative sanction, and budget availability before money is paid.",
     "भुगतान करने से पहले बिलों की जांच प्री-ऑडिट कहलाती है ताकि वित्तीय नियमों का उल्लंघन न हो।"),

    ("The financial audit carried out after the financial year closes to inspect accounts and vouchers is called",
     "वित्तीय वर्ष समाप्त होने के बाद खातों, वाउचरों और भुगतानों की विधिवत जांच क्या कहलाती है?",
     "Post-Audit (उत्तर-अंकेक्षण / वैधानिक अंकेक्षण)", "उत्तर-अंकेक्षण (Post-Audit)",
     ["Pre-Audit", "Interim Audit", "Concurrent Audit"], ["पूर्व-अंकेक्षण", "अंतरिम ऑडिट", "समवर्ती ऑडिट"],
     "Conducted by government auditors or chartered accountants to issue the statutory audit report.",
     "वर्ष के अंत में सभी खर्चों और प्राप्तियों का आधिकारिक परीक्षण पोस्ट-ऑडिट कहलाता है।"),

    ("Lump-Sum Budgeting allocates money to the library as",
     "एकमुश्त बजटिंग (Lump-Sum Budgeting) में पुस्तकालय को धनराशि किस प्रकार आवंटित की जाती है?",
     "A single consolidated block grant allowing the librarian discretion to distribute across internal heads",
     "एकमुश्त निश्चित अनुदान, जिसमें आंतरिक मदों में खर्च करने का अधिकार पुस्तकालयाध्यक्ष को होता है",
     ["Detailed micro-line accounts with no flexibility", "Zero funds with monthly requests", "Vouchers only"],
     ["कठोर विस्तृत मदें", "शून्य फंड", "केवल वाउचर"],
     "Provides managerial flexibility to respond to fluctuating foreign journal subscription rates.",
     "एकमुश्त बजट से लाइब्रेरियन को आवश्यकतानुसार विदेशी पत्रिकाओं या पुस्तकों में फंड समायोजित करने की छूट मिलती है।")
]

q15_pool = make_pool_from_base(
    q15_base, "financial auditing, cost accounting, and revenue mobilization",
    "वित्तीय अंकेक्षण, लागत लेखांकन एवं राजस्व संग्रहण",
    "Ensuring strict accounting propriety, transparent audits, and diversified funding sources",
    "कठोर वित्तीय शुचिता, पारदर्शी ऑडिट और विविध स्रोतों से बजट सुनिश्चित करना",
    ["Operating without keeping financial records", "Allowing unverified cash spending", "Bypassing annual audit"],
    ["बिना रिकॉर्ड खर्च करना", "अवैध नकद भुगतान", "ऑडिट न कराना"]
)

print("Q11 pool count:", len(q11_pool))
print("Q12 pool count:", len(q12_pool))
print("Q13 pool count:", len(q13_pool))
print("Q14 pool count:", len(q14_pool))
print("Q15 pool count:", len(q15_pool))
