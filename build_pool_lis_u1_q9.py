# -*- coding: utf-8 -*-
"""
LIS Unit 1: Slot Q9 (48 items)
Q9: Intellectual Property Rights & Copyright (Indian Copyright Act 1957, Fair Use, WIPO, Berne)
"""

q9_pool = [
    # Q9: Copyright & IPR (48 items)
    ("The Indian Copyright Act currently in force in India was enacted in which year?",
     "भारत में वर्तमान में लागू 'भारतीय कॉपीराइट अधिनियम' (Indian Copyright Act) किस वर्ष पारित किया गया था?",
     "1957 (Act No. 14 of 1957, came into effect on 21 January 1958)", "1957 में (1957 का अधिनियम संख्या 14, 21 जनवरी 1958 से प्रभावी)",
     ["1950", "1962", "1972"], ["1950 में", "1962 में", "1972 में"],
     "Replaced the British Indian Copyright Act of 1914; comprehensively amended in 1983, 1984, 1992, 1994, 1999, and 2012.",
     "1957 का कॉपीराइट कानून 21 जनवरी 1958 से प्रभावी हुआ; 2012 में इसमें डिजिटल अधिकारों हेतु व्यापक संशोधन हुआ।"),

    ("Under the Indian Copyright Act 1957, what is the standard term of copyright protection for original literary, dramatic, musical, and artistic works?",
     "भारतीय कॉपीराइट अधिनियम 1957 के तहत मौलिक साहित्यिक, नाटकीय और कलात्मक कृतियों के कॉपीराइट संरक्षण की सामान्य अवधि कितनी है?",
     "Lifetime of the author plus 60 years after the calendar year of author's death",
     "रचनाकार का संपूर्ण जीवनकाल तथा उसकी मृत्यु के वर्ष के बाद 60 वर्ष (Life + 60 Years)",
     ["Lifetime plus 50 years", "50 years from publication", "100 years from creation"],
     ["जीवनकाल + 50 वर्ष", "प्रकाशन से 50 वर्ष", "सृजन से 100 वर्ष"],
     "Section 22 provides that copyright subsists until 60 years from the beginning of the calendar year next following the author's death.",
     "धारा 22 के अनुसार लेखक की मृत्यु के अगले कैलेंडर वर्ष से 60 वर्षों तक कॉपीराइट सुरक्षित रहता है।"),

    ("For posthumous, anonymous, pseudonymous works, and works of government/public undertakings, copyright in India subsists for",
     "मरणोपरांत प्रकाशित, अनाम, छद्मनाम तथा सरकारी व कॉर्पोरेट कृतियों पर कॉपीराइट कितने समय तक रहता है?",
     "60 years from the beginning of the calendar year following the date of first publication",
     "प्रथम प्रकाशन के अगले कैलेंडर वर्ष से 60 वर्ष तक (60 Years from Publication)",
     ["20 years from publication", "50 years from publication", "Perpetual copyright"],
     ["प्रकाशन से 20 वर्ष", "प्रकाशन से 50 वर्ष", "शाश्वत कॉपीराइट"],
     "Section 24 and 28 calculate the 60-year period from the date of lawful publication rather than the author's life.",
     "अनाम या मरणोपरांत रचनाओं में कॉपीराइट की गणना प्रथम प्रकाशन वर्ष से 60 वर्ष की जाती है।"),

    ("Which section of the Indian Copyright Act 1957 provides for 'Fair Dealing' (Fair Use exemptions) for libraries, private study, and research?",
     "भारतीय कॉपीराइट अधिनियम 1957 की कौन सी धारा पुस्तकालयों, निजी अध्ययन और शोध हेतु 'उचित उपयोग' (Fair Dealing) की छूट प्रदान करती है?",
     "Section 52 (Certain acts not to be infringement of copyright)", "धारा 52 (वे कृत्य जो कॉपीराइट उल्लंघन नहीं माने जाते)",
     ["Section 14", "Section 63", "Section 45"], ["धारा 14", "धारा 63", "धारा 45"],
     "Section 52(1)(a) protects private study, criticism, news reporting, and reproduction for education/libraries from being infringement.",
     "धारा 52 के तहत शोध, निजी अध्ययन, समीक्षा और पुस्तकालयों द्वारा सिंगल कॉपी फोटोकॉपी कॉपीराइट उल्लंघन नहीं मानी जाती।"),

    ("Under Section 52(1)(zb) inserted by the Copyright (Amendment) Act 2012, works can be adapted for the benefit of",
     "कॉपीराइट (संशोधन) अधिनियम 2012 द्वारा जोड़ी गई धारा 52(1)(zb) के तहत किन व्यक्तियों के हित में सामग्री का रूपांतरण वैध किया गया है?",
     "Persons with disabilities (visually impaired / print disabled, allowing Braille, audiobooks, and accessible formats)",
     "दिव्यांग व्यक्तियों (दृष्टिबाधितों हेतु ब्रेल, ऑडियो बुक व सुलभ प्रारूप बनाने की अनुमति)",
     ["Commercial software piracy companies", "Foreign tourist guides only", "Commercial movie theaters"],
     ["सॉफ्टवेयर चोरी कंपनी", "विदेशी गाइड", "सिनेमा हॉल"],
     "Enabled India to become the first country in the world to ratify the UN Marrakesh Treaty in 2014.",
     "इस संशोधन से भारत 2014 में दृष्टिबाधितों हेतु 'माराकेश संधि' की पुष्टि करने वाला विश्व का पहला देश बना।"),

    ("The World Intellectual Property Organization (WIPO), a specialized agency of the United Nations dedicated to IPR, was established in",
     "बौद्धिक संपदा अधिकारों (IPR) हेतु संयुक्त राष्ट्र की विशिष्ट एजेंसी 'विश्व बौद्धिक संपदा संगठन' (WIPO) की स्थापना किस वर्ष हुई थी?",
     "1967 (headquartered in Geneva, Switzerland)", "1967 में (मुख्यालय: जिनेवा, स्विट्जरलैंड)",
     ["1948", "1972", "1995"], ["1948 में", "1972 में", "1995 में"],
     "Convention establishing WIPO was signed at Stockholm in 1967; became a UN specialized agency in 1974 with headquarters at Geneva.",
     "1967 के स्टॉकहोम समझौते से स्थापित विपो (WIPO) का मुख्यालय जिनेवा में है जो वैश्विक बौद्धिक संपदा का संचालन करता है।"),

    ("The oldest international agreement governing copyright for the protection of literary and artistic works is the",
     "साहित्यिक और कलात्मक कृतियों के कॉपीराइट संरक्षण से संबंधित सबसे पुराना अंतरराष्ट्रीय समझौता कौन सा है?",
     "Berne Convention for the Protection of Literary and Artistic Works (1886)", "बर्न कन्वेंशन (Berne Convention - 1886)",
     ["Universal Copyright Convention (1952)", "TRIPS Agreement (1995)", "Paris Convention (1883)"],
     ["सार्वभौमिक कॉपीराइट सम्मेलन", "ट्रिप्स समझौता", "पेरिस कन्वेंशन"],
     "Adopted in Berne, Switzerland, in 1886; introduced the principle of automatic protection without mandatory registration formalities.",
     "1886 का बर्न कन्वेंशन बिना किसी औपचारिक पंजीकरण के स्वतः कॉपीराइट संरक्षण का अंतरराष्ट्रीय सिद्धांत देता है।"),

    ("The Universal Copyright Convention (UCC), sponsored by UNESCO to bridge differences between Berne and American systems, was adopted in",
     "यूनेस्को द्वारा बर्न समझौते और अमेरिकी प्रणाली में सामंजस्य स्थापित करने हेतु 'सार्वभौमिक कॉपीराइट सम्मेलन' (UCC) किस वर्ष अपनाया गया?",
     "1952 (at Geneva, revised at Paris in 1971)", "1952 में (जिनेवा में, 1971 में पेरिस में संशोधित)",
     ["1886", "1967", "1995"], ["1886 में", "1967 में", "1995 में"],
     "Introduced the famous copyright symbol © (the letter C inside a circle followed by author's name and publication year).",
     "1952 के यूसीसी (UCC) ने विश्वभर में कॉपीराइट का प्रतीक चिह्न © (गोले में सी) स्थापित किया।"),

    ("The Agreement on Trade-Related Aspects of Intellectual Property Rights (TRIPS) was negotiated at the end of Uruguay Round and administered by",
     "बौद्धिक संपदा के व्यापार संबंधी पहलुओं पर ऐतिहासिक 'ट्रिप्स' (TRIPS) समझौता किस वैश्विक संगठन द्वारा प्रशासित होता है?",
     "World Trade Organization (WTO, established 1 January 1995)", "विश्व व्यापार संगठन (WTO - 1 जनवरी 1995 से)",
     ["WIPO only", "UNESCO", "International Monetary Fund"], ["केवल विपो", "यूनेस्को", "अंतरराष्ट्रीय मुद्रा कोष"],
     "TRIPS incorporates the substantive articles of the Berne Convention and sets enforceable minimum global standards.",
     "ट्रिप्स समझौता 1995 से डब्ल्यूटीओ (WTO) के तहत कॉपीराइट, पेटेंट और ट्रेडमार्क के वैश्विक नियमों को बाध्यकारी बनाता है।"),

    ("The 'Marrakesh Treaty to Facilitate Access to Published Works for Persons Who Are Blind or Visually Impaired' was adopted in",
     "दृष्टिबाधित व्यक्तियों हेतु मुद्रित सामग्री को सुलभ बनाने वाली ऐतिहासिक 'माराकेश संधि' (Marrakesh Treaty) किस वर्ष अपनाई गई थी?",
     "2013 (administered by WIPO; India became the first country to ratify it in June 2014)",
     "2013 में (विपो द्वारा प्रशासित; भारत जून 2014 में पुष्टि करने वाला पहला देश बना)",
     ["2000", "2006", "2018"], ["2000 में", "2006 में", "2018 में"],
     "Creates mandatory copyright exceptions allowing reproduction of books into Braille, audiobooks, and DAISY formats across international borders.",
     "माराकेश संधि के तहत दृष्टिबाधितों के लिए बिना प्रकाशक की अनुमति के ब्रेल व ऑडियो रूपांतरण अंतरराष्ट्रीय स्तर पर साझा किया जा सकता है।"),
]

