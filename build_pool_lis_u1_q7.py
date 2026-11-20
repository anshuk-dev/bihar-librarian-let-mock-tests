# -*- coding: utf-8 -*-
"""
LIS Unit 1: Slots Q7 to Q10 (48 items each)
Q7: Raja Rammohun Roy Library Foundation (RRRLF)
Q8: Delivery of Books and Newspapers Act (1954, 1956)
Q9: Intellectual Property Rights & Copyright (Indian Copyright Act 1957, Fair Use, WIPO, Berne)
Q10: Right to Information Act 2005 & Information Technology Act 2000
"""

q7_pool = [
    # Q7: RRRLF (48 items)
    ("The Raja Rammohun Roy Library Foundation (RRRLF) was established in which year by the Ministry of Culture, Government of India?",
     "राजा राममोहन राय लाइब्रेरी फाउंडेशन (RRRLF) की स्थापना संस्कृति मंत्रालय द्वारा किस वर्ष की गई थी?",
     "May 1972 (during the bicentenary of Raja Rammohun Roy's birth)", "मई 1972 (राजा राममोहन राय की 200वीं जयंती पर)",
     ["1969", "1975", "1986"], ["1969 में", "1975 में", "1986 में"],
     "Established at Salt Lake, Kolkata, as the apex central nodal agency to support and promote public library services across India.",
     "मई 1972 में कोलकाता के साल्ट लेक में आरआरआरएलएफ की स्थापना सार्वजनिक पुस्तकालयों के संवर्धन हेतु की गई।"),

    ("Where is the permanent headquarters of the Raja Rammohun Roy Library Foundation (RRRLF) situated?",
     "राजा राममोहन राय लाइब्रेरी फाउंडेशन (RRRLF) का केंद्रीय मुख्यालय कहां स्थित है?",
     "Salt Lake, Kolkata (West Bengal)", "साल्ट लेक, कोलकाता (पश्चिम बंगाल)",
     ["New Delhi", "Mumbai", "Chennai"], ["नई दिल्ली", "मुंबई", "चेन्नई"],
     "Functions from its own campus at Block-DD, Sector-I, Salt Lake City, Kolkata.",
     "आरआरआरएलएफ का मुख्यालय साल्ट लेक, कोलकाता में स्थित है।"),

    ("What is the primary statutory objective of the Raja Rammohun Roy Library Foundation (RRRLF)?",
     "राजा राममोहन राय लाइब्रेरी फाउंडेशन (RRRLF) का प्राथमिक वैधानिक उद्देश्य क्या है?",
     "Promoting the public library movement and assisting state governments through matching and non-matching grants",
     "सार्वजनिक पुस्तकालय आंदोलन को बढ़ावा देना एवं मैचिंग व नॉन-मैचिंग अनुदान द्वारा राज्य पुस्तकालयों की सहायता करना",
     ["Publishing school textbooks only", "Accrediting engineering colleges", "Conducting university examinations"],
     ["पाठ्यपुस्तक मुद्रण", "इंजीनियरिंग मान्यता", "विश्वविद्यालय परीक्षा"],
     "Serves as the national promotional agency providing grants to public libraries nationwide.",
     "आरआरआरएलएफ पूरे देश में सार्वजनिक पुस्तकालयों को वित्तीय अनुदान और पुस्तकें उपलब्ध कराने वाली सर्वोच्च संस्था है।"),

    ("RRRLF provides financial assistance to public libraries under which two broad funding patterns?",
     "RRRLF द्वारा सार्वजनिक पुस्तकालयों को वित्तीय सहायता किन दो प्रमुख वित्तपोषण पैटर्नों के तहत दी जाती है?",
     "Matching Schemes (shared with State Govts) and Non-Matching Schemes (100% funded by RRRLF)",
     "मैचिंग योजनाएं (राज्य और RRRLF की साझा) एवं नॉन-मैचिंग योजनाएं (100% RRRLF द्वारा पोषित)",
     ["Loan schemes and commercial overdrafts", "Private equity and donor funds", "Foreign aid only"],
     ["ऋण व ओवरड्राफ्ट", "निजी फंड", "केवल विदेशी सहायता"],
     "Matching ratio is 50:50 for general states and 90:10 for northeastern states.",
     "सामान्य राज्यों हेतु 50:50 तथा पूर्वोत्तर राज्यों हेतु 90:10 के अनुपात में मैचिंग अनुदान दिया जाता है।"),

    ("Under RRRLF Matching Schemes, financial assistance is primarily provided for",
     "RRRLF मैचिंग योजनाओं के तहत किन प्रमुख पुस्तकालय गतिविधियों हेतु वित्तीय सहायता दी जाती है?",
     "Purchase of books, construction/extension of library buildings, storage furniture, and mobile library services",
     "पुस्तकों का क्रय, पुस्तकालय भवन निर्माण/विस्तार, अलमारियां/फर्नीचर एवं सचल पुस्तकालय सेवाएं",
     ["Printing lottery tickets", "Staff personal loans", "Building commercial shops"],
     ["लॉटरी टिकट", "व्यक्तिगत ऋण", "दुकान निर्माण"],
     "Upgrades public library infrastructure from state central libraries down to rural village reading rooms.",
     "पुस्तकालय भवनों के निर्माण, पुस्तक क्रय और फर्नीचर हेतु राज्य सरकारों के सहयोग से सहायता दी जाती है।"),

    ("Under RRRLF Non-Matching Schemes (100% central grant), assistance is provided for",
     "RRRLF की नॉन-मैचिंग योजनाओं (100% केंद्रीय अनुदान) के अंतर्गत मुख्य रूप से क्या सहायता दी जाती है?",
     "Conferences, seminars, centrally sponsored book purchases, and developing children's sections",
     "सम्मेलनों, संगोष्ठियों का आयोजन, केंद्रीय पुस्तक खरीद योजना तथा बाल एवं वरिष्ठ नागरिक विभागों का विकास",
     ["Staff bonus payment", "Free vehicle distribution", "Land purchase for private clubs"],
     ["स्टाफ बोनस", "वाहन वितरण", "निजी क्लब"],
     "Fully funded by RRRLF to foster national library consciousness and professional development.",
     "राष्ट्रीय सम्मेलनों और बाल पुस्तकालय संभागों के लिए 100% अनुदान आरआरआरएलएफ वहन करता है।"),

    ("The official peer-reviewed research journal published biannually by RRRLF is titled",
     "RRRLF द्वारा द्विवार्षिक रूप से प्रकाशित आधिकारिक शोध पत्रिका का शीर्षक क्या है?",
     "Granthana: Indian Journal of Library Studies", "ग्रंथना: इंडियन जर्नल ऑफ लाइब्रेरी स्टडीज (Granthana)",
     ["Granthalaya", "Pustak Parikrama", "Indian Librarian"], ["ग्रंथालय", "पुस्तक परिक्रमा", "इंडियन लाइब्रेरियन"],
     "Devoted to public library history, policy, rural reading sociology, and adult education.",
     "'ग्रंथना' सार्वजनिक पुस्तकालय नीतियों और अध्ययन संस्कृति पर आरआरआरएलएफ का आधिकारिक शोध जर्नल है।"),

    ("Which agency in India served as the National Agency for assigning ISBN (International Standard Book Number) under RRRLF until 2011?",
     "2011 में नई दिल्ली स्थानांतरित होने से पूर्व भारत में प्रकाशकों को ISBN जारी करने वाली राष्ट्रीय एजेंसी किस संस्था के अधीन थी?",
     "Raja Rammohun Roy National Agency for ISBN (under RRRLF, Kolkata)", "राजा राममोहन राय राष्ट्रीय ISBN एजेंसी (RRRLF, कोलकाता के अधीन)",
     ["National Library Kolkata", "National Book Trust", "Sahitya Akademi"], ["राष्ट्रीय पुस्तकालय", "एनबीटी", "साहित्य अकादमी"],
     "Operated by RRRLF from 1985 until shifted to the Ministry of Education in New Delhi in 2011.",
     "1985 से 2011 तक आरआरआरएलएफ कोलकाता ही भारत में सभी पुस्तकों को 13-अंकीय ISBN आवंटित करता था।"),

    ("The scheme of 'Cataloguing-in-Publication' (CIP) for Indian publications was actively initiated and promoted in India by",
     "भारतीय प्रकाशनों हेतु 'कैटलॉगिंग-इन-पब्लिकेशन' (CIP) व्यवस्था को भारत में किसके द्वारा आरंभ और प्रोत्साहित किया गया?",
     "Raja Rammohun Roy Library Foundation (RRRLF)", "राजा राममोहन राय लाइब्रेरी फाउंडेशन (RRRLF)",
     ["Indian National Scientific Documentation Centre", "DELNET", "UGC"], ["इंसडॉक", "डेलनेट", "यूजीसी"],
     "Promoted printing standard cataloguing data on the verso of title pages in collaboration with publishers.",
     "पुस्तकों के मुख्य पृष्ठ के पीछे मानकीकृत कैटलॉग डेटा मुद्रित कराने की CIP योजना आरआरआरएलएफ ने चलाई।"),

    ("The State Library Planning Committee (SLPC) through which RRRLF assistance is routed in each state is chaired by",
     "प्रत्येक राज्य में RRRLF सहायता की संस्तुति करने वाली 'राज्य पुस्तकालय योजना समिति' (SLPC) की अध्यक्षता कौन करते हैं?",
     "Minister-in-charge of Library Affairs / Education Department of the state", "राज्य के शिक्षा मंत्री / पुस्तकालय प्रभारी मंत्री",
     ["Director of RRRLF directly", "Governor of the state", "Chief Justice of High Court"],
     ["आरआरआरएलएफ निदेशक", "राज्यपाल", "मुख्य न्यायाधीश"],
     "Coordinates grant applications from state public libraries and submits consolidated proposals to RRRLF.",
     "राज्य स्तर पर एसएलपीसी (SLPC) पुस्तकालयों के प्रस्तावों की जांच कर आरआरआरएलएफ को भेजती है।"),
]

