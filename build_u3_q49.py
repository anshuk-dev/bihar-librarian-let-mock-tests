# -*- coding: utf-8 -*-
"""
Bihar Librarian LET Mock Test Series - Question Pool: Unit 3, Q49 (48 Items)
Focus: Stock Verification (Physical Inventory Methods: Accession, Shelf List, Barcode/RFID),
GFR 2017 Rule 215 Norms, Loss Write-Offs, Weeding Policies (MUSTIE, Slote, Dormitory Library).
"""

q49_pool = [
    # 1
    ("What is the primary administrative definition of 'Stock Verification' (or Physical Inventory) in a library?",
     "पुस्तकालय में 'भंडार सत्यापन' (Stock Verification / भौतिक सत्यापन) की प्राथमिक प्रशासनिक परिभाषा क्या है?",
     "The systematic physical checking and counting of the library's actual physical holdings against official accession or shelf list records",
     "आधिकारिक परिग्रहण पंजी या शेल्फ लिस्ट रिकॉर्ड के साथ पुस्तकालय के वास्तविक भौतिक संग्रह की व्यवस्थित जांच और मिलान",
     ["Checking the market share prices of publishing companies", "Inspecting the personal bank accounts of library staff", "Counting how many students enter the cafeteria"],
     ["प्रकाशन कंपनियों के शेयर बाजार मूल्यों की जांच", "पुस्तकालय कर्मचारियों के व्यक्तिगत बैंक खातों का निरीक्षण", "कैफेटेरिया में जाने वाले छात्रों की गिनती करना"],
     "Stock verification ascertains the physical presence of documents, identifies missing books, locates misplaced volumes, and assesses preservation needs.",
     "भंडार सत्यापन से यह पता चलता है कि कौन सी पुस्तकें वास्तव में अलमारियों पर मौजूद हैं, कौन सी गुम हो गई हैं और किन्हें मरम्मत की आवश्यकता है।"),

    # 2
    ("Which of the following is widely recognized as the most scientific, efficient, and preferred manual method of stock verification?",
     "निम्नलिखित में से किसे भंडार सत्यापन की सबसे वैज्ञानिक, कुशल और पसंदीदा हस्तचालित (Manual) विधि माना जाता है?",
     "Shelf List Method (शेल्फ लिस्ट विधि / निधानी सूची विधि)",
     "शेल्फ लिस्ट विधि (Shelf List Method)",
     ["Accession Register Method", "Counting Method", "Separate Slip Method"],
     ["परिग्रहण पंजी विधि", "साधारण गणना विधि", "अलग पर्ची विधि"],
     "Because shelf list cards are arranged in the exact order in which books stand on shelves (Call Number order), checking is swift and orderly.",
     "शेल्फ लिस्ट अलमारी पर रखी पुस्तकों के वास्तविक क्रम (वर्गांक क्रम) में व्यवस्थित होती है, इसलिए इससे जांच सबसे तेज और व्यवस्थित होती है।"),

    # 3
    ("Why is the 'Accession Register Method' of stock verification generally discouraged in large modern libraries?",
     "बड़े आधुनिक पुस्तकालयों में भंडार सत्यापन की 'परिग्रहण पंजी विधि' को आमतौर पर हतोत्साहित क्यों किया जाता है?",
     "It causes heavy wear and tear to the permanent legal register, requires extensive back-and-forth flipping, and is extremely slow",
     "यह स्थायी कानूनी रजिस्टर को गंदा और जीर्ण-शीर्ण करता है, बार-बार पन्ने पलटने पड़ते हैं और यह अत्यंत धीमी प्रक्रिया है",
     ["Because accession registers are written in foreign languages", "Because the government bans opening registers", "Because accession registers are too small to read"],
     ["क्योंकि परिग्रहण रजिस्टर विदेशी भाषाओं में लिखे होते हैं", "क्योंकि सरकार रजिस्टर खोलने पर रोक लगाती है", "क्योंकि रजिस्टर पढ़ने में बहुत छोटे होते हैं"],
     "Flipping through hundreds of ledger pages while walking along shelves causes physical degradation to the primary legal archive of the library.",
     "भारी-भरकम परिग्रहण रजिस्टर को अलमारियों के बीच ले जाकर पन्ने पलटने से स्थायी सरकारी रिकॉर्ड फट जाता है और समय बहुत बर्बाद होता है।"),

    # 4
    ("How does the 'Loose Sheet Method' (or Numerical Check Sheet Method) operate during stock verification?",
     "भंडार सत्यापन के दौरान 'खुले पत्रक विधि' (Loose Sheet Method) किस प्रकार कार्य करती है?",
     "Sheets printed with continuous accession numbers (e.g., 1 to 50,000) are ticked or crossed off as each corresponding book is physically verified",
     "क्रमिक परिग्रहण संख्याओं (जैसे 1 से 50,000) वाले मुद्रित पत्रकों पर पुस्तक मिलने पर संबंधित संख्या को काट या टिक दिया जाता है",
     ["Staff write essays about each book on loose paper", "Loose book pages are counted and weighed", "Sheets of blank paper are inserted into every book"],
     ["कर्मचारी खुले कागजों पर प्रत्येक पुस्तक पर निबंध लिखते हैं", "खुले पन्नों को गिनकर तौला जाता है", "प्रत्येक पुस्तक में कोरे कागज लगाए जाते हैं"],
     "Unticked numbers on the sheets at the conclusion of the audit represent items missing or unaccounted for on the shelves.",
     "इस विधि में परिग्रहण संख्याओं की मुद्रित शीट पर टिक लगाया जाता है; अंत में जिन नंबरों पर टिक नहीं लगता, वे गुमशुदा पुस्तकें होती हैं।"),

    # 5
    ("In an automated library environment, how is rapid stock verification conducted using barcode technology?",
     "स्वचालित पुस्तकालय वातावरण में, बारकोड तकनीक का उपयोग करके तीव्र भंडार सत्यापन कैसे किया जाता है?",
     "Portable batch barcode terminals / wireless scanners scan book barcodes directly on the shelves, and software compares the file against the catalogue database",
     "पोर्टेबल हैंडहेल्ड बारकोड स्कैनर से अलमारियों पर सीधे बारकोड स्कैन किए जाते हैं, और सॉफ्टवेयर डेटाबेस से मिलान कर स्वतः रिपोर्ट बनाता है",
     ["By typing every accession number manually on a typewriter", "By photographing book spines with film cameras", "By photocopying barcodes on office Xerox machines"],
     ["टाइपराइटर पर प्रत्येक परिग्रहण संख्या हाथ से टाइप करके", "फिल्म कैमरों से पुस्तक की पीठ की तस्वीरें लेकर", "कार्यालय की फोटोकॉपी मशीन पर बारकोड कॉपी करके"],
     "Batch barcode scanners scan thousands of volumes per hour; the ILS instantly outputs lists of present, missing, and misplaced volumes.",
     "हैंडहेल्ड बारकोड स्कैनर से एक घंटे में हजारों पुस्तकें स्कैन हो जाती हैं और सॉफ्टवेयर तुरंत बता देता है कि कौन सी पुस्तकें गायब हैं।"),

    # 6
    ("How does RFID technology further accelerate the stock verification process compared to barcodes?",
     "बारकोड की तुलना में आरएफआईडी (RFID) तकनीक भंडार सत्यापन प्रक्रिया को और अधिक तीव्र कैसे बना देती है?",
     "Handheld RFID wands read tags wirelessly through books without line-of-sight, scanning an entire shelf of books in seconds simply by waving the wand",
     "हैंडहेल्ड आरएफआईडी वैंड बिना पुस्तक को निकाले और बिना सीधे देखे (Non-line-of-sight) अलमारी के सामने घुमाते ही सेकंडों में पूरे रैक को पढ़ लेती है",
     ["RFID requires opening every book to find hidden numbers", "RFID prints paper receipts for every single volume", "RFID works only when books are soaked in water"],
     ["RFID में छिपे नंबर खोजने हेतु प्रत्येक पुस्तक खोलनी पड़ती है", "RFID प्रत्येक पुस्तक की कागजी रसीद प्रिंट करता है", "RFID केवल तभी काम करता है जब पुस्तकें पानी में भीगी हों"],
     "RFID readers capture radio frequency signals from dozens of tags simultaneously, detecting missing, misplaced, and weeded items in real time.",
     "RFID वैंड को अलमारी के सामने से केवल लहराना होता है; रेडियो तरंगें बिना किताब छुए सभी टैग पढ़ लेती हैं और गलत रखी किताबें भी पकड़ लेती हैं।"),

    # 7
    ("What was Dr. S. R. Ranganathan's philosophy regarding closing the library for annual stock verification?",
     "वार्षिक भंडार सत्यापन के लिए पुस्तकालय बंद करने के संबंध में डॉ. एस. आर. रंगनाथन का क्या दृष्टिकोण था?",
     "He strongly opposed closing the library, asserting that verification should be done continuously throughout the year without disrupting readers",
     "उन्होंने पुस्तकालय बंद करने का कड़ा विरोध किया और कहा कि पाठकों की सेवा रोके बिना पूरे वर्ष निरंतर सत्यापन किया जाना चाहिए",
     ["He demanded closing the library for six months every year", "He believed stock verification should never be done", "He recommended locking all books in iron safes"],
     ["उन्होंने प्रतिवर्ष 6 माह पुस्तकालय बंद रखने की मांग की", "उनका मानना था कि कभी स्टॉक सत्यापन नहीं होना चाहिए", "उन्होंने सभी पुस्तकें लोहे की तिजोरियों में बंद करने की सिफारिश की"],
     "Ranganathan's Fifth Law ('Library is a growing organism') views closing a library as paralyzing a living service; he advocated perpetual sample checks.",
     "रंगनाथन के अनुसार पुस्तकालय बंद करना ज्ञान के प्रवाह को रोकना है; उन्होंने बिना पुस्तकालय बंद किए चक्रानुक्रम में निरंतर सत्यापन का समर्थन किया।"),

    # 8
    ("Under Government of India General Financial Rules (GFR) 2017 Rule 215, what frequency of physical verification is mandatory for collections up to 20,000 volumes?",
     "भारत सरकार के GFR 2017 नियम 215 के तहत, 20,000 खंडों तक के संग्रह वाले पुस्तकालयों के लिए भौतिक सत्यापन की क्या आवृत्ति अनिवार्य है?",
     "Annual physical verification every year (प्रतिवर्ष वार्षिक भौतिक सत्यापन)",
     "प्रतिवर्ष (Annual Physical Verification every year)",
     ["Once every 5 years", "Once every 10 years", "Only once during the librarian's entire career"],
     ["5 वर्षों में एक बार", "10 वर्षों में एक बार", "पुस्तकालयाध्यक्ष के पूरे कार्यकाल में केवल एक बार"],
     "GFR Rule 215 explicitly mandates: 'Physical verification of library books should be done every year in case of libraries having not more than twenty thousand volumes'.",
     "जीएफआर 215 स्पष्ट आदेश देता है कि 20,000 तक की पुस्तकों वाले पुस्तकालयों का शत-प्रतिशत सत्यापन प्रतिवर्ष होना अनिवार्य है।"),

    # 9
    ("Under GFR 2017 Rule 215, for library collections ranging from 20,000 to 50,000 volumes, physical verification must be performed at least:",
     "GFR 2017 नियम 215 के अंतर्गत, 20,000 से 50,000 पुस्तकों वाले पुस्तकालयों में भौतिक सत्यापन कम से कम कब किया जाना चाहिए?",
     "Once in three years (तीन वर्षों में एक बार)", "तीन वर्षों में एक बार (At least once in three years)",
     ["Every six months", "Annually without fail", "Once in 15 years"],
     ["प्रत्येक छह माह में", "बिना नागा प्रतिवर्ष", "15 वर्षों में एक बार"],
     "For collections between 20,000 and 50,000 volumes, GFR allows physical verification to be conducted at intervals not exceeding 3 years.",
     "20 हजार से 50 हजार पुस्तकों वाले पुस्तकालयों को तीन साल में कम से कम एक बार सत्यापन कराने की छूट दी गई है।"),

    # 10
    ("Under GFR 2017 Rule 215, for large libraries having more than 50,000 volumes, physical verification may be conducted by:",
     "GFR 2017 नियम 215 के तहत, 50,000 से अधिक पुस्तकों वाले बड़े पुस्तकालयों में सत्यापन किस प्रकार किया जा सकता है?",
     "Sample physical verification of not less than 10% of the collection at intervals of not more than 3 to 5 years",
     "कम से कम 10% संग्रह का नमूना (सैंपल) सत्यापन 3 से 5 वर्षों के अंतराल पर",
     ["Locking the library permanently", "Counting only the fiction section", "Checking only the librarian's desk drawer"],
     ["पुस्तकालय को स्थायी रूप से बंद करके", "केवल उपन्यास अनुभाग की गिनती करके", "केवल पुस्तकालयाध्यक्ष की मेज की दराज जांचकर"],
     "For over 50,000 volumes, sample checks of at least 10% are sufficient; full 100% census is required only if sample reveals unusual discrepancies.",
     "50 हजार से बड़े संग्रह में 3 से 5 साल में 10% का रैंडम सैंपल सत्यापन मान्य है; यदि इसमें भारी कमी मिले तभी पूरे संग्रह की जांच होती है।"),

    # 11
    ("Under GFR 2017 Rule 215, what rate of book loss is officially recognized as acceptable and reasonable in open-access libraries?",
     "GFR 2017 नियम 215 के अनुसार खुले प्रवेश (Open Access) वाले पुस्तकालयों में पुस्तकों की किस सीमा तक की हानि को स्वाभाविक और स्वीकार्य माना गया है?",
     "Loss of 5 volumes per 1,000 volumes issued and/or consulted in a year",
     "प्रति 1,000 जारी या संदर्भित पुस्तकों पर 5 पुस्तकों का नुकसान",
     ["Zero loss permitted (100% recovery from staff salary)", "50 volumes per 1,000 volumes", "100 volumes per 1,000 volumes"],
     ["शून्य नुकसान (वेतन से शत-प्रतिशत वसूली)", "प्रति 1,000 पर 50 पुस्तकें", "प्रति 1,000 पर 100 पुस्तकें"],
     "Rule 215 acknowledges that open access entails incidental loss, setting 5 books per 1,000 issued/consulted as the write-off threshold.",
     "सरकारी नियमों में माना गया है कि खुले पुस्तकालय में प्रति 1,000 प्रयुक्त पुस्तकों पर 5 पुस्तकों का नुकसान सामान्य टूट-फूट और क्षति की तरह स्वीकार्य है।"),

    # 12
    ("Under Indian administrative rules, can library professionals be held personally financially liable for missing books within the permissible GFR limit?",
     "भारतीय प्रशासनिक नियमों के अनुसार, क्या अनुमेय GFR सीमा के भीतर गायब हुई पुस्तकों के लिए पुस्तकालय कर्मचारियों को व्यक्तिगत रूप से जिम्मेदार ठहराया जा सकता है?",
     "No; library staff cannot be made personally liable for normal losses unless dishonesty, fraud, or gross negligence is established",
     "नहीं; जब तक बेईमानी, धोखाधड़ी या गंभीर लापरवाही सिद्ध न हो, तब तक कर्मचारियों से कोई वसूली नहीं की जा सकती",
     ["Yes; the head librarian must pay out of pocket immediately", "Yes; salaries of all junior assistants are suspended", "Yes; staff must surrender their personal books"],
     ["हाँ; मुख्य पुस्तकालयाध्यक्ष को तुरंत जेब से भरना होगा", "हाँ; सभी कनिष्ठ सहायकों का वेतन रोक दिया जाता है", "हाँ; कर्मियों को अपनी निजी पुस्तकें जमा करनी होंगी"],
     "The Ministry of Finance and UGC have affirmed that library staff are not storekeepers; reasonable losses are inherent to public service.",
     "वित्त मंत्रालय और यूजीसी का स्पष्ट निर्देश है कि पुस्तकालयाध्यक्ष स्टोरकीपर नहीं हैं; तय सीमा में नुकसान होने पर वेतन से कटौती नहीं की जा सकती।"),

    # 13
    ("The formal administrative and financial procedure of removing irrecoverable missing or damaged books from library accounts and records is called:",
     "पुस्तकालय अभिलेखों और खातों से अप्राप्य खोई हुई या नष्ट पुस्तकों को औपचारिक रूप से हटाने की प्रशासनिक प्रक्रिया क्या कहलाती है?",
     "Writing Off (बट्टे खाते में डालना / राइट-ऑफ करना)", "बट्टे खाते में डालना (Writing Off)",
     ["Stock Capitalization", "Depreciation Levy", "Asset Confiscation"],
     ["स्टॉक पूंजीकरण", "मूल्यह्रास कर", "संपत्ति जब्ती"],
     "Writing off requires formal authorization from the Competent Financial Authority (e.g., Executive Council / Board of Governors).",
     "राइट-ऑफ वह वैधानिक प्रक्रिया है जिसमें सक्षम वित्तीय अधिकारी की मंजूरी से गुमशुदा पुस्तकों को सरकारी संपत्ति रजिस्टर से हटा दिया जाता है।"),

    # 14
    ("What is an 'Untraceable List' (or Pending List) created during stock verification?",
     "भंडार सत्यापन के दौरान तैयार की गई 'अप्राप्य सूची' (Untraceable / Missing List) क्या होती है?",
     "A provisional list of books that could not be physically found on the shelves, maintained for a tracking period (e.g., 6 months) before declaring them permanently lost",
     "अलमारियों पर न मिली पुस्तकों की अनंतिम सूची, जिसे स्थायी रूप से खोया घोषित करने से पहले 6 महीने तक खोज हेतु रखा जाता है",
     ["A list of students expelled from college", "A catalogue of books written in secret codes", "An inventory of stolen computers"],
     ["कॉलेज से निकाले गए छात्रों की सूची", "गुप्त कोड में लिखी पुस्तकों की सूची", "चोरी हुए कंप्यूटरों की सूची"],
     "Many 'missing' books are merely misplaced; keeping them on a search list for a semester allows staff to locate and restore them.",
     "सत्यापन के तुरंत बाद किताब को खोया नहीं माना जाता; कई किताबें गलत अलमारी में दबी होती हैं, जिन्हें कुछ महीनों की तलाश के बाद ही बट्टे खाते डाला जाता है।"),

    # 15
    ("Stanley J. Slote formulated an influential weeding methodology in his classic book 'Weeding Library Collections' based on:",
     "स्टेनली जे. स्लोट ने अपनी क्लासिक पुस्तक 'वीडिंग लाइब्रेरी कलेक्शंस' में किस आधार पर एक प्रभावशाली छंटाई पद्धति तैयार की?",
     "Shelf-Time Period: analyzing the length of time an item has sat on the shelf since its last circulation",
     "शेल्फ-टाइम अवधि (Shelf-Time Period): यह विश्लेषण करना कि पिछली बार जारी होने के बाद से कोई पुस्तक कितने समय से अलमारी में बिना पढ़े रखी है",
     ["The physical weight of the book block", "The alphabetical order of author surnames", "The number of chapters in the table of contents"],
     ["पुस्तक का कुल शारीरिक वजन", "लेखक के कुलनाम का वर्णमाला क्रम", "विषय-सूची में अध्यायों की संख्या"],
     "Slote proved that the time elapsed since last checkout ('shelf-time period') is the most reliable predictor of future user demand.",
     "स्लोट ने सिद्ध किया कि जो किताब पिछले 3-5 वर्षों से अलमारी से एक बार भी नहीं निकली, उसके भविष्य में पढ़े जाने की संभावना लगभग शून्य होती है।"),

    # 16
    ("What does 'Core Collection' signify in Stanley Slote's weeding theory?",
     "स्टेनली स्लोट के छंटाई सिद्धांत में 'मुख्य संग्रह' (Core Collection) से क्या तात्पर्य है?",
     "The minimum, highly active portion of the collection capable of satisfying approximately 95% to 99% of total patron circulation demand",
     "संग्रह का वह न्यूनतम और अत्यधिक सक्रिय हिस्सा जो पाठकों की कुल अध्ययन मांग का लगभग 95% से 99% हिस्सा पूरा करने में सक्षम होता है",
     ["Books stored inside iron strongrooms", "Books published exclusively in Sanskrit", "Dictionaries reserved for faculty only"],
     ["लोहे के मजबूत कमरों में बंद पुस्तकें", "केवल संस्कृत में प्रकाशित पुस्तकें", "केवल प्राध्यापकों हेतु आरक्षित शब्दकोश"],
     "Slote showed that a relatively small, weeded 'core collection' meets virtually all patron reading needs while drastically reducing clutter.",
     "स्लोट का कहना था कि पुस्तकालय का केवल 20-30% संग्रह ही 95% पाठकों की जरूरत पूरी करता है, बाकी निष्क्रिय रद्दी को हटाया जा सकता है।"),

    # 17
    ("What is a 'Dormitory Library' or 'Secondary Storage Facility' in library system architecture?",
     "पुस्तकालय प्रणाली में 'डॉर्मिटरी लाइब्रेरी' (Dormitory Library) या द्वितीयक भंडारण सुविधा क्या होती है?",
     "A cost-effective, high-density offsite warehouse where seldom-used but historically valuable weeded materials are stored and retrieved on demand",
     "कम लागत वाला ऑफसाइट गोदाम जहां कम उपयोग की जाने वाली लेकिन ऐतिहासिक रूप से महत्वपूर्ण पुस्तकों को सघन रूप में सुरक्षित रखा जाता है",
     ["A hostel bedroom where students sleep with books", "A library open only from midnight to sunrise", "A children's reading room decorated with toys"],
     ["छात्रावास का कमरा जहाँ छात्र सोते हैं", "केवल आधी रात से सुबह तक खुला पुस्तकालय", "खिलौनों से सजा बच्चों का वाचनालय"],
     "Dormitory libraries (advocated by Ranganathan) preserve regional heritage without congesting active main university campus shelves.",
     "रंगनाथन ने 'डॉर्मिटरी लाइब्रेरी' की अवधारणा दी, ताकि पुरानी दुर्लभ पुस्तकों को नष्ट करने के बजाय शहर से बाहर सस्ते गोदाम में संजोया जा सके।"),

    # 18
    ("In the CREW method of weeding, what does the formula '5/3/MUSTIE' indicate for a particular subject category?",
     "CREW छंटाई पद्धति में, किसी विषय श्रेणी के लिए '5/3/MUSTIE' सूत्र का क्या अर्थ होता है?",
     "Weed if the book is older than 5 years since copyright, has had no circulation in the last 3 years, and meets any MUSTIE criteria",
     "यदि पुस्तक कॉपीराइट से 5 वर्ष से अधिक पुरानी है, पिछले 3 वर्षों में एक बार भी जारी नहीं हुई है, और किसी MUSTIE मानदंड को पूरा करती है तो छांट दें",
     ["Keep 5 copies, bind 3 copies, and buy 5 new books", "Check the book in 5 minutes, 3 times every month", "Sell books for 5 rupees after 3 days of purchase"],
     ["5 प्रतियां रखें, 3 जिल्द बंधवाएं और 5 नई खरीदें", "प्रतिमाह 3 बार 5 मिनट में पुस्तक जांचें", "खरीद के 3 दिन बाद 5 रुपये में बेचें"],
     "The numerical CREW benchmarks (e.g., 5/3/MUSTIE) give precise age and dormancy thresholds tailored to individual Dewey divisions.",
     "5/3/MUSTIE का अर्थ है: प्रकाशन को 5 साल बीत चुके हों, पिछले 3 साल से किसी ने न पढ़ा हो और वह फटी या पुरानी हो, तो उसे निकाल दें।"),

    # 19
    ("Why is weeding considered an application of S.R. Ranganathan's Fifth Law of Library Science ('The Library is a Growing Organism')?",
     "पुस्तकालय सामग्री की छंटाई (Weeding) को एस. आर. रंगनाथन के 5वें नियम ('पुस्तकालय एक वर्धनशील संस्था है') का अनुप्रयोग क्यों माना जाता है?",
     "Because living organisms must discard worn-out, dead cells through metabolic renewal to sustain overall health and vital growth",
     "क्योंकि स्वस्थ जीवन और निरंतर विकास बनाए रखने के लिए जीवित प्राणियों को अपनी मृत कोशिकाओं और अपशिष्ट का त्याग करना अनिवार्य होता है",
     ["Because growing organisms need to sleep twelve hours a day", "Because plants need fertilizer to produce colorful flowers", "Because older animals grow larger than younger animals"],
     ["क्योंकि बढ़ते जीवों को 12 घंटे सोना पड़ता है", "क्योंकि पौधों को फूल खिलाने हेतु खाद चाहिए", "क्योंकि पुराने जानवर नए से बड़े होते हैं"],
     "Ranganathan likened collection weeding to pruning a healthy tree: shedding dead wood revitalizes the living core.",
     "रंगनाथन ने कहा था कि जिस प्रकार जीवित वृक्ष की सूखी डालियों को काटना आवश्यक है, उसी प्रकार पुस्तकालय के विकास हेतु छंटाई अनिवार्य है।"),

    # 20
    ("Which of the following materials should NEVER be weeded during routine library collection de-selection?",
     "पुस्तकालय संग्रह की नियमित छंटाई (Weeding) के दौरान निम्नलिखित में से किसे कभी भी नहीं छांटना चाहिए?",
     "Rare local history documents, institutional archival records, and unique manuscripts",
     "दुर्लभ स्थानीय इतिहास के दस्तावेज, संस्थान के अभिलेखीय रिकॉर्ड और अनूठी पांडुलिपियां",
     ["15-year-old computer software user manuals", "Superseded duplicate income tax guides", "Tattered cheap paperbacks missing multiple pages"],
     ["15 साल पुरानी कंप्यूटर सॉफ्टवेयर नियमावलियां", "पुराने आयकर कानून के कई डुप्लीकेट संस्करण", "फटे-पुराने पन्नों वाले सस्ते पेपरबैक"],
     "Local historical ephemera and institutional archives are irreplaceable cultural heritage and must be preserved permanently.",
     "संस्थान का अपना ऐतिहासिक रिकॉर्ड, शहर का स्थानीय इतिहास और दुर्लभ पांडुलिपियां कभी नहीं फेंकी जातीं; वे स्थायी धरोहर हैं।"),

    # 21
    ("What is the legally approved procedure for disposing of books that have been formally weeded and written off by an Indian government institution?",
     "भारतीय सरकारी संस्थान द्वारा औपचारिक रूप से छांटी गई और बट्टे खाते डाली गई पुस्तकों के निपटान की कानूनी प्रक्रिया क्या है?",
     "Public auction / tender for paper recycling or donation to smaller schools/jails, with proceeds deposited in state revenue",
     "कागज पुनर्चक्रण हेतु सार्वजनिक नीलामी/निविदा या छोटे स्कूलों/जेलों को दान, और प्राप्त आय सरकारी खाते में जमा करना",
     ["Librarians taking the books home to sell privately", "Dumping the books in public city streets at night", "Giving the books free to commercial bookstore owners"],
     ["कर्मचारियों द्वारा किताबें घर ले जाकर निजी तौर पर बेचना", "रात में शहर की सड़कों पर किताबें फेंक देना", "दुकानदारों को मुफ्त में किताबें बांटना"],
     "Written-off books are dismantled/defaced to prevent unauthorized resale, then sold by sealed tender as pulping scrap or donated.",
     "छंटी हुई पुस्तकों पर 'विथड्रॉन' (Withdrawn) की मुहर लगाकर टेंडर के जरिए रद्दी लुगदी बनाने हेतु नीलाम किया जाता है और पैसा राजकोष में जमा होता है।"),

    # 22
    ("What must be stamped prominently across the title page and property marks of every weeded book prior to disposal?",
     "निपटान से पहले प्रत्येक छंटी हुई पुस्तक के शीर्षक पृष्ठ और स्वामित्व मुहरों पर कौन सी मुहर प्रमुखता से लगाई जानी चाहिए?",
     "'WITHDRAWN' or 'DISCARDED' (निकाला गया / निरस्त)",
     "'WITHDRAWN' या 'DISCARDED' (निरस्त / संग्रह से पृथक)",
     ["'NEW ARRIVAL'", "'BESTSELLER'", "'HIGHLY RECOMMENDED'"],
     ["'नया आगमन'", "'बेस्टसेलर'", "'अत्यधिक अनुशंसित'"],
     "Stamping 'WITHDRAWN' cancels legal institutional ownership and prevents unscrupulous individuals from reclaiming the item as stolen library property.",
     "'WITHDRAWN' की मुहर लगाने से पुस्तकालय का कानूनी स्वामित्व समाप्त हो जाता है, जिससे कोई व्यक्ति उसे चोरी की पुस्तक नहीं बता सकता।"),

    # 23
    ("When a book is written off and withdrawn, what updates must be made in the library records?",
     "जब किसी पुस्तक को बट्टे खाते डालकर संग्रह से हटाया जाता है, तो पुस्तकालय अभिलेखों में क्या संशोधन किया जाना अनिवार्य है?",
     "The withdrawal order number and date must be noted in the Accession Register, and all catalog/OPAC records must be deleted or marked withdrawn",
     "परिग्रहण पंजी में निकासी आदेश संख्या व तिथि दर्ज की जानी चाहिए, तथा कैटलॉग/OPAC से उसका रिकॉर्ड हटा या 'Withdrawn' कर दिया जाना चाहिए",
     ["The book title must be erased using white correction fluid", "The entire accession register page must be torn out", "The library building sign must be repainted"],
     ["सफेद फ्लुइड से पुस्तक का नाम मिटाना चाहिए", "रजिस्टर का पूरा पन्ना फाड़ देना चाहिए", "पुस्तकालय भवन का नाम बदलना चाहिए"],
     "The remarks column of the Accession Register records the formal authority write-off memo, keeping the financial inventory accurate.",
     "परिग्रहण पंजी के 'रिमार्क्स' कॉलम में सरकारी आदेश संख्या लिखी जाती है और कंप्यूटर कैटलॉग से स्टेटस हटाकर 'Withdrawn' कर दिया जाता है।"),

    # 24
    ("What is an 'Inventory Discrepancy Report'?",
     "भंडार विसंगति रिपोर्ट (Inventory Discrepancy Report) क्या होती है?",
     "The formal audit document summarizing the results of stock verification, listing total books checked, found, missing, damaged, and misplaced",
     "भंडार सत्यापन के परिणामों को संक्षेप में प्रस्तुत करने वाला औपचारिक ऑडिट दस्तावेज, जिसमें कुल जांची गई, पाई गई, खोई और क्षतिग्रस्त पुस्तकें दर्ज होती हैं",
     ["A police complaint against late borrowers", "A list of new books requested by students", "A budget proposal for buying furniture"],
     ["विलंब करने वाले पाठकों पर पुलिस शिकायत", "छात्रों द्वारा मांगी गई नई पुस्तकों की सूची", "फर्नीचर खरीदने का बजट प्रस्ताव"],
     "The discrepancy report provides institutional leadership with objective statistics on collection health and operational shrinkage.",
     "यह रिपोर्ट प्रबंधन को बताती है कि कुल कितनी किताबें सही मिलीं, कितनी खोई हैं और नुकसान सरकारी सीमा के भीतर है या नहीं।"),

    # 25
    ("What is the primary benefit of conducting stock verification using a 'Continuous Stock Verification' approach?",
     "निरंतर भंडार सत्यापन (Continuous Stock Verification) पद्धति अपनाने का प्राथमिक लाभ क्या है?",
     "The library never needs to close to patrons, the workload is distributed smoothly across the whole year, and shelves stay constantly rectified",
     "पुस्तकालय को पाठकों हेतु कभी बंद नहीं करना पड़ता, कार्यभार पूरे वर्ष समान रूप से बंट जाता है और अलमारियां हमेशा व्यवस्थित रहती हैं",
     ["Staff receive double overtime pay every single day", "All missing books are magically returned by mail", "The government doubles the library budget automatically"],
     ["कर्मियों को प्रतिदिन दोगुना ओवरटाइम मिलता है", "खोई पुस्तकें डाक से स्वतः लौट आती हैं", "सरकार बजट स्वतः दोगुना कर देती है"],
     "Continuous verification checks a few bays every week, catching misplaced books early and avoiding exhausting year-end shutdown crises.",
     "निरंतर सत्यापन में कर्मचारी हर हफ्ते 2-3 अलमारियां जांचते हैं; इससे न तो पाठक परेशान होते हैं और न ही साल के अंत में काम का बोझ पड़ता है।"),

    # 26
    ("What is 'Shelf Rectification' performed concurrently during stock verification?",
     "भंडार सत्यापन के साथ-साथ की जाने वाली 'शेल्फ रेक्टिफिकेशन' (अलमारी सुधार) क्या है?",
     "Arranging all misplaced books back into their strict classified Call Number order on the shelves",
     "गलत जगह रखी गई सभी पुस्तकों को अलमारियों पर उनके सटीक वर्गीकृत कॉल नंबर क्रम में पुनः लगाना",
     ["Painting the metal shelves with anti-rust paint", "Tearing out old pages to lighten shelf weight", "Measuring the height of books with a ruler"],
     ["धातु की अलमारियों पर जंगरोधी पेंट लगाना", "वजन कम करने हेतु पुराने पन्ने फाड़ना", "पैमाने से पुस्तकों की ऊंचाई नापना"],
     "Checking books shelf by shelf provides the perfect opportunity to restore correct classified sequence so patrons can locate them.",
     "सत्यापन के दौरान ही गलत जगह दबी किताबों को उनके सही विषय क्रम में लगा दिया जाता है, जिससे पाठकों को किताबें आसानी से मिल जाती हैं।"),

    # 27
    ("Why is a 'Physical Census' or simple counting method inadequate as a standalone stock verification technique?",
     "केवल पुस्तकों की भौतिक गिनती करना (Simple Counting Method) एक स्वतंत्र भंडार सत्यापन तकनीक के रूप में अपर्याप्त क्यों है?",
     "It only counts the total number of physical volumes present, but fails completely to identify WHICH specific titles are missing or stolen",
     "यह केवल मौजूद कुल भौतिक खंडों की संख्या गिनता है, लेकिन यह बताने में पूरी तरह असमर्थ है कि कौन सी विशिष्ट पुस्तकें गायब या चोरी हुई हैं",
     ["Because counting takes twenty years to complete", "Because numbers are forbidden in library science", "Because counting destroys paper bindings"],
     ["क्योंकि गिनती पूरी होने में 20 साल लगते हैं", "क्योंकि पुस्तकालय विज्ञान में अंक वर्जित हैं", "क्योंकि गिनती से जिल्दें फट जाती हैं"],
     "Counting might confirm 50,000 items are on shelves, but cannot reveal whether Shakespeare's First Folio was replaced by a worthless duplicate.",
     "केवल सिर गिनने से यह तो पता चलेगा कि 10,000 किताबें रखी हैं, लेकिन यह कभी नहीं पता चलेगा कि कौन सी महत्वपूर्ण और महंगी किताब चोरी हो गई।"),

    # 28
    ("In university libraries, who typically chairs the institutional 'Library Weeding and Stock Verification Committee'?",
     "विश्वविद्यालय पुस्तकालयों में, 'पुस्तकालय छंटाई एवं भंडार सत्यापन समिति' की अध्यक्षता आमतौर पर कौन करता है?",
     "A Dean, Senior Academic Professor, or the University Librarian as nominated by the Vice-Chancellor",
     "कुलपति द्वारा नामित कोई संकायाध्यक्ष (Dean), वरिष्ठ प्राध्यापक अथवा विश्वविद्यालय पुस्तकालय अध्यक्ष",
     ["A first-year undergraduate student", "The city municipal corporation mayor", "The library building security supervisor"],
     ["प्रथम वर्ष का स्नातक छात्र", "नगर निगम का महापौर", "पुस्तकालय भवन का सुरक्षा सुपरवाइजर"],
     "Having senior faculty and library professionals on the committee ensures that academic rigor and teaching needs govern all de-selection decisions.",
     "समिति में वरिष्ठ प्रोफेसर और पुस्तकालयाध्यक्ष होते हैं ताकि यह सुनिश्चित हो सके कि कोई भी उपयोगी शैक्षणिक पुस्तक गलती से न छंट जाए।"),

    # 29
    ("What is an 'Accession Register Call-Back Method' in stock verification?",
     "भंडार सत्यापन में 'परिग्रहण पंजी कॉल-बैक विधि' क्या होती है?",
     "One assistant reads the accession numbers from the shelves while another locates and ticks each number in the master Accession Register",
     "एक सहायक अलमारी से परिग्रहण संख्या बोलता जाता है जबकि दूसरा मुख्य परिग्रहण पंजी में उस संख्या को खोजकर टिक करता जाता है",
     ["Calling patrons on the telephone to ask about books", "Shouting book titles across the reading room", "Whistling when a rare book is found"],
     ["पाठकों को फोन करके किताबों के बारे में पूछना", "वाचनालय में जोर से किताबों के नाम चिल्लाना", "दुर्लभ पुस्तक मिलने पर सीटी बजाना"],
     "This traditional two-person verbal call-back method is slow, noisy, error-prone, and subjects the historic register to excessive handling.",
     "यह दो लोगों की बोलकर मिलाने वाली पुरानी विधि है, जिसमें समय बहुत लगता है, शोर होता है और भारी रजिस्टर के पन्ने फटने का डर रहता है।"),

    # 30
    ("What is the role of a 'Separate Slip Method' during manual stock verification?",
     "मैनुअल भंडार सत्यापन के दौरान 'अलग पर्ची विधि' (Separate Slip Method) की क्या भूमिका होती है?",
     "A fresh paper slip is written for each book found on the shelf, and then all slips are sorted numerically to detect gaps in accession numbers",
     "अलमारी पर मिली प्रत्येक पुस्तक के लिए एक नई पर्ची लिखी जाती है, और फिर सभी पर्चियों को संख्या क्रम में सजाकर गायब नंबरों का पता लगाया जाता है",
     ["Slips are pasted permanently to student identity cards", "Slips are thrown out of windows to test wind speed", "Slips are burned to test paper flammability"],
     ["पर्चियों को छात्रों के आई-कार्ड पर चिपकाया जाता है", "हवा की गति जांचने हेतु खिड़की से फेंका जाता है", "कागज की ज्वलनशीलता जांचने हेतु जलाया जाता है"],
     "Writing hundreds of thousands of slips requires massive manual labor and stationery, making it largely obsolete today.",
     "इस विधि में हर किताब की अलग पर्ची बनाकर क्रम से मिलाया जाता है; इसमें कागज और श्रम बहुत बर्बाद होता है इसलिए यह अब अप्रचलित है।"),

    # 31
    ("Which of the following is considered an ethical, professional reason to WEED a book from a public library collection?",
     "सार्वजनिक पुस्तकालय संग्रह से किसी पुस्तक को छांटने (Weed) का निम्नलिखित में से कौन सा नैतिक और व्यावसायिक कारण है?",
     "The medical or legal advice in the book is dangerously outdated and scientifically refuted",
     "पुस्तक में दी गई चिकित्सीय या कानूनी सलाह खतरनाक रूप से पुरानी और वैज्ञानिक रूप से खारिज हो चुकी है",
     ["The librarian personally dislikes the author's political party", "The author has a strange-sounding foreign surname", "The cover color of the book clashes with the wall paint"],
     ["पुस्तकालयाध्यक्ष को लेखक की पार्टी पसंद नहीं है", "लेखक का कुलनाम विदेशी है", "पुस्तक के कवर का रंग दीवार से मेल नहीं खाता"],
     "Outdated health, medical, tax, and legal manuals can cause severe real-world harm to citizens if left on active open shelves.",
     "पुरानी चिकित्सा या कानून की किताबें पाठकों को जानलेवा गलत जानकारी दे सकती हैं, इसलिए उन्हें अलमारियों से हटाना आवश्यक कर्तव्य है।"),

    # 32
    ("Why should books censored or banned by local political interest groups NOT be weeded without due institutional process?",
     "स्थानीय राजनीतिक समूहों द्वारा प्रतिबंधित या विवादित पुस्तकों को बिना संस्थागत प्रक्रिया के क्यों नहीं छांटा जाना चाहिए?",
     "Because libraries defend intellectual freedom and the public's right to information against partisan censorship",
     "क्योंकि पुस्तकालय पक्षपातपूर्ण सेंसरशिप के विरुद्ध बौद्धिक स्वतंत्रता और जनता के सूचना के अधिकार की रक्षा करते हैं",
     ["Because politicians will buy all library copies", "Because banned books have higher gold content in their paper", "Because librarians are required to obey all political parties"],
     ["क्योंकि नेता सभी प्रतियां खरीद लेंगे", "क्योंकि प्रतिबंधित पुस्तकों में सोना होता है", "क्योंकि कर्मियों को सभी दलों की बात माननी होती है"],
     "ALA's Library Bill of Rights and IFLA guidelines mandate that libraries resist partisan pressure to purge controversial viewpoints.",
     "पुस्तकालयों का धर्म वैचारिक विविधता और बौद्धिक स्वतंत्रता की रक्षा करना है; केवल किसी के विरोध के आधार पर किताबें नहीं हटाई जातीं।"),

    # 33
    ("What does 'Shelf Capacity Threshold' mean in library space planning and weeding?",
     "पुस्तकालय स्थान नियोजन और छंटाई में 'शेल्फ क्षमता सीमा' (Shelf Capacity Threshold) का क्या अर्थ है?",
     "The principle that when bookshelves reach 75% to 80% physical capacity, constant crowding occurs, necessitating immediate weeding",
     "यह सिद्धांत कि जब अलमारियां अपनी क्षमता के 75% से 80% तक भर जाती हैं, तो भीड़भाड़ रोकने हेतु तत्काल छंटाई आवश्यक हो जाती है",
     ["The maximum number of books a student can hold in two hands", "The breaking point where wooden shelves snap in half", "The financial cost of buying an iron cupboard"],
     ["छात्र द्वारा दो हाथों में उठाई जा सकने वाली पुस्तकें", "लकड़ी की अलमारी के दो टुकड़े होने की सीमा", "लोहे की अलमारी खरीदने का वित्तीय खर्च"],
     "When shelves exceed 80% capacity, books must be stacked horizontally, damaging spines and frustrating patron browsing.",
     "जब अलमारी 80% भर जाती है, तो नई किताबें रखने की जगह नहीं बचती और पन्ने मुड़ने लगते हैं; इस स्थिति में छंटाई अपरिहार्य हो जाती है।"),

    # 34
    ("What is an 'Accession Register Reconciliation'?",
     "परिग्रहण पंजी समाधान (Accession Register Reconciliation) क्या होता है?",
     "The final auditing step where found books, issued books, binding items, and written-off volumes are balanced against the total register count",
     "अंतिम ऑडिट चरण जहाँ मौजूद, जारी, जिल्दसाजी में गई और बट्टे खाते डाली गई पुस्तकों का मिलान कुल परिग्रहण संख्या से किया जाता है",
     ["Erasing all numbers from the accession book", "Writing duplicate author names in red pencil", "Recalculating foreign currency conversion rates"],
     ["परिग्रहण पंजी से सभी नंबर मिटाना", "लाल पेंसिल से डुप्लीकेट लेखक लिखना", "विदेशी मुद्रा दरों की दोबारा गणना करना"],
     "Reconciliation ensures that every single accession number from 1 to N is completely accounted for in one of the legitimate operational states.",
     "समाधान (Reconciliation) यह सिद्ध करता है कि क्रमांक 1 से लेकर अंतिम क्रमांक तक की प्रत्येक पुस्तक का वैध हिसाब मौजूद है।"),

    # 35
    ("What is a 'Zero-Loss Library' reality in open-access modern library management?",
     "आधुनिक खुले प्रवेश वाले पुस्तकालय प्रबंधन में 'शून्य-हानि पुस्तकालय' (Zero-Loss Library) की वास्तविकता क्या है?",
     "It is an unrealistic, counter-productive myth; an open library with active usage inevitably suffers minor incidental losses",
     "यह एक अवास्तविक और नुकसानदेह मिथक है; सक्रिय उपयोग वाले खुले पुस्तकालय में थोड़ी-बहुत आकस्मिक हानि होना अनिवार्य है",
     ["A library that never buys any books", "A library where all books are chained with iron locks", "A library that opens only on February 29th"],
     ["वह पुस्तकालय जो कभी किताबें नहीं खरीदता", "जहां सभी किताबें लोहे के तालों से बंधी हों", "जो केवल 29 फरवरी को खुलता है"],
     "Expecting zero losses forces staff to operate closed, locked cages that destroy open access and alienate readers.",
     "शून्य नुकसान की जिद करने पर किताबों को तालों में बंद करना पड़ेगा, जिससे पाठकों का पुस्तकों से संपर्क कट जाएगा और पुस्तकालय मृत हो जाएगा।"),

    # 36
    ("What is 'Deselection' as a term compared to 'Weeding'?",
     "'वीडिंग' (Weeding) की तुलना में 'डिसिलेक्शन' (Deselection) शब्द क्या दर्शाता है?",
     "Deselection is the positive, systematic, policy-driven professional term emphasizing the thoughtful curation of collection quality",
     "डिसिलेक्शन सकारात्मक, व्यवस्थित और नीति-आधारित व्यावसायिक शब्द है जो संग्रह की गुणवत्ता को संवारने पर बल देता है",
     ["Deselection means destroying all computers in the building", "Deselection means firing all temporary library workers", "Deselection refers exclusively to burning magazines"],
     ["इमारत के सभी कंप्यूटरों को नष्ट करना", "सभी अस्थायी कर्मचारियों को नौकरी से निकालना", "केवल पत्रिकाओं को आग के हवाले करना"],
     "Librarians prefer 'deselection' or 'collection re-evaluation' over 'weeding' to emphasize active quality management rather than discarding trash.",
     "व्यावसायिक भाषा में 'वीडिंग' की जगह 'डिसिलेक्शन' कहा जाता है, ताकि यह स्पष्ट हो कि यह कचरा फेंकना नहीं बल्कि संग्रह को चुस्त-दुरुस्त बनाना है।"),

    # 37
    ("What does 'Relocation' mean as an alternative to outright discarding weeded books?",
     "छांटी गई पुस्तकों को पूरी तरह नष्ट करने के विकल्प के रूप में 'स्थानांतरण' (Relocation) का क्या अर्थ है?",
     "Transferring low-demand books from prime campus shelving to closed compact storage, remote repositories, or branch libraries",
     "कम मांग वाली पुस्तकों को मुख्य परिसर की खुली अलमारियों से हटाकर कॉम्पैक्ट स्टोरेज, दूरस्थ रिपोजिटरी या शाखा पुस्तकालय में भेजना",
     ["Moving bookshelves from the first floor to the roof", "Shipping books overseas for tourist display", "Hiding books behind window curtains"],
     ["अलमारियों को पहली मंजिल से छत पर ले जाना", "पर्यटकों हेतु किताबें विदेश भेजना", "खिड़की के पर्दों के पीछे किताबें छिपाना"],
     "Relocation frees prime reading room shelf space while ensuring research materials remain accessible upon advance request.",
     "स्थानांतरण में किताबों को फेंका नहीं जाता बल्कि मुख्य हॉल से हटाकर पिछले कमरों या शाखाओं में रख दिया जाता है ताकि जरूरत पड़ने पर मिल सकें।"),

    # 38
    ("In automated ILS systems, what status is assigned to an item when a shelf verification sweep fails to scan its barcode?",
     "स्वचालित सॉफ्टवेयर में जब भंडार सत्यापन के दौरान किसी पुस्तक का बारकोड स्कैन नहीं हो पाता, तो उसे क्या स्थिति (Status) दी जाती है?",
     "'Missing from Inventory' or 'Lost on Inventory' (भंडार से अनुपलब्ध / लापता)",
     "'Missing on Inventory' (भंडार से अनुपलब्ध)",
     ["'Permanently Stolen by Staff'", "'Discarded to Scrap'", "'Transferred to Foreign Country'"],
     ["'कर्मियों द्वारा चुराई गई'", "'कबाड़ में बेची गई'", "'विदेश स्थानांतरित'"],
     "The system updates the OPAC status so patrons know the item is unaccounted for, preventing futile searches in the stacks.",
     "सॉफ्टवेयर कैटलॉग में पुस्तक का स्टेटस 'Missing' दिखा देता है ताकि पाठक अलमारी में जाकर उसे व्यर्थ न ढूंढते रहें।"),

    # 39
    ("What is an 'Accession Number Range Audit'?",
     "परिग्रहण संख्या सीमा ऑडिट (Range Audit) क्या है?",
     "Verifying a specific contiguous block of accession numbers (e.g., Accessions 50,001 to 60,000) during phased stock verification",
     "चरणबद्ध भंडार सत्यापन के दौरान परिग्रहण संख्याओं के एक विशिष्ट ब्लॉक (जैसे क्रमांक 50,001 से 60,000) की जांच करना",
     ["Counting all books whose titles begin with the letter 'R'", "Measuring the physical thickness of reference books", "Auditing the salaries of librarians in grade R"],
     ["'R' अक्षर से शुरू होने वाली पुस्तकों को गिनना", "संदर्भ पुस्तकों की मोटाई नापना", "ग्रेड R के पुस्तकालयाध्यक्षों के वेतन की जांच"],
     "Block audits divide massive collections into manageable quarterly projects, preventing staff fatigue.",
     "लाखों पुस्तकों के संग्रह को 10-10 हजार के नंबर ब्लॉकों में बांटकर जांचने से नियमित काम में कोई रुकावट नहीं आती।"),

    # 40
    ("What is 'Stock Rectification' frequency recommended in high-traffic academic libraries?",
     "अत्यधिक आवाजाही वाले कॉलेज/विश्वविद्यालय पुस्तकालयों में 'शेल्फ सुधार' (Shelf Rectification) कितनी बार किया जाना चाहिए?",
     "Daily or continuous routine maintenance (दैनिक या निरंतर नियमित रखरखाव)",
     "दैनिक या निरंतर (Daily Routine Maintenance)",
     ["Once every 10 years", "Only when the Chief Minister visits", "Once a century"],
     ["10 वर्षों में एक बार", "केवल मुख्यमंत्री के आगमन पर", "शताब्दी में एक बार"],
     "Daily morning shelf reading restores books misplaced by patrons the previous afternoon, keeping the open stack reliable.",
     "दैनिक रूप से सुबह अलमारियों को ठीक किया जाना चाहिए क्योंकि छात्र अक्सर किताबें गलत जगह रख देते हैं जिससे वे दूसरों को नहीं मिलतीं।"),

    # 41
    ("What does 'Mutilation of Books' mean in library stock inspection?",
     "पुस्तकालय भंडार निरीक्षण में 'पुस्तकों का विद्रूपण' (Mutilation of Books) क्या कहलाता है?",
     "The malicious act of tearing out pages, cutting diagrams, removing color plates, or underlining with ink by unscrupulous users",
     "अवांछित पाठकों द्वारा पुस्तक के पन्ने फाड़ना, चित्र काटना, रंगीन नक्शे निकाल लेना या स्याही से पन्नों को गंदा करना",
     ["Binding books in genuine calf leather", "Stamping official property marks on secret pages", "Pasting barcodes on the back cover"],
     ["असली चमड़े में जिल्द बांधना", "गुप्त पृष्ठों पर आधिकारिक मुहर लगाना", "पिछले कवर पर बारकोड चिपकाना"],
     "Mutilation severely impairs intellectual content and requires either page restoration, replacement, or eventual de-selection.",
     "विद्रूपण वह आपराधिक कृत्य है जिसमें स्वार्थी छात्र किताब के पन्ने या नक्शे फाड़ लेते हैं; ऐसी पुस्तकों की पहचान कर उन्हें ठीक किया जाता है।"),

    # 42
    ("Why should stock verification records be preserved permanently along with institutional audit papers?",
     "भंडार सत्यापन अभिलेखों को संस्थागत ऑडिट पत्रों के साथ स्थायी रूप से क्यों सुरक्षित रखा जाना चाहिए?",
     "Because they provide legal audit compliance, satisfy statutory government audits (CAG), and prove fiscal accountability of public assets",
     "क्योंकि वे वैधानिक सरकारी ऑडिट (CAG) की अनुपालना करते हैं और सार्वजनिक संपत्तियों की वित्तीय जवाबदेही सिद्ध करते हैं",
     ["To sell old audit papers to antique collectors", "To wrap parcels during interlibrary loans", "To serve as drawing paper for school competitions"],
     ["प्राचीन वस्तु संग्रहकर्ताओं को पुराने कागज बेचना", "पार्सल बांधने के लिए कागज का उपयोग करना", "चित्रकला प्रतियोगिताओं हेतु ड्राइंग पेपर बनाना"],
     "Statutory auditors and the Comptroller and Auditor General (CAG) examine stock verification discrepancy reports to verify asset integrity.",
     "भारत के नियंत्रक एवं महालेखापरीक्षक (CAG) और सरकारी ऑडिटर यह जांचते हैं कि सरकारी पैसे से खरीदी गई संपत्तियों का सही सत्यापन हुआ है या नहीं।"),

    # 43
    ("What is an 'Annual Report' contribution from the Stock Verification team?",
     "भंडार सत्यापन दल द्वारा पुस्तकालय की 'वार्षिक रिपोर्ट' (Annual Report) में क्या योगदान दिया जाता है?",
     "A certified statistical summary detailing total volumes verified, newly accessioned, worn-out/weeded, and net losses written off",
     "सत्यापित कुल पुस्तकों, नई जोड़ी गई पुस्तकों, छंटाई की गई पुस्तकों और बट्टे खाते डाले गए नुकसान का प्रमाणित सांख्यिकीय विवरण",
     ["A list of funny jokes told by library visitors", "Photographs of cafeteria menu cards", "The weather report of rainy days"],
     ["पाठकों द्वारा सुनाए गए चुटकुलों की सूची", "कैफेटेरिया मेनू कार्ड की तस्वीरें", "बरसात के दिनों की मौसम रिपोर्ट"],
     "The annual report provides institutional authorities and funding agencies with transparent metrics on collection size and maintenance.",
     "वार्षिक रिपोर्ट में यह प्रमाणित आंकड़ा जाता है कि वर्ष के अंत में पुस्तकालय में कुल कितनी वैध पुस्तकें जीवित और उपयोगी अवस्था में हैं।"),

    # 44
    ("What is a 'Sample Audit' in large research libraries exceeding 100,000 volumes?",
     "1 लाख से अधिक पुस्तकों वाले बड़े शोध पुस्तकालयों में 'नमूना ऑडिट' (Sample Audit) क्या होता है?",
     "Statistically inspecting a randomly selected representative percentage (e.g., 10%) of the collection across various subjects",
     "विभिन्न विषयों में संग्रह के सांख्यिकीय रूप से यादृच्छिक रूप से चुने गए प्रतिनिधि प्रतिशत (जैसे 10%) की गहन जांच करना",
     ["Checking only the front covers of all books", "Auditing books whose price is under ten rupees", "Inspecting only the magazines in the staff lounge"],
     ["सभी पुस्तकों के केवल सामने के कवर जांचना", "दस रुपये से कम मूल्य वाली पुस्तकें जांचना", "केवल स्टाफ लाउंज की पत्रिकाएं जांचना"],
     "If the loss rate in the 10% sample is comfortably below the permissible threshold, the entire collection is legitimately certified.",
     "यदि 10% रैंडम सैंपल में नुकसान सरकार की तय सीमा (0.5%) के भीतर आता है, तो पूरे संग्रह को सही मानकर ऑडिट पास कर दिया जाता है।"),

    # 45
    ("What happens if a sample audit of library books reveals abnormally high losses exceeding permissible government limits?",
     "यदि पुस्तकालय पुस्तकों के नमूना ऑडिट में स्वीकार्य सरकारी सीमा से असामान्य रूप से अधिक नुकसान का पता चलता है, तो क्या कदम उठाया जाता है?",
     "A full 100% census physical verification is mandated, and a formal inquiry is launched to detect systemic theft or fraud",
     "पूरे 100% संग्रह का पूर्ण भौतिक सत्यापन अनिवार्य किया जाता है, और संगठित चोरी या धोखाधड़ी की जांच हेतु औपचारिक जांच समिति बैठती है",
     ["The library is immediately bulldozed", "All books are given away free to street pedestrians", "The entire student body is expelled without inquiry"],
     ["पुस्तकालय को तुरंत ध्वस्त कर दिया जाता है", "सभी पुस्तकें राहगीरों में मुफ्त बांट दी जाती हैं", "बिना जांच पूरे छात्र समुदाय को निकाल दिया जाता है"],
     "Excessive unexplained shrinkage indicates security failure, requiring total inventory reconciliation and administrative investigation.",
     "यदि सैंपल में बहुत भारी चोरी पकड़ में आए, तो पूरी एक-एक किताब की जांच का आदेश दिया जाता है और सुरक्षा खामियों की उच्चस्तरीय जांच होती है।"),

    # 46
    ("What is 'Continuous Weeding' as part of daily library operations?",
     "दैनिक पुस्तकालय कार्यों के हिस्से के रूप में 'निरंतर छंटाई' (Continuous Weeding) क्या है?",
     "Staff identify and set aside worn-out, torn, superseded, or moldy volumes during daily shelving, circulation check-in, and shelf reading",
     "दैनिक पुस्तक लेन-देन, वापसी और अलमारियों की सफाई के दौरान ही फटी, पुरानी, फफूंद लगी या अनुपयोगी किताबों को पहचान कर अलग करना",
     ["Throwing five books into the trash every morning blindly", "Burning one bookshelf at the end of every week", "Selling books whenever staff need extra pocket money"],
     ["रोज सुबह आंखें बंद करके 5 किताबें फेंकना", "हर हफ्ते के अंत में एक अलमारी जलाना", "पॉकेट मनी की जरूरत होने पर किताबें बेचना"],
     "Integrating continuous weeding into daily workflows prevents massive backlogs and keeps open shelves aesthetically pleasing and current.",
     "दैनिक काम के साथ-साथ खराब किताबों को किनारे करते रहने से अलमारियों पर कभी कबाड़ इकट्ठा नहीं होता और संग्रह हमेशा आकर्षक रहता है।"),

    # 47
    ("Which section of the library generally coordinates the operational execution of stock verification across the building?",
     "पुस्तकालय का कौन सा अनुभाग आमतौर पर पूरे भवन में भंडार सत्यापन के परिचालन समन्वय का नेतृत्व करता है?",
     "Maintenance / Stack Section in coordination with Technical and Circulation sections",
     "रखरखाव / स्टैक अनुभाग, जो तकनीकी और परिसंचरण अनुभागों के साथ मिलकर काम करता है",
     ["Photocopy Counter Section", "Security Guard Gatehouse", "Gardening and Horticulture Wing"],
     ["फोटोकॉपी काउंटर अनुभाग", "सुरक्षा गार्ड गेटहाउस", "बागवानी अनुभाग"],
     "The maintenance section oversees stack arrangements, shelf lists, and physical racks, acting as the operational lead for inventory checks.",
     "स्टैक और मेंटेनेंस अनुभाग अलमारियों और शेल्फ लिस्ट का प्रभारी होता है, इसलिए वही सत्यापन के कार्य की मुख्य धुरी बनता है।"),

    # 48
    ("In summary, the ultimate professional goal of regular stock verification and weeding is to:",
     "संक्षेप में, नियमित भंडार सत्यापन और छंटाई का अंतिम व्यावसायिक लक्ष्य क्या है?",
     "Maintain an accurate, reliable, relevant, and vibrant collection that maximizes user satisfaction and saves reader time",
     "एक सटीक, विश्वसनीय, प्रासंगिक और जीवंत संग्रह बनाए रखना जो पाठकों की संतुष्टि बढ़ाए और उनका समय बचाए",
     ["Accumulate the largest possible mass of dusty paper on earth", "Trap students with massive overdue fines", "Keep all library books hidden away from human sight"],
     ["धरती पर धूल भरे कागजों का सबसे बड़ा ढेर लगाना", "छात्रों को भारी जुर्माने के जाल में फंसाना", "सभी पुस्तकों को मानवीय दृष्टि से छिपा कर रखना"],
     "Stock verification and weeding ensure the catalogue truthfully reflects physical reality, fulfilling Ranganathan's Laws of Library Science.",
     "इन प्रक्रियाओं से कैटलॉग और अलमारी का सच एक हो जाता है, जिससे पाठक जो किताब खोजता है वह उसे तुरंत सही जगह पर मिल जाती है।")
]

print("Q49 loaded, count:", len(q49_pool))
