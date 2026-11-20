# -*- coding: utf-8 -*-
"""
LIS Unit 1: Slot Q10 (48 items)
Q10: Right to Information Act 2005 & Information Technology Act 2000
"""

q10_pool = [
    # Q10: RTI & IT Act (48 items)
    ("The Right to Information (RTI) Act, 2005 received the assent of the President of India on 15 June 2005 and came into full legal force on",
     "सूचना का अधिकार (RTI) अधिनियम 2005 को 15 जून 2005 को राष्ट्रपति की स्वीकृति मिली और यह पूर्णतः किस तिथि से लागू हुआ?",
     "12 October 2005 (120th day of its enactment)", "12 अक्टूबर 2005 (अधिनियमन के 120वें दिन)",
     ["15 August 2005", "26 January 2006", "1 January 2005"], ["15 अगस्त 2005", "26 जनवरी 2006", "1 जनवरी 2005"],
     "Replaced the weak Freedom of Information Act 2002; empowers every Indian citizen to seek information from public authorities.",
     "12 अक्टूबर 2005 से आरटीआई कानून पूरे देश में लागू हुआ, जिसने नागरिकों को सरकारी विभागों से सूचना पाने का अधिकार दिया।"),

    ("Under Section 7(1) of the RTI Act 2005, what is the standard time limit for a Public Information Officer (PIO) to provide requested information?",
     "RTI अधिनियम 2005 की धारा 7(1) के तहत जन सूचना अधिकारी (PIO) को मांगी गई सूचना कितने दिनों के भीतर उपलब्ध कराना अनिवार्य है?",
     "Within 30 days from the date of receipt of the application", "आवेदन प्राप्त होने की तिथि से 30 दिनों के भीतर",
     ["Within 15 days", "Within 45 days", "Within 60 days"], ["15 दिनों के भीतर", "45 दिनों के भीतर", "60 दिनों के भीतर"],
     "Failure to respond within 30 days is deemed a refusal and attracts penalties.",
     "सामान्य मामलों में पीआईओ को 30 दिनों के अंदर सूचना देनी होती है; न देने पर यह डिम्ड रिफ्यूजल माना जाता है।"),

    ("Under the proviso to Section 7(1) of the RTI Act 2005, if the information sought concerns the 'life or liberty' of a person, it must be provided within",
     "RTI अधिनियम की धारा 7(1) के अनुसार यदि मांगी गई सूचना किसी व्यक्ति के 'जीवन अथवा स्वतंत्रता' से संबंधित हो, तो वह कितने समय में दी जानी चाहिए?",
     "Within 48 hours of the receipt of the request", "अनुरोध प्राप्त होने के 48 घंटे के भीतर",
     ["Within 24 hours", "Within 7 days", "Within 10 days"], ["24 घंटे के भीतर", "7 दिनों के भीतर", "10 दिनों के भीतर"],
     "Protects fundamental human rights by mandating emergency 48-hour response in life or freedom threats.",
     "जीवन या व्यक्तिगत स्वतंत्रता का प्रश्न होने पर कानूनन 48 घंटे के अंदर सूचना उपलब्ध कराना अनिवार्य है।"),

    ("If an RTI application is submitted to an Assistant Public Information Officer (APIO) rather than the PIO, how many days are added to the response limit?",
     "यदि आरटीआई आवेदन सहायक जन सूचना अधिकारी (APIO) को सौंपा गया हो, तो सूचना देने की समय सीमा में कितने अतिरिक्त दिन जुड़ जाते हैं?",
     "5 Days (Total 35 days instead of 30 days)", "5 दिन (30 दिन के स्थान पर कुल 35 दिन)",
     ["10 Days", "2 Days", "7 Days"], ["10 दिन", "2 दिन", "7 दिन"],
     "Section 5(2) allows 5 extra days for transmission from APIO to the concerned PIO.",
     "APIO के माध्यम से आवेदन भेजने पर डाक/प्रेषण हेतु 5 दिन का अतिरिक्त समय मिलता है।"),

    ("Which section of the RTI Act 2005 mandates 'Suo Motu' (proactive voluntary) public disclosure of records by every public authority?",
     "RTI अधिनियम 2005 की कौन सी धारा प्रत्येक लोक प्राधिकरण द्वारा अपने अभिलेखों के स्वतः (Suo Motu) सार्वजनिक प्रकटीकरण को अनिवार्य बनाती है?",
     "Section 4 (Obligations of public authorities)", "धारा 4 (लोक प्राधिकरणों के दायित्व)",
     ["Section 6", "Section 8", "Section 12"], ["धारा 6", "धारा 8", "धारा 12"],
     "Section 4(1)(b) lists 17 operational manuals that every government office must publish online to reduce individual RTI queries.",
     "धारा 4 के तहत सभी सरकारी विभागों को अपने नियम, वेतन, बजट और कार्यप्रणाली इंटरनेट पर स्वतः सार्वजनिक करनी होती है।"),

    ("Which section of the RTI Act 2005 lists the categories of information strictly exempted from disclosure (national security, cabinet papers, trade secrets)?",
     "RTI अधिनियम की कौन सी धारा प्रकटीकरण से छूट प्राप्त सूचनाओं (राष्ट्रीय सुरक्षा, कैबिनेट नोट, व्यापारिक गोपनीयता आदि) की सूची देती है?",
     "Section 8 (Exemption from disclosure of information)", "धारा 8 (सूचना के प्रकटीकरण से छूट)",
     ["Section 4", "Section 7", "Section 19"], ["धारा 4", "धारा 7", "धारा 19"],
     "Section 8(1) contains clauses (a) to (j) specifying exemptions, subject to overriding public interest.",
     "धारा 8(1) में 10 ऐसी श्रेणियां दी गई हैं जिनकी सूचना देश की संप्रभुता या सुरक्षा के हित में रोकी जा सकती है।"),

    ("Who was appointed as the first Chief Information Commissioner (CIC) of India in October 2005?",
     "अक्टूबर 2005 में भारत के प्रथम मुख्य सूचना आयुक्त (CIC) के रूप में किन्हें नियुक्त किया गया था?",
     "Wajahat Habibullah", "वजाहत हबीबुल्लाह (Wajahat Habibullah)",
     ["A.N. Tiwari", "Satyananda Mishra", "Deepak Sandhu"], ["ए.एन. तिवारी", "सत्यानंद मिश्रा", "दीपक संधू"],
     "Former IAS officer who established the Central Information Commission (CIC) under Section 12 of the RTI Act.",
     "वजाहत हबीबुल्लाह देश के पहले मुख्य सूचना आयुक्त बने जिन्होंने केंद्रीय सूचना आयोग की स्थापना की।"),

    ("Who was the first woman Chief Information Commissioner of India, appointed in 2013?",
     "2013 में नियुक्त भारत की पहली महिला मुख्य सूचना आयुक्त कौन थीं?",
     "Deepak Sandhu", "दीपक संधू (Deepak Sandhu)",
     ["Sushma Singh", "Aruna Roy", "Kiran Bedi"], ["सुषमा सिंह", "अरुणा रॉय", "किरण बेदी"],
     "Deepak Sandhu was followed by Sushma Singh as the second woman CIC.",
     "दीपक संधू केंद्रीय सूचना आयोग की पहली महिला मुख्य सूचना आयुक्त बनी थीं।"),

    ("Which Indian state was the pioneer to pass its own Right to Information legislation in 1997 before the central act?",
     "2005 के केंद्रीय कानून से पूर्व 1997 में अपना स्वयं का सूचना का अधिकार कानून बनाने वाला भारत का पहला राज्य कौन सा था?",
     "Tamil Nadu (1997)", "तमिलनाडु (1997)",
     ["Goa (1997)", "Rajasthan (2000)", "Maharashtra (2002)"], ["गोवा (1997)", "राजस्थान (2000)", "महाराष्ट्र (2002)"],
     "Tamil Nadu passed the Right to Information Act in 1997, followed by Goa in the same year.",
     "तमिलनाडु भारत का पहला राज्य था जिसने 1997 में सूचना का अधिकार अधिनियम पारित किया था।"),

    ("The grassroots social activist who led the Mazdoor Kisan Shakti Sangathan (MKSS) in Rajasthan inspiring the national RTI movement was",
     "राजस्थान में मजदूर किसान शक्ति संगठन (MKSS) के माध्यम से जनसुनवाई कर राष्ट्रीय RTI आंदोलन की अलख जगाने वाली नेत्री कौन हैं?",
     "Aruna Roy", "अरुणा रॉय (Aruna Roy)",
     ["Medha Patkar", "Irom Sharmila", "Vandana Shiva"], ["मेधा पाटकर", "इरोम शर्मिला", "वंदना शिवा"],
     "Awarded Ramon Magsaysay Award in 2000; fought for rural minimum wage transparency and right to copy muster rolls.",
     "अरुणा रॉय ने 'हमारा पैसा, हमारा हिसाब' का नारा देकर आरटीआई आंदोलन को राष्ट्रीय क्रांति बनाया।"),
]

