# -*- coding: utf-8 -*-
"""
Bihar Librarian LET Mock Test Series - Question Pool: Unit 3, Q47 (48 Items)
Focus: Serials & Periodicals Management (Kardex System, Ranganathan's Three-Card System,
Subscription Modes, Renewal Cycles, Claims, Missing Issues, Binding, TPI).
"""

q47_pool = [
    # 1
    ("Which commercial visible filing system manufactured by Remington Rand is widely used in libraries for recording serials?",
     "रेमिंगटन रैंड (Remington Rand) द्वारा निर्मित कौन सी दृश्य फाइलिंग प्रणाली पत्रिकाओं के रिकॉर्ड रखने हेतु पुस्तकालयों में व्यापक रूप से प्रयुक्त होती है?",
     "Kardex System (कारडेक्स प्रणाली)", "कारडेक्स प्रणाली (Kardex Visible Record System)",
     ["Three-Card System", "Browne System", "Newark System"],
     ["तीन-कार्ड प्रणाली", "ब्राउन प्रणाली", "नेवार्क प्रणाली"],
     "The Kardex system uses shallow sliding steel trays with overlapping visible title pockets to register serial arrivals.",
     "कारडेक्स स्टील की उथली दराजों वाली प्रणाली है, जिसमें पत्रिकाओं के शीर्षक सामने दिखते हैं और कार्डों को आसानी से देखा जा सकता है।"),

    # 2
    ("Who introduced the innovative 'Three-Card System' for periodicals management in India?",
     "भारत में पत्रिकाओं (सामयिकियों) के प्रबंधन हेतु अभिनव 'तीन-कार्ड प्रणाली' (Three-Card System) का आविष्कार किसने किया था?",
     "S. R. Ranganathan (एस. आर. रंगनाथन)", "एस. आर. रंगनाथन (S. R. Ranganathan)",
     ["B. S. Kesavan", "P. N. Kaula", "K. M. Asadullah"],
     ["बी. एस. केशवन", "पी. एन. कौला", "के. एम. असदुल्लाह"],
     "S. R. Ranganathan designed the Three-Card System (Register Card, Check Card, and Classified Index Card) in 1930 at Madras University.",
     "एस. आर. रंगनाथन ने 1930 में मद्रास विश्वविद्यालय में पत्रिकाओं के पंजीकरण और नियंत्रण हेतु तीन-कार्ड प्रणाली बनाई।"),

    # 3
    ("What are the three cards used in S.R. Ranganathan's Three-Card System for serials control?",
     "एस. आर. रंगनाथन की तीन-कार्ड प्रणाली में प्रयुक्त होने वाले तीन कार्ड कौन से हैं?",
     "Register Card, Check Card, and Classified Index Card (पंजीकरण कार्ड, जांच कार्ड और वर्गीकृत अनुक्रमणिका कार्ड)",
     "पंजीकरण कार्ड, जांच कार्ड और वर्गीकृत अनुक्रमणिका कार्ड (Register, Check & Classified Index Card)",
     ["Book Card, Reader Ticket, Date Card", "Main Card, Added Card, Cross Card", "Author Card, Title Card, Subject Card"],
     ["बुक कार्ड, पाठक टिकट, दिनांक कार्ड", "मुख्य कार्ड, सहायक कार्ड, क्रॉस कार्ड", "लेखक कार्ड, शीर्षक कार्ड, विषय कार्ड"],
     "The three cards perform specific roles: Register Card (receipt of issues), Check Card (monitoring gaps/delays), and Classified Index Card (payment/binding data).",
     "तीन कार्ड हैं: 1. रजिस्टर कार्ड (अंकों की प्राप्ति), 2. चेक कार्ड (अंकों की देरी पर नजर रखना), और 3. क्लासिफाइड इंडेक्स कार्ड (भुगतान और जिल्दसाजी का रिकॉर्ड)।"),

    # 4
    ("What is the standard physical size of the cards used in Ranganathan's Three-Card System?",
     "रंगनाथन की तीन-कार्ड प्रणाली में उपयोग किए जाने वाले कार्डों का मानक भौतिक आकार क्या होता है?",
     "5 inches x 3 inches (12.5 cm x 7.5 cm)", "5 x 3 इंच (12.5 सेमी x 7.5 सेमी)",
     ["8 inches x 5 inches", "6 inches x 4 inches", "10 inches x 8 inches"],
     ["8 x 5 इंच", "6 x 4 इंच", "10 x 8 इंच"],
     "The three cards use the internationally standardized 5x3 inch (12.5 x 7.5 cm) catalog card format.",
     "रंगनाथन के तीनों कार्ड मानक सूची कार्ड आकार (5 x 3 इंच या 12.5 x 7.5 सेमी) के होते हैं।"),

    # 5
    ("In Ranganathan's Three-Card System, which card is filed according to the expected due week of the arrival of the next journal issue?",
     "रंगनाथन की तीन-कार्ड प्रणाली में, अगले अंक के आने के संभावित सप्ताह के अनुसार किस कार्ड को व्यवस्थित किया जाता है?",
     "Check Card (जांच कार्ड / चेक कार्ड)", "जांच कार्ड (Check Card)",
     ["Register Card", "Classified Index Card", "Accession Card"],
     ["पंजीकरण कार्ड", "वर्गीकृत अनुक्रमणिका कार्ड", "परिग्रहण कार्ड"],
     "Check Cards are filed behind weekly guide cards (1 to 52); if an issue fails to arrive in its scheduled week, a claim is triggered immediately.",
     "चेक कार्ड को वर्ष के 52 सप्ताहों के गाइड कार्डों के पीछे रखा जाता है; यदि तय सप्ताह में अंक नहीं आता तो तुरंत क्लेम भेजा जाता है।"),

    # 6
    ("In Ranganathan's Three-Card System, how are 'Register Cards' arranged in their tray?",
     "रंगनाथन की तीन-कार्ड प्रणाली में, 'पंजीकरण कार्ड' (Register Cards) ट्रे में किस क्रम में रखे जाते हैं?",
     "Alphabetically by title of the periodical (पत्रिका के शीर्षक के वर्णमाला क्रम में)",
     "पत्रिका के शीर्षक के वर्णमाला क्रम में (Alphabetically by Periodical Title)",
     ["Chronologically by date of receipt", "By subscription price from highest to lowest", "By the country of publication"],
     ["प्राप्ति तिथि के कालानुक्रम में", "सदस्यता मूल्य के घटते क्रम में", "प्रकाशन देश के अनुसार"],
     "Register cards are arranged alphabetically by title, enabling immediate location upon receiving the daily mail.",
     "रजिस्टर कार्ड शीर्षक के वर्णमाला क्रम में सजे होते हैं ताकि डाक आते ही संबंधित पत्रिका का कार्ड तुरंत निकाला जा सके।"),

    # 7
    ("In Ranganathan's Three-Card System, how are 'Classified Index Cards' arranged?",
     "रंगनाथन की तीन-कार्ड प्रणाली में, 'वर्गीकृत अनुक्रमणिका कार्ड' (Classified Index Cards) किस क्रम में व्यवस्थित होते हैं?",
     "Classified order by Class Number (वर्गांक के वर्गीकृत क्रम में)",
     "वर्गांक के वर्गीकृत क्रम में (Classified Order by Class Number)",
     ["Alphabetically by publisher's name", "Alphabetically by vendor's name", "In order of annual subscription invoice number"],
     ["प्रकाशक के नाम के वर्णमाला क्रम में", "विक्रेता के नाम के वर्णमाला क्रम में", "वार्षिक बिल संख्या के क्रम में"],
     "Classified Index Cards are filed by Class Number, giving a subject-wise overview of all serials subscribed by the library.",
     "क्लासिफाइड इंडेक्स कार्ड विषय वर्गांक क्रम में रखे जाते हैं, जिससे पता चलता है कि किसी विशेष विषय में कौन-कौन सी पत्रिकाएं आ रही हैं।"),

    # 8
    ("In a Kardex visible recording unit, how many cards are typically paired together in each transparent pocket?",
     "कारडेक्स दृश्य रिकॉर्डिंग इकाई में, प्रत्येक पारदर्शी पॉकेट में आमतौर पर कितने कार्डों का जोड़ा लगाया जाता है?",
     "Two cards: Top card (payment and subscription history) and Bottom card (monthly/weekly recording grid)",
     "दो कार्ड: ऊपरी कार्ड (भुगतान और सदस्यता विवरण) तथा निचला कार्ड (दैनिक/मासिक प्राप्ति ग्रिड)",
     ["Single card only", "Four cards", "Five cards"],
     ["केवल एक कार्ड", "चार कार्ड", "पांच कार्ड"],
     "Kardex uses a pair of cards per title: the top card for annual payment and vendor records, and the bottom card for tracking individual issues.",
     "कारडेक्स में प्रति पत्रिका दो कार्ड होते हैं: ऊपरी कार्ड पर बिल और भुगतान का ब्यौरा होता है और निचले कार्ड पर अंकों की प्राप्ति दर्ज की जाती है।"),

    # 9
    ("What is the primary indicator strip displayed on the visible lower edge of each pocket in a Kardex tray?",
     "कारडेक्स ट्रे में प्रत्येक पॉकेट के निचले दृश्यमान किनारे पर कौन सी प्राथमिक संकेतक पट्टी दिखाई देती है?",
     "Colored sliding signal tabs (रंगीन स्लाइडिंग सिग्नल टैब)",
     "रंगीन स्लाइडिंग सिग्नल टैब (Colored Sliding Signal Tabs)",
     ["Metal barcode tags", "Magnetic security strips", "Holographic stamps"],
     ["धातु के बारकोड टैग", "चुंबकीय सुरक्षा पट्टियां", "होलोग्राफिक टिकट"],
     "Sliding colored signals on the visible bottom edge indicate subscription status, missing issues, or renewal reminders at a glance.",
     "किनारे पर लगी रंगीन पट्टियां एक नजर में दिखा देती हैं कि कौन सा अंक नहीं आया या किस पत्रिका का नवीनीकरण निकट है।"),

    # 10
    ("In journal subscription management, what is an 'Advance Payment'?",
     "पत्रिका सदस्यता प्रबंधन में 'अग्रिम भुगतान' (Advance Payment) क्या होता है?",
     "The universal practice where libraries must pay the entire annual subscription cost to publishers in advance before issues are mailed",
     "वह सार्वभौमिक प्रथा जिसमें पुस्तकालयों को पत्रिका अंक भेजे जाने से पहले ही पूरे वर्ष का सदस्यता शुल्क अग्रिम देना होता है",
     ["Paying after reading all issues for five years", "Paying in cash installments every Monday", "A loan given by the publisher to the library"],
     ["पांच साल तक सभी अंक पढ़ने के बाद भुगतान करना", "प्रत्येक सोमवार को नकद किश्तों में भुगतान करना", "प्रकाशक द्वारा पुस्तकालय को दिया गया ऋण"],
     "Unlike books, journal subscriptions globally require mandatory 100% advance payment prior to volume commencement.",
     "पुस्तकों के विपरीत, दुनिया भर में पत्रिकाओं की सदस्यता के लिए पूरे साल का पैसा प्रकाशक को 100% अग्रिम देना अनिवार्य होता है।"),

    # 11
    ("Why do libraries often employ 'Subscription Agents' (or Periodical Vendors) rather than ordering journals directly from individual publishers?",
     "पुस्तकालय अलग-अलग प्रकाशकों से सीधे पत्रिकाएं मंगाने के बजाय 'सदस्यता एजेंटों' (Subscription Agents) की सेवाएं क्यों लेते हैं?",
     "To consolidate hundreds of subscriptions, foreign currency invoices, and claims into a single consolidated local vendor relationship",
     "सैकड़ों पत्रिकाओं के आर्डरों, विदेशी मुद्रा बिलों और दावों को एक ही स्थानीय एजेंसी के माध्यम से सुगम बनाने हेतु",
     ["Because agents print all foreign journals locally at home", "Because publishers refuse to talk to universities", "Because subscription agents provide free paper binding"],
     ["क्योंकि एजेंट सभी विदेशी पत्रिकाएं घर पर ही छापते हैं", "क्योंकि प्रकाशक विश्वविद्यालयों से बात करने से मना करते हैं", "क्योंकि सदस्यता एजेंट मुफ्त जिल्दसाजी प्रदान करते हैं"],
     "Subscription agencies (like EBSCO, Informatics) handle foreign remittances, bundling, and missing issue follow-ups for a single handling fee.",
     "एजेंट एक ही बिल में दर्जनों देशों के प्रकाशकों से पत्रिकाएं मंगा देते हैं, जिससे पुस्तकालय को अलग-अलग विदेशी ड्राफ्ट नहीं बनाने पड़ते।"),

    # 12
    ("What is an 'Invoice of Serials' accompanied by under GOC guidelines in Indian libraries?",
     "भारतीय पुस्तकालयों में GOC दिशानिर्देशों के तहत पत्रिकाओं के बिल के साथ क्या संलग्न होना अनिवार्य है?",
     "Publisher's original price proof / catalog rate sheet and prevailing bank conversion rates",
     "प्रकाशक का मूल मूल्य प्रमाण (Price Proof) और तत्कालीन बैंक विदेशी मुद्रा विनिमय दर",
     ["Author's handwritten signature", "Customs clearance certificate for airplanes", "Tax exemption certificate for timber"],
     ["लेखक का हस्तलिखित हस्ताक्षर", "हवाई जहाजों के लिए सीमा शुल्क निकासी प्रमाण पत्र", "इमारती लकड़ी हेतु कर छूट प्रमाण पत्र"],
     "GOC requires vendors to attach original publisher price proofs and verified bank conversion exchange rates for all foreign journal invoices.",
     "विदेशी पत्रिकाओं के बिल के साथ प्रकाशक का प्रामाणिक मूल्य प्रमाण पत्र और बैंक विनिमय दर लगाना अनिवार्य होता है।"),

    # 13
    ("When does a standard academic journal subscription cycle typically run?",
     "एक मानक अकादमिक पत्रिका का सदस्यता चक्र आमतौर पर कब से कब तक चलता है?",
     "Calendar Year: January to December (कैलेंडर वर्ष: जनवरी से दिसंबर)",
     "कैलेंडर वर्ष: जनवरी से दिसंबर (Calendar Year: January to December)",
     ["Financial Year: April to March only", "Academic Year: July to June only", "Diwali to Diwali"],
     ["केवल वित्तीय वर्ष: अप्रैल से मार्च", "केवल शैक्षणिक वर्ष: जुलाई से जून", "दीपावली से दीपावली"],
     "Most international scholarly journals publish volumes aligned with the calendar year (January-December).",
     "अधिकांश अंतरराष्ट्रीय शोध पत्रिकाएं अपने खंड (Volume) कैलेंडर वर्ष (जनवरी से दिसंबर) के अनुसार प्रकाशित करती हैं।"),

    # 14
    ("What is a 'Missing Issue' in serials management?",
     "सामयिकी प्रबंधन में 'अप्र्राप्त अंक' (Missing Issue) क्या होता है?",
     "A published issue of a subscribed periodical that was never delivered to the library due to postal failure or vendor oversight",
     "सदस्यित पत्रिका का वह प्रकाशित अंक जो डाक की खराबी या विक्रेता की भूल के कारण पुस्तकालय में कभी नहीं पहुंचा",
     ["An issue discarded intentionally by the librarian", "An issue that contains only blank pages", "A special issue printed in Braille"],
     ["पुस्तकालयाध्यक्ष द्वारा जानबूझकर फेंका गया अंक", "ऐसा अंक जिसमें केवल कोरे पन्ने हों", "ब्रेल लिपि में छपा विशेष अंक"],
     "Missing issues break continuous sets, severely devaluing the annual volume unless promptly claimed and recovered.",
     "अप्र्राप्त अंक पत्रिका के पूरे खंड को अधूरा बना देता है, इसलिए समय रहते प्रकाशक से इसका दावा करना अत्यंत आवश्यक होता है।"),

    # 15
    ("Within what typical timeframe should a missing journal issue be claimed from an overseas publisher?",
     "विदेशी प्रकाशक से अप्र्राप्त पत्रिका अंक का दावा (Claim) आमतौर पर कितने समय के भीतर किया जाना चाहिए?",
     "Within 60 to 90 days of publication or dispatch (प्रकाशन या प्रेषण के 60 से 90 दिनों के भीतर)",
     "60 से 90 दिनों के भीतर (Within 60 to 90 days)",
     ["Within 5 years", "After 24 hours of printing", "Only at the end of the 10-year subscription"],
     ["5 वर्षों के भीतर", "छपने के 24 घंटे बाद", "10 वर्ष की सदस्यता समाप्त होने पर"],
     "Publishers maintain limited safety overstocks; claims submitted past 60-90 days are universally rejected as 'out of print'.",
     "प्रकाशक अतिरिक्त प्रतियां केवल कुछ महीनों तक रखते हैं; 90 दिन बीत जाने के बाद दावा करने पर अंक अप्राप्य घोषित हो जाता है।"),

    # 16
    ("What is a 'Bound Volume' of a periodical?",
     "पत्रिका का 'जिल्द बंधा खंड' (Bound Volume / बैक वॉल्यूम) क्या होता है?",
     "All individual loose issues of a complete volume (usually one year) bound together with the TPI into a single hardback book",
     "एक पूरे खंड (आमतौर पर एक वर्ष) के सभी खुले अंकों को TPI के साथ एक मजबूत जिल्द में बांधकर तैयार की गई पुस्तक",
     ["A stack of loose issues tied with a plastic rope", "A bundle of discarded journals sold to a recycler", "A collection of book reviews published online"],
     ["प्लास्टिक की रस्सी से बंधे खुले पन्नों का ढेर", "रद्दी वाले को बेची गई पुरानी पत्रिकाओं का बंडल", "ऑनलाइन प्रकाशित पुस्तक समीक्षाओं का संग्रह"],
     "Bound volumes convert fragile loose periodicals into permanent, sturdy reference books assigned an accession number.",
     "वर्ष के सभी अंकों को शीर्षक पृष्ठ और अनुक्रमणिका (TPI) के साथ पक्की जिल्द में बांधकर स्थायी संदर्भ पुस्तक बना दिया जाता है।"),

    # 17
    ("When are individual loose journal issues assigned a permanent Accession Number?",
     "खुली पत्रिकाओं के अलग-अलग अंकों को स्थायी परिग्रहण संख्या (Accession Number) कब दी जाती है?",
     "Only AFTER they are assembled and bound together into a complete Bound Volume",
     "केवल तभी जब वे एक पूर्ण खंड के रूप में संकलित होकर जिल्द (Bound Volume) में बंध जाते हैं",
     ["Immediately upon receiving the daily mail", "Before paying the subscription invoice", "Never under any circumstances"],
     ["दैनिक डाक में प्राप्त होते ही", "सदस्यता बिल का भुगतान करने से पहले", "किसी भी परिस्थिति में कभी नहीं"],
     "Individual daily/monthly issues are tracked on Kardex or check-in grids; only the completed, bound volume is formally accessioned.",
     "दैनिक या मासिक अंकों को रजिस्टर या कारडेक्स में दर्ज किया जाता है; परिग्रहण संख्या केवल जिल्द बंधे पूरे खंड को दी जाती है।"),

    # 18
    ("In periodical binding, what does 'Collating a Volume' before sending it to the binder mean?",
     "जिल्दसाज के पास भेजने से पहले पत्रिका खंड के 'कोलेशन' (Collating a Volume) का क्या अर्थ है?",
     "Verifying that all numbered issues, supplements, and the TPI are present in correct sequential order without missing pages",
     "यह जांचना कि सभी क्रमांकित अंक, सप्लीमेंट और TPI बिना किसी फटे पन्ने के सही क्रमिक क्रम में मौजूद हैं",
     ["Painting the edges of paper with gold ink", "Pasting barcode stickers on every page", "Counting the number of advertisements"],
     ["कागज के किनारों को सुनहरी स्याही से रंगना", "प्रत्येक पृष्ठ पर बारकोड स्टिकर चिपकाना", "विज्ञापनों की संख्या गिनना"],
     "Collation prevents binding defective, incomplete volumes that would be costly to dismantle later.",
     "जिल्दसाजी से पहले यह सुनिश्चित किया जाता है कि साल का कोई अंक या पन्ना गायब तो नहीं है, अन्यथा अधूरी जिल्द बंध जाएगी।"),

    # 19
    ("What is a 'Ceased Publication' in serials control?",
     "सामयिकी नियंत्रण में 'प्रकाशन बंद' (Ceased Publication) से क्या तात्पर्य है?",
     "A periodical that has permanently stopped publishing future issues",
     "वह पत्रिका जिसने भविष्य में अपने नए अंकों का प्रकाशन स्थायी रूप से समाप्त कर दिया है",
     ["A journal that has moved to a larger office", "A magazine with a change of editor", "A periodical printed on handmade paper"],
     ["वह पत्रिका जो बड़े कार्यालय में स्थानांतरित हो गई है", "संपादक बदलने वाली पत्रिका", "हाथ से बने कागज पर छपने वाली पत्रिका"],
     "When a serial ceases publication, its catalog record is closed with the final volume/year, and subscription renewals are terminated.",
     "जब कोई पत्रिका हमेशा के लिए बंद हो जाती है, तो उसके रिकॉर्ड को 'सीज्ड' घोषित कर दिया जाता है और आगे का बजट रोक दिया जाता है।"),

    # 20
    ("What is 'Title Change' or 'Successive Title Entry' in serials cataloguing?",
     "पत्रिका सूचीकरण में 'शीर्षक परिवर्तन' (Title Change) से क्या तात्पर्य है?",
     "When a journal changes its name (e.g., from 'Journal of Library Science' to 'International Journal of Information Science'), requiring a separate bibliographic record under modern cataloguing rules",
     "जब कोई पत्रिका अपना नाम बदल लेती है, जिसके लिए आधुनिक सूचीकरण नियमों के तहत एक नया अलग कैटलॉग रिकॉर्ड बनाना पड़ता है",
     ["Changing the font size of the cover title", "A student misreading the book title", "A typographical error by the printer"],
     ["कवर शीर्षक का फॉन्ट आकार बदलना", "छात्र द्वारा शीर्षक गलत पढ़ना", "प्रिंटर द्वारा मुद्रण की गलती"],
     "Under successive entry cataloging (AACR-2 and RDA), each major title change generates a new bibliographic record linked by reciprocal notes.",
     "जब पत्रिका का नाम बदलता है, तो पुराने नाम और नए नाम के लिए अलग-अलग रिकॉर्ड बनाकर उन्हें आपस में जोड़ दिया जाता है।"),

    # 21
    ("What does 'Open Access Journal' mean?",
     "खुली पहुंच वाली पत्रिका (Open Access Journal) का क्या अर्थ है?",
     "A peer-reviewed scholarly journal whose articles are freely available online to anyone without subscription fees or paywalls",
     "सहकर्मी-समीक्षित शोध पत्रिका जिसके लेख बिना किसी सदस्यता शुल्क या बाधा के ऑनलाइन सभी के लिए निःशुल्क उपलब्ध होते हैं",
     ["A magazine sold without a paper cover", "A journal that accepts articles without peer review", "A journal available only on public holidays"],
     ["बिना कागजी कवर के बिकने वाली पत्रिका", "ऐसी पत्रिका जो बिना समीक्षा के लेख छाप देती है", "केवल सार्वजनिक छुट्टियों पर उपलब्ध पत्रिका"],
     "Open access journals remove price barriers for readers, typically funded through institutional support or Author Processing Charges (APCs).",
     "ओपन एक्सेस जर्नल्स के शोध पत्र इंटरनेट पर कोई भी मुफ्त में पढ़ और डाउनलोड कर सकता है, इसके लिए कोई सब्सक्रिप्शन नहीं देना पड़ता।"),

    # 22
    ("What is the 'Directory of Open Access Journals' (DOAJ)?",
     "डायरेक्टरी ऑफ ओपन एक्सेस जर्नल्स (DOAJ) क्या है?",
     "A comprehensive, curated online directory that indexes high-quality, peer-reviewed open access journals globally",
     "एक प्रतिष्ठित ऑनलाइन निर्देशिका जो दुनिया भर की उच्च-गुणवत्ता वाली खुली पहुंच (Open Access) पत्रिकाओं को अनुक्रमित करती है",
     ["A commercial bookstore selling open textbooks", "A software for locking digital files", "A government register of copyrighted patents"],
     ["खुली पाठ्यपुस्तकें बेचने वाली व्यावसायिक दुकान", "डिजिटल फाइलों को लॉक करने का सॉफ्टवेयर", "कॉपीराइट पेटेंट का सरकारी रजिस्टर"],
     "Launched by Lund University in 2003, DOAJ indexes over 20,000 peer-reviewed open access journals across all disciplines.",
     "DOAJ लुंड विश्वविद्यालय द्वारा 2003 में शुरू की गई वह प्रामाणिक वैश्विक निर्देशिका है जो वैध ओपन एक्सेस पत्रिकाओं की सूची देती है।"),

    # 23
    ("What is an 'Article Processing Charge' (APC) in open access publishing?",
     "ओपन एक्सेस प्रकाशन में 'आर्टिकल प्रोसेसिंग चार्ज' (APC) क्या होता है?",
     "A publication fee paid by an author, their institution, or research funder to make an accepted article freely available to the public",
     "शोध लेख स्वीकृत होने पर लेखक या उसके संस्थान द्वारा दिया जाने वाला प्रकाशन शुल्क ताकि लेख पाठकों के लिए निःशुल्क उपलब्ध हो सके",
     ["A library late fine for damaged articles", "The cost of printing physical journal copies", "The salary paid to academic journal peer reviewers"],
     ["क्षतिग्रस्त लेखों हेतु पुस्तकालय जुर्माना", "पत्रिका की भौतिक प्रतियों की छपाई लागत", "शोध समीक्षकों को दिया जाने वाला वेतन"],
     "Under the 'Gold Open Access' model, APCs shift publishing costs from reader subscriptions to the research producer side.",
     "गोल्ड ओपन एक्सेस में पाठक से शुल्क लेने के बजाय लेखक का संस्थान APC भरता है ताकि पूरी दुनिया में शोध मुफ्त पढ़ा जा सके।"),

    # 24
    ("What is 'Green Open Access' (or Self-Archiving)?",
     "'ग्रीन ओपन एक्सेस' (Green Open Access / सेल्फ-आर्काइविंग) से क्या तात्पर्य है?",
     "The author deposits a preprint or postprint version of their published article into an institutional repository or disciplinary archive",
     "लेखक द्वारा अपने प्रकाशित शोध पत्र के प्री-प्रिंट या पोस्ट-प्रिंट प्रारूप को अपने विश्वविद्यालय के डिजिटल रिपोजिटरी में निःशुल्क जमा करना",
     ["Publishing articles printed exclusively on green recycled paper", "Writing research papers about agriculture and forestry only", "Selling old magazines at garden exhibitions"],
     ["केवल हरे पुनर्चक्रित कागज पर लेख छापना", "केवल कृषि और वानिकी पर शोध पत्र लिखना", "बगीचे की प्रदर्शनियों में पुरानी पत्रिकाएं बेचना"],
     "Green OA allows authors to legally share their research openly via institutional repositories (like Shodhganga or DSpace).",
     "ग्रीन ओपन एक्सेस में शोधकर्ता अपने लेख को अपनी यूनिवर्सिटी की वेबसाइट या रिपोजिटरी पर मुफ्त डाउनलोड हेतु उपलब्ध कराता है।"),

    # 25
    ("What is an 'Embargo' on an author's self-archived manuscript in Green Open Access?",
     "ग्रीन ओपन एक्सेस में लेखक के शोध पत्र पर 'एम्बार्गो' (Embargo) का क्या अर्थ है?",
     "A delay period (e.g., 6, 12, or 24 months) required by the commercial publisher before the repository manuscript can be made public",
     "वाणिज्यिक प्रकाशक द्वारा अनिवार्य की गई प्रतीक्षा अवधि (जैसे 6 या 12 महीने) जिसके बाद ही शोध पत्र को सार्वजनिक किया जा सकता है",
     ["A permanent ban on researching that scientific topic", "A fine paid for incorrect mathematical equations", "A period during which university libraries remain closed"],
     ["उस वैज्ञानिक विषय पर शोध करने पर स्थायी प्रतिबंध", "गलत गणितीय सूत्रों हेतु दिया गया जुर्माना", "वह अवधि जिसके दौरान पुस्तकालय बंद रहते हैं"],
     "Publishers mandate embargoes to preserve subscription revenues before public repository access begins.",
     "प्रकाशक अपने व्यापारिक हितों की रक्षा के लिए 6 से 12 महीने का एम्बार्गो लगाते हैं, जिसके बीतने पर ही लेख मुफ्त किया जा सकता है।"),

    # 26
    ("What is an 'ISSN' (International Standard Serial Number)?",
     "आईएसएसएन (ISSN - अंतरराष्ट्रीय मानक सामयिकी संख्या) क्या है?",
     "An 8-digit unique code used to identify serial publications regardless of language or country",
     "पत्रिकाओं (सामयिकियों) की विशिष्ट पहचान हेतु प्रयुक्त 8 अंकों का एक अंतरराष्ट्रीय कोड",
     ["A 13-digit code for printed books only", "A 10-digit tax identification number", "A barcode printed on university degrees"],
     ["केवल मुद्रित पुस्तकों हेतु 13 अंकों का कोड", "10 अंकों का टैक्स पहचान नंबर", "विश्वविद्यालय डिग्री पर मुद्रित बारकोड"],
     "ISSN consists of 8 digits partitioned by a hyphen into two groups of 4 digits (e.g., ISSN 1234-5679).",
     "ISSN 8 अंकों का अद्वितीय कोड होता है जो हाइफन द्वारा 4-4 अंकों के दो समूहों में बंटा होता है (जैसे ISSN 0970-4728)।"),

    # 27
    ("Which organization acts as the National Centre for ISSN in India?",
     "भारत में ISSN आवंटित करने के लिए राष्ट्रीय केंद्र (National Centre for ISSN) के रूप में कौन सी संस्था कार्य करती है?",
     "CSIR-NIScPR (National Institute of Science Communication and Policy Research, New Delhi)",
     "सीएसआईआर-निस्पर (CSIR-NIScPR, नई दिल्ली)",
     ["Raja Rammohun Roy National Agency for ISBN", "National Library of India, Kolkata", "University Grants Commission, New Delhi"],
     ["राजा राममोहन राय राष्ट्रीय एजेंसी (ISBN हेतु)", "भारतीय राष्ट्रीय पुस्तकालय, कोलकाता", "विश्वविद्यालय अनुदान आयोग (UGC)"],
     "CSIR-NIScPR (formerly INSDOC/NISCAIR) has served as the National Centre for ISSN assignment in India since 1986.",
     "भारत में पत्रिकाओं को ISSN जारी करने का आधिकारिक राष्ट्रीय केंद्र CSIR-NIScPR (पूर्व में NISCAIR), नई दिल्ली है।"),

    # 28
    ("In an 8-digit ISSN, what character is used if the final check digit calculates to the number 10?",
     "8 अंकों वाले ISSN में यदि अंतिम चेक अंक (Check Digit) की गणना 10 आती है, तो किस अक्षर का उपयोग किया जाता है?",
     "The Roman numeral 'X' (रोमन अंक 'X')", "रोमन अंक 'X' (Roman Numeral 'X')",
     ["The letter 'Z'", "The number '0'", "An asterisk '*'"],
     ["अक्षर 'Z'", "अंक '0'", "तारांकन '*'"],
     "In ISSN modulo 11 algorithm, the Roman numeral 'X' represents the check digit value of 10.",
     "ISSN के मॉड्यूल 11 एल्गोरिदम में 10 के मान को दर्शाने के लिए रोमन अंक 'X' का प्रयोग किया जाता है।"),

    # 29
    ("What is an 'e-ISSN' (Electronic ISSN)?",
     "ई-आईएसएसएन (e-ISSN) क्या होता है?",
     "The specific ISSN assigned to identify the digital or electronic online version of a serial publication",
     "किसी पत्रिका के डिजिटल या ऑनलाइन इलेक्ट्रॉनिक संस्करण की पहचान हेतु आवंटित विशिष्ट ISSN",
     ["An email address used by journal editors", "An electronic password to bypass firewalls", "An electric barcode scanner serial number"],
     ["पत्रिका संपादकों द्वारा प्रयुक्त ईमेल पता", "फायरवॉल को बायपास करने का पासवर्ड", "इलेक्ट्रिक बारकोड स्कैनर का सीरियल नंबर"],
     "Periodicals published in both print and electronic formats receive distinct identifiers: p-ISSN (print) and e-ISSN (electronic).",
     "जब पत्रिका प्रिंट और ऑनलाइन दोनों रूपों में निकलती है, तो दोनों को अलग कोड मिलते हैं: p-ISSN (प्रिंट) और e-ISSN (इलेक्ट्रॉनिक)।"),

    # 30
    ("What is a 'Peer-Reviewed Journal' (or Refereed Journal)?",
     "सहकर्मी-समीक्षित पत्रिका (Peer-Reviewed / Refereed Journal) क्या होती है?",
     "A journal that subjects submitted manuscripts to critical scrutiny by independent domain experts before deciding to publish",
     "वह पत्रिका जो प्रकाशन से पहले प्राप्त शोध पत्रों की विषय के स्वतंत्र निष्पक्ष विशेषज्ञों द्वारा गहन वैज्ञानिक समीक्षा कराती है",
     ["A newspaper edited by high school students", "A magazine containing only paid advertisements", "A newsletter published without any editorial board"],
     ["हाई स्कूल छात्रों द्वारा संपादित अखबार", "केवल सशुल्क विज्ञापन वाली पत्रिका", "बिना किसी संपादक मंडल का समाचार पत्र"],
     "Peer review ensures academic rigor, factual accuracy, and scientific validity of published scholarly literature.",
     "पीयर-रिव्यू में निष्पक्ष विशेषज्ञ शोध पत्र की गुणवत्ता, नवीनता और प्रमाणिकता की कड़ी जांच करते हैं, तभी वह छपता है।"),

    # 31
    ("What does 'Double-Blind Peer Review' mean in scholarly journal publishing?",
     "शोध पत्रिका प्रकाशन में 'डबल-ब्लाइंड पीयर रिव्यू' (Double-Blind Peer Review) का क्या अर्थ है?",
     "Neither the author knows the identity of the reviewers, nor do the reviewers know the identity of the author",
     "न तो लेखक को समीक्षकों के नाम का पता होता है और न ही समीक्षकों को लेखक के नाम या संस्थान का पता होता है",
     ["Both the author and reviewer are visually impaired", "The journal editor rejects papers without reading them", "Reviewers write reports without opening the file"],
     ["लेखक और समीक्षक दोनों दृष्टिबाधित होते हैं", "संपादक बिना पढ़े लेख अस्वीकार कर देता है", "समीक्षक बिना फाइल खोले रिपोर्ट लिखते हैं"],
     "Double-blind review eliminates personal, institutional, and geographical bias in evaluating research merit.",
     "डबल-ब्लाइंड समीक्षा में दोनों पक्षों की पहचान गुप्त रखी जाती है ताकि समीक्षा पूरी तरह निष्पक्ष और पूर्वाग्रह-मुक्त रहे।"),

    # 32
    ("What is a 'Predatory Journal'?",
     "शिकारी पत्रिका (Predatory Journal) से क्या अभिप्राय है?",
     "A deceptive, fraudulent open-access journal that charges author fees (APCs) without providing legitimate peer-review or editorial services",
     "धोखेबाज पत्रिका जो बिना वास्तविक सहकर्मी समीक्षा के केवल पैसे (APC) लेकर घटिया शोध पत्र धड़ल्ले से छाप देती है",
     ["A wildlife magazine about predatory lions and tigers", "A highly respected military defense research journal", "A journal that hunts for ancient historical manuscripts"],
     ["शेर और चीतों पर छपने वाली वन्यजीव पत्रिका", "अत्यंत प्रतिष्ठित सैन्य रक्षा शोध पत्रिका", "प्राचीन पांडुलिपियों की खोज करने वाली पत्रिका"],
     "Predatory publishers exploit the open-access APC model to profit off academics pressured to publish, publishing junk science.",
     "शिकारी पत्रिकाएं लेखकों से हजारों रुपये लेकर बिना किसी जांच के 2-3 दिन में फर्जी लेख छाप देती हैं, जिससे शोध की गुणवत्ता नष्ट होती है।"),

    # 33
    ("Who famously created and maintained 'Beall's List' of potential predatory publishers and journals until 2017?",
     "2017 तक संभावित शिकारी प्रकाशकों और पत्रिकाओं की प्रसिद्ध 'बील्स लिस्ट' (Beall's List) किसने बनाई और संचालित की थी?",
     "Jeffrey Beall (जेफरी बील - यूनिवर्सिटी ऑफ कोलोराडो डेनवर)",
     "जेफरी बील (Jeffrey Beall)",
     ["Eugene Garfield", "Derek de Solla Price", "S. R. Ranganathan"],
     ["यूजीन गारफील्ड", "डेरेक डी सोला प्राइस", "एस. आर. रंगनाथन"],
     "Librarian Jeffrey Beall coined the term 'predatory publisher' and maintained the definitive blacklist alerting researchers to rogue journals.",
     "अमेरिकी पुस्तकालय विज्ञानी जेफरी बील ने शिकारी पत्रिकाओं (Predatory Journals) का पर्दाफाश करने वाली ऐतिहासिक काली सूची बनाई थी।"),

    # 34
    ("What is the 'UGC-CARE List' established by the University Grants Commission in India?",
     "भारत में विश्वविद्यालय अनुदान आयोग (UGC) द्वारा स्थापित 'UGC-CARE सूची' क्या है?",
     "A curated reference list of quality-assured, credible peer-reviewed academic journals to curb predatory publishing in Indian academia",
     "भारतीय उच्च शिक्षा में शिकारी पत्रिकाओं पर रोक लगाने हेतु गुणवत्तापूर्ण प्रामाणिक शोध पत्रिकाओं की यूजीसी द्वारा अनुमोदित संदर्भ सूची",
     ["A medical insurance list for retired librarians", "A catalogue of discounted textbooks for poor students", "A register of blacklisted computer repair vendors"],
     ["सेवानिवृत्त कर्मियों हेतु चिकित्सा बीमा सूची", "गरीब छात्रों हेतु रियायती पुस्तकों की सूची", "काली सूची में डाले गए कंप्यूटर विक्रेताओं की सूची"],
     "UGC-CARE (Consortium for Academic and Research Ethics) maintains lists of approved journals for faculty recruitment and promotions.",
     "UGC-CARE सूची में शामिल पत्रिकाओं में छपे शोध पत्र ही भारत में शिक्षकों की पदोन्नति (CAS) और पीएचडी उपाधि हेतु मान्य होते हैं।"),

    # 35
    ("In journal indexing, what is an 'Impact Factor' (Journal Impact Factor - JIF)?",
     "पत्रिका अनुक्रमण में 'इम्पैक्ट फैक्टर' (Journal Impact Factor - JIF) क्या होता है?",
     "A scientometric metric reflecting the annual average number of citations received by recent articles published in that journal",
     "किसी शोध पत्रिका में प्रकाशित लेखों को प्राप्त होने वाले वार्षिक औसत उद्धरणों (Citations) की संख्या दर्शाने वाला वैज्ञानिक पैमाना",
     ["The physical impact resistance of book covers", "The speed of delivery by postal mail", "The total financial profit made by the publisher"],
     ["पुस्तक कवर की भौतिक मजबूती", "डाक द्वारा वितरण की गति", "प्रकाशक द्वारा कमाया गया कुल मुनाफा"],
     "JIF measures how frequently an average article in a journal has been cited over a two-year window, indicating journal influence.",
     "इम्पैक्ट फैक्टर यह बताता है कि किसी पत्रिका के लेखों को अन्य वैज्ञानिकों द्वारा कितनी बार अपने शोध में उद्धृत (साइट) किया गया है।"),

    # 36
    ("Who invented the Journal Impact Factor (JIF) and founded the Institute for Scientific Information (ISI)?",
     "जर्नल इम्पैक्ट फैक्टर (JIF) का आविष्कार किसने किया और इंस्टीट्यूट फॉर साइंटिफिक इंफॉर्मेशन (ISI) की स्थापना किसने की थी?",
     "Eugene Garfield (यूजीन गारफील्ड)", "यूजीन गारफील्ड (Eugene Garfield)",
     ["Derek de Solla Price", "Alan Pritchard", "F. W. Lancaster"],
     ["डेरेक डी सोला प्राइस", "एलन प्रिचर्ड", "एफ. डब्ल्यू. लैंकेस्टर"],
     "Eugene Garfield created Science Citation Index and introduced the Impact Factor in 1955, published annually in Journal Citation Reports (JCR).",
     "यूजीन गारफील्ड ने उद्धरण अनुक्रमण (Citation Indexing) और 1955 में इम्पैक्ट फैक्टर की अवधारणा देकर शोध मूल्यांकन में क्रांति ला दी।"),

    # 37
    ("Which annual publication by Clarivate Analytics provides authoritative Impact Factors and rankings of scholarly journals?",
     "क्लेरिवेट एनालिटिक्स (Clarivate Analytics) का कौन सा वार्षिक प्रकाशन शोध पत्रिकाओं के आधिकारिक इम्पैक्ट फैक्टर और रैंकिंग जारी करता है?",
     "Journal Citation Reports - JCR (जर्नल साइटेशन रिपोर्ट्स)",
     "जर्नल साइटेशन रिपोर्ट्स (Journal Citation Reports - JCR)",
     ["Ulrich's Periodicals Directory", "Index Medicus", "Chemical Abstracts"],
     ["उलरिख्स पीरियोडिकल्स डायरेक्टरी", "इंडेक्स मेडिकस", "केमिकल एब्सट्रैक्ट्स"],
     "JCR analyzes citation data from Web of Science to rank thousands of scientific journals by their Impact Factor and Quartile scores.",
     "JCR दुनिया भर की शीर्ष विज्ञान और सामाजिक विज्ञान पत्रिकाओं के इम्पैक्ट फैक्टर और Q1-Q4 रैंकिंग का सबसे प्रामाणिक स्रोत है।"),

    # 38
    ("What is 'Ulrich's Periodicals Directory' (Ulrichsweb)?",
     "उलरिख्स पीरियोडिकल्स डायरेक्टरी (Ulrichsweb) क्या है?",
     "The authoritative global bibliographic database providing comprehensive information on all active and ceased serials worldwide",
     "दुनिया भर की सभी सक्रिय और बंद हो चुकी पत्रिकाओं (सामयिकियों) की प्रामाणिक जानकारी प्रदान करने वाली वैश्विक निर्देशिका",
     ["A dictionary of foreign medical terms", "A catalogue of German rare manuscripts", "A software for scanning barcodes"],
     ["विदेशी चिकित्सा शब्दों का शब्दकोश", "जर्मन दुर्लभ पांडुलिपियों का कैटलॉग", "बारकोड स्कैन करने का सॉफ्टवेयर"],
     "First published by Carolyn Ulrich in 1932, Ulrich's provides publication frequency, publisher, ISSN, and peer-review status for 300,000+ serials.",
     "1932 से प्रकाशित उलरिख्स दुनिया की 3 लाख से अधिक पत्रिकाओं का इतिहास, आवृत्ति, प्रकाशक और पीयर-रिव्यू स्थिति जानने का सबसे बड़ा साधन है।"),

    # 39
    ("What does 'Frequency' of a periodical refer to?",
     "किसी पत्रिका की 'आवृत्ति' (Frequency) से क्या तात्पर्य है?",
     "The regular intervals at which successive issues of the serial are scheduled to be published (e.g., monthly, quarterly)",
     "वह निश्चित समयांतराल जिस पर पत्रिका के नए अंक नियमित रूप से प्रकाशित होते हैं (जैसे मासिक, त्रैमासिक)",
     ["The volume level of reading room noise", "The number of pages per chapter", "The frequency of radio waves used in Wi-Fi"],
     ["वाचनालय के शोर का स्तर", "प्रति अध्याय पृष्ठों की संख्या", "वाई-फाई में प्रयुक्त रेडियो तरंगों की आवृत्ति"],
     "Common frequencies include: Weekly (52/yr), Fortnightly (24/yr), Monthly (12/yr), Bimonthly (6/yr), Quarterly (4/yr), and Annual.",
     "सामान्य आवृत्तियां हैं: साप्ताहिक, पाक्षिक (15 दिन), मासिक, द्वि-मासिक (2 माह), त्रैमासिक (3 माह) और वार्षिक।"),

    # 40
    ("A periodical published once every two months is called a:",
     "प्रत्येक दो महीने में एक बार प्रकाशित होने वाली पत्रिका क्या कहलाती है?",
     "Bimonthly (द्वि-मासिक / बाइमंथली)", "द्वि-मासिक (Bimonthly)",
     ["Semimonthly", "Biennial", "Biannual"],
     ["अर्ध-मासिक (महीने में दो बार)", "द्विवार्षिक (दो साल में एक बार)", "अर्ध-वार्षिक (साल में दो बार)"],
     "Bimonthly means once every two months (6 issues per year); semimonthly means twice a month (24 issues per year).",
     "बाइमंथली (Bimonthly) का अर्थ है दो माह में एक बार (साल में 6 अंक); सेमिमंथली का अर्थ है महीने में दो बार।"),

    # 41
    ("A periodical published twice a year (every six months) is designated as:",
     "वर्ष में दो बार (प्रत्येक छह महीने में) प्रकाशित होने वाली पत्रिका को क्या कहा जाता है?",
     "Semiannual or Biannual (अर्ध-वार्षिक)", "अर्ध-वार्षिक (Semiannual / Biannual)",
     ["Biennial", "Bimonthly", "Fortnightly"],
     ["द्विवार्षिक (Biennial)", "द्वि-मासिक", "पाक्षिक"],
     "Semiannual (or biannual) appears twice each year (2 issues per volume); biennial occurs once every two years.",
     "सेमि-एनुअल (Semiannual) साल में दो बार निकलती है; जबकि बाइएनियल (Biennial) दो साल में एक बार होती है।"),

    # 42
    ("In serials control, what is a 'Supplement'?",
     "सामयिकी नियंत्रण में 'अनुपूरक' (Supplement) क्या होता है?",
     "An extra, separate issue published in addition to regular scheduled numbers, containing special symposia or conference papers",
     "नियमित अंकों के अतिरिक्त प्रकाशित किया जाने वाला विशेष अंक, जिसमें संगोष्ठियों या विशेष विषयों के शोध पत्र होते हैं",
     ["A replacement for a torn cover", "A discount coupon sent by the vendor", "A paper bookmark provided free"],
     ["फटे कवर का प्रतिस्थापन", "विक्रेता द्वारा भेजा गया छूट कूपन", "मुफ्त दिया गया बुकमार्क"],
     "Supplements must be tracked on the check-in record and collated along with regular numbers during annual volume binding.",
     "सप्लीमेंट नियमित अंकों से अलग विशेष अंक होते हैं, जिन्हें जिल्द बंधवाते समय खंड के अंत में साथ में बांधा जाता है।"),

    # 43
    ("In serials acquisition, what is 'Direct Subscription'?",
     "पत्रिका खरीद में 'प्रत्यक्ष सदस्यता' (Direct Subscription) से क्या तात्पर्य है?",
     "Subscribing and remitting payment directly to the publisher without utilizing a commercial middleman or subscription agent",
     "किसी मध्यस्थ या एजेंसी का सहारा लिए बिना सीधे मूल प्रकाशक को भुगतान भेजकर सदस्यता लेना",
     ["Buying used magazines from street vendors", "Borrowing journals from neighborhood libraries", "Downloading pirated PDFs from social media"],
     ["सड़क किनारे से पुरानी पत्रिकाएं खरीदना", "पड़ोस के पुस्तकालय से पत्रिकाएं मांगना", "सोशल मीडिया से पायरेटेड पीडीएफ डाउनलोड करना"],
     "Direct subscription avoids agent handling fees and is commonly used for domestic society journals.",
     "प्रत्यक्ष सदस्यता में पुस्तकालय सीधे प्रकाशक (जैसे राष्ट्रीय अकादमियों) को चेक भेजकर पत्रिकाएं मंगाता है।"),

    # 44
    ("What is a 'Consortium Journal Subscription'?",
     "कंसोर्टियम पत्रिका सदस्यता (Consortium Subscription) क्या है?",
     "A collective licensing arrangement where university libraries pool funds to negotiate bulk online access to thousands of e-journals",
     "सामूहिक लाइसेंसिंग व्यवस्था जहां कई विश्वविद्यालय मिलकर हजारों ऑनलाइन पत्रिकाओं के उपयोग का थोक समझौता करते हैं",
     ["Buying printed journals to share by postal parcel", "Subscribing to one single newspaper for the entire city", "Printing counterfeit journals at low cost"],
     ["डाक से बांटने हेतु मुद्रित पत्रिकाएं खरीदना", "पूरे शहर हेतु केवल एक अखबार मंगाना", "कम लागत में नकली पत्रिकाएं छापना"],
     "National consortia (like e-ShodhSindhu in India) secure massive discounts and campus-wide IP-based access for member institutions.",
     "ई-शोधसिंधु जैसा कंसोर्टियम विश्वविद्यालयों को 80-90% तक की भारी छूट पर विश्वस्तरीय ऑनलाइन जर्नल्स सुलभ कराता है।"),

    # 45
    ("What does 'IP-based Access' to electronic journals mean for a university campus?",
     "विश्वविद्यालय परिसर में ई-जर्नल्स के 'आईपी-आधारित उपयोग' (IP-based Access) का क्या अर्थ है?",
     "Any computer connected to the authorized campus network/Wi-Fi can access full-text articles without entering individual usernames and passwords",
     "परिसर के इंटरनेट/वाई-फाई से जुड़ा कोई भी कंप्यूटर बिना किसी व्यक्तिगत पासवर्ड के सीधे शोध लेख डाउनलोड कर सकता है",
     ["Access is restricted to international police officers only", "Users must show a physical identity card to the computer screen", "Patrons must insert paper coins into internet sockets"],
     ["पहुंच केवल अंतरराष्ट्रीय पुलिस तक सीमित है", "कंप्यूटर स्क्रीन को भौतिक आई-कार्ड दिखाना पड़ता है", "इंटरनेट सॉकेट में सिक्के डालने पड़ते हैं"],
     "Publishers whitelist the university's range of static public IP addresses, granting seamless authenticated access campus-wide.",
     "प्रकाशक विश्वविद्यालय के आईपी पतों (IP Range) को अधिकृत कर देते हैं जिससे कैंपस में बैठा कोई भी छात्र तुरंत जर्नल खोल सकता है।"),

    # 46
    ("What technology enables university students to access campus-subscribed e-resources from home or remote locations?",
     "विश्वविद्यालय के छात्रों को घर बैठे परिसर के सदस्यित ई-संसाधनों का उपयोग करने की सुविधा कौन सी तकनीक देती है?",
     "Remote Access / Off-Campus Access proxy systems like EZproxy or Shibboleth",
     "रिमोट एक्सेस / ऑफ-कैंपस एक्सेस प्रॉक्सी प्रणालियां जैसे ईजेडप्रॉक्सी (EZproxy) या शिबोलेथ (Shibboleth)",
     ["Bluetooth file sharing", "Infrared television remotes", "VHF walkie-talkies"],
     ["ब्लूटूथ फाइल शेयरिंग", "इन्फ्रारेड टीवी रिमोट", "वीएचएफ वॉकी-टॉकी"],
     "EZproxy and federated identity systems authenticate users via their university credentials and route traffic through campus IP addresses.",
     "EZproxy और Shibboleth जैसी प्रॉक्सी प्रणालियां छात्रों को घर बैठे अपने लैपटॉप से विश्वविद्यालय के डेटाबेस खोलने की सुविधा देती हैं।"),

    # 47
    ("What is an 'Electronic Resource Management' (ERM) system in modern libraries?",
     "आधुनिक पुस्तकालयों में 'इलेक्ट्रॉनिक संसाधन प्रबंधन' (ERM) प्रणाली क्या होती है?",
     "Software designed specifically to track electronic serial licensing, renewal workflows, trial access, vendor contacts, and usage stats",
     "विशेष रूप से ई-पत्रिकाओं के लाइसेंस, नवीनीकरण चक्र, विक्रेता संपर्कों और उपयोग आंकड़ों को प्रबंधित करने वाला सॉफ्टवेयर",
     ["A machine that cleans computer monitors", "A system for printing paper catalogue cards", "A digital clock on the library website"],
     ["कंप्यूटर मॉनिटर साफ करने वाली मशीन", "कागजी सूची कार्ड प्रिंट करने की प्रणाली", "पुस्तकालय वेबसाइट पर डिजिटल घड़ी"],
     "ERM systems (like Coral or Alma ERM) handle the complex, non-physical lifecycle of digital journal subscriptions.",
     "ईआरएम (ERM) सॉफ्टवेयर ई-जर्नल्स के जटिल समझौतों, लाइसेंस शर्तों और वार्षिक नवीनीकरण की पूरी प्रक्रिया को संभालता है।"),

    # 48
    ("In serials evaluation, what does 'Cost per Download' (CPD) measure?",
     "सामयिकी मूल्यांकन में 'लागत प्रति डाउनलोड' (Cost per Download - CPD) क्या मापता है?",
     "The annual subscription cost of an electronic journal divided by the total number of full-text articles downloaded by users",
     "किसी ई-पत्रिका की कुल वार्षिक सदस्यता लागत को उपयोगकर्ताओं द्वारा डाउनलोड किए गए कुल शोध पत्रों की संख्या से भाग देना",
     ["The electricity cost of running a laser printer", "The internet speed measured in megabytes per second", "The cost of buying external hard disks"],
     ["लेजर प्रिंटर चलाने की बिजली लागत", "मेगाबाइट प्रति सेकंड में इंटरनेट की गति", "एक्सटर्नल हार्ड डिस्क खरीदने का खर्च"],
     "CPD is the primary metric for deciding renewal: low CPD indicates high cost-effectiveness, while very high CPD prompts cancellation.",
     "लागत प्रति डाउनलोड (CPD) यह बताता है कि एक शोध पत्र को पढ़ने पर पुस्तकालय का कितना खर्च आया; अत्यधिक महंगा CPD होने पर जर्नल बंद कर दिया जाता है।")
]

print("Q47 loaded, count:", len(q47_pool))
