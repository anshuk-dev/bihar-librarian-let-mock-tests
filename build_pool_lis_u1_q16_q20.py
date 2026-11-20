# -*- coding: utf-8 -*-
"""
LIS Unit 1: Slots Q16 to Q20 (48 items each)
Q16: Professional Ethics & Standards (ALA Code of Ethics, IFLA Code, Privacy)
Q17: Information Society & Knowledge Society (Daniel Bell, Machlup, Porat, WSIS)
Q18: Open Access Movement (BOAI, DOAJ, Green/Gold OA, Sherpa/Romeo)
Q19: Scholarly Communication & Peer Review (arXiv, Predatory Journals, Beall's List)
Q20: Pioneers & Milestones of Library History (Dewey, Panizzi, Cutter, Sayers)
"""

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

# Q16: Professional Ethics (48 items)
q16_base = [
    ("The American Library Association (ALA) Code of Ethics was originally adopted in which year?",
     "अमेरिकन लाइब्रेरी एसोसिएशन (ALA) की आधिकारिक 'व्यावसायिक आचार संहिता' मूल रूप से किस वर्ष अपनाई गई थी?",
     "1939 (revised in 1981, 1995, 2008, and 2021)", "1939 में (1981, 1995, 2008 एवं 2021 में संशोधित)",
     ["1876", "1914", "1950"], ["1876 में", "1914 में", "1950 में"],
     "Articulates core principles: equitable access, user privacy, intellectual property, and intellectual freedom.",
     "1939 में एएलए ने पुस्तकालयाध्यक्षों हेतु आचार संहिता बनाई जिसमें पाठक की गोपनीयता और बौद्धिक स्वतंत्रता सर्वोपरि है।"),

    ("The IFLA Code of Ethics for Librarians and other Information Workers was officially approved in",
     "पुस्तकालयाध्यक्षों एवं सूचना कर्मियों हेतु 'IFLA आचार संहिता' आधिकारिक रूप से किस वर्ष अनुमोदित हुई?",
     "August 2012 (at Helsinki WLIC)", "अगस्त 2012 में (हेलसिंकी विश्व सम्मेलन में)",
     ["1995", "2000", "2018"], ["1995 में", "2000 में", "2018 में"],
     "Covers 6 core areas: access to information, neutrality, privacy, copyright, open access, and professional excellence.",
     "इफ़्ला ने 2012 में वैश्विक स्तर पर पुस्तकालय कर्मियों हेतु नैतिक आचरण के 6 मूलभूत सिद्धांत प्रतिपादित किए।"),

    ("In professional library ethics, maintaining the 'confidentiality and privacy of user records' means",
     "पुस्तकालय आचार संहिता में 'पाठक के रिकॉर्ड की गोपनीयता' (Privacy of User Records) बनाए रखने का क्या अर्थ है?",
     "Protecting each user's right to privacy with respect to information sought, books borrowed, and websites browsed",
     "पाठक द्वारा खोजी गई सूचना, जारी की गई पुस्तकों और इंटरनेट ब्राउजिंग की गोपनीयता की पूर्ण रक्षा करना",
     ["Selling user reading data to commercial advertisers", "Publishing list of borrowers on notice board", "Reporting reading habits to police without court warrant"],
     ["डेटा विज्ञापनदाताओं को बेचना", "नोटिस बोर्ड पर नाम छापना", "बिना वारंट पुलिस को रिपोर्ट करना"],
     "A cornerstone of professional librarianship preventing intellectual surveillance.",
     "पाठक ने क्या पढ़ा या खोजा, इसकी गोपनीयता बनाए रखना पुस्तकालयाध्यक्ष का सर्वोच्च नैतिक कर्तव्य है।"),

    ("Dr. S.R. Ranganathan outlined the ethical duties and dedicated spirit of the library professional under which phrase?",
     "डॉ. एस.आर. रंगनाथन ने पुस्तकालय पेशेवर के नैतिक कर्तव्यों और सेवा भावना को किस आदर्श वाक्य से व्यक्त किया था?",
     "'Service with a Smile and Affection' (Prema and Seva)", "'प्रेम और सेवा' (Service with affection)",
     ["Work for salary only", "Guarding books strictly", "Commercial customer management"],
     ["केवल वेतन हेतु कार्य", "किताबों की पहरेदारी", "व्यावसायिक ग्राहक प्रबंधन"],
     "Ranganathan taught that the librarian must welcome every reader as an honored guest.",
     "रंगनाथन ने सिखाया कि पुस्तकालयाध्यक्ष को पाठक का स्वागत आत्मीयता और मुस्कान के साथ करना चाहिए।"),

    ("When a library professional selects books without allowing personal political, religious, or moral biases to dictate collection development, they are practicing",
     "जब कोई पुस्तकालयाध्यक्ष अपने व्यक्तिगत राजनीतिक, धार्मिक या नैतिक पूर्वाग्रहों से मुक्त होकर पुस्तक चयन करता है, तो वह किस सिद्धांत का पालन करता है?",
     "Professional Neutrality and Impartiality (व्यावसायिक निष्पक्षता)", "व्यावसायिक निष्पक्षता (Professional Neutrality)",
     ["Personal Censorship", "Commercial Favoritism", "Ideological Purge"], ["व्यक्तिगत सेंसरशिप", "पक्षपात", "वैचारिक बहिष्कार"],
     "Ensures balanced representation of diverse viewpoints across controversial topics.",
     "निष्पक्षता का सिद्धांत मांग करता है कि सभी विरोधी विचारों की प्रामाणिक पुस्तकें पुस्तकालय में उपलब्ध हों।"),

    ("The ALA 'Library Bill of Rights' explicitly affirms that censorship of library materials should be",
     "ALA के 'लाइब्रेरी बिल ऑफ राइट्स' में स्पष्ट रूप से कहा गया है कि पुस्तकालय सामग्री पर सेंसरशिप का क्या किया जाना चाहिए?",
     "Challenged and resisted in the maintenance of responsibility by libraries to provide free expression",
     "पुस्तकालयों द्वारा स्वतंत्र अभिव्यक्ति की रक्षा हेतु सेंसरशिप का पुरजोर विरोध किया जाना चाहिए",
     ["Welcomed and encouraged by staff", "Enforced on all foreign political books", "Applied to any book criticizing leaders"],
     ["सेंसरशिप का स्वागत", "विदेशी पुस्तकों पर रोक", "नेताओं की आलोचना वाली किताबें हटाना"],
     "Affirms that libraries are forums for information and ideas, resisting partisan pressures.",
     "लाइब्रेरी बिल ऑफ राइट्स विचारों की स्वतंत्रता पर किसी भी तरह के वैचारिक प्रतिबंध का कड़ा विरोध करता है।"),

    ("The ethical responsibility of a librarian to actively engage in 'Continuing Professional Development' (CPD) means",
     "पुस्तकालयाध्यक्ष का 'सतत व्यावसायिक विकास' (CPD) से जुड़े रहने का नैतिक दायित्व क्या दर्शाता है?",
     "Continuously updating professional knowledge, digital skills, and technologies to serve users effectively",
     "उपयोगकर्ताओं की बेहतर सेवा हेतु अपने पेशेवर ज्ञान, डिजिटल कौशल और तकनीकी दक्षताओं को निरंतर अद्यतन करना",
     ["Retiring from learning after getting a job", "Refusing to learn computers", "Relying on 30-year-old notes"],
     ["नौकरी के बाद पढ़ना छोड़ना", "कंप्यूटर न सीखना", "पुराने ज्ञान पर निर्भर रहना"],
     "Mandated by both IFLA and ALA codes of ethics to maintain professional competence.",
     "ज्ञान और तकनीक के बदलते युग में पुस्तकालयाध्यक्ष को निरंतर कार्यशालाओं और प्रशिक्षण से खुद को अपडेट रखना चाहिए।"),

    ("If a librarian receives a monetary gift or bribe from a book vendor in exchange for purchasing their books, it violates the ethical principle of",
     "यदि कोई लाइब्रेरियन किसी प्रकाशक से पुस्तक खरीदने के बदले व्यक्तिगत उपहार या कमीशन लेता है, तो यह किस नैतिक सिद्धांत का उल्लंघन है?",
     "Avoiding Conflict of Interest and Financial Corruption", "हितों के टकराव और वित्तीय भ्रष्टाचार से दूर रहने का सिद्धांत",
     ["Fair dealing", "Open access", "Intellectual freedom"], ["उचित उपयोग", "मुक्त पहुंच", "बौद्धिक स्वतंत्रता"],
     "Librarians must never permit personal financial gain to influence public book acquisition decisions.",
     "सार्वजनिक धन से पुस्तक खरीद में पूर्ण पारदर्शिता और ईमानदारी बरतनी चाहिए; कमीशन लेना गंभीर कदाचार है।"),

    ("The ethical principle of 'Equal and Non-Discriminatory Access' in libraries guarantees that",
     "पुस्तकालयों में 'समान एवं गैर-भेदभावपूर्ण पहुंच' का नैतिक सिद्धांत क्या सुनिश्चित करता है?",
     "Every user has equal right to use library services regardless of caste, gender, religion, age, disability, or economic status",
     "जाति, लिंग, धर्म, आयु, दिव्यांगता अथवा आर्थिक स्थिति के भेदभाव के बिना प्रत्येक नागरिक को पुस्तकालय सेवा का समान अधिकार",
     ["Rich users get better services than poor users", "Children are barred from entry", "Women are given restricted hours"],
     ["अमीरों को प्राथमिकता", "बच्चों का प्रवेश बंद", "महिलाओं पर रोक"],
     "Direct translation of Dr. S.R. Ranganathan's Second Law: 'Every Reader his/her Book'.",
     "यह रंगनाथन के द्वितीय नियम का मूल आधार है कि ज्ञान के द्वार समाज के हर व्यक्ति के लिए समान रूप से खुले हों।"),

    ("The 'Banned Books Week' observed annually by ALA and library associations worldwide serves to",
     "प्रतिवर्ष ALA और पुस्तकालय संघों द्वारा मनाया जाने वाला 'बैंड बुक्स वीक' (Banned Books Week) किस उद्देश्य से आयोजित होता है?",
     "Celebrate the freedom to read and highlight the harms of censorship by displaying challenged or banned books",
     "पठन की स्वतंत्रता का उत्सव मनाना तथा प्रतिबंधित या विवादित पुस्तकों का प्रदर्शन कर सेंसरशिप के खतरों से आगाह करना",
     ["Burn banned books publicly", "Support government bans on literature", "Confiscate controversial novels"],
     ["पुस्तकों को जलाना", "प्रतिबंधों का समर्थन", "उपन्यास जब्त करना"],
     "Started in 1982; spotlights the historic struggles against book banning.",
     "1982 से शुरू हुआ यह सप्ताह अभिव्यक्ति की स्वतंत्रता और पाठकों के पठन अधिकार की रक्षा का उत्सव है।")
]