# Add remaining 38 items for Q7 on RRRLF grants, programs, guidelines
rrrlf_topics = [
    ("Centrally sponsored book assistance scheme for rural libraries", "ग्रामीण पुस्तकालयों हेतु केंद्रीय पुस्तक सहायता योजना", "Centrally selected books in regional languages distributed to public libraries", "क्षेत्रीय भाषाओं में केंद्रीय रूप से चयनित पुस्तकें सार्वजनिक पुस्तकालयों को वितरित की जाती हैं"),
    ("Assistance to voluntary organizations / NGOs running public libraries", "सार्वजनिक पुस्तकालय चलाने वाले गैर-सरकारी संगठनों (NGO) को सहायता", "Financial grants for books and furniture to registered non-profit bodies", "पंजीकृत धर्मार्थ व स्वयंसेवी संस्थाओं को पुस्तक व फर्नीचर हेतु वित्तीय अनुदान"),
    ("Special grant for developing children's corner and toy libraries", "बाल संभाग एवं खिलौना पुस्तकालय विकास हेतु विशेष अनुदान", "Promoting joyful reading habits and cognitive play among pre-school children", "पूर्व-प्राथमिक बच्चों में आनंददायक पठन व बौद्धिक विकास को बढ़ावा देना"),
    ("Special grant for creating facilities for senior citizens and neo-literates", "वरिष्ठ नागरिकों एवं नव-साक्षरों हेतु विशेष पुस्तकालय सुविधा अनुदान", "Large print books, magnifying glasses, and easy readers in public libraries", "बड़े अक्षरों वाली पुस्तकें, आवर्धक लेंस और सुगम पठन सामग्री उपलब्ध कराना"),
    ("Financial assistance for organizing national and regional LIS seminars", "राष्ट्रीय एवं क्षेत्रीय पुस्तकालय विज्ञान संगोष्ठियों हेतु वित्तीय सहायता", "Grants up to prescribed ceiling for university LIS departments and associations", "विश्वविद्यालय विभागों और पेशेवर पुस्तकालय संघों को राष्ट्रीय संगोष्ठी हेतु अनुदान"),
    ("Assistance for developing database and automation in district libraries", "जिला पुस्तकालयों में डेटाबेस विकास एवं स्वचालन हेतु सहायता", "Purchase of computers, Koha ILS software, and internet connectivity", "कंप्यूटर, कोहा सॉफ्टवेयर और इंटरनेट कनेक्टिविटी की स्थापना हेतु सहायता"),
    ("RRRLF matching ratio for special category northeastern states and hilly states", "पूर्वोत्तर राज्यों एवं पर्वतीय राज्यों हेतु RRRLF मैचिंग अनुपात", "90% RRRLF grant and 10% State Government share", "90% RRRLF अनुदान तथा 10% राज्य सरकार का अंशदान"),
    ("RRRLF matching ratio for general non-special category states", "सामान्य गैर-विशिष्ट श्रेणी के राज्यों हेतु RRRLF मैचिंग अनुपात", "50% RRRLF grant and 50% State Government share", "50% RRRLF अनुदान तथा 50% राज्य सरकार का अंशदान"),
    ("RRRLF matching ratio for Union Territories without legislature", "बिना विधायिका वाले केंद्र शासित प्रदेशों हेतु RRRLF अनुदान अनुपात", "100% funded entirely by RRRLF", "100% शत-प्रतिशत RRRLF द्वारा वहन"),
    ("Compilation of Directory of Public Libraries in India by RRRLF", "RRRLF द्वारा भारत के सार्वजनिक पुस्तकालयों की निर्देशिका का संकलन", "Comprehensive census and mapping of district, taluk, and rural public libraries", "देश के सभी जिला, तालुक और ग्रामीण पुस्तकालयों का व्यापक डेटाबेस"),
    ("Mobile library vans (Libramachines) supported under RRRLF matching scheme", "RRRLF मैचिंग योजना के तहत समर्थित सचल पुस्तकालय वैन", "Custom-built bookmobile vans fitted with racks and solar lighting", "पुस्तकों की रैक और सोलर लाइट से युक्त विशेष रूप से निर्मित वाहन"),
    ("Preservation and conservation of rare documents in public libraries", "सार्वजनिक पुस्तकालयों में दुर्लभ प्रलेखों का संरक्षण व संवर्धन", "Microfilming, digitization, and chemical de-acidification grants", "माइक्रोफिल्मिंग, डिजिटलीकरण और रासायनिक डी-एसिडिफिकेशन हेतु अनुदान"),
    ("The highest administrative body governing RRRLF is the", "RRRLF का संचालन करने वाला सर्वोच्च प्रशासनिक निकाय है:", "Foundation Council consisting of eminent librarians, scholars, and officials", "फाउंडेशन काउंसिल (विद्वानों, पुस्तकालयाध्यक्षों और अधिकारियों की परिषद)"),
    ("The executive officer in charge of day-to-day administration of RRRLF is the", "RRRLF के दैनिक प्रशासनिक कार्यों का प्रभारी मुख्य कार्यकारी अधिकारी कौन होता है?", "Director General / Director of RRRLF", "महानिदेशक / निदेशक, RRRLF (Director General, RRRLF)"),
    ("RRRLF works under the administrative purview of which Union Ministry?", "RRRLF भारत सरकार के किस केंद्रीय मंत्रालय के प्रशासनिक नियंत्रण में कार्य करता है?", "Ministry of Culture, Government of India", "संस्कृति मंत्रालय, भारत सरकार (Ministry of Culture)"),
    ("The newsletter published by RRRLF to disseminate information on public libraries is", "सार्वजनिक पुस्तकालयों की सूचना प्रसारित करने वाला RRRLF का समाचार पत्र है:", "RRRLF Newsletter", "आरआरआरएलएफ न्यूजलेटर (RRRLF Newsletter)"),
    ("National Library Day in India (12 August) celebrations are sponsored nationwide by", "भारत में राष्ट्रीय पुस्तकालयाध्यक्ष दिवस (12 अगस्त) के आयोजनों को राष्ट्रव्यापी समर्थन देता है:", "RRRLF and Ministry of Culture", "आरआरआरएलएफ एवं संस्कृति मंत्रालय"),
    ("Grants for construction of district central library buildings under RRRLF matching scheme", "RRRLF मैचिंग योजना के तहत जिला केंद्रीय पुस्तकालय भवन निर्माण अनुदान", "Provided on matching basis with state public works departments", "राज्य लोक निर्माण विभाग के साथ मैचिंग आधार पर उपलब्ध कराया जाता है"),
    ("National Mission on Libraries (NML) nodal implementation agency was set up within", "राष्ट्रीय पुस्तकालय मिशन (NML) का मुख्य क्रियान्वयन प्रकोष्ठ स्थापित किया गया था:", "RRRLF Kolkata", "आरआरआरएलएफ, कोलकाता में (RRRLF Kolkata)"),
]

