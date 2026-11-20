# -*- coding: utf-8 -*-
"""
Generator for Slot Q95: Semantic Web & Linked Open Data (LOD) - 48 items.
"""

q95_items = [
    # 1: Tim Berners-Lee 2001
    ("Who famously coined and popularized the vision of the 'Semantic Web' in a seminal 2001 Scientific American article?",
     "2001 में साइंटिफिक अमेरिकन के एक मौलिक लेख में 'सिमेंटिक वेब' (Semantic Web) की अवधारणा और दृष्टि को किसने प्रसिद्ध रूप से गढ़ा और लोकप्रिय बनाया?",
     "Tim Berners-Lee, James Hendler, and Ora Lassila",
     "टिम बर्नर्स-ली, जेम्स हेंडलर और ओरा लस्सीला",
     ["Bill Gates, Steve Jobs, and Paul Allen", "Melvil Dewey, S. R. Ranganathan, and C. A. Cutter", "Charles Babbage, Ada Lovelace, and Alan Turing"],
     ["बिल गेट्स, स्टीव जॉब्स और पॉल एलन", "मेलविल डेवी, एस. आर. रंगनाथन और सी. ए. कटर", "चार्ल्स बैबेज, एडा लवलेस और एलन ट्यूरिंग"],
     "Tim Berners-Lee, alongside James Hendler and Ora Lassila, published the landmark 2001 paper describing the Semantic Web as an extension of the existing Web in which information is given well-defined meaning.",
     "टिम बर्नर्स-ली, जेम्स हेंडलर और ओरा लस्सीला ने 2001 में साइंटिफिक अमेरिकन में 'द सिमेंटिक वेब' लेख लिखकर कंप्यूटरों द्वारा अर्थ समझने योग्य वेब का खाका पेश किया।"),

    # 2: Web of Documents vs Web of Data
    ("How does the fundamental architecture of the 'Semantic Web' differ from the traditional World Wide Web?",
     "'सिमेंटिक वेब' की मूलभूत वास्तुकला पारंपरिक वर्ल्ड वाइड वेब से किस प्रकार भिन्न है?",
     "It transforms the Web from a 'Web of human-readable documents' linked by hyperlinks into a machine-understandable 'Web of linked data and entities'",
     "यह वेब को हाइपरलिंक से जुड़े 'मानव-पठनीय दस्तावेजों के वेब' से मशीनों द्वारा समझने योग्य 'लिंक्ड डेटा और संस्थाओं के वेब' में बदल देता है",
     ["It replaces all computer monitors with acoustic voice-activated speakers", "It completely eliminates the use of telecommunication optical fiber cables", "It restricts web browsing strictly to certified university professors"],
     ["यह सभी कंप्यूटर मॉनिटरों को ध्वनि-सक्रिय स्पीकरों से बदल देता है", "यह दूरसंचार ऑप्टिकल फाइबर केबलों के उपयोग को पूरी तरह समाप्त कर देता है", "यह वेब ब्राउज़िंग को केवल प्रमाणित विश्वविद्यालय के प्रोफेसरों तक सीमित करता है"],
     "Traditional Web connects HTML documents intended for human consumption; the Semantic Web connects structured data and real-world entities so machines can process, reason, and infer knowledge.",
     "पारंपरिक वेब केवल इंसानों के पढ़ने के लिए वेब पेजों को जोड़ता है, जबकि सिमेंटिक वेब डेटा को इस तरह संरचित करता है कि कंप्यूटर और एल्गोरिदम उसके अर्थ को समझ सकें।"),

    # 3: RDF Triple structure
    ("What is the fundamental building block of the Resource Description Framework (RDF) data model?",
     "रिसोर्स डिस्क्रिप्शन फ्रेमवर्क (RDF) डेटा मॉडल का मूलभूत निर्माण खंड क्या है?",
     "A 'Triple' consisting of Subject, Predicate, and Object",
     "सब्जेक्ट, प्रेडिकेट और ऑब्जेक्ट (Subject, Predicate, Object) से बना एक 'ट्रिपल'",
     ["A 'Quad' consisting of IP address, Port, Protocol, and MAC address", "A 'Dual' consisting of Username and Password", "A 'Hexagon' consisting of six geometric vertices"],
     ["आईपी पता, पोर्ट, प्रोटोकॉल और मैक पते से बना एक 'क्वाड'", "उपयोगकर्ता नाम और पासवर्ड से बना एक 'ड्यूल'", "छह ज्यामितीय शीर्षों से बना एक 'हेक्सागोन'"],
     "Every statement in RDF is expressed as a triple: Subject (the resource), Predicate (the property or relationship), and Object (the value or related resource).",
     "RDF डेटा मॉडल का आधार 'ट्रिपल' है, जिसमें तीन भाग होते हैं: विषय (Subject), विधेय/गुणधर्म (Predicate), और वस्तु/मान (Object)।"),

    # 4: URI / IRI role
    ("Why are Uniform Resource Identifiers (URIs) and Internationalized Resource Identifiers (IRIs) essential in RDF triples?",
     "RDF ट्रिपल्स में यूनिफ़ॉर्म रिसोर्स आइडेंटिफ़ायर्स (URIs) और अंतर्राष्ट्रीयकृत रिसोर्स आइडेंटिफ़ायर्स (IRIs) क्यों आवश्यक हैं?",
     "They provide globally unique, unambiguous identifiers for real-world entities, concepts, and relationships across the entire web",
     "वे पूरे वेब पर वास्तविक दुनिया की संस्थाओं, अवधारणाओं और संबंधों के लिए विश्व स्तर पर अद्वितीय, स्पष्ट पहचानकर्ता प्रदान करते हैं",
     ["They act as temporary encryption passwords changed every twenty-four hours", "They serve as graphic file formats to display color book cover images", "They measure the physical bandwidth speed of fiber optic routers"],
     ["वे हर चौबीस घंटे में बदले जाने वाले अस्थायी एन्क्रिप्शन पासवर्ड के रूप में कार्य करते हैं", "वे रंगीन पुस्तक कवर छवियों को प्रदर्शित करने के लिए ग्राफिक फ़ाइल स्वरूपों के रूप में काम करते हैं", "वे फाइबर ऑप्टिक राउटर की भौतिक बैंडविड्थ गति को मापते हैं"],
     "URIs ensure that resources (e.g., an author, a place, or a subject concept) have universal, persistent identities that avoid linguistic ambiguity and name collisions.",
     "URI और IRI वेब पर प्रत्येक संसाधन (जैसे लेखक, विषय या पुस्तक) को एक अद्वितीय वैश्विक पहचान देते हैं, जिससे नाम के भ्रम दूर होते हैं।"),

    # 5: RDF Serializations
    ("Which of the following is NOT a standardized serialization format for representing RDF graphs?",
     "निम्नलिखित में से कौन सा RDF ग्राफ़ को प्रस्तुत करने के लिए एक मानकीकृत सीरियलाइज़ेशन प्रारूप नहीं है?",
     "Adobe Shockwave Flash (.SWF)",
     "एडोब शॉकवेव फ़्लैश (.SWF)",
     ["Turtle (Terse RDF Triple Language)", "JSON-LD (JavaScript Object Notation for Linked Data)", "N-Triples and RDF/XML"],
     ["टर्टल (Turtle - Terse RDF Triple Language)", "JSON-LD (लिंक्ड डेटा के लिए जावास्क्रिप्ट ऑब्जेक्ट नोटेशन)", "N-Triples और RDF/XML"],
     "RDF graphs can be serialized in formats such as Turtle, RDF/XML, N-Triples, N3, and JSON-LD. Shockwave Flash is a deprecated multimedia format.",
     "RDF को व्यक्त करने के लिए Turtle, JSON-LD, RDF/XML, N-Triples आदि प्रारूपों का उपयोग किया जाता है; एडोब फ़्लैश एक मल्टीमीडिया प्रारूप है।"),

    # 6: Turtle format
    ("What makes 'Turtle' (Terse RDF Triple Language) particularly popular among ontology designers and knowledge graph developers?",
     "ओंटोलॉजी डिजाइनरों और नॉलेज ग्राफ़ डेवलपर्स के बीच 'टर्टल' (Turtle) विशेष रूप से लोकप्रिय क्यों है?",
     "It is a compact, highly human-readable, and concise textual syntax for expressing RDF statements using prefix shortcuts",
     "यह प्रीफ़िक्स शॉर्टकट का उपयोग करके RDF कथनों को व्यक्त करने के लिए एक संक्षिप्त, अत्यधिक मानव-पठनीय और स्पष्ट टेक्स्ट सिंटैक्स है",
     ["It compiles RDF triples into binary machine code executed directly by computer processors", "It converts all text into handwritten calligraphy fonts automatically", "It compresses text into encrypted audio recordings for listening on radio"],
     ["यह RDF ट्रिपल्स को कंप्यूटर प्रोसेसर द्वारा सीधे निष्पादित बाइनरी मशीन कोड में संकलित करता है", "यह सभी टेक्स्ट को स्वचालित रूप से हस्तलिखित सुलेख फ़ॉन्ट में परिवर्तित करता है", "यह रेडियो पर सुनने के लिए टेक्स्ट को एन्क्रिप्टेड ऑडियो रिकॉर्डिंग में संपीड़ित करता है"],
     "Turtle syntax avoids the verbose XML tags of RDF/XML, making complex knowledge graphs easy for humans to read, write, and debug.",
     "Turtle प्रारूप RDF/XML की तुलना में बहुत सरल और मानव-पठनीय है, जिसमें प्रीफ़िक्स के माध्यम से ट्रिपल्स को संक्षेप में लिखा जाता है।"),

    # 7: JSON-LD
    ("Why has JSON-LD (JavaScript Object Notation for Linked Data) become the de facto standard for Linked Data on the modern web?",
     "JSON-LD (जावास्क्रिप्ट ऑब्जेक्ट नोटेशन फॉर लिंक्ड डेटा) आधुनिक वेब पर लिंक्ड डेटा के लिए वास्तविक मानक क्यों बन गया है?",
     "It allows linked data to be seamlessly serialized inside standard JSON structures easily consumed by web developers and search engines without new parsers",
     "यह लिंक्ड डेटा को मानक JSON संरचनाओं के भीतर सहजता से व्यवस्थित करने की अनुमति देता है जिसे वेब डेवलपर्स और सर्च इंजन बिना नए पार्सर के आसानी से पढ़ सकते हैं",
     ["It forces web browsers to disable all CSS stylesheets and JavaScript scripts", "It prevents web crawlers from indexing library catalogs and academic repositories", "It requires all internet servers to run on proprietary closed-source microchips"],
     ["यह वेब ब्राउज़रों को सभी CSS स्टाइलशीट और जावास्क्रिप्ट स्क्रिप्ट को अक्षम करने के लिए मजबूर करता है", "यह वेब क्रॉलर्स को पुस्तकालय कैटलॉग और अकादमिक रिपॉजिटरी को अनुक्रमित करने से रोकता है", "इसके लिए सभी इंटरनेट सर्वरों को मालिकाना क्लोज्ड-सोर्स माइक्रोचिप्स पर चलने की आवश्यकता होती है"],
     "JSON-LD is a W3C recommendation that lets developers add linked data context (such as Schema.org metadata) directly into conventional JSON web APIs.",
     "JSON-LD वेब डेवलपर्स के लिए अत्यंत सहज है क्योंकि यह साधारण JSON प्रारूप में ही लिंक्ड डेटा संदर्भ जोड़ देता है, जिसे गूगल जैसे सर्च इंजन आसानी से समझ लेते हैं।"),

    # 8: RDFS (RDF Schema)
    ("What is the primary role of 'RDF Schema' (RDFS) in the Semantic Web layered architecture?",
     "सिमेंटिक वेब की स्तरित वास्तुकला में 'RDF स्कीमा' (RDFS) की प्राथमिक भूमिका क्या है?",
     "Providing a data-modeling vocabulary to define classes, subclasses, properties, domains, and ranges for structuring RDF resources",
     "RDF संसाधनों को संरचित करने के लिए क्लास, सब-क्लास, गुणधर्म, डोमेन और रेंज को परिभाषित करने हेतु एक डेटा-मॉडलिंग शब्दावली प्रदान करना",
     ["Encrypting web traffic using 4096-bit mathematical cryptographic keys", "Formatting printed barcodes on library circulation circulation desk slips", "Managing high-speed cache memory inside server central processing units"],
     ["4096-बिट गणितीय क्रिप्टोग्राफिक कुंजियों का उपयोग करके वेब ट्रैफ़िक को एन्क्रिप्ट करना", "पुस्तकालय संचलन डेस्क पर्चियों पर मुद्रित बारकोड को प्रारूपित करना", "सर्वर सेंट्रल प्रोसेसिंग इकाइयों के अंदर उच्च गति कैश मेमोरी का प्रबंधन करना"],
     "RDFS extends RDF by providing ontological primitives like rdfs:Class, rdfs:subClassOf, rdfs:subPropertyOf, rdfs:domain, and rdfs:range.",
     "RDFS (RDF स्कीमा) एक बुनियादी शब्दावली प्रदान करता है जिससे हम यह परिभाषित कर सकते हैं कि कौन सी चीज़ किस वर्ग (Class) या उपवर्ग की है और उनके गुणधर्म क्या हैं।"),

    # 9: OWL (Web Ontology Language)
    ("What added expressive power does the Web Ontology Language (OWL) provide over basic RDF Schema?",
     "वेब ऑन्टोलॉजी लैंग्वेज (OWL) बुनियादी RDF स्कीमा की तुलना में क्या अतिरिक्त अभिव्यंजक शक्ति प्रदान करती है?",
     "Rich constructs for formal logic, property characteristics (transitive, symmetric, inverse), cardinality restrictions, and automated automated inference",
     "औपचारिक तर्क, गुणधर्म विशेषताओं (संक्रामक, सममित, व्युत्क्रम), कार्डिनैलिटी प्रतिबंध और स्वचालित अनुमान के लिए समृद्ध निर्माण",
     ["The ability to stream 4K resolution digital video over copper telephone cables", "A physical electronic circuit board mounted inside barcode scanners", "An automated robotic system for vacuum cleaning library carpet floors"],
     ["तांबे के टेलीफोन केबलों पर 4K रिज़ॉल्यूशन डिजिटल वीडियो स्ट्रीम करने की क्षमता", "बारकोड स्कैनर के अंदर लगाया गया एक भौतिक इलेक्ट्रॉनिक सर्किट बोर्ड", "पुस्तकालय के कालीन फर्श को वैक्यूम करने के लिए एक स्वचालित रोबोट प्रणाली"],
     "OWL is a W3C standard based on description logics, enabling automated reasoners to deduce new facts that were not explicitly stated in the graph.",
     "OWL (Web Ontology Language) अधिक जटिल तार्किक संबंध (जैसे सममित, संक्रामक, विलोम संबंध) और कार्डिनैलिटी परिभाषित करने की अनुमति देता है जिससे कंप्यूटर नए निष्कर्ष निकाल सकते हैं।"),

    # 10: OWL sublanguages
    ("Which of the following represents the three standardized sublanguages of OWL 1 designed to balance expressive power and computational tractability?",
     "निम्नलिखित में से कौन सा अभिव्यंजक शक्ति और कम्प्यूटेशनल सुगमता को संतुलित करने के लिए डिज़ाइन की गई OWL 1 की तीन मानकीकृत उपभाषाओं का प्रतिनिधित्व करता है?",
     "OWL Lite, OWL DL (Description Logics), and OWL Full",
     "OWL लाइट (Lite), OWL DL (डिस्क्रिप्शन लॉजिक्स), और OWL फुल (Full)",
     ["OWL Basic, OWL Intermediate, and OWL Advanced", "OWL Alpha, OWL Beta, and OWL Gamma", "OWL Micro, OWL Mini, and OWL Macro"],
     ["OWL बेसिक, OWL इंटरमीडिएट, और OWL एडवांस्ड", "OWL अल्फा, OWL बीटा, और OWL गामा", "OWL माइक्रो, OWL मिनी, और OWL मैक्रो"],
     "OWL 1 was partitioned into OWL Lite (simple constraints), OWL DL (computationally complete and decidable), and OWL Full (maximum expressiveness without computational guarantees).",
     "OWL 1 को तीन स्तरों में विभाजित किया गया था: OWL Lite, OWL DL (जो तार्किक रूप से निर्णयक्षम है), और OWL Full (अधिकतम स्वतंत्रता परंतु अनिर्णयक्षम)।"),

    # 11: owl:sameAs
    ("What is the exact semantic meaning of the property 'owl:sameAs' in Linked Open Data?",
     "लिंक्ड ओपन डेटा में 'owl:sameAs' गुणधर्म का सटीक सिमेंटिक अर्थ क्या है?",
     "It asserts that two distinct URIs refer to the exact same real-world entity or resource",
     "यह दावा करता है कि दो अलग-अलग यूआरआई (URIs) बिल्कुल एक ही वास्तविक दुनिया की इकाई या संसाधन को संदर्भित करते हैं",
     ["It asserts that two books share the same physical paper binding and printing ink", "It indicates that two patrons have borrowed books from the library on the same calendar day", "It deletes duplicate files from server storage hard drives permanently"],
     ["यह दावा करता है कि दो पुस्तकें एक ही भौतिक कागज़ की बाइंडिंग और छपाई की स्याही साझा करती हैं", "यह इंगित करता है कि दो संरक्षकों ने एक ही कैलेंडर दिन पर पुस्तकालय से पुस्तकें उधार ली हैं", "यह सर्वर स्टोरेज हार्ड ड्राइव से डुप्लिकेट फ़ाइलों को स्थायी रूप से हटा देता है"],
     "owl:sameAs is used to link identity across independent datasets, e.g., stating that a VIAF URI and a Wikidata URI refer to the exact same human author.",
     "owl:sameAs का उपयोग यह बताने के लिए किया जाता है कि दो अलग-अलग डेटाबेस (जैसे VIAF और विकिडेटा) में मौजूद दो अलग यूआरआई वास्तव में एक ही व्यक्ति या चीज़ के हैं।"),

    # 12: SPARQL Query Language
    ("What is SPARQL in the context of the Semantic Web and Knowledge Graphs?",
     "सिमेंटिक वेब और नॉलेज ग्राफ़ के संदर्भ में 'SPARQL' क्या है?",
     "The W3C standardized query language and protocol designed specifically for querying and manipulating RDF graph data",
     "W3C मानकीकृत क्वेरी भाषा और प्रोटोकॉल जो विशेष रूप से RDF ग्राफ़ डेटा को क्वेरी और हेरफेर करने के लिए डिज़ाइन किया गया है",
     ["A physical barcode scanner manufactured for cataloging old rare manuscripts", "A proprietary operating system developed exclusively for library mainframe supercomputers", "A local network firewall rule blocking unauthorized patron internet downloads"],
     ["पुरानी दुर्लभ पांडुलिपियों को सूचीबद्ध करने के लिए निर्मित एक भौतिक बारकोड स्कैनर", "विशेष रूप से पुस्तकालय मेनफ्रेम सुपरकंप्यूटर के लिए विकसित एक मालिकाना ऑपरेटिंग सिस्टम", "अनधिकृत संरक्षक इंटरनेट डाउनलोड को अवरुद्ध करने वाला एक स्थानीय नेटवर्क फ़ायरवॉल नियम"],
     "SPARQL (SPARQL Protocol and RDF Query Language) allows users and applications to retrieve complex graph patterns across distributed RDF triple stores.",
     "SPARQL सिमेंटिक वेब और RDF डेटाबेस (ट्रिपल स्टोर) के लिए उसी प्रकार की क्वेरी भाषा है जैसे रिलेशनल डेटाबेस (RDBMS) के लिए SQL होती है।"),

    # 13: SPARQL query forms
    ("Which of the following are the four primary query forms supported by SPARQL 1.1?",
     "निम्नलिखित में से कौन से चार प्राथमिक क्वेरी रूप हैं जो SPARQL 1.1 द्वारा समर्थित हैं?",
     "SELECT, CONSTRUCT, ASK, and DESCRIBE",
     "SELECT, CONSTRUCT, ASK, और DESCRIBE",
     ["INSERT, UPDATE, DELETE, and TRUNCATE", "GET, POST, PUT, and DELETE", "FIND, LOCATE, RETRIEVE, and REPORT"],
     ["INSERT, UPDATE, DELETE, और TRUNCATE", "GET, POST, PUT, और DELETE", "FIND, LOCATE, RETRIEVE, और REPORT"],
     "SPARQL defines SELECT (returns tabular data), CONSTRUCT (returns a new RDF graph), ASK (returns a boolean true/false), and DESCRIBE (returns RDF data describing resources).",
     "SPARQL में चार मुख्य क्वेरी फॉर्म होते हैं: SELECT (टेबुलर परिणाम), CONSTRUCT (नया RDF ग्राफ बनाना), ASK (हाँ/ना उत्तर), और DESCRIBE (संसाधन का पूरा विवरण)।"),

    # 14: Tim Berners-Lee 5-Star Open Data
    ("In Tim Berners-Lee's famous '5-Star Linked Open Data' deployment scheme, what constitutes a 5-star dataset?",
     "टिम बर्नर्स-ली की प्रसिद्ध '5-स्टार लिंक्ड ओपन डेटा' योजना में, 5-स्टार डेटासेट क्या होता है?",
     "Data available on the web under an open license, in machine-readable non-proprietary structured format using open W3C standards (RDF/SPARQL), AND linked to other external datasets",
     "ओपन लाइसेंस के तहत वेब पर उपलब्ध डेटा, खुले W3C मानकों (RDF/SPARQL) का उपयोग करके मशीन-पठनीय गैर-मालिकाना संरचित प्रारूप में, और अन्य बाहरी डेटासेट से जुड़ा हुआ (Linked)",
     ["Data printed on waterproof acid-free paper bound in leather encyclopedias", "Data protected behind 5 separate military firewall encryption authentication layers", "Data sold exclusively to certified commercial multinational corporations"],
     ["चमड़े के विश्वकोशों में बंधी वाटरप्रूफ एसिड-मुक्त कागज़ पर मुद्रित डेटा", "5 अलग-अलग सैन्य फ़ायरवॉल एन्क्रिप्शन प्रमाणीकरण परतों के पीछे संरक्षित डेटा", "विशेष रूप से प्रमाणित वाणिज्यिक बहुराष्ट्रीय निगमों को बेचा जाने वाला डेटा"],
     "The 5 stars are: 1★ Web open license; 2★ Structured (e.g. Excel); 3★ Non-proprietary (e.g. CSV); 4★ W3C open standards (RDF/URIs); 5★ Linked to other people's data to provide context.",
     "5-स्टार लिंक्ड डेटा की पाँचवीं स्टार तब मिलती है जब आपका डेटा खुले मानकों (RDF/SPARQL) में हो और वह संदर्भ प्रदान करने के लिए दुनिया के अन्य लिंक्ड डेटासेट से जुड़ा हुआ हो।"),

    # 15: 1-Star to 4-Star distinctions
    ("Under the 5-Star Open Data model, providing a public dataset as a PDF document earns how many stars?",
     "5-स्टार ओपन डेटा मॉडल के तहत, एक सार्वजनिक डेटासेट को पीडीएफ (PDF) दस्तावेज़ के रूप में प्रदान करने पर कितने स्टार मिलते हैं?",
     "1 Star (available on the web under an open licence, but locked in an unstructured document format)",
     "1 स्टार (ओपन लाइसेंस के तहत वेब पर उपलब्ध, लेकिन असंरचित दस्तावेज़ प्रारूप में बंद)",
     ["3 Stars", "4 Stars", "5 Stars"],
     ["3 स्टार", "4 स्टार", "5 स्टार"],
     "A PDF on the web with an open license gets 1 star; it is accessible, but extracting structured data requires difficult OCR or manual scraping.",
     "खुले लाइसेंस के साथ पीडीएफ फाइल केवल 1 स्टार प्राप्त करती है क्योंकि कंप्यूटर उसमें मौजूद डेटा को सीधे तालिकाओं के रूप में प्रोसेस नहीं कर सकता।"),

    # 16: BIBFRAME background
    ("Why did the Library of Congress (LC) initiate the development of BIBFRAME (Bibliographic Framework)?",
     "लाइब्रेरी ऑफ कांग्रेस (LC) ने बिबफ्रेम (BIBFRAME - Bibliographic Framework) के विकास की शुरुआत क्यों की?",
     "To transition library bibliographic cataloging from legacy, siloed MARC 21 flat records into a modern Linked Open Data web architecture",
     "पुस्तकालय ग्रंथसूची कैटलॉगिंग को पुराने, अलग-थलग पड़े MARC 21 फ्लैट रिकॉर्ड से एक आधुनिक लिंक्ड ओपन डेटा वेब आर्किटेक्चर में स्थानांतरित करने के लिए",
     ["To completely eliminate human librarians and replace them with automated cash registers", "To force all libraries to discard physical paper books and burn paper cards", "To establish a proprietary commercial paywall around worldwide public library catalogs"],
     ["मानव लाइब्रेरियनों को पूरी तरह से समाप्त करना और उन्हें स्वचालित नकद रजिस्टरों से बदलना", "सभी पुस्तकालयों को भौतिक कागज़ की किताबों को त्यागने और कागज़ के कार्डों को जलाने के लिए मजबूर करना", "दुनिया भर के सार्वजनिक पुस्तकालय कैटलॉग के चारों ओर एक मालिकाना वाणिज्यिक पेवॉल स्थापित करना"],
     "MARC 21 was designed in the 1960s for printing physical 3x5 catalog cards; BIBFRAME uses Linked Data principles to make library bibliographic data discoverable across the open Web.",
     "MARC 21 को 1960 के दशक में कैटलॉग कार्ड छापने के लिए बनाया गया था; BIBFRAME को इसलिए विकसित किया गया ताकि पुस्तकालयों का कैटलॉग डेटा वेब पर लिंक्ड डेटा के रूप में खोजा जा सके।"),

    # 17: BIBFRAME 2.0 Core Entities
    ("What are the three core levels of abstraction in the BIBFRAME 2.0 entity model?",
     "BIBFRAME 2.0 इकाई मॉडल में अमूर्तता के तीन मुख्य स्तर कौन से हैं?",
     "Work, Instance, and Item",
     "वर्क (Work), इंस्टेंस (Instance), और आइटम (Item)",
     ["Book, Chapter, and Page", "Title, Author, and Subject", "Record, Field, and Subfield"],
     ["पुस्तक, अध्याय, और पृष्ठ", "शीर्षक, लेखक, और विषय", "रिकॉर्ड, फ़ील्ड, और सबफ़ील्ड"],
     "BIBFRAME 2.0 organizes bibliographic description into: Work (conceptual essence, e.g. Hamlet), Instance (individual physical/electronic publication, e.g. 2020 paperback), and Item (specific copy on a shelf).",
     "BIBFRAME 2.0 का मूल मॉडल तीन स्तरों पर आधारित है: वर्क (बौद्धिक कृति), इंस्टेंस (उसका विशिष्ट संस्करण या प्रकाशन), और आइटम (शेल्फ पर रखी भौतिक प्रति)।"),

    # 18: BIBFRAME Additional Classes
    ("In addition to Work, Instance, and Item, what key supporting entities are defined in BIBFRAME 2.0?",
     "वर्क, इंस्टेंस और आइटम के अलावा, BIBFRAME 2.0 में किन प्रमुख सहायक इकाइयों को परिभाषित किया गया है?",
     "Agent, Subject, and Event",
     "एजेंट (Agent), विषय (Subject), और घटना (Event)",
     ["Barcode, RFID, and Printer", "Dewey Number, Cutter Number, and Book Number", "Circulation, Acquisition, and Serials"],
     ["बारकोड, आरएफआईडी, और प्रिंटर", "डेवी संख्या, कटर संख्या, और पुस्तक संख्या", "संचलन, अधिग्रहण, और पत्रिकाएं"],
     "BIBFRAME defines Agents (people, organizations), Subjects (concepts, places, topics), and Events to establish rich relationships connected to Works and Instances.",
     "BIBFRAME में एजेंट (लेखक या प्रकाशक), विषय (अवधारणाएं या स्थान) और घटनाओं को अलग इकाई के रूप में जोड़कर समृद्ध ज्ञान नेटवर्क बनाया जाता है।"),

    # 19: SKOS (Simple Knowledge Organization System)
    ("What is 'SKOS' (Simple Knowledge Organization System) primarily used for in the Semantic Web?",
     "सिमेंटिक वेब में 'SKOS' (Simple Knowledge Organization System) का मुख्य उपयोग किसलिए किया जाता है?",
     "Representing controlled vocabularies, thesauri, classification schemes, and taxonomy concepts as machine-readable Linked Data",
     "नियंत्रित शब्दावलियों, थिसॉरस, वर्गीकरण योजनाओं और टैक्सोनॉमी अवधारणाओं को मशीन-पठनीय लिंक्ड डेटा के रूप में प्रस्तुत करना",
     ["Streaming encrypted video files across university digital classroom networks", "Managing payroll records and annual vacation allowances for library employees", "Controlling temperature and humidity sensors inside physical rare book preservation vaults"],
     ["विश्वविद्यालय के डिजिटल क्लासरूम नेटवर्क पर एन्क्रिप्टेड वीडियो फ़ाइलों को स्ट्रीम करना", "पुस्तकालय कर्मचारियों के लिए पेरोल रिकॉर्ड और वार्षिक अवकाश भत्ते का प्रबंधन करना", "भौतिक दुर्लभ पुस्तक संरक्षण वाल्टों के अंदर तापमान और आर्द्रता सेंसर को नियंत्रित करना"],
     "SKOS is a W3C recommendation designed to express the semantic structure of thesauri, subject headings, and classification schedules (like LCSH or DDC) using RDF.",
     "SKOS एक W3C मानक है जिसका उपयोग पुस्तकालय थिसॉरस, विषय शीर्षकों (जैसे LCSH) और वर्गीकरण योजनाओं को सिमेंटिक वेब पर जोड़ने के लिए किया जाता है।"),

    # 20: SKOS Core Properties
    ("Which of the following sets of properties are foundational to the SKOS vocabulary for hierarchical and associative relations?",
     "पदानुक्रमित और साहचर्य संबंधों के लिए निम्नलिखित में से कौन से गुणधर्म SKOS शब्दावली के लिए मूलभूत हैं?",
     "skos:broader, skos:narrower, and skos:related",
     "skos:broader, skos:narrower, और skos:related",
     ["skos:parent, skos:child, and skos:sibling", "skos:higher, skos:lower, and skos:equal", "skos:before, skos:after, and skos:between"],
     ["skos:parent, skos:child, और skos:sibling", "skos:higher, skos:lower, और skos:equal", "skos:before, skos:after, और skos:between"],
     "SKOS uses skos:broader (BT), skos:narrower (NT), and skos:related (RT) to mirror standard thesaurus relationships defined in ISO 25964.",
     "SKOS में थिसॉरस के व्यापक पद (BT) के लिए skos:broader, संकीर्ण पद (NT) के लिए skos:narrower और संबंधित पद (RT) के लिए skos:related का उपयोग होता है।"),

    # 21: SKOS Lexical Labels
    ("In SKOS, what property is used to specify the authorized, preferred human-readable label for a concept in a given language?",
     "SKOS में किसी दी गई भाषा में किसी अवधारणा के लिए अधिकृत, पसंदीदा मानव-पठनीय लेबल निर्दिष्ट करने के लिए किस गुणधर्म का उपयोग किया जाता है?",
     "skos:prefLabel",
     "skos:prefLabel",
     ["skos:altLabel", "skos:hiddenLabel", "skos:note"],
     ["skos:altLabel", "skos:hiddenLabel", "skos:note"],
     "skos:prefLabel denotes the preferred descriptor (e.g., 'Economics'), while skos:altLabel provides synonyms, lead-in terms, or acronyms (e.g., 'Political Economy').",
     "skos:prefLabel मुख्य पसंदीदा शब्द (Descriptor) के लिए उपयोग किया जाता है, जबकि गैर-पसंदीदा या समानार्थी शब्दों के लिए skos:altLabel का उपयोग होता है।"),

    # 22: FOAF (Friend of a Friend)
    ("What is the primary purpose of the 'FOAF' (Friend of a Friend) ontology in the Semantic Web?",
     "सिमेंटिक वेब में 'FOAF' (Friend of a Friend) ऑन्टोलॉजी का प्राथमिक उद्देश्य क्या है?",
     "Describing people, their biographical attributes, activities, and their social and professional relationships to other people and organizations",
     "लोगों, उनकी जीवनी संबंधी विशेषताओं, गतिविधियों और अन्य लोगों तथा संगठनों के साथ उनके सामाजिक व व्यावसायिक संबंधों का वर्णन करना",
     ["Cataloging sound recordings of rare classical orchestral musical compositions", "Managing the physical check-in and checkout queues at university circulation desks", "Calculating late fine surcharges for overdue books in school libraries"],
     ["दुर्लभ शास्त्रीय आर्केस्ट्रा संगीत रचनाओं की ध्वनि रिकॉर्डिंग को सूचीबद्ध करना", "विश्वविद्यालय संचलन डेस्क पर भौतिक चेक-इन और चेकआउट कतारों का प्रबंधन करना", "स्कूल पुस्तकालयों में अतिदेय पुस्तकों के लिए विलंब शुल्क अधिभार की गणना करना"],
     "FOAF defines classes like foaf:Person and properties like foaf:name, foaf:mbox, and foaf:knows to describe individuals and social networks in RDF.",
     "FOAF ऑन्टोलॉजी का उपयोग व्यक्तियों (Person), उनके ईमेल, कार्यस्थल और उनके आपसी संपर्कों व सामाजिक संबंधों को सिमेंटिक वेब पर प्रस्तुत करने के लिए किया जाता है।"),

    # 23: Dublin Core in RDF
    ("How is the Dublin Core Metadata Initiative (DCMI) terms namespace represented in RDF statements?",
     "RDF कथनों में डबलिन कोर मेटाडेटा इनिशिएटिव (DCMI) नियम नेमस्पेस का प्रतिनिधित्व कैसे किया जाता है?",
     "http://purl.org/dc/terms/ (often abbreviated with prefix 'dcterms:')",
     "http://purl.org/dc/terms/ (अक्सर प्रीफ़िक्स 'dcterms:' के साथ संक्षिप्त)",
     ["http://www.google.com/dublincore/", "http://loc.gov/standards/dcmi/", "http://w3c.org/metadata/dublin/"],
     ["http://www.google.com/dublincore/", "http://loc.gov/standards/dcmi/", "http://w3c.org/metadata/dublin/"],
     "DCMI Metadata Terms uses persistent URLs (PURLs) under http://purl.org/dc/terms/ to identify properties like dcterms:title, dcterms:creator, and dcterms:issued in RDF.",
     "डबलिन कोर के 15 मूल और विस्तारित तत्वों को RDF में http://purl.org/dc/terms/ नेमस्पेस (dcterms) के तहत वैश्विक यूआरआई के रूप में उपयोग किया जाता है।"),

    # 24: Schema.org origins
    ("Which consortium of major commercial web search engines created 'Schema.org' in 2011 to promote structured data on the web?",
     "वेब पर संरचित डेटा को बढ़ावा देने के लिए 2011 में प्रमुख वाणिज्यिक वेब खोज इंजनों के किस संघ ने 'Schema.org' का निर्माण किया?",
     "Google, Microsoft (Bing), Yahoo!, and Yandex",
     "Google, Microsoft (Bing), Yahoo!, और Yandex",
     ["Apple, IBM, Oracle, and Sun Microsystems", "Facebook, Twitter, LinkedIn, and Instagram", "Cisco, Intel, Qualcomm, and Broadcom"],
     ["Apple, IBM, Oracle, और Sun Microsystems", "Facebook, Twitter, LinkedIn, और Instagram", "Cisco, Intel, Qualcomm, और Broadcom"],
     "Schema.org was launched in June 2011 as a collaborative effort by Google, Bing, Yahoo!, and Yandex to create a single shared schema for structured web data.",
     "Schema.org को 2011 में Google, Microsoft Bing, Yahoo और Yandex द्वारा संयुक्त रूप से लॉन्च किया गया था ताकि वेब पेजों में संरचित स्कीमा मार्कअप जोड़ा जा सके।"),

    # 25: Schema.org for Libraries
    ("Which Schema.org entity type is specifically tailored to describe a physical or public library branch on the web?",
     "कौन सा Schema.org इकाई प्रकार विशेष रूप से वेब पर किसी भौतिक या सार्वजनिक पुस्तकालय शाखा का वर्णन करने के लिए तैयार किया गया है?",
     "schema:Library (a subtype of LocalBusiness and Organization)",
     "schema:Library (LocalBusiness और Organization का एक उप-प्रकार)",
     ["schema:BookstoreChain", "schema:GovernmentWarehouse", "schema:PostalDeliveryCenter"],
     ["schema:BookstoreChain", "schema:GovernmentWarehouse", "schema:PostalDeliveryCenter"],
     "schema:Library allows libraries to publish structured data including opening hours, branch address, contact info, and geolocation directly readable by search engines.",
     "Schema.org में schema:Library का उपयोग पुस्तकालय के पते, खुलने के समय, संपर्क विवरण और भौगोलिक स्थान को सर्च इंजन के लिए संरचित रूप में मार्कअप करने हेतु होता है।"),

    # 26: VIAF (Virtual International Authority File)
    ("What is the primary function of the Virtual International Authority File (VIAF) hosted by OCLC?",
     "OCLC द्वारा होस्ट की गई वर्चुअल इंटरनेशनल अथॉरिटी फाइल (VIAF) का प्राथमिक कार्य क्या है?",
     "Connecting national authority files (from Library of Congress, BnF, DNB, etc.) into a unified, linked open data authority service for authors and creators",
     "विभिन्न राष्ट्रीय प्राधिकरण फ़ाइलों (जैसे LC, BnF, DNB) को लेखकों और रचनाकारों के लिए एक एकीकृत, लिंक्ड ओपन डेटा प्राधिकरण सेवा में जोड़ना",
     ["Selling commercial barcodes and scanner hardware to private corporations", "Archiving pirated full-text digital copies of commercial movies", "Issuing national driving licenses and travel passports to library patrons"],
     ["निजी निगमों को वाणिज्यिक बारकोड और स्कैनर हार्डवेयर बेचना", "वाणिज्यिक फिल्मों की पायरेटेड पूर्ण-पाठ डिजिटल प्रतियों को संग्रहीत करना", "पुस्तकालय संरक्षकों को राष्ट्रीय ड्राइविंग लाइसेंस और यात्रा पासपोर्ट जारी करना"],
     "VIAF clusters name authority records from national libraries worldwide, establishing a single authority cluster URI with linked names across multiple languages and scripts.",
     "VIAF दुनिया भर के राष्ट्रीय पुस्तकालयों की प्राधिकरण फ़ाइलों (जैसे विभिन्न लिपियों में लेखकों के नाम) को एक साथ जोड़कर एक साझा लिंक्ड डेटा यूआरआई प्रदान करता है।"),

    # 27: Wikidata
    ("Why is 'Wikidata' widely recognized as a transformative Knowledge Graph for the library and GLAM community?",
     "'विकिडेटा' (Wikidata) को पुस्तकालय और GLAM समुदाय के लिए एक परिवर्तनकारी नॉलेज ग्राफ़ के रूप में व्यापक रूप से क्यों मान्यता प्राप्त है?",
     "It is a freely accessible, multilingual, collaboratively edited linked knowledge base providing structured data for entities with unique Q-identifiers (e.g. Q42)",
     "यह एक स्वतंत्र रूप से सुलभ, बहुभाषी, सहयोगात्मक रूप से संपादित लिंक्ड ज्ञान का आधार है जो अद्वितीय Q-पहचानकर्ताओं (जैसे Q42) के साथ संस्थाओं के लिए संरचित डेटा प्रदान करता है",
     ["It is a proprietary commercial database charging annual million-dollar licensing subscriptions", "It only allows text written in ancient Latin and ancient Greek languages", "It stores digital backups of computer hardware firmware files exclusively"],
     ["यह एक मालिकाना वाणिज्यिक डेटाबेस है जो वार्षिक मिलियन-डॉलर लाइसेंसिंग शुल्क लेता है", "यह केवल प्राचीन लैटिन और प्राचीन ग्रीक भाषाओं में लिखे गए पाठ की अनुमति देता है", "यह विशेष रूप से कंप्यूटर हार्डवेयर फर्मवेयर फ़ाइलों के डिजिटल बैकअप को संग्रहीत करता है"],
     "Wikidata assigns permanent identifiers (Items like Q42 for Douglas Adams, Properties like P31 for 'instance of') and offers a public SPARQL endpoint (query.wikidata.org).",
     "विकिडेटा विकिमीडिया की खुली लिंक्ड डेटा परियोजना है, जहाँ प्रत्येक व्यक्ति, स्थान या पुस्तक को एक विशिष्ट Q-आइडेंटिफायर मिलता है, जिसे कोई भी SPARQL से क्वेरी कर सकता है।"),

    # 28: DBpedia
    ("What is 'DBpedia' and how is its knowledge graph generated?",
     "'डीबीपीडिया' (DBpedia) क्या है और इसका नॉलेज ग्राफ़ कैसे तैयार किया जाता है?",
     "A community effort that automatically extracts structured information from Wikipedia infoboxes, categories, and links, publishing it as Linked Open Data",
     "एक सामुदायिक प्रयास जो विकिपीडिया इन्फोबॉक्स, श्रेणियों और लिंक्स से संरचित जानकारी को स्वचालित रूप से निकालता है और इसे लिंक्ड ओपन डेटा के रूप में प्रकाशित करता है",
     ["A proprietary database created by commercial encyclopedias to replace public libraries", "An optical character recognition software designed to digitize printed telephone directories", "A hardware firewall appliance manufactured to filter unwanted internet spam emails"],
     ["सार्वजनिक पुस्तकालयों को बदलने के लिए वाणिज्यिक विश्वकोशों द्वारा बनाया गया एक मालिकाना डेटाबेस", "मुद्रित टेलीफोन निर्देशिकाओं को डिजिटाइज़ करने के लिए डिज़ाइन किया गया एक ऑप्टिकल कैरेक्टर रिकग्निशन सॉफ्टवेयर", "अवांछित इंटरनेट स्पैम ईमेल को फ़िल्टर करने के लिए निर्मित एक हार्डवेयर फ़ायरवॉल उपकरण"],
     "DBpedia turns unstructured Wikipedia articles into structured RDF triples, serving as one of the central linking hubs in the Linked Open Data cloud.",
     "DBpedia विकिपीडिया के इन्फोबॉक्स से संरचित डेटा निकालकर उसे RDF ट्रिपल्स में बदल देता है, जो लिंक्ड ओपन डेटा क्लाउड का एक मुख्य केंद्र है।"),

    # 29: id.loc.gov
    ("What is the significance of the Library of Congress Linked Data Service accessible at 'id.loc.gov'?",
     "'id.loc.gov' पर उपलब्ध लाइब्रेरी ऑफ कांग्रेस लिंक्ड डेटा सेवा का क्या महत्व है?",
     "It publishes authoritative library vocabularies including LCSH, LCC, Name Authorities, and MARC codes as open, dereferenceable RDF linked data",
     "यह आधिकारिक पुस्तकालय शब्दावलियों जैसे LCSH, LCC, नाम प्राधिकरण और MARC कोड को खुले, डीरेफ़रेंसेबल RDF लिंक्ड डेटा के रूप में प्रकाशित करता है",
     ["It acts as an online shopping portal selling Library of Congress office furniture", "It streams live radio broadcasts of US congressional legislative debates", "It issues copyright lawsuits against university students borrowing history books"],
     ["यह लाइब्रेरी ऑफ कांग्रेस कार्यालय फर्नीचर बेचने वाले एक ऑनलाइन शॉपिंग पोर्टल के रूप में कार्य करता है", "यह अमेरिकी कांग्रेस की विधायी बहसों के लाइव रेडियो प्रसारण को स्ट्रीम करता है", "यह इतिहास की किताबें उधार लेने वाले विश्वविद्यालय के छात्रों के खिलाफ कॉपीराइट मुकदमे जारी करता है"],
     "id.loc.gov makes standard cataloging vocabularies machine-actionable, providing stable URIs for subject headings like 'Librarianship' or 'Information Science'.",
     "id.loc.gov के माध्यम से लाइब्रेरी ऑफ कांग्रेस ने अपनी सभी प्रमुख शब्दावलियों (LCSH, LCC) को सिमेंटिक वेब पर मुफ्त में यूआरआई के साथ उपलब्ध करा दिया है।"),

    # 30: FAST by OCLC
    ("What is 'FAST' (Faceted Application of Subject Terminology) developed by OCLC?",
     "OCLC द्वारा विकसित 'FAST' (Faceted Application of Subject Terminology) क्या है?",
     "A simplified, faceted adaptation of Library of Congress Subject Headings (LCSH) designed specifically to function smoothly as Linked Open Data",
     "लाइब्रेरी ऑफ कांग्रेस सब्जेक्ट हेडिंग्स (LCSH) का एक सरलीकृत, फेसेटेड अनुकूलन जो विशेष रूप से लिंक्ड ओपन डेटा के रूप में सुचारू रूप से कार्य करने के लिए डिज़ाइन किया गया है",
     ["A high-speed optical fiber cable connecting public libraries across North America", "A proprietary sorting algorithm used inside automated book drop machines", "A rapid book repair adhesive formula used in paper conservation laboratories"],
     ["उत्तरी अमेरिका के सार्वजनिक पुस्तकालयों को जोड़ने वाली एक उच्च गति ऑप्टिकल फाइबर केबल", "स्वचालित पुस्तक ड्रॉप मशीनों के अंदर उपयोग किया जाने वाला एक मालिकाना सॉर्टिंग एल्गोरिदम", "कागज़ संरक्षण प्रयोगशालाओं में उपयोग किया जाने वाला एक तीव्र पुस्तक मरम्मत चिपकने वाला सूत्र"],
     "FAST breaks complex pre-coordinated LCSH strings into 8 distinct facets (Personal, Corporate, Event, Title, Uniform, Topical, Geographic, Chronological, Form) with URIs.",
     "FAST ने जटिल LCSH शीर्षकों को 8 अलग-अलग स्वतंत्र पहलुओं (Facets) में बांट दिया है, जिससे उन्हें लिंक्ड डेटा के रूप में जोड़ना और खोजना बेहद आसान हो गया है।"),

    # 31: ISNI (ISO 27729)
    ("What is the 'ISNI' (International Standard Name Identifier - ISO 27729) and how is it used in linked data?",
     "'ISNI' (इंटरनेशनल स्टैंडर्ड नेम आइडेंटिफ़ायर - ISO 27729) क्या है और लिंक्ड डेटा में इसका उपयोग कैसे किया जाता है?",
     "A 16-digit globally unique identifier that persistently resolves the public identities of contributors (authors, researchers, musicians, organizations)",
     "एक 16-अंकीय विश्व स्तर पर अद्वितीय पहचानकर्ता जो योगदानकर्ताओं (लेखकों, शोधकर्ताओं, संगीतकारों, संगठनों) की सार्वजनिक पहचान को स्थायी रूप से हल करता है",
     ["A serial barcode number stamped on physical library catalog card trays", "An encrypted computer password required to log into university WiFi routers", "A 10-digit international standard number used exclusively for serial periodicals"],
     ["भौतिक पुस्तकालय कैटलॉग कार्ड ट्रे पर मुहर लगी एक सीरियल बारकोड संख्या", "विश्वविद्यालय वाईफाई राउटर में लॉग इन करने के लिए आवश्यक एक एन्क्रिप्टेड कंप्यूटर पासवर्ड", "विशेष रूप से धारावाहिक पत्रिकाओं के लिए उपयोग की जाने वाली 10-अंकीय अंतरराष्ट्रीय मानक संख्या"],
     "ISNI uniquely identifies creators across media and industries, bridging libraries, academic publishing (ORCID uses ISNI format), music, and digital rights management.",
     "ISNI (ISO 27729) एक 16 अंकों की वैश्विक पहचान संख्या है जो दुनिया भर के लेखकों, कलाकारों और शोधकर्ताओं की पहचान को बिना किसी भ्रम के स्पष्ट करती है।"),

    # 32: Protégé ontology editor
    ("Which open-source ontology editor developed by Stanford University is widely used worldwide for creating and managing OWL and RDF ontologies?",
     "स्टैनफोर्ड यूनिवर्सिटी द्वारा विकसित कौन सा ओपन-सोर्स ऑन्टोलॉजी एडिटर दुनिया भर में OWL और RDF ऑन्टोलॉजी बनाने और प्रबंधित करने के लिए व्यापक रूप से उपयोग किया जाता है?",
     "Protégé",
     "प्रोटेजी (Protégé)",
     ["GIMP Photo Editor", "Audacity Audio Studio", "Blender 3D Suite"],
     ["गिम्प फोटो एडिटर", "ऑडेसिटी ऑडियो स्टूडियो", "ब्लेंडर 3D सूट"],
     "Protégé is the world's leading open-source platform for ontology modeling, knowledge-base construction, and description-logic reasoning visualization.",
     "Protégé स्टैनफोर्ड विश्वविद्यालय द्वारा विकसित सबसे लोकप्रिय ओपन-सोर्स सॉफ्टवेयर है जिसका उपयोग सिमेंटिक वेब के लिए ऑन्टोलॉजी और ज्ञान मॉडल बनाने में होता है।"),

    # 33: Triple Store
    ("In database terminology, what is a 'Triple Store' (Graph Database)?",
     "डेटाबेस शब्दावली में 'ट्रिपल स्टोर' (ग्राफ़ डेटाबेस) क्या है?",
     "A specialized database purpose-built for the storage, indexing, and retrieval of semantic data structured as RDF triples through SPARQL queries",
     "एक विशेष डेटाबेस जो विशेष रूप से SPARQL प्रश्नों के माध्यम से RDF ट्रिपल्स के रूप में संरचित सिमेंटिक डेटा के भंडारण, अनुक्रमण और पुनर्प्राप्ति के लिए बनाया गया है",
     ["A warehouse that stores exactly three identical printed copies of every novel", "A relational database that only permits tables with three columns", "A computer floppy disk capable of holding three text documents simultaneously"],
     ["एक गोदाम जो प्रत्येक उपन्यास की ठीक तीन समान मुद्रित प्रतियों को संग्रहीत करता है", "एक रिलेशनल डेटाबेस जो केवल तीन कॉलम वाली तालिकाओं की अनुमति देता है", "एक कंप्यूटर फ़्लॉपी डिस्क जो एक साथ तीन टेक्स्ट दस्तावेज़ रखने में सक्षम है"],
     "Leading triple stores include Apache Jena Fuseki, OpenLink Virtuoso, Ontotext GraphDB, Stardog, and Blazegraph.",
     "ट्रिपल स्टोर एक विशेष डेटाबेस होता है जो तालिकाओं (tables) के बजाय RDF ट्रिपल्स (सब्जेक्ट-प्रेडिकेट-ऑब्जेक्ट) को स्टोर करता है और SPARQL का समर्थन करता है।"),

    # 34: Apache Jena
    ("What is 'Apache Jena' in the Semantic Web development ecosystem?",
     "सिमेंटिक वेब विकास पारिस्थितिकी तंत्र में 'अपाचे जेना' (Apache Jena) क्या है?",
     "An open-source Java framework providing an RDF API, SPARQL query engine (ARQ), reasoning subsystem, and triple store server (Fuseki)",
     "एक ओपन-सोर्स जावा फ्रेमवर्क जो RDF API, SPARQL क्वेरी इंजन (ARQ), रीज़निंग सबसिस्टम और ट्रिपल स्टोर सर्वर (Fuseki) प्रदान करता है",
     ["A proprietary commercial word processor designed for compiling doctoral dissertations", "An audio driver utility used to connect electronic microphones to computer speakers", "A web browser plugin that disables all hypertext links on university library portals"],
     ["डॉक्टरेट शोध प्रबंधों को संकलित करने के लिए डिज़ाइन किया गया एक मालिकाना वाणिज्यिक वर्ड प्रोसेसर", "कंप्यूटर स्पीकरों से इलेक्ट्रॉनिक माइक्रोफ़ोन को जोड़ने के लिए उपयोग की जाने वाली एक ऑडियो ड्राइवर उपयोगिता", "एक वेब ब्राउज़र प्लगइन जो विश्वविद्यालय पुस्तकालय पोर्टलों पर सभी हाइपरटेक्स्ट लिंक को अक्षम करता है"],
     "Apache Jena is the foundational open-source Java toolkit for building Semantic Web and Linked Data applications.",
     "Apache Jena एक प्रमुख ओपन-सोर्स जावा फ्रेमवर्क है जिसमें RDF डेटा को पढ़ने, लिखने, स्टोर करने (Fuseki) और SPARQL क्वेरी चलाने के सभी टूल्स उपलब्ध हैं।"),

    # 35: Semantic Reasoners
    ("What is the function of a 'Semantic Reasoner' (inference engine) such as HermiT, Pellet, or FaCT++?",
     "हर्मिट (HermiT), पेलेट (Pellet) या FaCT++ जैसे 'सिमेंटिक रीज़नर्स' (अनुमान इंजन) का क्या कार्य है?",
     "Inferring logical consequences, discovering implicit relationships, and detecting logical contradictions within an ontology based on formal rules",
     "औपचारिक नियमों के आधार पर ऑन्टोलॉजी के भीतर तार्किक परिणामों का अनुमान लगाना, अंतर्निहित संबंधों की खोज करना और तार्किक अंतर्विरोधों का पता लगाना",
     ["Compressing high-definition video files into micro-thumbnails for catalog displays", "Calculating library overdue fine penalties and issuing automated bank invoices", "Scanning paper documents for ink stains and paper tears before binding"],
     ["कैटलॉग डिस्प्ले के लिए हाई-डेफिनिशन वीडियो फ़ाइलों को माइक्रो-थंबनेल में संपीड़ित करना", "पुस्तकालय अतिदेय जुर्माना दंड की गणना करना और स्वचालित बैंक चालान जारी करना", "बाइंडिंग से पहले स्याही के दाग और कागज़ के फटने के लिए कागज़ के दस्तावेजों को स्कैन करना"],
     "Reasoners process OWL axioms to infer unstated truths (e.g., if A is parent of B and B is parent of C, inferring that A is grandparent of C) and verify consistency.",
     "रीज़नर (Reasoner) ऑन्टोलॉजी के नियमों का विश्लेषण करके नए अप्रत्यक्ष निष्कर्ष निकालता है और यह जांचता है कि डेटा में कोई तार्किक विरोधाभास तो नहीं है।"),

    # 36: Linked Data 4 Principles
    ("Which of the following is NOT one of the Four Linked Data Principles outlined by Tim Berners-Lee in 2006?",
     "2006 में टिम बर्नर्स-ली द्वारा उल्लिखित चार लिंक्ड डेटा सिद्धांतों में से कौन सा एक नहीं है?",
     "Data must be encrypted behind proprietary corporate firewalls accessible only through paid API licenses",
     "डेटा को मालिकाना कॉर्पोरेट फ़ायरवॉल के पीछे एन्क्रिप्ट किया जाना चाहिए जो केवल सशुल्क एपीआई लाइसेंस के माध्यम से सुलभ हो",
     ["Use URIs as names for things", "Use HTTP URIs so that people and machines can look up those names", "When someone looks up a URI, provide useful information using open standards (RDF, SPARQL) and include links to other URIs"],
     ["चीजों के नाम के रूप में यूआरआई (URIs) का उपयोग करें", "HTTP URIs का उपयोग करें ताकि लोग और मशीनें उन नामों को देख सकें", "जब कोई यूआरआई देखता है, तो खुले मानकों (RDF, SPARQL) का उपयोग करके उपयोगी जानकारी प्रदान करें और अन्य यूआरआई के लिंक शामिल करें"],
     "Tim Berners-Lee's 4 principles mandate open, accessible HTTP URIs and interconnected links to expand the global web of data, completely opposite of proprietary paywalls.",
     "टिम बर्नर्स-ली के 4 सिद्धांत कहते हैं: 1. चीजों के लिए URI इस्तेमाल करें; 2. HTTP URI रखें; 3. मानक RDF जानकारी दें; 4. अन्य डेटा के लिंक्स जोड़ें। सशुल्क दीवारें इसके विरुद्ध हैं।"),

    # 37: Dereferenceable URI
    ("In the Semantic Web, what is meant by a 'Dereferenceable URI'?",
     "सिमेंटिक वेब में 'डीरेफ़रेंसेबल यूआरआई' (Dereferenceable URI) से क्या तात्पर्य है?",
     "A URI using the HTTP protocol that, when requested over the network, successfully returns a meaningful representation describing the identified entity",
     "HTTP प्रोटोकॉल का उपयोग करने वाला एक यूआरआई, जिसे नेटवर्क पर अनुरोध किए जाने पर, पहचानी गई इकाई का वर्णन करने वाला एक सार्थक विवरण सफलतापूर्वक प्राप्त होता है",
     ["A broken link that intentionally redirects users to an HTTP 404 error page", "A web address that permanently deletes the user's internet browsing history", "A private local IP address that can only be accessed within an offline intranet server"],
     ["एक टूटा हुआ लिंक जो जानबूझकर उपयोगकर्ताओं को HTTP 404 त्रुटि पृष्ठ पर पुनर्निर्देशित करता है", "एक वेब पता जो उपयोगकर्ता के इंटरनेट ब्राउज़िंग इतिहास को स्थायी रूप से हटा देता है", "एक निजी स्थानीय आईपी पता जिसे केवल एक ऑफ़लाइन इंट्रानेट सर्वर के भीतर ही एक्सेस किया जा सकता है"],
     "Dereferencing means an application can send an HTTP GET request to the URI and receive back structured RDF data or HTML explaining what that URI represents.",
     "डीरेफ़रेंसेबल यूआरआई का मतलब है कि जब कोई ब्राउज़र या प्रोग्राम उस यूआरआई पर HTTP अनुरोध भेजता है, तो सर्वर उस संसाधन की पूरी जानकारी लौटाता है।"),

    # 38: Content Negotiation (ConNeg)
    ("How does 'Content Negotiation' (ConNeg) operate when resolving Linked Data URIs?",
     "लिंक्ड डेटा यूआरआई को हल करते समय 'कंटेंट नेगोशिएशन' (Content Negotiation - ConNeg) कैसे काम करता है?",
     "The web server inspects the client's HTTP 'Accept' header and delivers HTML for human web browsers, or RDF/Turtle/JSON-LD for automated software agents",
     "वेब सर्वर क्लाइंट के HTTP 'Accept' हेडर की जांच करता है और मानव वेब ब्राउज़रों के लिए HTML, या स्वचालित सॉफ्टवेयर एजेंटों के लिए RDF/Turtle/JSON-LD प्रदान करता है",
     ["The server negotiates a commercial pricing subscription before downloading any file", "The server translates English text into Latin before saving database records", "The server adjusts screen brightness depending on ambient room lighting conditions"],
     ["सर्वर किसी भी फ़ाइल को डाउनलोड करने से पहले एक वाणिज्यिक मूल्य निर्धारण सदस्यता पर बातचीत करता है", "सर्वर डेटाबेस रिकॉर्ड सहेजने से पहले अंग्रेजी पाठ का लैटिन में अनुवाद करता है", "सर्वर कमरे की रोशनी की स्थिति के आधार पर स्क्रीन की चमक को समायोजित करता है"],
     "Content negotiation allows a single URI to serve both human readers (displaying an attractive webpage) and software algorithms (serving raw RDF triples).",
     "कंटेंट नेगोशिएशन के जरिए सर्वर पहचान लेता है कि रिक्वेस्ट इंसान के ब्राउज़र से आई है (तो सुंदर HTML पेज दिखाता है) या कंप्यूटर प्रोग्राम से (तो RDF/JSON डेटा देता है)।"),

    # 39: Europeana Data Model (EDM)
    ("What is the 'Europeana Data Model' (EDM) designed for in the GLAM and digital library domain?",
     "GLAM और डिजिटल पुस्तकालय क्षेत्र में 'यूरोपाना डेटा मॉडल' (EDM) किसके लिए डिज़ाइन किया गया है?",
     "An open, RDF-based metadata framework capable of aggregating, harmonizing, and interconnecting diverse cultural heritage objects across European museums, libraries, and archives",
     "एक खुला, RDF-आधारित मेटाडेटा ढांचा जो यूरोपीय संग्रहालयों, पुस्तकालयों और अभिलेखागारों में विविध सांस्कृतिक विरासत वस्तुओं को एकत्रित, सामंजस्यपूर्ण और आपस में जोड़ने में सक्षम है",
     ["A billing software designed to collect television licensing taxes across the European Union", "A proprietary security protocol used by European commercial banking networks", "A hardware standard for European railway locomotive signaling systems"],
     ["यूरोपीय संघ में टेलीविज़न लाइसेंसिंग कर एकत्र करने के लिए डिज़ाइन किया गया एक बिलिंग सॉफ्टवेयर", "यूरोपीय वाणिज्यिक बैंकिंग नेटवर्क द्वारा उपयोग किया जाने वाला एक मालिकाना सुरक्षा प्रोटोकॉल", "यूरोपीय रेलवे लोकोमोटिव सिग्नलिंग सिस्टम के लिए एक हार्डवेयर मानक"],
     "EDM bridges different descriptive standards (Dublin Core, MARC, EAD, LIDO) using Semantic Web ontologies to deliver a unified discovery platform.",
     "EDM (यूरोपाना डेटा मॉडल) विभिन्न पुस्तकालयों, अभिलेखागारों और संग्रहालयों के डेटा (मार्क्स, डबलिन कोर आदि) को सिमेंटिक वेब के जरिए एक साथ जोड़ता है।"),

    # 40: DPLA Linked Data Profile
    ("How does the Digital Public Library of America (DPLA) structure its aggregated cultural metadata?",
     "डिजिटल पब्लिक लाइब्रेरी ऑफ अमेरिका (DPLA) अपने एकत्रित सांस्कृतिक मेटाडेटा को कैसे संरचित करता है?",
     "Using an RDF application profile inspired by the Europeana Data Model (EDM) and serialized in JSON-LD",
     "यूरोपाना डेटा मॉडल (EDM) से प्रेरित और JSON-LD में क्रमबद्ध एक RDF एप्लिकेशन प्रोफ़ाइल का उपयोग करके",
     ["Using legacy unindexed Microsoft Access database tables (.MDB files)", "Using static non-searchable PDF image scans stored on tape cartridges", "Using proprietary encrypted CD-ROM disc files with custom viewing software"],
     ["विरासत अप्रक्रमित माइक्रोसॉफ्ट एक्सेस डेटाबेस टेबल (.MDB फ़ाइलें) का उपयोग करके", "टेप कार्ट्रिज पर संग्रहीत स्थिर गैर-खोज योग्य पीडीएफ छवि स्कैन का उपयोग करके", "कस्टम देखने वाले सॉफ्टवेयर के साथ मालिकाना एन्क्रिप्टेड सीडी-रोम डिस्क फ़ाइलों का उपयोग करके"],
     "DPLA aggregates millions of items from US libraries and archives using an EDM-based Linked Data model serialized in JSON-LD with a public API.",
     "DPLA पूरे अमेरिका के पुस्तकालयों और संग्रहालयों के करोड़ों दस्तावेजों को EDM पर आधारित JSON-LD लिंक्ड डेटा मॉडल के माध्यम से जोड़ता है।"),

    # 41: CIDOC CRM (ISO 21127)
    ("What is 'CIDOC CRM' (ISO 21127) and what is its core design paradigm?",
     "'सीआईडीओसी सीआरएम' (CIDOC CRM - ISO 21127) क्या है और इसका मुख्य डिज़ाइन प्रतिमान क्या है?",
     "An event-centric formal ontology developed for the semantic integration and documentation of cultural heritage and museum collections",
     "सांस्कृतिक विरासत और संग्रहालय संग्रहों के सिमेंटिक एकीकरण और प्रलेखन के लिए विकसित एक घटना-केंद्रित (event-centric) औपचारिक ऑन्टोलॉजी",
     ["A customer relationship management software designed to sell commercial software licenses", "A book binding specification standard for paperback academic textbooks", "An algorithm for calculating late book return fines at public library checkout counters"],
     ["वाणिज्यिक सॉफ्टवेयर लाइसेंस बेचने के लिए डिज़ाइन किया गया एक ग्राहक संबंध प्रबंधन सॉफ्टवेयर", "पेपरबैक अकादमिक पाठ्यपुस्तकों के लिए एक पुस्तक बाइंडिंग विनिर्देश मानक", "सार्वजनिक पुस्तकालय चेकआउट काउंटरों पर देर से पुस्तक वापसी के जुर्माने की गणना के लिए एक एल्गोरिदम"],
     "CIDOC CRM models cultural heritage around 'Events' that link actors, places, times, and material objects together.",
     "CIDOC CRM (ISO 21127) संग्रहालयों और सांस्कृतिक विरासत के लिए एक अंतरराष्ट्रीय ऑन्टोलॉजी है, जो सभी ऐतिहासिक वस्तुओं को 'घटनाओं' (Events) के माध्यम से जोड़ती है।"),

    # 42: FRBRoo
    ("What is 'FRBRoo' (Functional Requirements for Bibliographic Records - Object Oriented)?",
     "'FRBRoo' (ग्रंथसूची रिकॉर्ड के लिए कार्यात्मक आवश्यकताएं - ऑब्जेक्ट ओरिएंटेड) क्या है?",
     "An ontological harmonization that blends the library FRBR entity-relationship model with the museum CIDOC CRM event-centric ontology",
     "एक ऑन्टोलॉजिकल सामंजस्य जो पुस्तकालय FRBR इकाई-संबंध मॉडल को संग्रहालय CIDOC CRM घटना-केंद्रित ऑन्टोलॉजी के साथ मिश्रित करता है",
     ["A computer game developed to teach school children basic alphabet typing skills", "An open-source desktop operating system designed to replace Microsoft Windows in libraries", "A robotic hardware scanner designed to turn physical catalog cards into plastic tokens"],
     ["स्कूली बच्चों को बुनियादी वर्णमाला टाइपिंग कौशल सिखाने के लिए विकसित एक कंप्यूटर गेम", "पुस्तकालयों में माइक्रोसॉफ्ट विंडोज को बदलने के लिए डिज़ाइन किया गया एक ओपन-सोर्स डेस्कटॉप ऑपरेटिंग सिस्टम", "एक रोबोटिक हार्डवेयर स्कैनर जिसे भौतिक कैटलॉग कार्ड को प्लास्टिक टोकन में बदलने के लिए डिज़ाइन किया गया है"],
     "FRBRoo bridges library cataloging (WEMI) and museum documentation by expressing bibliographic creation and production as temporal events.",
     "FRBRoo पुस्तकालयों के FRBR मॉडल और संग्रहालयों के CIDOC CRM मॉडल का एक संयुक्त रूप है, जो किताबों के निर्माण को ऐतिहासिक घटना के रूप में दर्ज करता है।"),

    # 43: Linked Open Vocabularies (LOV)
    ("What is 'Linked Open Vocabularies' (LOV) in the Semantic Web ecosystem?",
     "सिमेंटिक वेब पारिस्थितिकी तंत्र में 'लिंक्ड ओपन वोकेबुलरीज़' (LOV) क्या है?",
     "A curated registry and search platform that monitors, interlinks, and indexes high-quality reusable RDFS and OWL vocabularies and ontologies",
     "एक क्यूरेटेड रजिस्ट्री और खोज मंच जो उच्च-गुणवत्ता वाले पुन: प्रयोज्य RDFS और OWL शब्दावलियों और ऑन्टोलॉजी की निगरानी, इंटरलिंक और अनुक्रमित करता है",
     ["A dating website designed exclusively for university library researchers", "A commercial software license store that sells proprietary font families", "An automated spam email generator that targets academic journal editors"],
     ["विशेष रूप से विश्वविद्यालय के पुस्तकालय शोधकर्ताओं के लिए डिज़ाइन की गई एक डेटिंग वेबसाइट", "एक वाणिज्यिक सॉफ्टवेयर लाइसेंस स्टोर जो मालिकाना फ़ॉन्ट परिवार बेचता है", "एक स्वचालित स्पैम ईमेल जनरेटर जो अकादमिक जर्नल संपादकों को लक्षित करता है"],
     "LOV (lov.linkeddata.es) helps ontology developers discover existing terms and avoid reinventing properties, promoting interoperability across knowledge graphs.",
     "LOV एक केंद्रीय खोज मंच और निर्देशिका है जहाँ दुनिया भर में बनी सभी प्रमाणित RDF/OWL शब्दावलियों और ऑन्टोलॉजी को खोजा और पुन: उपयोग किया जा सकता है।"),

    # 44: PROV-O Ontology
    ("What is the primary function of the W3C 'PROV-O' (Provenance Ontology)?",
     "W3C 'PROV-O' (प्रोवेनेंस ऑन्टोलॉजी) का प्राथमिक कार्य क्या है?",
     "Providing a standardized set of classes and properties to model the provenance, history, origin, and stewardship of digital entities and data",
     "डिजिटल संस्थाओं और डेटा के उद्गम, इतिहास, उत्पत्ति और प्रबंधन को मॉडल करने के लिए क्लास और गुणधर्मों का एक मानकीकृत सेट प्रदान करना",
     ["Calculating printer ink density when printing high-resolution color maps", "Managing air conditioning humidity levels inside rare document display glass cases", "Scheduling custodial staff cleaning shifts across university campus libraries"],
     ["उच्च-रिज़ॉल्यूशन रंगीन मानचित्रों को प्रिंट करते समय प्रिंटर स्याही घनत्व की गणना करना", "दुर्लभ दस्तावेज़ प्रदर्शन ग्लास केस के अंदर एयर कंडीशनिंग आर्द्रता के स्तर का प्रबंधन करना", "विश्वविद्यालय परिसर के पुस्तकालयों में सफाई कर्मचारियों की सफाई शिफ्ट का समय निर्धारित करना"],
     "PROV-O defines core classes (prov:Entity, prov:Activity, prov:Agent) and relations (prov:wasGeneratedBy, prov:wasAttributedTo) to capture authoritative lineage.",
     "PROV-O ऑन्टोलॉजी यह दर्ज करने के लिए बनाई गई है कि कोई डिजिटल डेटा कहाँ से उत्पन्न हुआ, किसने बनाया, उसमें क्या संशोधन हुए और उसका इतिहास क्या रहा है।"),

    # 45: Linked Data Licensing
    ("Why is the Creative Commons Zero (CC0) Public Domain Dedication recommended as best practice for publishing Linked Open Data?",
     "लिंक्ड ओपन डेटा प्रकाशित करने के लिए क्रिएटिव कॉमन्स ज़ीरो (CC0) पब्लिक डोमेन समर्पण को सर्वोत्तम अभ्यास के रूप में क्यों अनुशंसित किया जाता है?",
     "It waives all copyright restrictions worldwide, eliminating legal friction and attribution stacking when millions of linked data triples from different sources are merged",
     "यह दुनिया भर में सभी कॉपीराइट प्रतिबंधों को माफ करता है, कानूनी बाधाओं को समाप्त करता है जब विभिन्न स्रोतों से लाखों लिंक्ड डेटा ट्रिपल्स को आपस में जोड़ा जाता है",
     ["It forces commercial search engines to pay mandatory royalty fees to library catalogers", "It locks database triples inside an encrypted container that expires after thirty days", "It requires every library patron to sign a legal non-disclosure affidavit before searching"],
     ["यह वाणिज्यिक खोज इंजनों को पुस्तकालय कैटलॉगर्स को अनिवार्य रॉयल्टी शुल्क का भुगतान करने के लिए मजबूर करता है", "यह डेटाबेस ट्रिपल्स को एक एन्क्रिप्टेड कंटेनर के अंदर बंद कर देता है जो तीस दिनों के बाद समाप्त हो जाता है", "खोजने से पहले प्रत्येक पुस्तकालय संरक्षक को एक कानूनी गैर-प्रकटीकरण हलफनामे पर हस्ताक्षर करने की आवश्यकता होती है"],
     "When combining RDF graphs from thousands of open datasets, attribution requirements (like CC-BY) create legally impossible 'attribution stacking'; CC0 allows seamless semantic federation.",
     "जब विभिन्न स्रोतों के करोड़ों ट्रिपल्स को एक साथ मिलाकर नॉलेज ग्राफ बनता है, तो CC0 लाइसेंस सबसे उपयुक्त होता है ताकि एट्रिब्यूशन का कोई कानूनी झंझट न रहे।"),

    # 46: Knowledge Graph in Discovery
    ("How does modern library discovery software leverage Knowledge Graphs and Linked Data to improve user search experience?",
     "आधुनिक पुस्तकालय खोज सॉफ्टवेयर उपयोगकर्ता खोज अनुभव को बेहतर बनाने के लिए नॉलेज ग्राफ़ और लिंक्ड डेटा का लाभ कैसे उठाता है?",
     "By generating exploratory 'knowledge panels', displaying related subjects, author biographical context, and recommending connected works across disciplines",
     "खोजबीन संबंधी 'नॉलेज पैनल' बनाकर, संबंधित विषयों को प्रदर्शित करके, लेखक की जीवनी का संदर्भ देकर और विभिन्न विषयों में जुड़ी कृतियों की सिफारिश करके",
     ["By replacing all search results with commercial banner ads for luxury consumer electronics", "By automatically locking out any user who enters an incorrectly spelled search query", "By restricting search access exclusively to patrons physically located inside the library basement"],
     ["लक्जरी उपभोक्ता इलेक्ट्रॉनिक्स के लिए वाणिज्यिक बैनर विज्ञापनों के साथ सभी खोज परिणामों को बदलकर", "गलत वर्तनी वाली खोज क्वेरी दर्ज करने वाले किसी भी उपयोगकर्ता को स्वचालित रूप से लॉक करके", "खोज पहुंच को विशेष रूप से पुस्तकालय के बेसमेंट के अंदर भौतिक रूप से स्थित संरक्षकों तक सीमित करके"],
     "Linked data powers dynamic entity panels (similar to Google Knowledge Graph) in modern discovery layers, helping researchers traverse from an author to their co-authors, subjects, and related works.",
     "नॉलेज ग्राफ के जरिए पुस्तकालय सर्च में भी गूगल जैसा 'नॉलेज पैनल' दिखता है, जहाँ लेखक की तस्वीर, जीवनी, उनके समकालीन विद्वान और संबंधित किताबें एक क्लिक पर मिल जाती हैं।"),

    # 47: Linked Data and RDA
    ("How does the Resource Description and Access (RDA) standard align with Semantic Web architecture?",
     "रिसोर्स डिस्क्रिप्शन एंड एक्सेस (RDA) मानक सिमेंटिक वेब आर्किटेक्चर के साथ कैसे संरेखित होता है?",
     "RDA is mapped to formal RDF element sets and value vocabularies with persistent URIs hosted on the RDA Registry (rdaregistry.info)",
     "RDA को RDA रजिस्ट्री (rdaregistry.info) पर होस्ट किए गए स्थायी यूआरआई के साथ औपचारिक RDF तत्व सेट और मान शब्दावलियों में मैप किया गया है",
     ["RDA forbids the use of any electronic computers in cataloging departments", "RDA requires all catalog records to be written exclusively with mechanical typewriters", "RDA completely abolishes the use of International Standard Book Numbers (ISBN)"],
     ["RDA कैटलॉगिंग विभागों में किसी भी इलेक्ट्रॉनिक कंप्यूटर के उपयोग पर रोक लगाता है", "RDA की आवश्यकता है कि सभी कैटलॉग रिकॉर्ड विशेष रूप से मैकेनिकल टाइपराइटर से लिखे जाएं", "RDA इंटरनेशनल स्टैंडर्ड बुक नंबर (ISBN) के उपयोग को पूरी तरह से समाप्त कर देता है"],
     "The Open Metadata Registry hosts RDA element sets (e.g., rda:creator, rda:expressionOf) enabling cataloging data created under RDA to be seamlessly published as RDF Linked Data.",
     "RDA मानक को सिमेंटिक वेब के अनुकूल बनाया गया है; rdaregistry.info पर RDA के सभी तत्वों के लिए स्थायी यूआरआई उपलब्ध हैं ताकि कैटलॉग सीधे RDF में बदल सके।"),

    # 48: 5 Laws of LIS & Semantic Web
    ("How does the Semantic Web and Linked Open Data most directly fulfill S. R. Ranganathan's Fourth Law of Library Science ('Save the Time of the Reader')?",
     "सिमेंटिक वेब और लिंक्ड ओपन डेटा सबसे सीधे डॉ. एस. आर. रंगनाथन के पुस्तकालय विज्ञान के चौथे नियम ('पाठक का समय बचाएं') को कैसे पूरा करते हैं?",
     "By breaking down institutional data silos, enabling seamless machine-to-machine knowledge discovery, and delivering direct contextual answers across global networks in milliseconds",
     "संस्थागत डेटा साइलो को तोड़कर, सहज मशीन-से-मशीन ज्ञान खोज को सक्षम करके, और मिलीसेकंड में वैश्विक नेटवर्क में सीधे प्रासंगिक उत्तर देकर",
     ["By forcing readers to manually walk to every national library across the globe to view paper records", "By making all catalog systems completely unsearchable without paid commercial passwords", "By reducing library opening hours to fifteen minutes once a week"],
     ["कागज़ के रिकॉर्ड देखने के लिए पाठकों को दुनिया भर के हर राष्ट्रीय पुस्तकालय में व्यक्तिगत रूप से जाने के लिए मजबूर करके", "सशुल्क वाणिज्यिक पासवर्ड के बिना सभी कैटलॉग प्रणालियों को पूरी तरह से गैर-खोज योग्य बनाकर", "सप्ताह में एक बार पुस्तकालय खुलने के समय को घटाकर पंद्रह मिनट करके"],
     "Linked Data interconnects disparate libraries, archives, and repositories into a seamless global web of knowledge, saving researchers immense time and effort.",
     "सिमेंटिक वेब दुनिया भर के पुस्तकालयों के अलग-अलग डेटा को आपस में जोड़ देता है, जिससे पाठक को एक ही खोज में संपूर्ण प्रासंगिक ज्ञान तुरंत मिल जाता है और उसका कीमती समय बचता है।")
]

print(f"Total Q95 items: {len(q95_items)}")
assert len(q95_items) == 48

with open("build_u5_q95.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nSlot Q95: Semantic Web & Linked Open Data (LOD) - 48 items.\n"""\n\n')
    f.write("q95_pool = [\n")
    for item in q95_items:
        f.write(f"    {repr(item)},\n")
    f.write("]\n")
    f.write("print('Q95 loaded, count:', len(q95_pool))\n")

print("Created build_u5_q95.py successfully!")