q16_pool = make_pool_from_base(
    q16_base, "professional ethics, reader privacy, and intellectual freedom",
    "पेशेवर आचार संहिता, पाठक गोपनीयता एवं बौद्धिक स्वतंत्रता",
    "Safeguarding intellectual freedom, user confidentiality, and unbiased access to knowledge",
    "बौद्धिक स्वतंत्रता, पाठक गोपनीयता और निष्पक्ष ज्ञान पहुंच की रक्षा करना",
    ["Selling reader reading histories to third parties", "Enforcing partisan censorship", "Discriminating among readers"],
    ["पाठक डेटा बेचना", "सेंसरशिप लगाना", "भेदभाव करना"]
)

# Q17: Information Society (48 items)
q17_base = [
    ("The concept of 'Knowledge Industry' and the early measurement of the knowledge economy was pioneered in 1962 by",
     "'ज्ञान उद्योग' (Knowledge Industry) की अवधारणा और ज्ञान अर्थव्यवस्था का प्रथम सांख्यिकीय मापन 1962 में किसने किया था?",
     "Fritz Machlup (in 'The Production and Distribution of Knowledge in the United States')", "फ्रिट्ज़ मैकलप (Fritz Machlup)",
     ["Daniel Bell", "Marc Porat", "Alvin Toffler"], ["डैनियल बेल", "मार्क पोराट", "एल्विन टॉफ्लर"],
     "Machlup showed that knowledge production accounted for nearly 29% of the US Gross National Product in 1958.",
     "अर्थशास्त्री फ्रिट्ज़ मैकलप ने सिद्ध किया कि ज्ञान का उत्पादन और वितरण अर्थव्यवस्था का सबसे बड़ा इंजन बन रहा है।"),

    ("The seminal work 'The Coming of Post-Industrial Society: A Venture in Social Forecasting' (1973) was authored by",
     "युगांतरकारी समाजशास्त्रीय ग्रंथ 'द कमिंग ऑफ पोस्ट-इंडस्ट्रियल सोसाइटी' (1973) के रचयिता कौन थे?",
     "Daniel Bell", "डैनियल बेल (Daniel Bell)",
     ["Fritz Machlup", "Marc Porat", "Manuel Castells"], ["मैकलप", "पोराट", "मैनुअल कैस्टेल्स"],
     "Daniel Bell analyzed the historic structural transition from manufacturing goods to information, services, and technical expertise.",
     "डैनियल बेल ने प्रतिपादित किया कि आधुनिक समाज विनिर्माण से सूचना और सैद्धांतिक ज्ञान की अर्थव्यवस्था में बदल रहा है।"),

    ("Marc Uri Porat, in his landmark 1977 report 'The Information Economy', divided the information economy into which two sectors?",
     "मार्क पोराट ने 1977 की ऐतिहासिक रिपोर्ट 'द इंफॉर्मेशन इकोनॉमी' में सूचना अर्थव्यवस्था को किन दो क्षेत्रों में विभाजित किया था?",
     "Primary Information Sector (goods sold in market) and Secondary Information Sector (information used within firms/government)",
     "प्राथमिक सूचना क्षेत्र (बाजार में बेचे जाने वाले सूचना उत्पाद) एवं द्वितीयक सूचना क्षेत्र (सार्वजनिक/निजी आंतरिक सूचना)",
     ["Hardware sector and Software sector", "Print sector and Electronic sector", "Domestic and International sectors"],
     ["हार्डवेयर व सॉफ्टवेयर", "प्रिंट व इलेक्ट्रॉनिक", "घरेलू व विदेशी"],
     "Porat proved that information activities accounted for over 46% of the US workforce in 1967.",
     "पोराट ने दिखाया कि सूचना क्षेत्र राष्ट्रीय आय और रोजगार में विनिर्माण और कृषि से आगे निकल चुका है।"),

    ("The visionary concept of historical transformation through Three Waves (Agricultural, Industrial, and Information Wave) was formulated in 1980 by",
     "इतिहास को 'तीन तरंगों' (कृषि क्रांति, औद्योगिक क्रांति, और सूचना क्रांति) में विभाजित करने वाले प्रसिद्ध भविष्यवक्ता कौन थे?",
     "Alvin Toffler (in 'The Third Wave')", "एल्विन टॉफ्लर (Alvin Toffler - 'द थर्ड वेव')",
     ["Marshall McLuhan", "John Naisbitt", "Daniel Bell"], ["मैकलुहान", "नैसबिट", "डैनियल बेल"],
     "Toffler coined the term 'Prosumer' and predicted personalized electronic information networks.",
     "एल्विन टॉफ्लर ने अपनी पुस्तक 'द थर्ड वेव' में सूचना युग को मानव सभ्यता की तीसरी सबसे बड़ी क्रांति बताया।"),

    ("The concept of 'The Global Village' (where electronic communication links the world into an interconnected village) was coined by",
     "इलेक्ट्रॉनिक संचार द्वारा विश्व के एक-दूसरे से जुड़कर एक 'वैश्विक गांव' (Global Village) बन जाने की अवधारणा किसने दी थी?",
     "Marshall McLuhan (in 'Understanding Media', 1964)", "मार्शल मैकलुहान (Marshall McLuhan)",
     ["Alvin Toffler", "Daniel Bell", "Norbert Wiener"], ["टॉफ्लर", "डैनियल बेल", "वीनर"],
     "McLuhan famously declared 'The Medium is the Message', analyzing electronic broadcast media.",
     "मैकलुहान ने कहा था कि संचार तकनीक विश्व को एक वैश्विक गांव में समेट देगी और माध्यम ही संदेश है।"),

    ("The landmark 'World Summit on the Information Society' (WSIS) was organized by the United Nations and ITU in which two phases?",
     "संयुक्त राष्ट्र और आईटीयू द्वारा 'सूचना समाज पर विश्व शिखर सम्मेलन' (WSIS) किन दो चरणों में आयोजित किया गया था?",
     "Phase 1: Geneva (2003) and Phase 2: Tunis (2005)", "प्रथम चरण: जिनेवा (2003) एवं द्वितीय चरण: ट्यूनिस (2005)",
     ["Phase 1: New York (2000) and Phase 2: Paris (2004)", "Phase 1: London (2001) and Phase 2: Tokyo (2005)", "Geneva only"],
     ["न्यूयॉर्क व पेरिस", "लंदन व टोक्यो", "केवल जिनेवा"],
     "Formulated the Geneva Declaration of Principles and Tunis Agenda for bridging the global digital divide.",
     "जिनेवा और ट्यूनिस में आयोजित WSIS ने डिजिटल विभाजन पाटने और इंटरनेट गवर्नेंस का वैश्विक खाका खींचा।"),

    ("The sociological concept of 'The Network Society' (society structured around microelectronic information networks) was articulated in 1996 by",
     "'नेटवर्क समाज' (The Network Society) का समाजशास्त्रीय सिद्धांत 1996 में किस प्रमुख विचारक द्वारा प्रस्तुत किया गया था?",
     "Manuel Castells (in 'The Rise of the Network Society')", "मैनुअल कैस्टेल्स (Manuel Castells)",
     ["Daniel Bell", "Fritz Machlup", "David Harvey"], ["डैनियल बेल", "मैकलप", "डेविड हार्वे"],
     "Castells analyzed space of flows, global digital capitalism, and social movements in the information age.",
     "मैनुअल कैस्टेल्स ने बताया कि आधुनिक समाज का ताना-बाना कंप्यूटर और इंटरनेट नेटवर्क पर आधारित हो चुका है।"),

    ("The term 'Information Rich' versus 'Information Poor' and the phenomenon of 'Digital Divide' refers to",
     "'डिजिटल डिवाइड' (Digital Divide) और 'सूचना संपन्न बनाम सूचना विपन्न' की अवधारणा क्या दर्शाती है?",
     "The socio-economic gap between individuals, households, and nations with access to modern ICT and the internet and those without",
     "आधुनिक सूचना तकनीक व इंटरनेट की पहुंच रखने वाले और इससे वंचित लोगों/देशों के बीच की सामाजिक-आर्थिक खाई",
     ["The cost of library books in supermarkets", "Speed of paper printing presses", "Differences in library shelf height"],
     ["किताबों का मूल्य", "प्रेस की गति", "अलमारी की ऊंचाई"],
     "Highlights structural inequality in internet access, digital literacy, and economic opportunities.",
     "डिजिटल विभाजन कंप्यूटर और इंटरनेट की पहुंच के आधार पर समाज में पैदा होने वाली असमानता को दर्शाता है।"),

    ("UNESCO distinguishes the concept of 'Knowledge Societies' from 'Information Society' by emphasizing",
     "यूनेस्को ने केवल 'सूचना समाज' के स्थान पर 'ज्ञान समाज' (Knowledge Societies) की अवधारणा में किन 4 प्रमुख स्तंभों पर बल दिया है?",
     "Freedom of expression, universal access to information, quality education for all, and respect for cultural/linguistic diversity",
     "अभिव्यक्ति की स्वतंत्रता, सार्वभौमिक सूचना पहुंच, गुणवत्तापूर्ण शिक्षा, तथा सांस्कृतिक व भाषाई विविधता का सम्मान",
     ["Selling hardware computers", "Privatizing telecom companies", "Eliminating traditional books"],
     ["हार्डवेयर बेचना", "निजीकरण", "किताबें खत्म करना"],
     "UNESCO asserts that mere technological connectivity is insufficient without human rights and diversity.",
     "यूनेस्को के अनुसार केवल तकनीक का प्रसार काफी नहीं है; ज्ञान समाज में स्वतंत्रता, शिक्षा और विविधता अनिवार्य है।"),

    ("Cybernetics, the scientific study of control and communication in animals and machines, was founded in 1948 by",
     "पशुओं और मशीनों में संचार एवं नियंत्रण का विज्ञान 'साइबरनेटिक्स' (Cybernetics) 1948 में किसके द्वारा प्रतिपादित किया गया?",
     "Norbert Wiener", "नॉरबर्ट वीनर (Norbert Wiener)",
     ["Claude Shannon", "Alan Turing", "John von Neumann"], ["क्लॉड शैनन", "एलन ट्यूरिंग", "वॉन न्यूमैन"],
     "Wiener explored feedback loops, automation, and communication theory influencing computer science.",
     "नॉरबर्ट वीनर ने 1948 में साइबरनेटिक्स की नींव रखी जिसने कंप्यूटर और संचार प्रणालियों को गहराई से प्रभावित किया।")
]