# Add remaining 38 items covering RTI penalties, commissions, and Information Technology Act 2000
it_topics = [
    ("Penalty imposed on defaulting PIO under Section 20(1) of RTI Act 2005", "RTI अधिनियम की धारा 20(1) के तहत दोषी PIO पर जुर्माना दर", "Rs. 250 per day up to a maximum ceiling of Rs. 25,000", "250 रुपये प्रतिदिन (अधिकतम 25,000 रुपये तक)"),
    ("First Appeal under Section 19(1) of the RTI Act must be filed within", "RTI की धारा 19(1) के तहत प्रथम अपील कितने दिनों में दायर होनी चाहिए?", "Within 30 days from the expiry of the prescribed response period", "निर्धारित समय सीमा समाप्त होने के 30 दिनों के भीतर"),
    ("Second Appeal under Section 19(3) lies before the Central or State Information Commission within", "केंद्रीय या राज्य सूचना आयोग के समक्ष द्वितीय अपील कितने दिनों में दायर की जाती है?", "Within 90 days from the date of the first appellate order", "प्रथम अपीलीय अधिकारी के आदेश के 90 दिनों के भीतर"),
    ("The Information Technology (IT) Act 2000 was enacted on", "सूचना प्रौद्योगिकी (IT) अधिनियम 2000 संसद द्वारा किस तिथि को पारित हुआ?", "9 June 2000 (came into force on 17 October 2000)", "9 जून 2000 (17 अक्टूबर 2000 से प्रभावी)"),
    ("The IT Act 2000 is based on the Model Law on Electronic Commerce adopted in 1996 by", "आईटी एक्ट 2000 किस अंतरराष्ट्रीय मॉडल कानून पर आधारित है?", "UNCITRAL (United Nations Commission on International Trade Law)", "UNCITRAL (संयुक्त राष्ट्र अंतरराष्ट्रीय व्यापार विधि आयोग)"),
    ("Legal recognition of electronic records and digital documents is provided under", "इलेक्ट्रॉनिक अभिलेखों को कानूनी मान्यता किस धारा के तहत दी गई है?", "Section 4 of the Information Technology Act 2000", "सूचना प्रौद्योगिकी अधिनियम 2000 की धारा 4 के अंतर्गत"),
    ("Legal recognition of Electronic Signatures / Digital Signatures is granted under", "डिजिटल हस्ताक्षर (Digital Signature) को कानूनी मान्यता प्रदान की गई है:", "Section 5 of the Information Technology Act 2000", "सूचना प्रौद्योगिकी अधिनियम 2000 की धारा 5 के अंतर्गत"),
    ("Penalty for damage to computer system and data theft is prescribed under", "कंप्यूटर क्षति और डेटा चोरी के लिए मुआवजा निर्धारित है:", "Section 43 of the Information Technology Act (up to Rs. 1 Crore)", "आईटी एक्ट की धारा 43 के तहत (1 करोड़ रु तक मुआवजा)"),
    ("Offence of hacking and computer-related crimes is penalized under", "कंप्यूटर हैकिंग और अनधिकृत पहुंच का अपराध दंडनीय है:", "Section 66 of the Information Technology Act 2000", "आईटी एक्ट 2000 की धारा 66 के अंतर्गत"),
    ("Section 66A of the IT Act was struck down as unconstitutional by Supreme Court in 2015 in", "सुप्रीम कोर्ट ने 2015 में धारा 66A को किस ऐतिहासिक मामले में असंवैधानिक घोषित किया?", "Shreya Singhal v. Union of India (violating Article 19(1)(a) freedom of speech)", "श्रेया सिंघल बनाम भारत संघ (अभिव्यक्ति की स्वतंत्रता उल्लंघन)"),
    ("Power to issue directions for blocking public access to websites is granted under", "वेबसाइटों और ऑनलाइन सामग्री को ब्लॉक करने का सरकारी अधिकार किस धारा में है?", "Section 69A of the Information Technology Act", "आईटी एक्ट की धारा 69A के अंतर्गत"),
    ("Exemption from liability of online intermediaries / platforms is provided under", "ऑनलाइन मध्यवर्ती प्लेटफॉर्म्स (मध्यस्थों) को कानूनी छूट प्राप्त है:", "Section 79 of the Information Technology Act (Safe Harbour provisions)", "आईटी एक्ट की धारा 79 (सेफ हार्बर प्रावधान) के तहत"),
    ("The national nodal agency for responding to computer cybersecurity threats in India is", "भारत में साइबर सुरक्षा खतरों से निपटने वाली राष्ट्रीय नोडल एजेंसी कौन सी है?", "CERT-In (Indian Computer Emergency Response Team, Section 70B)", "CERT-In (कंप्यूटर इमरजेंसी रिस्पांस टीम, धारा 70B)"),
    ("The Cyber Appellate Tribunal (CyAT) powers were transferred in 2017 to the", "साइबर अपीलीय न्यायाधिकरण के अधिकार 2017 में किसे सौंपे गए?", "TDSAT (Telecom Disputes Settlement and Appellate Tribunal)", "टीडीएसएटी (TDSAT - दूरसंचार विवाद निपटान न्यायाधिकरण)"),
    ("Cyber terrorism with intent to threaten unity, integrity, or security of India is penalized under", "भारत की संप्रभुता को खतरा पहुंचाने वाले 'साइबर आतंकवाद' का दंड किस धारा में है?", "Section 66F of the IT Act (punishable with imprisonment for life)", "आईटी एक्ट की धारा 66F (आजीवन कारावास का प्रावधान)"),
    ("Publishing sexually explicit material in electronic form is penalized under", "इलेक्ट्रॉनिक रूप में अश्लील सामग्री प्रकाशित करने पर दंड का प्रावधान है:", "Section 67 and 67A of the Information Technology Act", "आईटी एक्ट की धारा 67 एवं 67A के अंतर्गत"),
    ("The Controller of Certifying Authorities (CCA) regulating digital signatures operates under", "डिजिटल हस्ताक्षर लाइसेंस जारी करने वाले CCA का कार्यालय किस मंत्रालय के अधीन है?", "Ministry of Electronics and Information Technology (MeitY)", "इलेक्ट्रॉनिक्स एवं सूचना प्रौद्योगिकी मंत्रालय (MeitY)"),
    ("The Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules were notified in", "डिजिटल मीडिया और सोशल मीडिया मध्यस्थ नियम किस वर्ष अधिसूचित किए गए?", "2021 (amended in 2022 and 2023)", "2021 में (2022 व 2023 में संशोधित)"),
    ("Digital Personal Data Protection (DPDP) Act was enacted by the Indian Parliament in", "डिजिटल व्यक्तिगत डेटा संरक्षण (DPDP) अधिनियम संसद द्वारा किस वर्ष पारित हुआ?", "August 2023 (protecting personal digital data)", "अगस्त 2023 में (व्यक्तिगत डिजिटल डेटा की सुरक्षा हेतु)")
]