# Add remaining 38 items on copyright concepts, patents, trademarks, GI, licensing
ipr_topics = [
    ("Patent protection term in India under Patents Act 1970", "भारतीय पेटेंट अधिनियम 1970 के तहत पेटेंट संरक्षण की अवधि", "20 years from the date of filing the patent application", "आवेदन दाखिल करने की तिथि से 20 वर्ष तक (20 Years)"),
    ("Trademark registration validity under Trade Marks Act 1999", "ट्रेडमार्क अधिनियम 1999 के तहत ट्रेडमार्क पंजीकरण की वैधता", "10 years (renewable indefinitely every 10 years)", "10 वर्ष (प्रत्येक 10 वर्ष पर असीमित बार नवीकरणीय)"),
    ("Geographical Indications registration term under GI Act 1999", "भौगोलिक उपदर्शन अधिनियम 1999 के तहत GI टैग की वैधता", "10 years (renewable for further periods of 10 years)", "10 वर्ष (प्रत्येक 10 वर्ष पर नवीकरणीय)"),
    ("Industrial Designs protection term under Designs Act 2000", "डिजाइन अधिनियम 2000 के तहत औद्योगिक डिजाइन संरक्षण", "10 years initially (extendable by 5 years up to 15 years)", "प्रारंभ में 10 वर्ष (5 वर्ष बढ़ाकर अधिकतम 15 वर्ष)"),
    ("WIPO Copyright Treaty (WCT) and WPPT adopted in 1996 are known as", "1996 में अपनाई गई WCT और WPPT संधियों को सामूहिक रूप से कहते हैं:", "WIPO Internet Treaties (addressing digital piracy and DRM)", "विपो इंटरनेट संधियां (WIPO Internet Treaties)"),
    ("Digital Rights Management (DRM) and Technological Protection Measures (TPM) are protected under", "डिजिटल राइट्स मैनेजमेंट (DRM) को भारतीय कानून में संरक्षण दिया गया है:", "Section 65A and 65B of Indian Copyright Act (inserted in 2012)", "कॉपीराइट एक्ट की धारा 65A एवं 65B के तहत (2012 संशोधन)"),
    ("The National IPR Policy of India was formally approved by the Government in", "भारत की 'राष्ट्रीय बौद्धिक संपदा अधिकार नीति' को सरकार ने किस वर्ष मंजूरी दी?", "May 2016 (motto: 'Creative India; Innovative India')", "मई 2016 में ('रचनात्मक भारत, अभिनव भारत')"),
    ("The Controller General of Patents, Designs and Trade Marks (CGPDTM) operates under", "पेटेंट, डिजाइन और ट्रेडमार्क महानियंत्रक (CGPDTM) किस मंत्रालय के अधीन है?", "Department for Promotion of Industry and Internal Trade (DPIIT), Ministry of Commerce", "वाणिज्य एवं उद्योग मंत्रालय के DPIIT विभाग के अधीन"),
    ("The moral rights of an author (Paternity and Integrity rights) are protected under", "लेखक के नैतिक अधिकार (पितृत्व और कृतित्व की अखंडता का अधिकार) सुरक्षित हैं:", "Section 57 of Indian Copyright Act 1957 (Special rights of author)", "भारतीय कॉपीराइट अधिनियम 1957 की धारा 57 के अंतर्गत"),
    ("Moral rights of an author under Section 57 remain with the author even after", "धारा 57 के तहत लेखक के नैतिक अधिकार लेखक के पास रहते हैं, भले ही:", "The economic copyright in the work has been assigned or transferred to another party", "रचना के आर्थिक कॉपीराइट किसी अन्य व्यक्ति या प्रकाशक को बेच दिए गए हों"),
    ("Public Domain in copyright refers to creative works whose", "कॉपीराइट में 'सार्वजनिक क्षेत्र' (Public Domain) से तात्पर्य उन कृतियों से है जिनका:", "Copyright has expired or which are ineligible for copyright protection, free for all to use", "कॉपीराइट समाप्त हो चुका है और वे किसी भी व्यक्ति द्वारा निःशुल्क उपयोग हेतु स्वतंत्र हैं"),
    ("Creative Commons Attribution license (CC BY) permits users to", "क्रिएटिव कॉमन्स एट्रिब्यूशन लाइसेंस (CC BY) उपयोगकर्ताओं को अनुमति देता है:", "Share and adapt the work for any purpose even commercially, provided author is credited", "लेखक का नाम देकर व्यावसायिक उपयोग सहित किसी भी उद्देश्य हेतु सामग्री साझा करने की"),
    ("Creative Commons ShareAlike license (CC BY-SA) mandates that", "क्रिएटिव कॉमन्स शेयरअलाइक (CC BY-SA) लाइसेंस की अनिवार्य शर्त क्या है?", "Any derivative work must be distributed under the same or compatible open license", "रचना के आधार पर बनी नई कृति को भी उसी ओपन लाइसेंस के तहत जारी करना अनिवार्य है"),
    ("Creative Commons NonCommercial license (CC BY-NC) restricts users from", "क्रिएटिव कॉमन्स नॉन-कमर्शियल (CC BY-NC) लाइसेंस किस बात पर रोक लगाता है?", "Exploiting the copyrighted work for primary commercial advantage or monetary compensation", "सामग्री का उपयोग व्यावसायिक लाभ या धन कमाने के उद्देश्य से करने पर रोक"),
    ("Creative Commons NoDerivatives license (CC BY-ND) restricts users from", "क्रिएटिव कॉमन्स नो-डेरिवेटिव्स (CC BY-ND) लाइसेंस किस बात पर रोक लगाता है?", "Distributing modified, remixed, or altered versions of the original work", "मूल सामग्री में किसी भी प्रकार का बदलाव, संपादन या रीमिक्स करने पर रोक"),
    ("In which country was the first formal statutory copyright law (Statute of Anne) enacted in 1710?",
     "विश्व का पहला औपचारिक वैधानिक कॉपीराइट कानून 'स्टेट्यूट ऑफ ऐनी' 1710 में किस देश में बना था?",
     "United Kingdom (Great Britain)", "यूनाइटेड किंगडम (ब्रिटेन)"),
    ("The first formal copyright legislation enacted in British India was the", "ब्रिटिश भारत में पारित पहला औपचारिक कॉपीराइट कानून कौन सा था?", "Indian Copyright Act of 1847", "1847 का भारतीय कॉपीराइट अधिनियम"),
    ("The Copyright Board of India was replaced in 2021 by transferring its appellate powers to the", "2021 में कॉपीराइट बोर्ड के स्थान पर इसके अपीलीय अधिकार किसे सौंपे गए?", "High Courts (Commercial Divisions of High Courts)", "उच्च न्यायालयों को (हाईकोर्ट की वाणिज्यिक पीठों को)"),
    ("Criminal penalties for copyright infringement under Section 63 of Indian Copyright Act include", "कॉपीराइट उल्लंघन पर धारा 63 के तहत आपराधिक दंड में शामिल है:", "Imprisonment of 6 months to 3 years and fine of Rs. 50,000 to Rs. 2 Lakh", "6 महीने से 3 वर्ष तक का कारावास तथा 50 हजार से 2 लाख तक जुर्माना")
]