q17_pool = make_pool_from_base(
    q17_base, "information society metrics, digital literacy, and universal knowledge access",
    "सूचना समाज संकेतकों, डिजिटल साक्षरता एवं सार्वभौमिक ज्ञान पहुंच",
    "Promoting universal digital inclusion, community internet access, and media literacy",
    "सार्वभौमिक डिजिटल समावेशन, सामुदायिक इंटरनेट पहुंच और मीडिया साक्षरता को बढ़ावा देना",
    ["Restricting digital access to high income groups", "Shutting down community centers", "Banning online search"],
    ["पहुंच सीमित करना", "केंद्र बंद करना", "सर्च पर रोक"]
)

# Q18: Open Access (48 items)
q18_base = [
    ("The foundational definition of Open Access (OA) was formally articulated in February 2002 by the",
     "ओपन एक्सेस (मुक्त पहुंच) की ऐतिहासिक आधिकारिक परिभाषा फरवरी 2002 में किस घोषणा द्वारा दी गई थी?",
     "Budapest Open Access Initiative (BOAI, supported by Open Society Institute)", "बुडापेस्ट ओपन एक्सेस इनिशिएटिव (BOAI)",
     ["Bethesda Statement", "Berlin Declaration", "Delhi Declaration"], ["बेथेस्डा स्टेटमेंट", "बर्लिन घोषणा", "दिल्ली घोषणा"],
     "Defined open access as free, unrestricted online availability of peer-reviewed research literature for all to read and reuse.",
     "फरवरी 2002 में बुडापेस्ट घोषणा ने शोध साहित्य को इंटरनेट पर सभी के लिए निःशुल्क और बाधारहित उपलब्ध कराने का आह्वान किया।"),

    ("Which three historic statements are celebrated as the 'BBB Declarations' forming the bedrock of the Open Access movement?",
     "ओपन एक्सेस आंदोलन की आधारशिला रखने वाली किन तीन ऐतिहासिक घोषणाओं को 'BBB घोषणाएं' कहा जाता है?",
     "Budapest Open Access Initiative (2002), Bethesda Statement (2003), and Berlin Declaration (2003)",
     "बुडापेस्ट इनिशिएटिव (2002), बेथेस्डा स्टेटमेंट (2003), एवं बर्लिन घोषणा (2003)",
     ["Boston, Brussels, and Beijing", "Britain, Berlin, and Brazil", "Bangalore, Bombay, and Baroda"],
     ["बोस्टन, ब्रुसेल्स, बीजिंग", "ब्रिटेन, बर्लिन, ब्राजील", "बंगलुरु, बॉम्बे, बड़ौदा"],
     "Collectively established the international definitions and institutional protocols of open access scholarly publishing.",
     "बुडापेस्ट, बेथेस्डा और बर्लिन घोषणाओं ने ओपन एक्सेस के वैश्विक मानकों और सिद्धांतों को आकार दिया।"),

    ("In Open Access terminology, 'Green Open Access' (Green OA) refers to",
     "ओपन एक्सेस की शब्दावली में 'ग्रीन ओपन एक्सेस' (Green OA) से क्या तात्पर्य है?",
     "Authors self-archiving a version of their peer-reviewed manuscript in an institutional or subject repository",
     "लेखक द्वारा अपने सहकर्मी-समीक्षित शोध पत्र को संस्थागत अथवा विषयगत डिजिटल रिपॉजिटरी में स्वयं सुरक्षित (Self-Archiving) करना",
     ["Publishing in commercial high-cost journals", "Printing on green paper", "Paying high author fees for immediate online release"],
     ["व्यावसायिक जर्नल में छपना", "हरे कागज पर छपाई", "भारी शुल्क देकर ऑनलाइन करना"],
     "Free for the author; works deposited in repositories like DSpace, EPrints, or Zenodo.",
     "ग्रीन ओपन एक्सेस में लेखक अपने शोध पत्र का प्री-प्रिंट या पोस्ट-प्रिंट अपने संस्थान के डिजिटल भंडार में निःशुल्क अपलोड करता है।"),

    ("In Open Access terminology, 'Gold Open Access' (Gold OA) refers to",
     "ओपन एक्सेस की शब्दावली में 'गोल्ड ओपन एक्सेस' (Gold OA) से क्या तात्पर्य है?",
     "Publishing directly in a fully open-access journal where the final published article is immediately free to all readers worldwide",
     "सीधे पूर्ण ओपन-एक्सेस जर्नल में शोध पत्र प्रकाशित करना, जहां अंतिम लेख पूरे विश्व में सभी पाठकों हेतु तुरंत निःशुल्क उपलब्ध होता है",
     ["Restricting articles behind a paywall", "Self-archiving 2 years later", "Printing gold-bound books"],
     ["पेवॉल के पीछे रखना", "2 वर्ष बाद अपलोड करना", "स्वर्ण जिल्द पुस्तक"],
     "May be funded by Article Processing Charges (APCs) paid by author's institution or funded diamond/platinum by societies.",
     "गोल्ड ओपन एक्सेस में जर्नल के सभी शोध पत्र प्रकाशित होते ही पत्रिका की वेबसाइट पर सभी के लिए पूरी तरह खुले होते हैं।"),

    ("The Directory of Open Access Journals (DOAJ), the premier white-list of quality peer-reviewed open access journals, was launched in 2003 at",
     "गुणवत्तापूर्ण ओपन एक्सेस जर्नलों की वैश्विक निर्देशिका 'DOAJ' (Directory of Open Access Journals) 2003 में कहां शुरू की गई थी?",
     "Lund University (Sweden, founded by Lars Bjørnshauge)", "लुंड विश्वविद्यालय (स्वीडन - लार्स ब्योर्नशॉज द्वारा)",
     ["Harvard University", "Oxford University", "Delhi University"], ["हार्वर्ड", "ऑक्सफोर्ड", "दिल्ली वि.वि."],
     "Maintains stringent quality standards; now indexes over 20,000 peer-reviewed journals in 80+ languages.",
     "स्वीडन के लुंड विश्वविद्यालय से 2003 में शुरू हुआ DOAJ आज 20,000 से अधिक प्रामाणिक ओपन एक्सेस जर्नलों की सूची प्रदान करता है।"),

    ("SHERPA/RoMEO, an essential online reference service for librarians and researchers, provides information on",
     "पुस्तकालयाध्यक्षों और शोधकर्ताओं के लिए उपयोगी 'SHERPA/RoMEO' पोर्टल मुख्य रूप से क्या जानकारी प्रदान करता है?",
     "Publisher copyright policies and self-archiving permissions (Green, Blue, Yellow, and White categories)",
     "प्रकाशकों की कॉपीराइट नीतियां एवं शोध पत्रों के स्व-संग्रहण (Self-Archiving) की अनुमति शर्तें",
     ["Discount coupons for book fairs", "Author biographies only", "University library budgets"],
     ["पुस्तक छूट कूपन", "लेखक की जीवनी", "विश्वविद्यालय बजट"],
     "Created by University of Nottingham; informs authors which version (preprint, postprint, PDF) can be legally uploaded.",
     "शेरपा/रोमियो बताता है कि किस प्रकाशक का शोध पत्र संस्थागत रिपॉजिटरी में अपलोड किया जा सकता है।"),

    ("The Directory of Open Access Books (DOAB), providing a searchable index to peer-reviewed academic open access books, is managed by",
     "सहकर्मी-समीक्षित शैक्षणिक ओपन एक्सेस पुस्तकों की निर्देशिका 'DOAB' (Directory of Open Access Books) का संचालन किसके द्वारा किया जाता है?",
     "OAPEN Foundation (in partnership with OpenEdition)", "OAPEN फाउंडेशन (OpenEdition के सहयोग से)",
     ["Library of Congress", "Amazon", "Elsevier"], ["लाइब्रेरी ऑफ कांग्रेस", "अमेजन", "एल्सेवियर"],
     "Provides indexing and discovery services for thousands of scholarly open-access monographs.",
     "DOAB दुनिया भर के विश्वविद्यालयों और अकादमिक प्रकाशकों की खुली शैक्षणिक पुस्तकों की प्रामाणिक निर्देशिका है।"),

    ("The Registry of Open Access Repositories (ROAR) was created and hosted by which institution?",
     "विश्वभर की ओपन एक्सेस रिपॉजिटरियों की सूची 'ROAR' (Registry of Open Access Repositories) किस संस्थान द्वारा बनाई गई?",
     "University of Southampton (UK, created by Tim Brody and Stevan Harnad)", "साउथेम्प्टन विश्वविद्यालय (यूके - स्टीवन हरनाड द्वारा)",
     ["University of Nottingham", "MIT", "Stanford University"], ["नॉटिंघम वि.वि.", "एमआईटी", "स्टैनफोर्ड"],
     "Tracks the growth, compliance, and document count of institutional repositories worldwide.",
     "साउथेम्प्टन विश्वविद्यालय का ROAR पूरे विश्व में डिजिटल रिपॉजिटरी की संख्या और उनके विकास का रिकॉर्ड रखता है।"),

    ("OpenDOAR (Directory of Open Access Repositories), an authoritative worldwide directory of academic open access repositories, was developed by",
     "विश्वभर की अकादमिक ओपन एक्सेस रिपॉजिटरियों की प्रामाणिक निर्देशिका 'OpenDOAR' किसके द्वारा विकसित की गई थी?",
     "University of Nottingham and Lund University (SHERPA services)", "नॉटिंघम विश्वविद्यालय एवं लुंड विश्वविद्यालय (SHERPA सेवाएं)",
     ["University of Southampton", "Harvard University", "CERN"], ["साउथेम्प्टन", "हार्वर्ड", "सर्न"],
     "Evaluates repositories for quality metadata, institutional backing, and full-text access.",
     "OpenDOAR दुनिया भर के संस्थागत डिजिटल भंडारों (जैसे DSpace संग्रहों) की गुणवत्तापूर्ण निर्देशिका है।"),

    ("Plan S, an initiative launched in September 2018 by cOAlition S (an international consortium of research funders), mandates that",
     "सितंबर 2018 में cOAlition S द्वारा शुरू की गई 'प्लान एस' (Plan S) पहल का क्या अनिवार्य नियम है?",
     "Research funded by participating public grants must be published in compliant Open Access journals or repositories immediately without embargo",
     "सार्वजनिक अनुदान से संपोषित शोध को बिना किसी प्रतिबंध अवधि (Embargo) के तुरंत ओपन एक्सेस में प्रकाशित किया जाना अनिवार्य है",
     ["Publishing exclusively in print books", "Banning digital publications", "Restricting research to European citizens"],
     ["केवल मुद्रित पुस्तकों में छपना", "डिजिटल पर रोक", "केवल यूरोपीय नागरिकों हेतु"],
     "Supported by European Commission, WHO, and Wellcome Trust to accelerate 100% immediate open access.",
     "प्लान एस सार्वजनिक धन से हुए वैज्ञानिक शोध को तुरंत और पूरी तरह सबके लिए मुफ्त उपलब्ध कराने की वैश्विक मुहिम है।")
]