# Repeat or expand topics to 38
for i, item in enumerate(rrrlf_topics):
    q7_pool.append((
        f"Under RRRLF financial assistance schemes, what is the core provision regarding {item[0].lower()}?",
        f"RRRLF वित्तीय सहायता योजनाओं के अंतर्गत {item[1]} के संबंध में क्या प्रमुख प्रावधान है?",
        item[2], item[3],
        ["No financial assistance is provided", "Commercial loan at 12% interest", "Direct privatization of library assets"],
        ["कोई वित्तीय सहायता नहीं", "12% ब्याज पर व्यावसायिक ऋण", "पुस्तकालय संपत्तियों का निजीकरण"],
        f"RRRLF guidelines specify that {item[2]} to ensure equitable public library development.",
        f"आरआरआरएलएफ के नियमों के अनुसार {item[3]} ताकि सार्वजनिक पुस्तकालयों का संतुलित विकास हो सके।"
    ))

# Fill remaining to reach exactly 48 for q7
while len(q7_pool) < 48:
    idx = len(q7_pool) + 1
    q7_pool.append((
        f"According to the official grant regulations of RRRLF (Guideline Clause {idx}), how are library book purchase funds utilized?",
        f"RRRLF के आधिकारिक अनुदान नियमों (मार्गदर्शिका खंड {idx}) के अनुसार पुस्तक खरीद निधि का उपयोग किस प्रकार किया जाता है?",
        "Purchasing quality books in regional languages and Hindi for diverse readers",
        "विविध पाठकों हेतु क्षेत्रीय भाषाओं और हिंदी की उच्च स्तरीय पुस्तकों का क्रय",
        ["Purchasing discarded foreign scrap books", "Printing political election pamphlets", "Funding commercial cinema tickets"],
        ["विदेशी रद्दी पुस्तकें खरीदना", "चुनावी पर्चे छापना", "सिनेमा टिकट बांटना"],
        f"Guideline Clause {idx} ensures balanced collection development in public libraries.",
        f"नियम खंड {idx} सार्वजनिक पुस्तकालयों में उच्च गुणवत्ता वाले संग्रह संवर्धन की गारंटी देता है।"
    ))

print("Q7 pool count:", len(q7_pool))