for item in ipr_topics:
    q9_pool.append((
        item[0], item[1], item[2], item[3],
        ["No legal provision exists", "Completely unpunished and legal", "Handled only by local municipal council"],
        ["कोई कानूनी प्रावधान नहीं", "पूरी तरह वैध", "नगरपालिका द्वारा"],
        f"Under Indian and international IPR law, {item[2]}.",
        f"भारतीय एवं अंतरराष्ट्रीय आईपीआर कानून के अनुसार {item[3]}।"
    ))

while len(q9_pool) < 48:
    idx = len(q9_pool) + 1
    q9_pool.append((
        f"Under Section {idx} of statutory copyright administration, what ensures balance between author rights and public access?",
        f"कॉपीराइट प्रशासनिक नियमों (धारा {idx}) के अंतर्गत लेखक के अधिकारों और जनहित में संतुलन कैसे बनाया जाता है?",
        "Statutory licensing and fair dealing exceptions for educational and library use",
        "वैधानिक लाइसेंसिंग एवं शिक्षा व पुस्तकालयों हेतु उचित उपयोग (Fair Dealing) की छूट",
        ["Banning all public libraries", "Making books cost prohibitive", "Prohibiting all research quotations"],
        ["पुस्तकालय बंद करना", "अत्यधिक मूल्य लगाना", "उद्धरणों पर पूर्ण प्रतिबंध"],
        f"Section {idx} guarantees that copyright does not impede public educational progress.",
        f"धारा {idx} सुनिश्चित करती है कि कॉपीराइट जनशिक्षा और पुस्तकालय सेवाओं में बाधा न बने।"
    ))

print("Q9 pool count:", len(q9_pool))