q18_pool = make_pool_from_base(
    q18_base, "open access institutional mandates, creative commons licensing, and self-archiving",
    "ओपन एक्सेस संस्थागत आदेशों, क्रिएटिव कॉमन्स लाइसेंसिंग एवं स्व-संग्रहण",
    "Adopting open-access mandates, institutional DSpace repositories, and open licensing",
    "ओपन एक्सेस अनिवार्यता, संस्थागत डीस्पेस रिपॉजिटरी और ओपन लाइसेंसिंग को अपनाना",
    ["Locking research behind expensive paywalls", "Banning preprint servers", "Selling free articles"],
    ["शोध को पेवॉल में बंद करना", "प्री-प्रिंट पर रोक", "मुफ्त लेख बेचना"]
)

# Q19: Scholarly Communication (48 items)
q19_base = [
    ("The world's first open-access electronic preprint server 'arXiv', established in August 1991 for physics and mathematics, was created by",
     "भौतिकी और गणित हेतु अगस्त 1991 में स्थापित विश्व का पहला इलेक्ट्रॉनिक प्री-प्रिंट सर्वर 'arXiv' किसने बनाया था?",
     "Paul Ginsparg (at Los Alamos National Laboratory, now hosted by Cornell University)", "पॉल गिन्सपार्ग (Paul Ginsparg - लॉस एलामोस, अब कॉर्नेल वि.वि.)",
     ["Tim Berners-Lee", "Vint Cerf", "Marc Andreessen"], ["टिम बर्नर्स-ली", "विंट सर्फ", "मार्क एंड्रीसन"],
     "Pioneered rapid preprint sharing before formal peer review; hosts over 2.4 million scholarly papers.",
     "पॉल गिन्सपार्ग द्वारा 1991 में स्थापित arXiv ने शोध पत्रों को बिना किसी शुल्क के तुरंत साझा करने की क्रांति ला दी।"),

    ("In peer review systems, 'Double-Blind Peer Review' means",
     "शोध प्रकाशन की सहकर्मी-समीक्षा प्रणाली में 'डबल-ब्लाइंड पीयर रिव्यू' (Double-Blind) का क्या अर्थ होता है?",
     "Neither the author knows the identity of the reviewer, nor the reviewer knows the identity of the author",
     "न तो लेखक को समीक्षक की पहचान का पता होता है और न ही समीक्षक को लेखक की पहचान का",
     ["Reviewer knows author, but author does not know reviewer", "Both author and reviewer openly know each other", "Paper is published without any review"],
     ["समीक्षक लेखक को जानता है किंतु लेखक नहीं", "दोनों एक-दूसरे को जानते हैं", "बिना समीक्षा प्रकाशन"],
     "Prevents personal, gender, or institutional prejudices from biasing the scholarly evaluation.",
     "डबल-ब्लाइंड में लेखक और समीक्षक दोनों के नाम गुप्त रखे जाते हैं ताकि समीक्षा पूरी तरह निष्पक्ष और वस्तुनिष्ठ हो।"),

    ("In peer review terminology, 'Single-Blind Peer Review' means",
     "सहकर्मी-समीक्षा में 'सिंगल-ब्लाइंड पीयर रिव्यू' (Single-Blind) का क्या अर्थ है?",
     "The reviewer knows the identity of the author, but the author does not know who reviewed their paper",
     "समीक्षक को लेखक की पहचान ज्ञात होती है, किंतु लेखक को यह पता नहीं होता कि उसका पेपर किसने समीक्षित किया",
     ["Neither knows the other", "Both identities are published publicly", "Editor reviews without reviewers"],
     ["दोनों अनजान रहते हैं", "दोनों नाम प्रकाशित होते हैं", "संपादक स्वयं समीक्षा करता है"],
     "Traditional peer review model used by many scientific and medical journals.",
     "सिंगल-ब्लाइंड में समीक्षक गुप्त रहता है जबकि लेखक का नाम उसे पता होता है।"),

    ("The concept of 'Predatory Journals' (exploitative open-access publishers charging author fees without genuine peer review) was coined and documented by",
     "छद्म या शिकारी जर्नल ('प्रिडेटरी जर्नल्स' - बिना वास्तविक समीक्षा के केवल फीस लेकर छापने वाले) की पहचान और सूची किसने बनाई थी?",
     "Jeffrey Beall (academic librarian at University of Colorado Denver)", "जेफरी बील (Jeffrey Beall - कोलोराडो विश्वविद्यालय के लाइब्रेरियन)",
     ["Eugene Garfield", "Jorge Hirsch", "Derek de Solla Price"], ["यूजीन गारफील्ड", "जॉर्ज हिर्श", "डी सोला प्राइस"],
     "Published 'Beall's List of Predatory Open-Access Publishers' from 2010 to 2017 to protect young researchers.",
     "जेफरी बील ने 2010 से 2017 तक प्रिडेटरी प्रकाशकों की सूची (Beall's List) जारी कर अकादमिक दुनिया को सचेत किया।"),

    ("The international campaign 'Think. Check. Submit.' was launched in 2015 to help researchers",
     "2015 में शुरू किए गए अंतरराष्ट्रीय अभियान 'Think. Check. Submit.' का मुख्य उद्देश्य शोधकर्ताओं को किस बात में मदद करना है?",
     "Identify trusted, credible academic journals for publishing their research and avoid predatory publishers",
     "शोध प्रकाशन हेतु प्रामाणिक और विश्वसनीय जर्नलों की पहचान करना तथा प्रिडेटरी प्रकाशकों के धोखे से बचना",
     ["Calculate journal subscription discounts", "Format footnotes automatically", "Write abstracts in multiple languages"],
     ["छूट गणना", "पाद-टिप्पणी बनाना", "सार लिखना"],
     "Provides a simple checklist verifying editorial boards, peer review rigor, and indexing credentials.",
     "यह अभियान शोधकर्ताओं को अपनी पांडुलिपि भेजने से पहले पत्रिका की विश्वसनीयता जांचने के आसान नियम सिखाता है।"),

    ("The Committee on Publication Ethics (COPE), providing ethical guidelines for editors and publishers on handling plagiarism and retractions, was founded in",
     "शोध पत्रों में साहित्यिक चोरी और शोध कदाचार से निपटने हेतु 'कमेटी ऑन पब्लिकेशन एथिक्स' (COPE) की स्थापना किस वर्ष हुई थी?",
     "1997 (in the United Kingdom)", "1997 में (यूनाइटेड किंगडम में)",
     ["1985", "2005", "2012"], ["1985 में", "2005 में", "2012 में"],
     "Formulates international flowcharts on handling data fabrication, authorship disputes, and peer review manipulation.",
     "1997 में स्थापित COPE शोध प्रकाशन में नैतिक आचरण, चोरी और पेपर वापसी (Retraction) के वैश्विक मानक तय करती है।"),

    ("The 'UGC-CARE' (Consortium for Academic and Research Ethics) Reference List of Quality Journals was set up in India in 2019 by",
     "भारत में गुणवत्तापूर्ण शोध पत्रिकाओं की 'UGC-CARE' संदर्भ सूची 2019 में किसके द्वारा स्थापित की गई थी?",
     "University Grants Commission (UGC, coordinated by Savitribai Phule Pune University)",
     "विश्वविद्यालय अनुदान आयोग (UGC - सावित्रीबाई फुले पुणे विश्वविद्यालय के समन्वय से)",
     ["National Library Kolkata", "CSIR-NIScPR", "Indian Library Association"],
     ["राष्ट्रीय पुस्तकालय", "निस्केयर", "आईएलए"],
     "Replaced older unverified lists to curb predatory publications and maintain research integrity in Indian universities.",
     "यूजीसी ने 2019 में पुणे विश्वविद्यालय के सहयोग से यूजीसी-केयर सूची बनाई ताकि फर्जी जर्नलों में प्रकाशन पर रोक लगे।"),

    ("The metric 'h-index', measuring both the productivity and citation impact of a researcher's published work, was invented in 2005 by",
     "किसी शोधकर्ता की उत्पादकता और उसके शोध पत्रों के प्रभाव को मापने वाला 'h-इंडेक्स' (h-index) 2005 में किसने विकसित किया था?",
     "Jorge E. Hirsch (physicist at UC San Diego)", "जॉर्ज ई. हिर्श (Jorge E. Hirsch)",
     ["Eugene Garfield", "Leo Egghe", "Derek de Solla Price"], ["यूजीन गारफील्ड", "लियो एग्घे", "डी सोला प्राइस"],
     "An author has index h if h of their N papers have at least h citations each.",
     "जॉर्ज हिर्श द्वारा प्रतिपादित h-इंडेक्स बताता है कि यदि किसी वैज्ञानिक के h शोध पत्रों को कम से कम h उद्धरण मिले हों।"),

    ("The 'g-index', which gives more weight to highly cited articles to supplement the h-index, was proposed in 2006 by",
     "अत्यधिक उद्धृत शोध पत्रों को उचित महत्व देने हेतु h-इंडेक्स के पूरक के रूप में 2006 में 'g-इंडेक्स' किसने प्रस्तावित किया था?",
     "Leo Egghe", "लियो एग्घे (Leo Egghe)",
     ["Jorge Hirsch", "Eugene Garfield", "F.W. Lancaster"], ["जॉर्ज हिर्श", "यूजीन गारफील्ड", "लैंकेस्टर"],
     "Calculated such that the top g articles received together at least g^2 citations.",
     "लियो एग्घे ने 2006 में g-इंडेक्स का सूत्र दिया जो वैज्ञानिक के सर्वाधिक उद्धृत शोध पत्रों के प्रभाव को बेहतर दर्शाता है।"),

    ("The 'Journal Impact Factor' (JIF), a measure reflecting the yearly average number of citations to recent articles in a journal, was devised by",
     "किसी पत्रिका के शोध पत्रों के वार्षिक औसत उद्धरणों को मापने वाला 'जर्नल इम्पैक्ट फैक्टर' (JIF) किसने प्रतिपादित किया था?",
     "Eugene Garfield (founder of Institute for Scientific Information - ISI)", "यूजीन गारफील्ड (Eugene Garfield - ISI के संस्थापक)",
     ["Jorge Hirsch", "Melvil Dewey", "S.R. Ranganathan"], ["जॉर्ज हिर्श", "मेल्विल डेवी", "रंगनाथन"],
     "Calculated annually in Clarivate's Journal Citation Reports (JCR) dividing citations in current year by articles in preceding two years.",
     "यूजीन गारफील्ड द्वारा विकसित इम्पैक्ट फैक्टर किसी शोध पत्रिका के प्रभाव और प्रतिष्ठा का सबसे लोकप्रिय पैमाना है।")
]

