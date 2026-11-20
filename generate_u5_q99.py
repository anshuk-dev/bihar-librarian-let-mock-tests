# -*- coding: utf-8 -*-
"""
Generator for Slot Q99: Electronic Resource Management (ERM) & Usage Standards - 48 items.
"""

q99_items = [
    # 1: ERMS definition & necessity
    ("Why did academic libraries find it necessary to implement dedicated Electronic Resource Management Systems (ERMS)?",
     "अकादमिक पुस्तकालयों को समर्पित इलेक्ट्रॉनिक संसाधन प्रबंधन प्रणाली (ERMS) लागू करना क्यों आवश्यक लगा?",
     "Traditional Integrated Library Systems (ILS) were designed for physical inventory and could not manage complex digital licensing terms, proxy access, OpenURL resolvers, and renewal workflows",
     "पारंपरिक एकीकृत पुस्तकालय प्रणालियाँ (ILS) भौतिक इन्वेंट्री के लिए डिज़ाइन की गई थीं और जटिल डिजिटल लाइसेंसिंग शर्तों, प्रॉक्सी पहुँच, OpenURL रिज़ॉल्वर और नवीनीकरण कार्यप्रवाह का प्रबंधन नहीं कर सकती थीं",
     ["Because university rules mandate that every department must buy identical duplicate software", "Because ERMS platforms are incapable of displaying text on internet browsers", "Because physical books were completely outlawed by international copyright treaties"],
     ["क्योंकि विश्वविद्यालय के नियम अनिवार्य करते हैं कि प्रत्येक विभाग को समान डुप्लिकेट सॉफ्टवेयर खरीदना चाहिए", "क्योंकि ERMS प्लेटफॉर्म इंटरनेट ब्राउज़रों पर टेक्स्ट प्रदर्शित करने में असमर्थ हैं", "क्योंकि भौतिक पुस्तकों को अंतरराष्ट्रीय कॉपीराइट संधियों द्वारा पूरी तरह से गैरकानूनी घोषित कर दिया गया था"],
     "ERMS tracks the entire non-physical lifecycle: vendor contacts, multi-year license rights, IP ranges, coverage dates, and administrative passwords across thousands of journal packages.",
     "पारंपरिक ILS केवल भौतिक किताबों की शेल्फ और संचलन का हिसाब रखता था; ई-जर्नल्स के जटिल लाइसेंस, आईपी रेंज, एक्सेस अधिकार और रिन्यूअल की तारीखों को संभालने के लिए ERMS की आवश्यकता पड़ी।"),

    # 2: DLF ERMI
    ("Which initiative launched between 2001 and 2004 by the Digital Library Federation established the foundational conceptual data model for ERM systems?",
     "डिजिटल लाइब्रेरी फेडरेशन द्वारा 2001 और 2004 के बीच शुरू की गई किस पहल ने ERM प्रणालियों के लिए मूलभूत वैचारिक डेटा मॉडल स्थापित किया?",
     "DLF ERMI (Electronic Resource Management Initiative)",
     "DLF ERMI (इलेक्ट्रॉनिक रिसोर्स मैनेजमेंट इनिशिएटिव)",
     ["W3C Semantic Web Initiative", "UNESCO Memory of the World", "NISO Z39.50 Standard Group"],
     ["W3C सिमेंटिक वेब इनिशिएटिव", "यूनेस्को मेमोरी ऑफ द वर्ल्ड", "NISO Z39.50 मानक समूह"],
     "The DLF ERMI report established the definitive functional requirements, data dictionaries, and lifecycle workflows that guided all modern commercial and open-source ERM platforms.",
     "DLF ERMI (2001-2004) ने सबसे पहले ई-रिसोर्स मैनेजमेंट का पूरा डेटा मॉडल और कार्यप्रणाली का खाका तैयार किया, जिस पर आज के सभी ERM सॉफ्टवेयर आधारित हैं।"),

    # 3: Electronic Resource Lifecycle
    ("What are the primary progressive stages comprising the complete Electronic Resource Lifecycle in academic libraries?",
     "अकादमिक पुस्तकालयों में संपूर्ण इलेक्ट्रॉनिक संसाधन जीवनचक्र में कौन से प्राथमिक प्रगतिशील चरण शामिल हैं?",
     "Discovery/Trial -> Evaluation -> License Negotiation -> Procurement -> Technical Setup -> Access/Maintenance -> Usage Evaluation -> Renewal/Cancellation",
     "खोज/परीक्षण -> मूल्यांकन -> लाइसेंस वार्ता -> खरीद -> तकनीकी सेटअप -> पहुँच/रखरखाव -> उपयोग मूल्यांकन -> नवीनीकरण/रद्द करना",
     ["Printing -> Binding -> Stamping -> Shelving -> Dusting -> Discarding", "Authoring -> Peer Review -> Typesetting -> Printing -> Shipping", "Classifying -> Cataloging -> Barcoding -> Book Dropping -> Shredding"],
     ["छपाई -> बाइंडिंग -> मुहर लगाना -> शेल्फिंग -> धूल झाड़ना -> त्यागना", "लेखन -> सहकर्मी समीक्षा -> टाइपसेटिंग -> छपाई -> शिपिंग", "वर्गीकरण -> कैटलॉगिंग -> बारकोडिंग -> बुक ड्रॉपिंग -> श्रेडिंग"],
     "Unlike physical books that are bought once and shelved, e-resources require ongoing active management across technical, financial, and legal dimensions throughout their life cycle.",
     "ई-रिसोर्स का जीवनचक्र एक निरंतर चलने वाला चक्र है: ट्रायल लेना, कीमत और लाइसेंस पर बातचीत, आईपी सेटअप, उपयोग के आंकड़े देखना और फिर अगले साल रिन्यू या कैंसिल करने का निर्णय लेना।"),

    # 4: COUNTER Project Purpose
    ("What is the primary mission of the 'COUNTER' (Counting Online Usage of NeTworked Electronic Resources) initiative?",
     "'काउंटर' (COUNTER - Counting Online Usage of NeTworked Electronic Resources) पहल का प्राथमिक मिशन क्या है?",
     "Providing an international standard code of practice ensuring libraries receive credible, consistent, and directly comparable vendor-supplied online usage statistics",
     "एक अंतरराष्ट्रीय मानक आचार संहिता प्रदान करना जो यह सुनिश्चित करता है कि पुस्तकालयों को विश्वसनीय, सुसंगत और सीधे तुलना योग्य विक्रेता-आपूर्ति वाले ऑनलाइन उपयोग के आंकड़े प्राप्त हों",
     ["Selling commercial barcodes and scanner hardware to private corporations", "Managing physical circulation checkouts and borrower fines at university circulation desks", "Calculating late fine surcharges for overdue books in school libraries"],
     ["निजी निगमों को वाणिज्यिक बारकोड और स्कैनर हार्डवेयर बेचना", "विश्वविद्यालय संचलन डेस्क पर भौतिक संचलन चेकआउट और उधारकर्ता जुर्माने का प्रबंधन करना", "स्कूल पुस्तकालयों में अतिदेय पुस्तकों के लिए विलंब शुल्क अधिभार की गणना करना"],
     "Before COUNTER, every publisher reported usage differently (e.g. counting simple clicks as downloads); COUNTER guarantees audited, apples-to-apples usage metrics.",
     "COUNTER से पहले हर प्रकाशक अपने हिसाब से बढ़ा-चढ़ाकर आंकड़े देता था; COUNTER ने अंतरराष्ट्रीय मानक बनाए ताकि यह सही-सही पता चल सके कि किस जर्नल को सचमुच कितनी बार पढ़ा या डाउनलोड किया गया।"),

    # 5: COUNTER Release 5 Master Reports
    ("Which of the following represents the four flexible 'Master Reports' introduced in COUNTER Code of Practice Release 5 (R5)?",
     "निम्नलिखित में से कौन सा COUNTER कोड ऑफ प्रैक्टिस रिलीज़ 5 (R5) में पेश की गई चार लचीली 'मास्टर रिपोर्टों' का प्रतिनिधित्व करता है?",
     "Title Master Report (TR), Platform Master Report (PR), Database Master Report (DR), and Item Master Report (IR)",
     "टाइटल मास्टर रिपोर्ट (TR), प्लेटफॉर्म मास्टर रिपोर्ट (PR), डेटाबेस मास्टर रिपोर्ट (DR), और आइटम मास्टर रिपोर्ट (IR)",
     ["Book Report 1, Book Report 2, Journal Report 1, and Journal Report 2", "Annual Report, Monthly Report, Weekly Report, and Daily Report", "Alpha Report, Beta Report, Gamma Report, and Delta Report"],
     ["बुक रिपोर्ट 1, बुक रिपोर्ट 2, जर्नल रिपोर्ट 1, और जर्नल रिपोर्ट 2", "वार्षिक रिपोर्ट, मासिक रिपोर्ट, साप्ताहिक रिपोर्ट, और दैनिक रिपोर्ट", "अल्फा रिपोर्ट, बीटा रिपोर्ट, गामा रिपोर्ट, और डेल्टा रिपोर्ट"],
     "COUNTER Release 5 restructured reporting into four comprehensive Master Reports with filtered Standard Views (e.g. TR_J1, TR_B1) to dramatically simplify reporting.",
     "COUNTER Release 5 में 4 मुख्य मास्टर रिपोर्ट होती हैं: TR (किताबों और जर्नल्स के टाइटल के लिए), PR (प्लेटफॉर्म के लिए), DR (डेटाबेस के लिए), और IR (व्यक्तिगत आर्टिकल्स के लिए)।"),

    # 6: COUNTER R5 TR_J1 Standard View
    ("In COUNTER Release 5, what does the Standard View 'TR_J1' specifically track?",
     "COUNTER रिलीज़ 5 में, मानक दृश्य 'TR_J1' विशेष रूप से क्या ट्रैक करता है?",
     "Journal requests (PDF and HTML full text) excluding Gold Open Access usage, filtered by month",
     "गोल्ड ओपन एक्सेस उपयोग को छोड़कर जर्नल अनुरोध (PDF और HTML पूर्ण पाठ), महीने के अनुसार फ़िल्टर किया गया",
     ["Book chapter downloads across university digital libraries", "Total searches executed on electronic database search engines", "Physical attendance counts at academic reference assistance desks"],
     ["विश्वविद्यालय के डिजिटल पुस्तकालयों में पुस्तक अध्याय डाउनलोड", "इलेक्ट्रॉनिक डेटाबेस खोज इंजनों पर निष्पादित कुल खोजें", "अकादमिक संदर्भ सहायता डेस्क पर भौतिक उपस्थिति की गणना"],
     "TR_J1 ('Journal Requests Excluding OA_Gold') measures paid subscription journal utility, providing the exact usage numbers needed to calculate cost-per-use during renewals.",
     "TR_J1 रिपोर्ट यह दिखाती है कि पुस्तकालय द्वारा पैसे देकर खरीदे गए जर्नल्स के कितने आर्टिकल्स (HTML/PDF) पढ़े गए (मुफ्त ओपन एक्सेस वाले हटाकर), जिससे रिन्यूअल के समय सही लागत का पता चलता है।"),

    # 7: Investigations vs Requests in COUNTER R5
    ("What is the crucial analytical distinction between an 'Investigation' and a 'Request' in COUNTER Release 5?",
     "COUNTER रिलीज़ 5 में 'इन्वेस्टिगेशन' (Investigation) और 'रिक्वेस्ट' (Request) के बीच महत्वपूर्ण विश्लेषणात्मक अंतर क्या है?",
     "An Investigation counts any interaction with an item (viewing abstract, citation, or full text); a Request counts specifically viewing or downloading the actual full-text content",
     "एक इन्वेस्टिगेशन किसी वस्तु के साथ किसी भी बातचीत (सार, उद्धरण, या पूर्ण पाठ देखना) की गणना करता है; एक रिक्वेस्ट विशेष रूप से वास्तविक पूर्ण-पाठ सामग्री को देखने या डाउनलोड करने की गणना करता है",
     ["An Investigation is performed by police detectives, while a Request is submitted by library students", "An Investigation applies only to print paper books, while a Request applies only to digital files", "An Investigation measures internet bandwidth, while a Request measures server processor speed"],
     ["एक इन्वेस्टिगेशन पुलिस जासूसों द्वारा की जाती है, जबकि एक रिक्वेस्ट पुस्तकालय के छात्रों द्वारा प्रस्तुत की जाती है", "एक इन्वेस्टिगेशन केवल प्रिंट पेपर किताबों पर लागू होता है, जबकि एक रिक्वेस्ट केवल डिजिटल फाइलों पर लागू होता है", "एक इन्वेस्टिगेशन इंटरनेट बैंडविड्थ को मापता है, जबकि एक रिक्वेस्ट सर्वर प्रोसेसर की गति को मापता है"],
     "Investigations reflect total discovery and user interest; Requests represent actual consumptive access to the full-text research article or book chapter.",
     "Investigation का मतलब है कि छात्र ने आर्टिकल का केवल एब्स्ट्रैक्ट या शीर्षक देखा; जबकि Request का मतलब है कि उसने पूरा शोध पत्र (Full-text PDF या HTML) खोलकर पढ़ा या डाउनलोड किया।"),

    # 8: Unique vs Total Metrics in COUNTER R5
    ("Why did COUNTER Release 5 introduce 'Unique_Item_Requests' alongside 'Total_Item_Requests'?",
     "COUNTER रिलीज़ 5 ने 'Total_Item_Requests' के साथ 'Unique_Item_Requests' क्यों पेश किया?",
     "To eliminate double-counting when a patron downloads both HTML and PDF versions of the same article or repeatedly clicks download within the same user session",
     "जब कोई संरक्षक एक ही लेख के HTML और PDF दोनों संस्करणों को डाउनलोड करता है या एक ही उपयोगकर्ता सत्र के भीतर बार-बार डाउनलोड क्लिक करता है, तो दोहरी गिनती को समाप्त करने के लिए",
     ["To force publishers to issue financial refunds for slow internet loading speeds", "To prevent library patrons from sharing research links on academic social networks", "To measure the physical battery depletion of mobile smartphones opening electronic journals"],
     ["धीमी इंटरनेट लोडिंग गति के लिए प्रकाशकों को वित्तीय धनवापसी जारी करने के लिए मजबूर करना", "पुस्तकालय संरक्षकों को अकादमिक सोशल नेटवर्क पर शोध लिंक साझा करने से रोकने के लिए", "इलेक्ट्रॉनिक पत्रिकाओं को खोलने वाले मोबाइल स्मार्टफोन की भौतिक बैटरी की कमी को मापना"],
     "Unique_Item_Requests counts multiple downloads of the same article within a session as exactly one request, providing a much cleaner metric of true scholarly demand.",
     "यदि कोई छात्र एक ही सेशन में एक ही पेपर का HTML भी खोलता है और PDF भी डाउनलोड करता है, तो Unique Request उसे 2 के बजाय 1 ही गिनता है, जिससे आंकड़े बिल्कुल सटीक रहते हैं।"),

    # 9: SUSHI Protocol (ANSI/NISO Z39.93)
    ("What is the primary function of the 'SUSHI' protocol (Standardized Usage Statistics Harvesting Initiative - ANSI/NISO Z39.93)?",
     "'SUSHI' प्रोटोकॉल (Standardized Usage Statistics Harvesting Initiative - ANSI/NISO Z39.93) का प्राथमिक कार्य क्या है?",
     "Automating the machine-to-machine harvesting and delivery of COUNTER usage reports directly into library ERM systems using RESTful web services",
     "RESTful वेब सेवाओं का उपयोग करके सीधे पुस्तकालय ERM प्रणालियों में COUNTER उपयोग रिपोर्टों के मशीन-से-मशीन संचयन और वितरण को स्वचालित करना",
     ["A Japanese culinary standard governing the preparation of seafood in university cafeterias", "A hardware network cable standard connecting library computers to local printers", "An encryption algorithm used to secure bank credit card transactions over the internet"],
     ["विश्वविद्यालय कैफेटेरिया में समुद्री भोजन तैयार करने को नियंत्रित करने वाला एक जापानी पाक मानक", "पुस्तकालय कंप्यूटरों को स्थानीय प्रिंटर से जोड़ने वाला एक हार्डवेयर नेटवर्क केबल मानक", "इंटरनेट पर बैंक क्रेडिट कार्ड लेनदेन को सुरक्षित करने के लिए उपयोग किया जाने वाला एक एन्क्रिप्शन एल्गोरिदम"],
     "SUSHI frees librarians from manually logging into hundreds of publisher websites every month to download CSV files, automatically fetching COUNTER data via APIs.",
     "SUSHI प्रोटोकॉल (ANSI/NISO Z39.93) लाइब्रेरियन को सैकड़ों प्रकाशकों की वेबसाइटों पर अलग-अलग लॉगिन करके फाइलें डाउनलोड करने के झंझट से मुक्ति देता है; यह API से आंकड़े खुद मंगवा लेता है।"),

    # 10: KBART Standard (NISO RP-9-2014)
    ("What is the purpose of the 'KBART' (Knowledge Bases And Related Tools) recommended practice published by NISO?",
     "NISO द्वारा प्रकाशित 'KBART' (Knowledge Bases And Related Tools) अनुशंसित अभ्यास का उद्देश्य क्या है?",
     "Standardizing the formatting and exchange of title lists and coverage metadata between content providers and link resolver knowledge bases",
     "सामग्री प्रदाताओं और लिंक रिज़ॉल्वर ज्ञान अड्डों के बीच शीर्षक सूचियों और कवरेज मेटाडेटा के स्वरूपण और आदान-प्रदान का मानकीकरण करना",
     ["Calculating annual income tax deductions for university professors publishing monographs", "Setting physical dimension specifications for library book return drop boxes", "A software protocol for streaming high-definition audio recordings across local networks"],
     ["मोनोग्राफ प्रकाशित करने वाले विश्वविद्यालय के प्रोफेसरों के लिए वार्षिक आयकर कटौती की गणना करना", "पुस्तकालय पुस्तक वापसी ड्रॉप बॉक्स के लिए भौतिक आयाम विनिर्देश निर्धारित करना", "स्थानीय नेटवर्क पर उच्च-परिभाषा ऑडियो रिकॉर्डिंग स्ट्रीमिंग के लिए एक सॉफ्टवेयर प्रोटोकॉल"],
     "KBART establishes strict tab-delimited file structures (title, ISSN, eISSN, start/end dates, URL) ensuring link resolvers accurately reflect publisher package contents.",
     "KBART एक मानकीकृत तालिका प्रारूप (TSV/Excel) है जिसके माध्यम से प्रकाशक अपने जर्नल्स की पूरी सूची, ISSN और कवरेज तिथियाँ लिंक रिज़ॉल्वर को देते हैं ताकि सही लिंक खुल सके।"),

    # 11: OpenURL (ANSI/NISO Z39.88)
    ("In digital scholarly linking, how does 'OpenURL' (ANSI/NISO Z39.88) operate?",
     "डिजिटल विद्वत्तापूर्ण लिंकिंग में 'OpenURL' (ANSI/NISO Z39.88) कैसे काम करता है?",
     "It packages citation metadata into a standardized URL query string and transports it to a library link resolver to dynamically locate full-text copies",
     "यह उद्धरण मेटाडेटा को एक मानकीकृत URL क्वेरी स्ट्रिंग में पैकेज करता है और पूर्ण-पाठ प्रतियों को गतिशील रूप से खोजने के लिए इसे पुस्तकालय लिंक रिज़ॉल्वर तक पहुंचाता है",
     ["It permanently removes all subscription paywalls from commercial scientific databases", "It forces web browsers to delete patron cookies and history after every search session", "It compiles computer source code into executable binary applications automatically"],
     ["यह वाणिज्यिक वैज्ञानिक डेटाबेस से सभी सदस्यता पेवॉल को स्थायी रूप से हटा देता है", "यह प्रत्येक खोज सत्र के बाद वेब ब्राउज़रों को संरक्षक कुकीज़ और इतिहास को हटाने के लिए मजबूर करता है", "यह कंप्यूटर स्रोत कोड को निष्पादित करने योग्य बाइनरी अनुप्रयोगों में स्वचालित रूप से संकलित करता है"],
     "OpenURL bridges the discovery-to-delivery gap: clicking 'Find It @ My Library' sends citation metadata to the link resolver, connecting the user directly to the licensed PDF.",
     "OpenURL तकनीक के जरिए जब छात्र किसी इंडेक्स (जैसे Scopus या PubMed) में आर्टिकल देखता है, तो 'Find It' बटन उस उद्धरण की पूरी जानकारी लेकर कॉलेज के लिंक रिज़ॉल्वर से असली PDF खोल देता है।"),

    # 12: Link Resolvers & Knowledge Bases
    ("What are the two core components that enable a library 'Link Resolver' (such as Ex Libris SFX or Alma Link Resolver) to function?",
     "पुस्तकालय 'लिंक रिज़ॉल्वर' (जैसे Ex Libris SFX या Alma Link Resolver) को कार्य करने में सक्षम बनाने वाले दो मुख्य घटक कौन से हैं?",
     "An OpenURL-aware algorithmic resolver engine AND an up-to-date Knowledge Base detailing institutional holdings and access coverage",
     "एक OpenURL-जागरूक एल्गोरिथम रिज़ॉल्वर इंजन और संस्थागत होल्डिंग्स और एक्सेस कवरेज का विवरण देने वाला एक अद्यतन ज्ञान का आधार (Knowledge Base)",
     ["A physical barcode scanner AND a laser printing machine", "A high-speed fiber optic switchboard AND a copper telephone line", "A relational SQL database table AND a paper spiral notebook"],
     ["एक भौतिक बारकोड स्कैनर और एक लेजर प्रिंटिंग मशीन", "एक उच्च गति फाइबर ऑप्टिक स्विचबोर्ड और एक तांबे की टेलीफोन लाइन", "एक रिलेशनल SQL डेटाबेस तालिका और एक कागज़ सर्पिल नोटबुक"],
     "The engine parses the incoming OpenURL citation metadata, while the Knowledge Base verifies whether the library subscribes to that journal and year, generating the direct link.",
     "लिंक रिज़ॉल्वर के 2 हिस्से होते हैं: रिज़ॉल्वर इंजन (जो लिंक पढ़ता है) और नॉलेज बेस (जो यह जांचता है कि हमारे कॉलेज ने उस साल की पत्रिका खरीदी है या नहीं और सही लिंक पर भेजता है)।"),

    # 13: EZproxy Configuration
    ("How does 'EZproxy' (developed by Useful Utilities, now maintained by OCLC) deliver remote off-campus access to licensed databases?",
     "'EZproxy' (OCLC द्वारा प्रबंधित) लाइसेंस प्राप्त डेटाबेस तक दूरस्थ ऑफ-कैंपस पहुँच कैसे प्रदान करता है?",
     "It acts as a reverse proxy, intercepting off-campus patron web requests, authenticating users against campus credentials, and rewriting URLs to route requests through the library's authorized IP",
     "यह एक रिवर्स प्रॉक्सी के रूप में कार्य करता है, ऑफ-कैंपस संरक्षक वेब अनुरोधों को रोकता है, परिसर के क्रेडेंशियल्स के खिलाफ उपयोगकर्ताओं को प्रमाणित करता है, और पुस्तकालय के अधिकृत आईपी के माध्यम से अनुरोधों को रूट करने के लिए URL को फिर से लिखता है",
     ["It physically mails paper photocopies of requested journal articles to students' home addresses", "It requires students to install proprietary computer operating systems on their personal laptops", "It permanently disables external internet access across all off-campus student residential apartments"],
     ["यह छात्रों के घर के पते पर अनुरोधित जर्नल लेखों की भौतिक कागज़ी फोटोकॉपी डाक द्वारा भेजता है", "इसके लिए छात्रों को अपने व्यक्तिगत लैपटॉप पर मालिकाना कंप्यूटर ऑपरेटिंग सिस्टम स्थापित करने की आवश्यकता होती है", "यह सभी ऑफ-कैंपस छात्र आवासीय अपार्टमेंट में बाहरी इंटरनेट पहुंच को स्थायी रूप से अक्षम करता है"],
     "EZproxy dynamically rewrites database domain URLs (e.g., `jstor.org` becomes `jstor.org.ezproxy.univ.edu`), making remote users appear to vendors as if they are on campus.",
     "EZproxy एक रिवर्स प्रॉक्सी सर्वर है; जब छात्र घर से कॉलेज की लाइब्रेरी खोलता है, तो यह उसके लिंक को रीराइट कर देता है ताकि प्रकाशक की वेबसाइट को लगे कि छात्र कॉलेज के अंदर बैठकर ही पढ़ रहा है।"),

    # 14: SAML / OpenAthens vs IP Proxying
    ("What significant security and tracking advantage does federated access (such as OpenAthens or Shibboleth via SAML) offer over legacy IP-based proxying?",
     "पारंपरिक आईपी-आधारित प्रॉक्सींग पर फ़ेडरेटेड एक्सेस (जैसे SAML के माध्यम से OpenAthens या Shibboleth) क्या महत्वपूर्ण सुरक्षा और ट्रैकिंग लाभ प्रदान करता है?",
     "Granular, attribute-based identity management allowing access without exposing broad institutional IP ranges to malicious credential scraping",
     "विस्तृत, विशेषता-आधारित पहचान प्रबंधन जो दुर्भावनापूर्ण क्रेडेंशियल स्क्रैपिंग के लिए व्यापक संस्थागत आईपी श्रेणियों को उजागर किए बिना पहुंच की अनुमति देता है",
     ["It eliminates the need for computer monitors in university reading rooms", "It forces all students to complete mandatory written typing speed examinations", "It allows commercial publishers to seize physical ownership of campus buildings"],
     ["यह विश्वविद्यालय के रीडिंग रूम में कंप्यूटर मॉनिटर की आवश्यकता को समाप्त करता है", "यह सभी छात्रों को अनिवार्य लिखित टाइपिंग गति परीक्षाओं को पूरा करने के लिए मजबूर करता है", "यह वाणिज्यिक प्रकाशकों को परिसर भवनों के भौतिक स्वामित्व को जब्त करने की अनुमति देता है"],
     "Federated SAML authentication verifies user attributes (e.g., enrolled biology student) individually, isolating compromised accounts without publishers blocking the entire university's IP range.",
     "IP प्रॉक्सी में यदि एक भी पासवर्ड हैक हो जाए तो प्रकाशक पूरे कॉलेज का इंटरनेट ब्लॉक कर देता है; जबकि OpenAthens (SAML) व्यक्तिगत पहचान पर काम करता है, जिससे केवल उसी छात्र का खाता रुकता है, पूरा कॉलेज नहीं।"),

    # 15: Cost-Per-Use (CPU) Formula
    ("What is the standard formula used by electronic resource librarians to calculate the Cost-Per-Use (CPU) of an e-journal subscription?",
     "ई-जर्नल सदस्यता के प्रति-उपयोग लागत (CPU) की गणना करने के लिए इलेक्ट्रॉनिक संसाधन लाइब्रेरियनों द्वारा उपयोग किया जाने वाला मानक सूत्र क्या है?",
     "Total Annual Subscription Cost divided by Total Annual Usage (Unique Item Requests)",
     "कुल वार्षिक सदस्यता लागत को कुल वार्षिक उपयोग (अद्वितीय आइटम अनुरोध) से विभाजित किया गया",
     ["Total Annual Usage multiplied by Total Library Square Footage", "Total Journal Page Count divided by Total Enrolled University Students", "Total Library Staff Salaries divided by Total Overdue Book Fines"],
     ["कुल वार्षिक उपयोग को कुल पुस्तकालय वर्ग फुटेज से गुणा किया गया", "कुल जर्नल पृष्ठ संख्या को कुल नामांकित विश्वविद्यालय छात्रों से विभाजित किया गया", "कुल पुस्तकालय कर्मचारियों के वेतन को कुल अतिदेय पुस्तक जुर्माने से विभाजित किया गया"],
     "Cost-Per-Use (e.g., \$5,000 subscription / 1,000 article downloads = \$5.00 CPU) benchmarks resource value, identifying titles where interlibrary loan or pay-per-view is more economical.",
     "Cost-Per-Use (CPU) का सूत्र है: कुल वार्षिक सदस्यता शुल्क ÷ कुल डाउनलोड (Unique Requests)। यदि किसी जर्नल का CPU बहुत अधिक (जैसे प्रति डाउनलोड ₹5000) निकले, तो उसे रिन्यू करने के बजाय कैंसिल कर दिया जाता है।"),

    # 16: The "Big Deal"
    ("In academic library serials acquisitions, what is 'The Big Deal'?",
     "अकादमिक पुस्तकालय धारावाहिक अधिग्रहण में 'द बिग डील' (The Big Deal) क्या है?",
     "A multi-year comprehensive licensing package where a library or consortium purchases bundled online access to a publisher's entire journal catalog at a discounted aggregate rate",
     "एक बहु-वर्षीय व्यापक लाइसेंसिंग पैकेज जहाँ एक पुस्तकालय या संघ रियायती कुल दर पर प्रकाशक के संपूर्ण जर्नल कैटलॉग तक बंडल की गई ऑनलाइन पहुँच खरीदता है",
     ["A contract where a private commercial vendor purchases physical ownership of the university campus", "An agreement requiring all university library staff to receive identical annual financial bonuses", "A policy mandating that every undergraduate student must author one published peer-reviewed textbook"],
     ["एक अनुबंध जहाँ एक निजी वाणिज्यिक विक्रेता विश्वविद्यालय परिसर का भौतिक स्वामित्व खरीदता है", "एक समझौता जिसके तहत सभी विश्वविद्यालय पुस्तकालय कर्मचारियों को समान वार्षिक वित्तीय बोनस प्राप्त करने की आवश्यकता होती है", "एक नीति जो अनिवार्य करती है कि प्रत्येक स्नातक छात्र को एक प्रकाशित सहकर्मी-समीक्षित पाठ्यपुस्तक लिखनी होगी"],
     "Pioneered in the late 1990s, Big Deals provided vast access but consumed massive proportions of library budgets, leading many institutions to recently unbundle due to unsustainable inflation.",
     "'द बिग डील' 1990 के दशक में शुरू हुई थी जहाँ प्रकाशक (जैसे Elsevier) अपने सभी सैकड़ों जर्नल्स का एक बंडल पैकेज बेचते थे; आज बहुत से पुस्तकालय अत्यधिक महँगाई के कारण इन बंडलों को तोड़ रहे हैं।"),

    # 17: Perpetual Access & Post-Cancellation Rights
    ("Why is negotiating explicit 'Perpetual Access' (Post-Cancellation Access - PCA) rights essential in e-resource licensing?",
     "ई-संसाधन लाइसेंसिंग में स्पष्ट 'शाश्वत पहुँच' (पोस्ट-कैंसलेशन एक्सेस - PCA) अधिकारों पर बातचीत करना क्यों आवश्यक है?",
     "It guarantees the library retains permanent digital access to the specific years/volumes paid for, even if the subscription is canceled in the future",
     "यह गारंटी देता है कि पुस्तकालय उन विशिष्ट वर्षों/खंडों तक स्थायी डिजिटल पहुँच बनाए रखता है जिनके लिए भुगतान किया गया है, भले ही भविष्य में सदस्यता रद्द कर दी जाए",
     ["It forces commercial publishers to replace paper books with free physical computers", "It allows library patrons to sell digital articles on commercial online auction platforms", "It requires university libraries to permanently close down their physical study rooms"],
     ["यह वाणिज्यिक प्रकाशकों को कागज़ की किताबों को मुफ्त भौतिक कंप्यूटरों से बदलने के लिए मजबूर करता है", "यह पुस्तकालय संरक्षकों को वाणिज्यिक ऑनलाइन नीलामी मंचों पर डिजिटल लेख बेचने की अनुमति देता है", "इसके लिए विश्वविद्यालय के पुस्तकालयों को अपने भौतिक अध्ययन कक्षों को स्थायी रूप से बंद करने की आवश्यकता होती है"],
     "Without PCA clauses, canceling an e-journal subscription instantly wipes out access to past published issues the library paid for during previous years.",
     "PCA (पोस्ट-कैंसलेशन एक्सेस) खंड यह कानूनी गारंटी देता है कि यदि कॉलेज ने 2015 से 2024 तक का शुल्क दिया है, तो भविष्य में सब्सक्रिप्शन बंद होने पर भी उन 10 वर्षों के पुराने अंक छात्र हमेशा पढ़ सकेंगे।"),

    # 18: Authorized Users & Walk-in Rights
    ("In university electronic resource license agreements, who are 'Walk-in Users'?",
     "विश्वविद्यालय इलेक्ट्रॉनिक संसाधन लाइसेंस समझौतों में 'वॉक-इन उपयोगकर्ता' (Walk-in Users) कौन हैं?",
     "Members of the general public who are physically present on library premises and permitted to access licensed databases via designated campus terminals",
     "आम जनता के सदस्य जो पुस्तकालय परिसर में भौतिक रूप से मौजूद हैं और निर्दिष्ट परिसर टर्मिनलों के माध्यम से लाइसेंस प्राप्त डेटाबेस तक पहुँचने की अनुमति रखते हैं",
     ["Students who jog or walk around the university sports stadium track", "Robotic mechanical androids that patrol library book stacks overnight", "Commercial book salesmen who walk door-to-door selling encyclopedias"],
     ["विश्वविद्यालय के खेल स्टेडियम ट्रैक पर जॉगिंग या टहलने वाले छात्र", "रोबोटिक मैकेनिकल एंड्रॉइड जो रात भर पुस्तकालय की किताबों के ढेरों पर गश्त करते हैं", "वाणिज्यिक पुस्तक विक्रेता जो घर-घर जाकर विश्वकोश बेचते हैं"],
     "Academic libraries advocate for walk-in rights to fulfill their public mission, allowing community visitors to conduct research inside the library without remote login credentials.",
     "वॉक-इन यूज़र्स वे बाहरी आम नागरिक या शोधार्थी हैं जो लाइब्रेरी में व्यक्तिगत रूप से आकर वहाँ के कंप्यूटरों पर बैठकर लाइसेंस प्राप्त ई-जर्नल्स पढ़ सकते हैं।"),

    # 19: Interlibrary Loan (ILL) Clauses in Licenses
    ("What does a favorable 'Interlibrary Loan' (ILL) clause in an e-resource license agreement allow the library to do?",
     "एक ई-संसाधन लाइसेंस समझौते में एक अनुकूल 'इंटरलाइब्रेरी ऋण' (ILL) खंड पुस्तकालय को क्या करने की अनुमति देता है?",
     "Supplying a single digital copy of an article or book chapter to another non-profit library for research use via secure electronic transmission (e.g., Ariel, Odyssey)",
     "सुरक्षित इलेक्ट्रॉनिक ट्रांसमिशन (जैसे, एरियल, ओडिसी) के माध्यम से अनुसंधान उपयोग के लिए किसी अन्य गैर-लाभकारी पुस्तकालय को किसी लेख या पुस्तक अध्याय की एक डिजिटल प्रति की आपूर्ति करना",
     ["Reselling commercial database subscriptions to private multinational corporations", "Printing ten thousand copies of a copyrighted textbook to sell in commercial bookstores", "Permanently seizing ownership of the publishing company's corporate headquarters"],
     ["निजी बहुराष्ट्रीय निगमों को वाणिज्यिक डेटाबेस सदस्यता फिर से बेचना", "वाणिज्यिक किताबों की दुकानों में बेचने के लिए एक कॉपीराइट पाठ्यपुस्तक की दस हजार प्रतियां छापना", "प्रकाशन कंपनी के कॉर्पोरेट मुख्यालय के स्वामित्व को स्थायी रूप से जब्त करना"],
     "Publishers often attempt to forbid digital ILL; librarians negotiate clauses permitting secure electronic document delivery to assist partner institutions.",
     "अनुकूल ILL खंड यह अधिकार देता है कि यदि किसी दूसरे कॉलेज के छात्र को किसी आर्टिकल की सख्त ज़रूरत हो, तो हमारा पुस्तकालय सुरक्षित डिजिटल माध्यम से एक प्रति उस कॉलेज को भेज सकता है।"),

    # 20: CORAL Open-Source ERM
    ("What is 'CORAL' in the field of library electronic resource management?",
     "पुस्तकालय इलेक्ट्रॉनिक संसाधन प्रबंधन के क्षेत्र में 'CORAL' क्या है?",
     "A modular, open-source Electronic Resource Management system originally developed by the University of Notre Dame",
     "एक मॉड्यूलर, ओपन-सोर्स इलेक्ट्रॉनिक रिसोर्स मैनेजमेंट सिस्टम जो मूल रूप से नोट्रे डेम विश्वविद्यालय द्वारा विकसित किया गया है",
     ["A marine biology research database indexing ocean coral reef ecosystems", "A commercial hardware barcode printer manufactured by Zebra Technologies", "A proprietary operating system developed to replace Linux on server mainframes"],
     ["समुद्री प्रवाल भित्ति पारिस्थितिकी तंत्र को अनुक्रमित करने वाला एक समुद्री जीव विज्ञान अनुसंधान डेटाबेस", "ज़ेबरा टेक्नोलॉजीज द्वारा निर्मित एक वाणिज्यिक हार्डवेयर बारकोड प्रिंटर", "सर्वर मेनफ्रेम पर लिनक्स को बदलने के लिए विकसित एक मालिकाना ऑपरेटिंग सिस्टम"],
     "CORAL consists of interoperable modules: Organizations, Resources, Licensing, Usage Statistics, and Terms Tool, providing an accessible open-source ERM solution.",
     "CORAL नोट्रे डेम यूनिवर्सिटी द्वारा विकसित एक प्रसिद्ध ओपन-सोर्स ERM सॉफ्टवेयर है; इसके अलग-अलग मॉड्यूल (लाइसेंस, संसाधन, वेंडर्स, उपयोग सांख्यिकी) ई-संसाधनों का सुचारू प्रबंधन करते हैं।"),

    # 21: Transformative Agreements
    ("What is a 'Transformative Agreement' (such as 'Read and Publish' or 'Publish and Read') in academic publishing?",
     "अकादमिक प्रकाशन में 'परिवर्तनकारी समझौता' (Transformative Agreement - जैसे 'रीड एंड पब्लिश' या 'पब्लिश एंड रीड') क्या है?",
     "A contractual model where institutional subscription payments are shifted towards funding Open Access publishing fees (APCs) for affiliated authors while retaining journal reading access",
     "एक संविदात्मक मॉडल जहाँ संस्थागत सदस्यता भुगतानों को पत्रिका पढ़ने की पहुँच बनाए रखते हुए संबद्ध लेखकों के लिए ओपन एक्सेस प्रकाशन शुल्क (APCs) के वित्तपोषण की ओर स्थानांतरित किया जाता है",
     ["A contract transforming academic university professors into commercial fiction authors", "An agreement where printed paper textbooks are physically transformed into digital microfilms", "A merger combining ten private commercial publishing corporations into a single state monopoly"],
     ["अकादमिक विश्वविद्यालय के प्रोफेसरों को वाणिज्यिक कथा लेखकों में बदलने वाला एक अनुबंध", "एक समझौता जहाँ मुद्रित कागज़ की पाठ्यपुस्तकों को भौतिक रूप से डिजिटल माइक्रोफिल्म में बदल दिया जाता है", "दस निजी वाणिज्यिक प्रकाशन निगमों को एक एकल राज्य एकाधिकार में मिलाने वाला विलय"],
     "Transformative agreements seek to transition the scholarly communication ecosystem from a closed paywalled subscription model to a fully open-access paradigm.",
     "परिवर्तनकारी समझौते (Read & Publish) में कॉलेज प्रकाशक को जो फीस देता है, उसमें न केवल जर्नल्स पढ़ने का अधिकार मिलता है, बल्कि कॉलेज के प्रोफेसर्स के रिसर्च पेपर्स बिना अतिरिक्त APC दिए मुफ्त ओपन एक्सेस में छपते हैं।"),

    # 22: SERU (NISO RP-7-2012)
    ("What is 'SERU' (Shared Electronic Resource Understanding) developed by NISO?",
     "NISO द्वारा विकसित 'SERU' (Shared Electronic Resource Understanding) क्या है?",
     "A recommended framework of shared expectations that libraries and publishers can mutually adopt as an alternative to formal, negotiated legal license contracts",
     "साझा अपेक्षाओं का एक अनुशंसित ढांचा जिसे पुस्तकालय और प्रकाशक औपचारिक, बातचीत वाले कानूनी लाइसेंस अनुबंधों के विकल्प के रूप में पारस्परिक रूप से अपना सकते हैं",
     ["A software standard for encrypting video streams on university cable television", "A postal shipping guideline for transporting rare fragile historical manuscripts", "A standardized mechanical specification for library wooden circulation desks"],
     ["विश्वविद्यालय केबल टेलीविजन पर वीडियो स्ट्रीम को एन्क्रिप्ट करने के लिए एक सॉफ्टवेयर मानक", "दुर्लभ नाजुक ऐतिहासिक पांडुलिपियों के परिवहन के लिए एक डाक शिपिंग दिशानिर्देश", "पुस्तकालय की लकड़ी के संचलन डेस्क के लिए एक मानकीकृत यांत्रिक विनिर्देश"],
     "SERU saves immense legal time and cost for smaller publishers and libraries by relying on established norms of good faith, fair use, and mutual trust rather than negotiated contracts.",
     "SERU (NISO) छोटे प्रकाशकों और पुस्तकालयों के लिए एक वरदान है; इसमें लंबे कानूनी समझौतों और वकीलों की फीस के बिना आपसी विश्वास और स्थापित नियमों के आधार पर ई-संसाधनों की खरीद होती है।"),

    # 23: Embargo Periods
    ("In commercial aggregator databases (like EBSCOhost Academic Search or ProQuest Central), what is an 'Embargo Period'?",
     "वाणिज्यिक एग्रीगेटर डेटाबेस (जैसे EBSCOhost Academic Search या ProQuest Central) में 'एम्बार्गो अवधि' (Embargo Period) क्या है?",
     "A vendor-imposed delay (typically 3 to 12 months) before the most recent full-text journal issues are made available in aggregated collections",
     "एक विक्रेता द्वारा लगाया गया विलंब (आमतौर पर 3 से 12 महीने) इससे पहले कि सबसे हालिया पूर्ण-पाठ जर्नल के मुद्दे एकत्रित संग्रह में उपलब्ध कराए जाएं",
     ["A permanent ban prohibiting university students from searching historical databases", "A mandatory waiting period where patrons must wait thirty days before receiving a library card", "A physical lock placed on library bookshelves during scheduled examination hours"],
     ["विश्वविद्यालय के छात्रों को ऐतिहासिक डेटाबेस खोजने से रोकने वाला एक स्थायी प्रतिबंध", "एक अनिवार्य प्रतीक्षा अवधि जहाँ संरक्षकों को पुस्तकालय कार्ड प्राप्त करने से पहले तीस दिन प्रतीक्षा करनी होगी", "निर्धारित परीक्षा घंटों के दौरान पुस्तकालय की किताबों की अलमारियों पर लगाया गया एक भौतिक ताला"],
     "Publishers place embargoes on aggregator databases to protect their highly profitable direct individual journal subscriptions from being cannibalized by cheap aggregated packages.",
     "एम्बार्गो (Embargo) का अर्थ है कि एग्रीगेटर डेटाबेस में पत्रिका का सबसे नया अंक तुरंत नहीं मिलता, बल्कि प्रकाशक 6 महीने या 1 साल बाद (देरी से) उपलब्ध कराता है ताकि उसकी सीधी महंगी सदस्यता बिकती रहे।"),

    # 24: Article Processing Charges (APCs)
    ("What are 'Article Processing Charges' (APCs) in the Gold Open Access publishing model?",
     "गोल्ड ओपन एक्सेस प्रकाशन मॉडल में 'आर्टिकल प्रोसेसिंग शुल्क' (APCs) क्या हैं?",
     "Fees charged to authors, institutions, or funders to make an accepted peer-reviewed article immediately and permanently free to the global public upon publication",
     "स्वीकृत सहकर्मी-समीक्षित लेख को प्रकाशन पर तुरंत और स्थायी रूप से वैश्विक जनता के लिए निःशुल्क बनाने के लिए लेखकों, संस्थानों या वित्तपोषकों से लिया जाने वाला शुल्क",
     ["Late fine penalties charged to students who return paper books after their scheduled due dates", "Commercial customs duties paid to import printed books across international borders", "Licensing fees charged to university libraries to install barcode scanning software"],
     ["निर्धारित देय तिथियों के बाद कागज़ की किताबें वापस करने वाले छात्रों पर लगाया जाने वाला विलंब शुल्क जुर्माना", "अंतरराष्ट्रीय सीमाओं के पार मुद्रित पुस्तकों के आयात के लिए भुगतान किया जाने वाला वाणिज्यिक सीमा शुल्क", "बारकोड स्कैनिंग सॉफ़्टवेयर स्थापित करने के लिए विश्वविद्यालय पुस्तकालयों से लिया जाने वाला लाइसेंस शुल्क"],
     "APCs shift publishing costs from readers (subscriptions) to authors/institutions (publication fees), typically accompanied by Creative Commons open licenses (CC-BY).",
     "गोल्ड ओपन एक्सेस में पाठक से कोई पैसा नहीं लिया जाता; इसके बजाय शोध पत्र को पूरी दुनिया के लिए हमेशा मुफ्त रखने हेतु लेखक या उसके विश्वविद्यालय द्वारा APC (प्रकाशन शुल्क) दिया जाता है।"),

    # 25: Green Open Access vs Gold Open Access
    ("What is the primary operational distinction between 'Green Open Access' and 'Gold Open Access'?",
     "'ग्रीन ओपन एक्सेस' (Green Open Access) और 'गोल्ड ओपन एक्सेस' (Gold Open Access) के बीच प्राथमिक परिचालन अंतर क्या है?",
     "Gold OA publishes the article immediately open access on the publisher's journal platform; Green OA involves self-archiving a preprint or postprint in an institutional repository",
     "गोल्ड OA प्रकाशक के जर्नल प्लेटफॉर्म पर लेख को तुरंत ओपन एक्सेस प्रकाशित करता है; ग्रीन OA में एक संस्थागत रिपॉजिटरी में प्रीप्रिंट या पोस्टप्रिंट को स्वयं-संग्रहीत (Self-archiving) करना शामिल है",
     ["Gold OA costs nothing to anyone, while Green OA costs one million dollars per article", "Gold OA is strictly for biology research, while Green OA is strictly for agricultural science", "Gold OA requires physical printing on gold leaf paper, while Green OA is printed on green recycled paper"],
     ["गोल्ड OA किसी के लिए कुछ भी खर्च नहीं करता है, जबकि ग्रीन OA की लागत प्रति लेख एक मिलियन डॉलर है", "गोल्ड OA विशेष रूप से जीव विज्ञान अनुसंधान के लिए है, जबकि ग्रीन OA विशेष रूप से कृषि विज्ञान के लिए है", "गोल्ड OA को सोने की पत्ती वाले कागज़ पर भौतिक छपाई की आवश्यकता होती है, जबकि ग्रीन OA को हरे पुनर्चक्रित कागज़ पर मुद्रित किया जाता है"],
     "Green OA allows authors to share their peer-reviewed manuscripts freely via repositories (like DSpace) without paying publisher APC fees, often following an embargo period.",
     "गोल्ड OA में प्रकाशक अपनी वेबसाइट पर ही लेख सबको मुफ्त देता है (अक्सर APC लेकर); जबकि ग्रीन OA में लेखक अपने शोध पत्र की प्रति अपने कॉलेज की रिपॉजिटरी (जैसे Shodhganga/DSpace) में खुद अपलोड करता है।"),

    # 26: Diamond / Platinum Open Access
    ("Why is 'Diamond' (or Platinum) Open Access considered the most equitable scholarly communication model?",
     "'डायमंड' (या प्लैटिनम) ओपन एक्सेस को सबसे न्यायसंगत विद्वत्तापूर्ण संचार मॉडल क्यों माना जाता है?",
     "Neither authors pay publication fees (no APCs) NOR readers pay subscription fees; the journal is fully funded by universities, scholarly societies, or government grants",
     "न तो लेखक प्रकाशन शुल्क (कोई APC नहीं) का भुगतान करते हैं और न ही पाठक सदस्यता शुल्क का भुगतान करते हैं; पत्रिका पूरी तरह से विश्वविद्यालयों, विद्वान समाजों, या सरकारी अनुदानों द्वारा वित्तपोषित होती है",
     ["It gives free physical diamond gemstones to every university student who authors a research paper", "It requires all scientific articles to be encrypted with military-grade quantum passwords", "It restricts journal readership exclusively to certified billionaire investors"],
     ["यह शोध पत्र लिखने वाले प्रत्येक विश्वविद्यालय के छात्र को मुफ्त भौतिक हीरे के रत्न देता है", "इसके लिए सभी वैज्ञानिक लेखों को सैन्य-ग्रेड क्वांटम पासवर्ड के साथ एन्क्रिप्ट करने की आवश्यकता होती है", "यह पत्रिका पाठकों को विशेष रूप से प्रमाणित अरबपति निवेशकों तक सीमित करता है"],
     "Diamond OA eliminates financial barriers on both sides of knowledge creation, ensuring equitable participation for scholars in developing countries.",
     "डायमंड ओपन एक्सेस सबसे निष्पक्ष मॉडल है क्योंकि इसमें न तो पाठक से कोई पैसा लिया जाता है और न ही लेखक से कोई फीस (APC) ली जाती है; इसका पूरा खर्च विश्वविद्यालय या सरकार उठाती है।"),

    # 27: CrossRef and DOIs
    ("What essential infrastructure does 'CrossRef' provide for electronic scholarly journal linking?",
     "इलेक्ट्रॉनिक विद्वत्तापूर्ण जर्नल लिंकिंग के लिए 'CrossRef' क्या आवश्यक बुनियादी ढांचा प्रदान करता है?",
     "A non-profit membership organization that registers persistent Digital Object Identifiers (DOIs) and deposits/queries cross-publisher citation linking metadata",
     "एक गैर-लाभकारी सदस्यता संगठन जो स्थायी डिजिटल ऑब्जेक्ट पहचानकर्ता (DOIs) को पंजीकृत करता है और क्रॉस-प्रकाशक उद्धरण लिंकिंग मेटाडेटा को जमा/क्वेरी करता है",
     ["A commercial software store that sells proprietary font families to academic book authors", "A physical parcel delivery service shipping bound academic periodicals across international borders", "An automated robotic system for vacuum cleaning library carpet floors"],
     ["एक वाणिज्यिक सॉफ्टवेयर स्टोर जो अकादमिक पुस्तक लेखकों को मालिकाना फ़ॉन्ट परिवार बेचता है", "एक भौतिक पार्सल वितरण सेवा जो अंतरराष्ट्रीय सीमाओं के पार बाउंड अकादमिक पत्रिकाओं को भेजती है", "पुस्तकालय के कालीन फर्श को वैक्यूम करने के लिए एक स्वचालित रोबोट प्रणाली"],
     "CrossRef enables reference linking across competitive publishers: clicking a reference in an Elsevier paper resolves directly to the cited Springer Nature article via its DOI.",
     "CrossRef दुनिया भर के प्रकाशकों का एक साझा नेटवर्क है; जब आप किसी पेपर के संदर्भ में किसी दूसरे प्रकाशक के पेपर पर क्लिक करते हैं, तो DOI के जरिए वह पेपर तुरंत खुल जाता है।"),

    # 28: Electronic Resource Usage Consolidation
    ("What problem does an 'Usage Consolidation' tool (like EBSCO Usage Consolidation or 360 Core) solve for library managers?",
     "एक 'उपयोग समेकन' उपकरण (जैसे EBSCO Usage Consolidation या 360 Core) पुस्तकालय प्रबंधकों के लिए किस समस्या का समाधान करता है?",
     "Aggregating COUNTER usage reports from dozens of disparate publishers, matching usage against local subscription costs, and generating unified Cost-Per-Use reports",
     "दर्जनों अलग-अलग प्रकाशकों से COUNTER उपयोग रिपोर्टों को एकत्रित करना, स्थानीय सदस्यता लागतों के खिलाफ उपयोग का मिलान करना, और एकीकृत लागत-प्रति-उपयोग रिपोर्ट तैयार करना",
     ["Consolidating physical paper catalog cards into a single wooden drawer cabinet", "Calculating late fine surcharges for overdue books in school libraries", "Compressing high-definition video files into micro-thumbnails for catalog displays"],
     ["भौतिक कागज़ के कैटलॉग कार्डों को एक एकल लकड़ी के दराज कैबिनेट में समेकित करना", "स्कूल पुस्तकालयों में अतिदेय पुस्तकों के लिए विलंब शुल्क अधिभार की गणना करना", "कैटलॉग डिस्प्ले के लिए हाई-डेफिनिशन वीडियो फ़ाइलों को माइक्रो-थंबनेल में संपीड़ित करना"],
     "Usage consolidators streamline data analytics, automatically pulling SUSHI feeds and calculating cost-per-use metrics across the entire electronic portfolio in one interface.",
     "उपयोग समेकन (Usage Consolidation) टूल्स सभी अलग-अलग प्रकाशकों के उपयोग के आंकड़ों और कॉलेज के बिलों को एक जगह मिलाकर दिखा देते हैं कि कुल मिलाकर कौन सा पैकेज फायदेमंद रहा और कौन सा नुकसानदेह।"),

    # 29: Indemnification Clauses in Licenses
    ("Why do university legal counsels scrutinize 'Indemnification' clauses in electronic resource contracts?",
     "विश्वविद्यालय के कानूनी सलाहकार इलेक्ट्रॉनिक संसाधन अनुबंधों में 'क्षतिपूर्ति' (Indemnification) खंडों की सूक्ष्म जांच क्यों करते हैं?",
     "To ensure public universities are not unlawfully held financially liable for individual patrons' rogue copyright infringements or unpreventable platform security breaches",
     "यह सुनिश्चित करने के लिए कि सार्वजनिक विश्वविद्यालयों को व्यक्तिगत संरक्षकों के अनधिकृत कॉपीराइट उल्लंघन या अपरिहार्य प्लेटफ़ॉर्म सुरक्षा उल्लंघनों के लिए गैरकानूनी रूप से वित्तीय रूप से उत्तरदायी नहीं ठहराया जाता है",
     ["To force publishers to buy life insurance policies for all university undergraduate students", "To require commercial vendors to pay the entire annual tuition fees for enrolled students", "To permanently transfer ownership of all university patents to commercial publishing executives"],
     ["प्रकाशकों को सभी विश्वविद्यालय स्नातक छात्रों के लिए जीवन बीमा पॉलिसियां ​​खरीदने के लिए मजबूर करना", "वाणिज्यिक विक्रेताओं को नामांकित छात्रों के लिए संपूर्ण वार्षिक शिक्षण शुल्क का भुगतान करने की आवश्यकता", "सभी विश्वविद्यालय पेटेंट के स्वामित्व को वाणिज्यिक प्रकाशन अधिकारियों को स्थायी रूप से स्थानांतरित करना"],
     "Public universities are often legally prohibited by state statutes from indemnifying private vendors; contracts must clarify that the library is not an insurer for individual student actions.",
     "क्षतिपूर्ति (Indemnification) खंड की जांच इसलिए जरूरी है ताकि यदि किसी छात्र ने अपने स्तर पर कोई गैरकानूनी डाउनलोडिंग कर ली, तो प्रकाशक उसका जुर्माना कॉलेज या विश्वविद्यालय के मत्थे न मढ़ सके।"),

    # 30: Governing Law Clauses
    ("What is the preferred standard for the 'Governing Law and Jurisdiction' clause when an Indian university signs an e-resource contract?",
     "जब कोई भारतीय विश्वविद्यालय ई-संसाधन अनुबंध पर हस्ताक्षर करता है तो 'शासी कानून और क्षेत्राधिकार' (Governing Law and Jurisdiction) खंड के लिए पसंदीदा मानक क्या है?",
     "The laws and court jurisdictions of India (or the specific Indian state where the university resides)",
     "भारत के कानून और अदालत के क्षेत्राधिकार (या विशिष्ट भारतीय राज्य जहाँ विश्वविद्यालय स्थित है)",
     ["The commercial corporate laws of the State of Delaware, United States", "The maritime commercial shipping laws of the Republic of Panama", "The municipal town council bylaws of the publisher's international headquarters"],
     ["डेलावेयर राज्य, संयुक्त राज्य अमेरिका के वाणिज्यिक कॉर्पोरेट कानून", "पनामा गणराज्य के समुद्री वाणिज्यिक शिपिंग कानून", "प्रकाशक के अंतरराष्ट्रीय मुख्यालय के नगरपालिका नगर परिषद उपनियम"],
     "Indian public institutions cannot agree to foreign jurisdictions; disputes must be settled under Indian law (Arbitration and Conciliation Act) in domestic courts.",
     "भारतीय विश्वविद्यालयों को हमेशा यह शर्त रखनी चाहिए कि किसी भी विवाद की स्थिति में मुकदमा भारत की अदालतों और भारतीय कानून के तहत ही चलेगा, अमेरिका या इंग्लैंड में नहीं।"),

    # 31: Open Access Directory (DOAJ)
    ("What is the 'DOAJ' (Directory of Open Access Journals) and what role does it play in ERM knowledge bases?",
     "'DOAJ' (डायरेक्टरी ऑफ ओपन एक्सेस जर्नल्स) क्या है और यह ERM ज्ञान अड्डों में क्या भूमिका निभाता है?",
     "A community-curated online directory that indexes and verifies high-quality, peer-reviewed, open-access scholarly journals across all academic disciplines",
     "एक समुदाय-क्यूरेटेड ऑनलाइन निर्देशिका जो सभी शैक्षणिक विषयों में उच्च-गुणवत्ता, सहकर्मी-समीक्षित, ओपन-एक्सेस विद्वत्तापूर्ण पत्रिकाओं को अनुक्रमित और सत्यापित करती है",
     ["A commercial bookstore selling second-hand digital textbook licenses to private corporations", "A security software designed to block open-access scholarly literature on university intranets", "An automated algorithm that charges university professors per-page publishing fees"],
     ["निजी निगमों को पुरानी डिजिटल पाठ्यपुस्तक लाइसेंस बेचने वाली एक वाणिज्यिक किताबों की दुकान", "विश्वविद्यालय इंट्रानेट पर ओपन-एक्सेस विद्वत्तापूर्ण साहित्य को अवरुद्ध करने के लिए डिज़ाइन किया गया एक सुरक्षा सॉफ्टवेयर", "एक स्वचालित एल्गोरिदम जो विश्वविद्यालय के प्रोफेसरों से प्रति-पृष्ठ प्रकाशन शुल्क लेता है"],
     "DOAJ serves as an authoritative filter for legitimate open-access publishing, protecting libraries and scholars against predatory, un-peer-reviewed journals.",
     "DOAJ (Directory of Open Access Journals) दुनिया भर की प्रामाणिक और उच्च-स्तरीय ओपन एक्सेस पत्रिकाओं की आधिकारिक सूची है; यह फर्जी या गैर-मानक (Predatory) पत्रिकाओं से बचाती है।"),

    # 32: Predatory Publishing Warning Signs
    ("Which of the following is a classic indicator of a 'Predatory' or deceptive scholarly journal?",
     "निम्नलिखित में से कौन सा एक 'शिकारी / फर्जी' (Predatory) या भ्रामक विद्वत्तापूर्ण पत्रिका का एक क्लासिक संकेतक है?",
     "Aggressive spam email solicitations, fake or hijacked impact factors, lack of rigorous peer review, and promising publication within 48 hours upon APC payment",
     "आक्रामक स्पैम ईमेल आमंत्रण, नकली या अपहृत प्रभाव कारक (Impact Factors), कठोर सहकर्मी समीक्षा की कमी, और APC भुगतान पर 48 घंटों के भीतर प्रकाशन का वादा",
     ["Inclusion in Scopus, Web of Science, and the Directory of Open Access Journals (DOAJ)", "Adherence to the Committee on Publication Ethics (COPE) rigorous publishing guidelines", "Transparent public disclosure of editorial board members with verified institutional affiliations"],
     ["स्कोपस, वेब ऑफ साइंस और डायरेक्टरी ऑफ ओपन एक्सेस जर्नल्स (DOAJ) में शामिल होना", "प्रकाशन नैतिकता समिति (COPE) के कठोर प्रकाशन दिशानिर्देशों का पालन", "सत्यापित संस्थागत संबद्धता वाले संपादकीय बोर्ड के सदस्यों का पारदर्शी सार्वजनिक प्रकटीकरण"],
     "Predatory journals exploit the author-pays Gold OA model solely for financial profit, compromising academic integrity by publishing unvetted papers.",
     "फर्जी (Predatory) जर्नल्स पैसे (APC) लेकर बिना किसी जांच या पीयर रिव्यू के 2 दिन में रिसर्च पेपर छापने का झांसा देते हैं और नकली इम्पैक्ट फैक्टर दिखाकर शोधार्थियों को ठगते हैं।"),

    # 33: COPE (Committee on Publication Ethics)
    ("What is the 'Committee on Publication Ethics' (COPE) in academic journal publishing?",
     "अकादमिक जर्नल प्रकाशन में 'प्रकाशन नैतिकता समिति' (COPE - Committee on Publication Ethics) क्या है?",
     "A non-profit organization providing ethical guidelines, codes of conduct, and flowcharts for journal editors and publishers to handle plagiarism, authorship disputes, and retractions",
     "एक गैर-लाभकारी संगठन जो जर्नल संपादकों और प्रकाशकों के लिए साहित्यिक चोरी, लेखकत्व विवादों और शोध वापसी (Retractions) को संभालने के लिए नैतिक दिशानिर्देश, आचार संहिता और फ्लोचार्ट प्रदान करता है",
     ["A commercial software company that sells automated catalog card printing machinery", "A government intelligence agency monitoring university classroom lecture discussions", "An association representing private commercial textbook sales representatives"],
     ["एक वाणिज्यिक सॉफ्टवेयर कंपनी जो स्वचालित कैटलॉग कार्ड प्रिंटिंग मशीनरी बेचती है", "विश्वविद्यालय कक्षा व्याख्यान चर्चाओं की निगरानी करने वाली एक सरकारी खुफिया एजेंसी", "निजी वाणिज्यिक पाठ्यपुस्तक बिक्री प्रतिनिधियों का प्रतिनिधित्व करने वाला एक संघ"],
     "COPE sets ethical benchmarks across the global publishing industry, ensuring transparent investigations into duplicate submissions, data fabrication, and peer review fraud.",
     "COPE दुनिया भर के जर्नल्स के लिए नैतिक आचार संहिता तय करता है; जब किसी पेपर में डेटा की चोरी, फर्जी लेखक या साहित्यिक चोरी का विवाद होता है, तो COPE के नियमों से फैसला होता है।"),

    # 34: Retraction Watch
    ("What vital role does 'Retraction Watch' play in electronic scholarly communication and database integrity?",
     "इलेक्ट्रॉनिक विद्वत्तापूर्ण संचार और डेटाबेस अखंडता में 'रिट्रेक्शन वॉच' (Retraction Watch) क्या महत्वपूर्ण भूमिका निभाता है?",
     "Tracking and indexing formally retracted scientific papers, exposing fraudulent data, image manipulation, and paper mill operations to prevent citation of debunked research",
     "औपचारिक रूप से वापस लिए गए (Retracted) वैज्ञानिक पत्रों को ट्रैक और अनुक्रमित करना, धोखाधड़ी वाले डेटा, छवि हेरफेर, और पेपर मिल संचालन को उजागर करना ताकि खारिज किए गए शोध के उद्धरण को रोका जा सके",
     ["Selling second-hand physical printing press machinery to newspaper syndicates", "Encrypting current internet websites so students cannot read them without subscriptions", "Streaming live commercial Hollywood movies directly to mobile smartphones"],
     ["अखबार सिंडिकेट्स को पुरानी भौतिक प्रिंटिंग प्रेस मशीनरी बेचना", "वर्तमान इंटरनेट वेबसाइटों को एन्क्रिप्ट करना ताकि छात्र सदस्यता के बिना उन्हें न पढ़ सकें", "लाइव वाणिज्यिक हॉलीवुड फिल्मों को सीधे मोबाइल स्मार्टफोन पर स्ट्रीम करना"],
     "Retraction Watch alerts librarians and discovery systems when published studies are withdrawn due to falsified findings, ensuring dead science is not perpetuated.",
     "Retraction Watch उन सभी रिसर्च पेपर्स का रिकॉर्ड रखता है जिन्हें धोखाधड़ी या गलत डेटा के कारण प्रकाशक द्वारा वापस (Retract) ले लिया गया है, ताकि अन्य शोधार्थी उनका गलत हवाला न दें।"),

    # 35: Paper Mills in Scholarly Publishing
    ("In contemporary academic publishing ethics, what is a 'Paper Mill'?",
     "समकालीन शैक्षणिक प्रकाशन नैतिकता में 'पेपर मिल' (Paper Mill) क्या है?",
     "An unethical commercial syndicate that manufactures and sells fabricated, plagiarized, or ghostwritten scientific manuscripts to authors desperate for publication credits",
     "एक अनैतिक वाणिज्यिक सिंडिकेट जो प्रकाशन क्रेडिट के लिए बेताब लेखकों को मनगढ़ंत, साहित्यिक चोरी वाले, या भूत-लिखित (ghostwritten) वैज्ञानिक पांडुलिपियों का निर्माण और बिक्री करता है",
     ["A physical industrial factory that recycles used cardboard boxes into smooth printing paper", "A government office that issues legal copyright registration certificates to book publishers", "A university department dedicated to studying the chemical properties of plant cellulose"],
     ["एक भौतिक औद्योगिक कारखाना जो इस्तेमाल किए गए कार्डबोर्ड बक्से को चिकने छपाई कागज़ में पुनर्चक्रित करता है", "एक सरकारी कार्यालय जो पुस्तक प्रकाशकों को कानूनी कॉपीराइट पंजीकरण प्रमाण पत्र जारी करता है", "पौधों के सेल्यूलोज के रासायनिक गुणों का अध्ययन करने के लिए समर्पित एक विश्वविद्यालय विभाग"],
     "Paper mills compromise global literature through fake data, fabricated co-authors, and bribed peer reviewers, prompting major publisher mass-retractions.",
     "पेपर मिलें ऐसे गिरोह हैं जो पैसे लेकर डॉक्टरों या प्रोफेसर्स के नाम पर फर्जी और मनगढ़ंत रिसर्च पेपर तैयार करके जर्नल्स में छपवाते हैं; यह अकादमिक जगत का बड़ा अपराध है।"),

    # 36: NISO EDIFACT in ERM
    ("How does the NISO EDIFACT standard streamline acquisitions within library systems?",
     "NISO EDIFACT मानक पुस्तकालय प्रणालियों के भीतर अधिग्रहण को कैसे सुव्यवस्थित करता है?",
     "Enabling automated electronic data interchange between library ILS/ERM systems and book/serial vendors for purchase orders, order acknowledgments, claims, and electronic invoices",
     "खरीद आदेशों, आदेश पावती, दावों और इलेक्ट्रॉनिक चालानों के लिए पुस्तकालय ILS/ERM प्रणालियों और पुस्तक/धारावाहिक विक्रेताओं के बीच स्वचालित इलेक्ट्रॉनिक डेटा इंटरचेंज को सक्षम करना",
     ["Formatting printed barcodes on library circulation desk slips", "Managing high-speed cache memory inside server central processing units", "A software protocol for streaming high-definition audio recordings across local networks"],
     ["पुस्तकालय संचलन डेस्क पर्चियों पर मुद्रित बारकोड को प्रारूपित करना", "सर्वर सेंट्रल प्रोसेसिंग इकाइयों के अंदर उच्च गति कैश मेमोरी का प्रबंधन करना", "स्थानीय नेटवर्क पर उच्च-परिभाषा ऑडियो रिकॉर्डिंग स्ट्रीमिंग के लिए एक सॉफ्टवेयर प्रोटोकॉल"],
     "EDIFACT automates technical commerce: purchase orders are transmitted electronically without paper mail, and electronic invoices automatically update fund ledgers in the ILS.",
     "EDIFACT के जरिए किताबों और पत्रिकाओं के ऑर्डर और बिल सीधे कंप्यूटर-से-कंप्यूटर बिना कागज़ के भेजे जाते हैं, जिससे बिल पास होने और भुगतान में कोई मानवीय देरी नहीं होती।"),

    # 37: E-Resource Troubleshooting Protocols
    ("When a patron reports being blocked by a vendor paywall for a known subscribed journal, what is the first troubleshooting step an electronic resource manager performs?",
     "जब कोई संरक्षक ज्ञात सदस्यता प्राप्त पत्रिका के लिए विक्रेता पेवॉल द्वारा अवरुद्ध होने की रिपोर्ट करता है, तो एक इलेक्ट्रॉनिक संसाधन प्रबंधक पहला समस्या निवारण कदम क्या करता है?",
     "Verifying proxy server routing, checking whether the library's registered IP ranges are still active with the vendor, and confirming subscription renewal payment status",
     "प्रॉक्सी सर्वर रूटिंग का सत्यापन करना, यह जांचना कि क्या पुस्तकालय की पंजीकृत आईपी श्रेणियां विक्रेता के साथ अभी भी सक्रिय हैं, और सदस्यता नवीनीकरण भुगतान स्थिति की पुष्टि करना",
     ["Immediately canceling all university student library borrower cards across the campus", "Demanding that the publisher physically refund all historical subscription payments from 1950", "Permanently disconnecting the entire university campus from the global internet"],
     ["परिसर में सभी विश्वविद्यालय छात्र पुस्तकालय उधारकर्ता कार्डों को तुरंत रद्द करना", "यह मांग करना कि प्रकाशक 1950 से सभी ऐतिहासिक सदस्यता भुगतानों को भौतिक रूप से वापस करे", "पूरे विश्वविद्यालय परिसर को वैश्विक इंटरनेट से स्थायी रूप से डिस्कनेक्ट करना"],
     "Most paywall lockouts stem from dropped IP authentication strings, proxy configuration changes, expired SSL certs, or platform migrations by the publisher.",
     "जब अचानक किसी जर्नल पर पैसे मांगने (Paywall) लगे, तो सबसे पहले यह जांचा जाता है कि कहीं कॉलेज का आईपी एड्रेस तो नहीं बदल गया या प्रॉक्सी सर्वर में कोई दिक्कत तो नहीं आई।"),

    # 38: Creative Commons CC-BY License
    ("Why is the Creative Commons Attribution license (CC-BY) the gold standard for Open Access journal articles?",
     "ओपन एक्सेस जर्नल लेखों के लिए क्रिएटिव कॉमन्स एट्रिब्यूशन लाइसेंस (CC-BY) स्वर्ण मानक क्यों है?",
     "It permits anyone to share, copy, adapt, and build upon the work for any purpose (even commercially), provided original authorship credit is properly given",
     "यह किसी को भी किसी भी उद्देश्य के लिए (यहां तक कि व्यावसायिक रूप से) काम को साझा करने, कॉपी करने, अनुकूलित करने और निर्माण करने की अनुमति देता है, बशर्ते कि मूल लेखकत्व श्रेय ठीक से दिया गया हो",
     ["It forbids anyone from reading the research article without written government authorization", "It requires all readers to pay a mandatory five-dollar fee every time they open the PDF", "It permanently transfers the author's copyright ownership to commercial search engines"],
     ["यह किसी को भी लिखित सरकारी प्राधिकरण के बिना शोध लेख पढ़ने से रोकता है", "यह सभी पाठकों को हर बार पीडीएफ खोलने पर अनिवार्य पांच डॉलर का शुल्क देने की आवश्यकता होती है", "यह लेखक के कॉपीराइट स्वामित्व को वाणिज्यिक खोज इंजनों को स्थायी रूप से स्थानांतरित करता है"],
     "CC-BY maximizes scholarly reuse, text and data mining, and translation while ensuring the original academic creators receive permanent citation attribution.",
     "CC-BY लाइसेंस दुनिया में सबसे खुला और लोकप्रिय है; यह किसी को भी लेख पढ़ने, अनुवाद करने और आगे शोध में इस्तेमाल की पूरी छूट देता है, बस मूल लेखक का नाम लिखना ज़रूरी होता है।"),

    # 39: CC-BY-NC and Commercial Mining
    ("What operational limitation does a 'Non-Commercial' clause (CC-BY-NC) impose that can hinder digital humanities and scientific research?",
     "एक 'गैर-वाणिज्यिक' खंड (CC-BY-NC) क्या परिचालन सीमा लगाता है जो डिजिटल मानविकी और वैज्ञानिक अनुसंधान में बाधा डाल सकता है?",
     "It restricts commercial entities from text-and-data mining (TDM) the literature and can legally prohibit republishing in commercial open-access databases or educational coursepacks",
     "यह वाणिज्यिक संस्थाओं को साहित्य के टेक्स्ट-एंड-डेटा माइनिंग (TDM) से प्रतिबंधित करता है और व्यावसायिक ओपन-एक्सेस डेटाबेस या शैक्षिक पाठ्यक्रम पैक में पुनर्प्रकाशन को कानूनी रूप से प्रतिबंधित कर सकता है",
     ["It forces universities to demolish physical library buildings within twenty-four hours", "It mandates that all research papers must be written in rhyme and meter", "It prevents academic libraries from purchasing electronic computers"],
     ["यह विश्वविद्यालयों को चौबीस घंटे के भीतर भौतिक पुस्तकालय भवनों को ध्वस्त करने के लिए मजबूर करता है", "यह अनिवार्य करता है कि सभी शोध पत्र तुकबंदी और मीटर में लिखे जाने चाहिए", "यह अकादमिक पुस्तकालयों को इलेक्ट्रॉनिक कंप्यूटर खरीदने से रोकता है"],
     "While intended to stop commercial exploitation, NC restrictions frequently create legal ambiguities that prevent inclusion in open course reserves or automated research indexing.",
     "हालांकि CC-BY-NC व्यावसायिक कंपनियों को मुनाफ़ा कमाने से रोकता है, लेकिन इससे कभी-कभी यह भ्रम पैदा हो जाता है कि क्या कोई निजी कॉलेज या सर्च इंजन इसका डेटा माइनिंग कर सकता है या नहीं।"),

    # 40: Shodhganga in Indian ERM
    ("What is 'Shodhganga' developed and maintained by the INFLIBNET Centre?",
     "INFLIBNET केंद्र द्वारा विकसित और अनुरक्षित 'शोधगंगा' (Shodhganga) क्या है?",
     "The national open-access digital repository of Indian electronic doctoral theses and dissertations (ETDs) submitted by research scholars across Indian universities",
     "भारतीय विश्वविद्यालयों में शोधार्थियों द्वारा प्रस्तुत भारतीय इलेक्ट्रॉनिक डॉक्टरेट शोध प्रबंधों और शोध प्रबंधों (ETDs) का राष्ट्रीय ओपन-एक्सेस डिजिटल रिपॉजिटरी",
     ["A software program designed to print paper barcodes on physical catalog cards", "A high-speed optical fiber cable connecting public libraries across North America", "A proprietary operating system developed to replace Linux on server mainframes"],
     ["भौतिक कैटलॉग कार्ड पर कागज़ के बारकोड प्रिंट करने के लिए डिज़ाइन किया गया एक सॉफ़्टवेयर प्रोग्राम", "उत्तरी अमेरिका के सार्वजनिक पुस्तकालयों को जोड़ने वाली एक उच्च गति ऑप्टिकल फाइबर केबल", "सर्वर मेनफ्रेम पर लिनक्स को बदलने के लिए विकसित एक मालिकाना ऑपरेटिंग सिस्टम"],
     "Shodhganga hosts over 500,000 full-text Indian PhD theses, preventing research duplication and providing open global access to Indian academic scholarship.",
     "शोधगंगा (INFLIBNET) भारत का राष्ट्रीय डिजिटल भंडार है जहाँ देश भर के विश्वविद्यालयों की 5 लाख से अधिक पीएचडी थीसिस मुफ्त और ओपन एक्सेस में पढ़ने के लिए उपलब्ध हैं।"),

    # 41: ShodhGangotri
    ("How does 'ShodhGangotri' complement the Shodhganga national repository in India?",
     "'शोधगंगोत्री' (ShodhGangotri) भारत में शोधगंगा राष्ट्रीय रिपॉजिटरी का पूरक कैसे है?",
     "It is a digital repository of approved research proposals (synopses) submitted for PhD registration, providing a window into ongoing research and preventing duplication",
     "यह पीएचडी पंजीकरण के लिए प्रस्तुत अनुमोदित अनुसंधान प्रस्तावों (सिनॉप्सिस) का एक डिजिटल भंडार है, जो चल रहे शोध में एक खिड़की प्रदान करता है और दोहराव को रोकता है",
     ["It is a commercial bookstore selling second-hand digital textbook licenses to private corporations", "It stores digital backups of computer hardware firmware files exclusively", "It is an automated algorithm that charges university professors per-page publishing fees"],
     ["यह निजी निगमों को पुरानी डिजिटल पाठ्यपुस्तक लाइसेंस बेचने वाली एक वाणिज्यिक किताबों की दुकान है", "यह विशेष रूप से कंप्यूटर हार्डवेयर फर्मवेयर फ़ाइलों के डिजिटल बैकअप को संग्रहीत करता है", "यह एक स्वचालित एल्गोरिदम है जो विश्वविद्यालय के प्रोफेसरों से प्रति-पृष्ठ प्रकाशन शुल्क लेता है"],
     "While Shodhganga archives completed theses, ShodhGangotri tracks registered research synopses, preventing researchers from selecting already claimed research topics.",
     "शोधगंगा में पूरी हो चुकी थीसिस होती हैं; जबकि शोधगंगोत्री में वर्तमान में चल रहे शोध का सिनॉप्सिस (प्रस्ताव) दर्ज होता है ताकि दो छात्र एक ही विषय पर काम न करने लगें।"),

    # 42: e-ShodhSindhu Consortium
    ("What is 'e-ShodhSindhu' created by the Ministry of Education in India?",
     "भारत में शिक्षा मंत्रालय द्वारा निर्मित 'ई-शोधसिंधु' (e-ShodhSindhu) क्या है?",
     "A merged national consortium providing centrally negotiated, highly subsidized electronic journal and database subscriptions to higher educational institutions across India",
     "एक विलय किया गया राष्ट्रीय संघ जो पूरे भारत में उच्च शिक्षण संस्थानों को केंद्रीय रूप से बातचीत की गई, अत्यधिक सब्सिडी वाली इलेक्ट्रॉनिक जर्नल और डेटाबेस सदस्यता प्रदान करता है",
     ["A postal shipping service that transports printed books between state library departments", "A hardware firewall appliance manufactured to filter unwanted internet spam emails", "An automated robotic lawnmower designed to maintain university campus gardens"],
     ["एक डाक शिपिंग सेवा जो राज्य पुस्तकालय विभागों के बीच मुद्रित पुस्तकों का परिवहन करती है", "अवांछित इंटरनेट स्पैम ईमेल को फ़िल्टर करने के लिए निर्मित एक हार्डवेयर फ़ायरवॉल उपकरण", "विश्वविद्यालय परिसर के बगीचों को बनाए रखने के लिए डिज़ाइन किया गया एक स्वचालित रोबोटिक लॉनमूवर"],
     "e-ShodhSindhu combined the UGC-INFONET, N-LIST, and INDEST-AICTE consortia to maximize bargaining power with global publishers (Elsevier, Springer, Wiley, IEEE).",
     "ई-शोधसिंधु (e-ShodhSindhu) भारत सरकार का राष्ट्रीय कंसोर्टियम है जो देश भर के विश्वविद्यालयों और कॉलेजों को अंतरराष्ट्रीय जर्नल्स और डेटाबेस बहुत सस्ती दर पर उपलब्ध कराता है।"),

    # 43: N-LIST for Colleges
    ("What is the primary target beneficiary community of INFLIBNET's 'N-LIST' project?",
     "INFLIBNET की 'एन-लिस्ट' (N-LIST) परियोजना का प्राथमिक लक्षित लाभार्थी समुदाय क्या है?",
     "Undergraduate and postgraduate students, researchers, and faculty members of affiliated colleges across India (especially in rural and semi-urban areas)",
     "पूरे भारत में संबद्ध कॉलेजों के स्नातक और स्नातकोत्तर छात्र, शोधकर्ता और संकाय सदस्य (विशेष रूप से ग्रामीण और अर्ध-शहरी क्षेत्रों में)",
     ["Commercial multinational software engineering corporations", "Overseas foreign diplomats visiting national embassies in New Delhi", "Military defense contractors manufacturing telecommunication satellites"],
     ["वाणिज्यिक बहुराष्ट्रीय सॉफ्टवेयर इंजीनियरिंग निगम", "नई दिल्ली में राष्ट्रीय दूतावासों का दौरा करने वाले विदेशी राजनयिक", "दूरसंचार उपग्रहों का निर्माण करने वाले सैन्य रक्षा ठेकेदार"],
     "N-LIST extends e-ShodhSindhu benefits to thousands of non-university colleges, providing remote access to over 6,000 e-journals and 199,500+ e-books for a nominal fee.",
     "N-LIST विशेष रूप से छोटे और दूरदराज के कॉलेजों के लिए बनाया गया है, जहाँ के छात्रों को केवल ₹5,900 वार्षिक कॉलेज शुल्क में लाखों ई-बुक्स और हज़ारों ई-जर्नल्स की सीधी पहुँच मिलती है।"),

    # 44: Core vs Non-Core Subscriptions
    ("In collection assessment, how do librarians categorize e-journal titles to guide tough cancellation decisions?",
     "संग्रह मूल्यांकन में, कठिन रद्दीकरण निर्णयों का मार्गदर्शन करने के लिए लाइब्रेरियन ई-जर्नल शीर्षकों को कैसे वर्गीकृत करते हैं?",
     "Classifying titles as 'Core' (essential to ongoing degree curricula with consistently low CPU) versus 'Peripheral/Specialized' (low usage and extremely high CPU)",
     "शीर्षकों को 'कोर' (लगातार कम सीपीयू के साथ चल रहे डिग्री पाठ्यक्रम के लिए आवश्यक) बनाम 'परिधीय/विशेष' (कम उपयोग और अत्यधिक उच्च सीपीयू) के रूप में वर्गीकृत करना",
     ["Categorizing books solely by the color of their front cover binding cloth", "Classifying journals based on the astrological zodiac sign of the founding publisher", "Dividing journals by the physical weight of paper stock used in printing"],
     ["केवल उनके सामने के कवर बाइंडिंग कपड़े के रंग के आधार पर पुस्तकों को वर्गीकृत करना", "संस्थापक प्रकाशक की ज्योतिषीय राशि के आधार पर पत्रिकाओं को वर्गीकृत करना", "छपाई में प्रयुक्त कागज़ के स्टॉक के भौतिक वजन द्वारा पत्रिकाओं को विभाजित करना"],
     "Core journals are protected from budget cuts; non-core titles with exorbitant cost-per-use are canceled and replaced with rapid interlibrary loan or pay-per-view access.",
     "कोर (Core) जर्नल्स वे हैं जो सिलेबस के लिए अति आवश्यक हैं और खूब पढ़े जाते हैं; जबकि पेरिफेरल जर्नल्स वे हैं जिन्हें साल में बमुश्किल 1-2 लोग पढ़ते हैं और उन्हें बजट कटने पर हटा दिया जाता है।"),

    # 45: OpenURL Router / Proxy Rewriting
    ("Why must an EZproxy server's configuration file (`config.txt`) be updated when a publisher moves from HTTP to HTTPS or changes domains?",
     "जब कोई प्रकाशक HTTP से HTTPS पर जाता है या डोमेन बदलता है तो EZproxy सर्वर की कॉन्फ़िगरेशन फ़ाइल (`config.txt`) को क्यों अपडेट किया जाना चाहिए?",
     "Because EZproxy relies on explicit stanza definitions (URLs, hostnames, and cookies) to recognize, intercept, and rewrite traffic for authorized authentication",
     "क्योंकि EZproxy अधिकृत प्रमाणीकरण के लिए ट्रैफ़िक को पहचानने, रोकने और फिर से लिखने के लिए स्पष्ट श्लोक परिभाषाओं (URL, होस्टनाम और कुकीज़) पर निर्भर करता है",
     ["Because computers refuse to process numbers larger than 100 on internet routers", "Because changing domains automatically deletes all PDF files stored on publisher web servers", "Because the Indian Telegraph Act mandates reformatting server drives upon domain changes"],
     ["क्योंकि कंप्यूटर इंटरनेट राउटर पर 100 से बड़ी संख्याओं को संसाधित करने से इनकार करते हैं", "क्योंकि डोमेन बदलने से प्रकाशक वेब सर्वर पर संग्रहीत सभी पीडीएफ फाइलें स्वचालित रूप से हटा दी जाती हैं", "क्योंकि भारतीय टेलीग्राफ अधिनियम डोमेन परिवर्तन पर सर्वर ड्राइव को रीफॉर्मेट करना अनिवार्य करता है"],
     "An out-of-date EZproxy stanza fails to rewrite the new domain, causing off-campus users to hit the publisher's public paywall rather than the authenticated session.",
     "EZproxy के config.txt में हर प्रकाशक का सही डोमेन और नियम लिखना पड़ता है; यदि प्रकाशक ने पता बदल लिया और EZproxy अपडेट नहीं हुआ, तो छात्रों के सामने सीधे पेवॉल आ जाएगा।"),

    # 46: Usage Drop Alerting
    ("Why should an ERM system feature automated 'Usage Drop Alerts'?",
     "एक ERM प्रणाली में स्वचालित 'उपयोग गिरावट अलर्ट' (Usage Drop Alerts) की सुविधा क्यों होनी चाहिए?",
     "To rapidly notify librarians when usage for a major subscribed resource drops to zero unexpectedly, signaling silent technical issues like broken proxy links or expired certificates",
     "जब किसी प्रमुख सदस्यता प्राप्त संसाधन का उपयोग अप्रत्याशित रूप से शून्य हो जाता है, तो लाइब्रेरियनों को तुरंत सूचित करना, टूटे हुए प्रॉक्सी लिंक या समाप्त प्रमाण पत्र जैसी मूक तकनीकी समस्याओं का संकेत देना",
     ["To penalize students who do not read enough scientific journals during examination weeks", "To automatically turn off computer monitors in the library basement at midnight", "To reduce the physical bandwidth speed of the university campus internet connection"],
     ["उन छात्रों को दंडित करना जो परीक्षा के हफ्तों के दौरान पर्याप्त वैज्ञानिक पत्रिकाएं नहीं पढ़ते हैं", "आधी रात को पुस्तकालय के बेसमेंट में कंप्यूटर मॉनिटर को स्वचालित रूप से बंद करना", "विश्वविद्यालय परिसर के इंटरनेट कनेक्शन की भौतिक बैंडविड्थ गति को कम करना"],
     "Automated alerts catch authentication failures before patrons get frustrated, ensuring technical problems are diagnosed and resolved proactively.",
     "यदि किसी लोकप्रिय डेटाबेस का उपयोग अचानक शून्य हो जाए, तो सिस्टम तुरंत अलर्ट भेजता है ताकि लाइब्रेरियन को पता चल जाए कि कोई तकनीकी खराबी (जैसे लिंक टूटना) आ गई है।"),

    # 47: Electronic Resource De-selection
    ("What quantitative and qualitative criteria guide the de-selection (weeding/cancellation) of electronic resources in an academic library?",
     "एक अकादमिक पुस्तकालय में इलेक्ट्रॉनिक संसाधनों के चयन-रद्द (छंटाई/रद्दीकरण) का मार्गदर्शन करने वाले मात्रात्मक और गुणात्मक मानदंड क्या हैं?",
     "High cost-per-use, declining multi-year usage trends, curricular misalignment, publisher price inflation above budget caps, and availability in open-access repositories",
     "उच्च लागत-प्रति-उपयोग, घटती बहु-वर्षीय उपयोग प्रवृत्तियाँ, पाठ्यचर्या का गलत संरेखण, बजट सीमा से ऊपर प्रकाशक मूल्य मुद्रास्फीति, और ओपन-एक्सेस रिपॉजिटरी में उपलब्धता",
     ["The physical thickness and binding color of paper covers on past archive issues", "The personal political opinions of the publishing corporation's chief executive officer", "The geographic distance in miles between the university and the publisher's warehouse"],
     ["पिछले संग्रह मुद्दों पर कागज़ के कवर की भौतिक मोटाई और बाइंडिंग रंग", "प्रकाशन निगम के मुख्य कार्यकारी अधिकारी के व्यक्तिगत राजनीतिक विचार", "विश्वविद्यालय और प्रकाशक के गोदाम के बीच मील में भौगोलिक दूरी"],
     "Cancellation decisions balance rigorous empirical metrics (COUNTER CPU) with liaison faculty consultation to protect critical departmental research needs.",
     "ई-रिसोर्स को कैंसिल करने से पहले आँकड़े देखे जाते हैं: क्या इसका Cost-Per-Use बहुत ज़्यादा है? क्या प्रोफेसर्स और छात्र इसे पढ़ रहे हैं? और क्या इसके पेपर ओपन एक्सेस में मुफ्त मिल रहे हैं?"),

    # 48: Fifth Law of LIS & Electronic Resource Management
    ("How does modern Electronic Resource Management vividly fulfill S. R. Ranganathan's Fifth Law of Library Science ('The Library is a Growing Organism')?",
     "आधुनिक इलेक्ट्रॉनिक संसाधन प्रबंधन डॉ. एस. आर. रंगनाथन के पुस्तकालय विज्ञान के पांचवें नियम ('पुस्तकालय एक वर्धनशील संस्था है') को सबसे स्पष्ट रूप से कैसे पूरा करता है?",
     "By expanding the library's reach infinitely into the digital sphere, managing millions of electronic articles without physical shelf space constraints, and evolving with technology",
     "पुस्तकालय की पहुँच को डिजिटल क्षेत्र में असीम रूप से विस्तारित करके, भौतिक शेल्फ स्थान की बाधाओं के बिना लाखों इलेक्ट्रॉनिक लेखों का प्रबंधन करके, और प्रौद्योगिकी के साथ विकसित होकर",
     ["By completely abolishing physical paper books and burning historical library archives", "By forcing all library patrons to buy expensive commercial smartphones every semester", "By restricting library catalog access strictly to print books acquired before the year 1900"],
     ["भौतिक कागज़ की किताबों को पूरी तरह से समाप्त करना और ऐतिहासिक पुस्तकालय अभिलेखागार को जलाना", "सभी पुस्तकालय संरक्षकों को हर सेमेस्टर में महंगे वाणिज्यिक स्मार्टफोन खरीदने के लिए मजबूर करना", "वर्ष 1900 से पहले अधिग्रहित प्रिंट पुस्तकों तक पुस्तकालय कैटलॉग पहुंच को सख्ती से सीमित करना"],
     "ERM allows libraries to grow endlessly in knowledge and accessibility, overcoming the physical boundaries of concrete buildings through digital collections.",
     "रंगनाथन का पाँचवाँ नियम कहता है कि पुस्तकालय एक बढ़ता हुआ जीव है; ERMS ने पुस्तकालय को चारदीवारी और अलमारियों से मुक्त कर दिया है, जिससे बिना जगह की कमी के लाखों ई-पुस्तकों का संग्रह बढ़ता रहता है।")
]

print(f"Total Q99 items: {len(q99_items)}")
assert len(q99_items) == 48

with open("build_u5_q99.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nSlot Q99: Electronic Resource Management (ERM) & Usage Standards - 48 items.\n"""\n\n')
    f.write("q99_pool = [\n")
    for item in q99_items:
        f.write(f"    {repr(item)},\n")
    f.write("]\n")
    f.write("print('Q99 loaded, count:', len(q99_pool))\n")

print("Created build_u5_q99.py successfully!")