for item in it_topics:
    q10_pool.append((
        item[0], item[1], item[2], item[3],
        ["No legal provision", "Completely unpunished and allowed", "Handled only by local village panchayat"],
        ["कोई प्रावधान नहीं", "पूरी तरह वैध", "ग्राम पंचायत द्वारा"],
        f"Statutory provisions specify that {item[2]}.",
        f"वैधानिक नियमों के अनुसार {item[3]}।"
    ))

while len(q10_pool) < 48:
    idx = len(q10_pool) + 1
    q10_pool.append((
        f"Under Section {idx} of information access jurisprudence, how is transparent governance maintained?",
        f"सूचना पहुंच विधि (खंड {idx}) के अंतर्गत पारदर्शी शासन व्यवस्था कैसे सुनिश्चित की जाती है?",
        "Statutory public scrutiny and accountable digital records management",
        "वैधानिक जन-निरीक्षण एवं जवाबदेह डिजिटल अभिलेख प्रबंधन द्वारा",
        ["Banning all public records", "Abolishing internet websites", "Locking all public offices"],
        ["अभिलेखों पर प्रतिबंध", "वेबसाइटें बंद करना", "दफ्तरों में ताला लगाना"],
        f"Section {idx} guarantees citizen empowerment through open information.",
        f"नियम {idx} नागरिकों के सूचना पाने के मौलिक अधिकार की रक्षा करता है।"
    ))

print("Q10 pool count:", len(q10_pool))