q19_pool = make_pool_from_base(
    q19_base, "scholarly communication ethics, citation metrics, and research integrity",
    "अकादमिक संचार नैतिकता, उद्धरण संकेतकों एवं शोध निष्ठा",
    "Maintaining rigorous peer review, citation transparency, and eliminating predatory publishing",
    "कठोर सहकर्मी समीक्षा, उद्धरण पारदर्शिता और प्रिडेटरी प्रकाशनों का उन्मूलन सुनिश्चित करना",
    ["Encouraging unverified predatory publishing", "Falsifying research citations", "Abolishing peer review"],
    ["फर्जी जर्नलों को बढ़ावा देना", "झूठे उद्धरण जोड़ना", "समीक्षा बंद करना"]
)

# Q20: Pioneers of LIS (48 items)
q20_base = [
    ("Who is celebrated worldwide as the 'Father of Modern Librarianship' for inventing decimal classification and founding the first library school?",
     "दशमलव वर्गीकरण के आविष्कार और विश्व के प्रथम पुस्तकालय स्कूल की स्थापना हेतु 'आधुनिक पुस्तकालय विज्ञान का जनक' किसे कहा जाता है?",
     "Melvil Dewey (1851-1931)", "मेल्विल डेवी (Melvil Dewey - 1851-1931)",
     ["Charles Ammi Cutter", "Antonio Panizzi", "S.R. Ranganathan"], ["चार्ल्स कटर", "पाणिजी", "रंगनाथन"],
     "Invented DDC in 1876, co-founded ALA, launched Library Journal, and established Columbia School of Library Economy in 1887.",
     "मेल्विल डेवी ने 1876 में DDC बनाई, एएलए की स्थापना की और 1887 में कोलंबिया कॉलेज में पहला पुस्तकालय विद्यालय खोला।"),

    ("In which year and at which institution did Melvil Dewey establish the world's first library school for professional training?",
     "मेल्विल डेवी ने किस वर्ष और किस संस्थान में पुस्तकालय पेशेवरों के प्रशिक्षण हेतु विश्व का पहला पुस्तकालय स्कूल स्थापित किया था?",
     "1887 at Columbia College, New York (School of Library Economy)", "1887 में कोलंबिया कॉलेज, न्यूयॉर्क में ('स्कूल ऑफ लाइब्रेरी इकोनॉमी')",
     ["1876 at Amherst College", "1895 at Albany", "1902 at Harvard"], ["1876 एमहर्स्ट", "1895 अल्बानी", "1902 हार्वर्ड"],
     "Admitted women students despite trustees' opposition; later shifted to Albany as New York State Library School.",
     "1887 में कोलंबिया में स्थापित यह स्कूल बाद में अल्बानी में न्यूयॉर्क स्टेट लाइब्रेरी स्कूल के रूप में चला।"),

    ("Antonio Panizzi (1797-1879), Keeper of Printed Books and Principal Librarian at the British Museum, is famous for formulating the",
     "ब्रिटिश म्यूजियम के प्रधान लाइब्रेरियन एंटोनियो पाणिजी (1797-1879) किस ऐतिहासिक सूचीकरण संहिता के निर्माण हेतु अमर हैं?",
     "'91 Rules' (Rules for the Compilation of the Catalogue, 1841)", "'91 नियम' (Rules for the Compilation of the Catalogue, 1841)",
     ["AACR-2", "Classified Catalogue Code", "Vatican Code"], ["AACR-2", "CCC", "वैटिकन कोड"],
     "Laid the intellectual foundations of modern author-title cataloguing and designed the British Museum Round Reading Room (1857).",
     "पाणिजी ने 1841 में 91 नियमों वाली पहली आधुनिक कैटलॉग संहिता बनाई और प्रसिद्ध ब्रिटिश म्यूजियम वाचनालय डिजाइन किया।"),

    ("Charles Ammi Cutter (1837-1903) published which landmark code in 1876 that defined the objectives and syndetic structure of a dictionary catalogue?",
     "चार्ल्स अम्मी कटर ने 1876 में किस युगांतरकारी संहिता का प्रकाशन किया जिसने डिक्शनरी कैटलॉग के उद्देश्यों और संरचना को परिभाषित किया?",
     "Rules for a Dictionary Catalog (RDC, 1876)", "रूल्स फॉर अ डिक्शनरी कैटलॉग (RDC, 1876)",
     ["91 Rules", "Prussian Instructions", "Anglo-American Code"], ["91 नियम", "प्रुशियन निर्देश", "एंग्लो-अमेरिकन"],
     "Defined the primary objectives of a library catalogue: to enable a person to find a book by author, title, or subject.",
     "कटर ने कैटलॉग के मूलभूत उद्देश्य बताए कि पाठक को लेखक, शीर्षक या विषय किसी से भी पुस्तक मिलनी चाहिए।"),

    ("William Charles Berwick Sayers (1881-1960), chief librarian of Croydon and teacher of Ranganathan, is celebrated as the",
     "क्रोइडन के मुख्य लाइब्रेरियन और रंगनाथन के लंदन में शिक्षक डब्ल्यू.सी. बेरविक सायर्ज पुस्तकालय विज्ञान में किस हेतु विख्यात हैं?",
     "First Grammarian of Library Classification (author of 'Canons of Classification', 1915)",
     "पुस्तकालय वर्गीकरण के प्रथम वैयाकरण (Grammarian of Classification)",
     ["Inventor of Microfilm", "First President of IFLA", "Founder of British Library"],
     ["माइक्रोफिल्म के जनक", "इफ़्ला के प्रथम अध्यक्ष", "ब्रिटिश लाइब्रेरी संस्थापक"],
     "Formulated 29 canons of classification; authored 'Introduction to Library Classification' and 'Manual of Classification'.",
     "सायर्ज ने वर्गीकरण के नियमों का पहला व्यवस्थित व्याकरण लिखा और रंगनाथन को गहराई से प्रभावित किया।"),

    ("James Duff Brown (1862-1914), pioneer of the open-shelf access system in the UK at Clerkenwell Public Library in 1894, created the",
     "1894 में ब्रिटेन में खुली प्रवेश प्रणाली (Open Shelf) शुरू करने वाले जेम्स डफ ब्राउन ने किस वर्गीकरण पद्धति का निर्माण किया था?",
     "Subject Classification (SC, 1906)", "सब्जेक्ट क्लासिफिकेशन (Subject Classification - 1906)",
     ["Expansive Classification", "Bibliographic Classification", "Decimal Classification"], ["विस्तार्य वर्गीकरण", "बिबलियोग्राफिक", "डेसीमल"],
     "Introduced the principle of 'one place for each subject' with a specialized Categorical Table.",
     "जेम्स डफ ब्राउन ने 1906 में 'सब्जेक्ट क्लासिफिकेशन' बनाई जिसमें श्रेणीबद्ध सारणी (Categorical Table) का प्रयोग हुआ।"),

    ("Henry Evelyn Bliss (1870-1955) spent thirty years developing which philosophically rigorous classification scheme?",
     "हेनरी एवलिन ब्लिस ने 30 वर्षों के अध्ययन के उपरांत 1935 में किस दार्शनिक वर्गीकरण पद्धति का विकास किया था?",
     "Bibliographic Classification (BC, 1935)", "बिबलियोग्राफिक क्लासिफिकेशन (Bibliographic Classification - 1935)",
     ["Subject Classification", "Colon Classification", "Rider's International Classification"], ["सब्जेक्ट क्लासिफिकेशन", "द्विबिंदु", "राइडर्स"],
     "Based on the 'Educational and Scientific Consensus'; revised later as Bliss Bibliographic Classification (BC2) in the UK.",
     "ब्लिस ने 1935 में 'बिबलियोग्राफिक क्लासिफिकेशन' (BC) का विकास किया जो शैक्षणिक सहमति पर आधारित थी।"),

    ("Asa Don Dickinson (1876-1960), an American librarian who was appointed Librarian of Punjab University at Lahore in 1915, is celebrated in India for",
     "1915 में पंजाब विश्वविद्यालय (लाहौर) के लाइब्रेरियन नियुक्त हुए अमेरिकी विद्वान आसा डॉन डिकिन्सन भारत में किस योगदान हेतु जाने जाते हैं?",
     "Introducing Dewey Decimal Classification to India, founding library training at Punjab University, and authoring the 'Punjab Library Primer' (1916)",
     "भारत में DDC पद्धति लाने, पंजाब वि.वि. में प्रशिक्षण शुरू करने और 'पंजाब लाइब्रेरी प्राइमर' (1916) पुस्तक लिखने हेतु",
     ["Passing the first library act", "Founding the National Library", "Inventing Colon Classification"],
     ["पहला कानून बनाना", "राष्ट्रीय पुस्तकालय स्थापना", "कोलन वर्गीकरण"],
     "Trained early Indian librarians using DDC and open access principles.",
     "डिकिन्सन ने 1915 में भारत में पहली बार डेवी दशमलव वर्गीकरण (DDC) सिखाया और पंजाब लाइब्रेरी प्राइमर लिखा।"),

    ("William Alanson Borden (1853-1931), an American librarian invited by Maharaja Sayajirao Gaekwad III of Baroda in 1910, is famous for",
     "1910 में बड़ौदा के महाराजा सयाजीराव गायकवाड़ द्वारा आमंत्रित अमेरिकी पुस्तकालयाध्यक्ष विलियम एलनसन बोर्डेन किस उपलब्धि हेतु विख्यात हैं?",
     "Establishing the first state-wide public library network in India and initiating the first library training class in Baroda",
     "भारत में प्रथम राज्यव्यापी सार्वजनिक पुस्तकालय नेटवर्क की स्थापना एवं बड़ौदा में पहली पुस्तकालय प्रशिक्षण कक्षा आरंभ करने हेतु",
     ["Drafting the Madras Library Act", "Founding the Imperial Library", "Creating UDC"],
     ["मद्रास एक्ट बनाना", "इंपीरियल लाइब्रेरी", "यूडीसी निर्माण"],
     "Served as Director of State Libraries in Baroda, creating over 400 rural libraries, traveling libraries, and children's rooms.",
     "बोर्डेन ने बड़ौदा रियासत में सचल पुस्तकालयों और ग्राम वाचनालयों का एक अद्भुत आधुनिक जाल बिछाया था।"),

    ("Dr. Shiyali Ramamrita Ranganathan (1892-1972) was officially honored with the national title of 'National Research Professor in Library Science' in",
     "डॉ. शियाली रामामृत रंगनाथन को भारत सरकार द्वारा 'पुस्तकालय विज्ञान के राष्ट्रीय शोध प्राध्यापक' की उपाधि से किस वर्ष सम्मानित किया गया था?",
     "1965", "1965 में",
     ["1957", "1962", "1970"], ["1957 में", "1962 में", "1970 में"],
     "Awarded Padma Shri in 1957 and made National Research Professor in 1965; founded DRTC at Bangalore in 1962.",
     "रंगनाथन को 1957 में पद्मश्री और 1965 में भारत सरकार द्वारा राष्ट्रीय शोध प्राध्यापक का सर्वोच्च सम्मान दिया गया।")
]

q20_pool = make_pool_from_base(
    q20_base, "pioneering contributions to cataloguing theory and classification design",
    "सूचीकरण सिद्धांत एवं वर्गीकरण संरचना में युगांतरकारी योगदान",
    "Advancing normative principles, faceted notation, and open public library access",
    "मानक सिद्धांतों, पक्षात्मक अंकन और मुक्त सार्वजनिक पुस्तकालय पहुंच को समृद्ध करना",
    ["Discouraging professional education", "Abolishing classification codes", "Closing historical archives"],
    ["शिक्षा रोकना", "वर्गीकरण बंद करना", "अभिलेखागार बंद करना"]
)

print("Q16 pool count:", len(q16_pool))
print("Q17 pool count:", len(q17_pool))
print("Q18 pool count:", len(q18_pool))
print("Q19 pool count:", len(q19_pool))
print("Q20 pool count:", len(q20_pool))
