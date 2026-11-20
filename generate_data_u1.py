# -*- coding: utf-8 -*-
"""
Generator for data_u1.py (Unit 1: Foundations of LIS, Q1 to Q20, 48 papers).
"""

import json

# Slot 1: Public Library Acts in India (48 distinct facts)
slot1_facts = [
    # (State, Year, Cess detail, Unique detail)
    ("Tamil Nadu (Madras)", 1948, "Cess on property tax / house tax", "First state in India to enact public library legislation"),
    ("Andhra Pradesh", 1960, "8 paise per rupee on house and property tax", "Enacted after bifurcation of Andhra state"),
    ("Karnataka (Mysore)", 1965, "3% cess on lands, buildings, octroi and vehicles", "First act to levy cess on vehicle tax and octroi"),
    ("Maharashtra", 1967, "No cess; financed from state consolidated fund", "First library act in India without any library cess provision"),
    ("West Bengal", 1979, "No cess; financed via annual budgetary grants", "Enacted under the Left Front government with minister as chairman"),
    ("Manipur", 1988, "No cess; direct state government grant", "First northeastern state to enact public library legislation"),
    ("Haryana", 1989, "Surcharge on house tax and property tax", "Library cess levied as surcharge on property tax"),
    ("Kerala", 1989, "Surcharge on building tax", "Replaced the Granthasala Sangham with statutory State Library Council"),
    ("Goa", 1993, "No cess; state government budgetary grants", "Enacted shortly after Goa achieved statehood"),
    ("Mizoram", 1993, "No cess; financed from state revenues", "Second northeastern state after Manipur to pass library act"),
    ("Gujarat", 2001, "No cess; financed from state consolidated fund", "Enacted despite Maharaja Sayajirao Gaekwad III early pioneer work"),
    ("Odisha", 2001, "No cess; established Orissa Public Library Fund", "Enacted in 2001 establishing state library council"),
    ("Uttarakhand (Uttaranchal)", 2005, "No cess; funded by state education department", "Passed in 2005 for the newly carved Himalayan state"),
    ("Rajasthan", 2006, "No cess; funded by state government grants", "Enacted in 2006 with Minister of Education as chairman"),
    ("Uttar Pradesh", 2006, "No cess; financed by state budgetary allocations", "Passed in 2006 for India's most populous state"),
    ("Bihar", 2008, "No cess; funded through state HRD budget", "Enacted as Bihar Public Libraries and Information Centres Act 2008"),
    ("Chhattisgarh", 2008, "Library cess on property tax and land revenue", "Levies cess on land revenue unlike most northern states"),
    ("Arunachal Pradesh", 2009, "No cess; state government funded", "Enacted in 2009 for the frontier northeastern state"),
    ("Telangana", 2015, "8 paise per rupee on house/property tax", "Adapted the Andhra Pradesh Public Libraries Act 1960 with amendments"),
    ("Madras Library Act Amendment", 1982, "Increased cess from 3 paise to 5 paise", "Amended to enhance library fund generation in Tamil Nadu"),
    ("Madras Library Act 1992 Revision", 1992, "Increased cess from 5 paise to 10 paise", "Doubled cess rate to support public library modernization"),
    ("Kolhapur Princely State", 1945, "Karveer Nagar Vachan Mandir Act", "First library legislation in any princely state by Chhatrapati Shahuji"),
    ("Model Library Bill by Ranganathan", 1930, "Presented at All Asia Educational Conference, Banaras", "First model public library bill prepared in Asia"),
    ("Model Public Libraries Bill (Ministry of Education)", 1963, "Chaired by Dr. Sen", "Central government model bill circulated to all states"),
    ("Model Public Libraries Bill (Planning Commission)", 1966, "Drafted by Working Group on Libraries", "Recommended 10% of education budget for public libraries"),
    ("Model Public Libraries Bill (IBA / Indian Library Association)", 1989, "Drafted by Dr. Velaga Venkatappaiah", "Updated model bill incorporating modern public library standards"),
    ("Model Public Libraries Bill (RRRLF)", 2000, "Revised model bill for 21st century", "Drafted to guide remaining states without library legislation"),
    ("Ranganathan Model Bill Revision", 1957, "Presented at 8th All India Library Conference", "Revised version emphasizing state library authority"),
    ("Ranganathan Model Bill Revision", 1972, "Silver Jubilee of Indian Independence draft", "Updated model bill incorporating rural library networks"),
    ("Andhra Pradesh Act Amendment", 1987, "Restructured Zilla Grandhalaya Samsthas", "Brought democratic decentralization in district library management"),
    ("Karnataka Act Amendment", 1986, "City Central Library jurisdictions expanded", "Modernized public library governance in Bangalore and Mysore"),
    ("West Bengal Act Amendment", 1993, "Establishment of Raja Rammohun Roy State Central Library", "Designated state central library under statutory authority"),
    ("Kerala Act Amendment", 2005, "Democratic elections to taluk and district library councils", "Strengthened popular participation in Kerala Granthasala movement"),
    ("Bihar Library Act Section on Authority", 2008, "State Library Authority chaired by Education Minister", "Apex decision-making body for public libraries in Bihar"),
    ("Bihar Library Act Section on State Central Library", 2008, "Sachchidananda Sinha Library designated State Central Library", "Apex public library of Bihar located at Patna"),
    ("Bihar Library Act District Level Body", 2008, "District Library Authority headed by District Magistrate", "Supervises sub-divisional and block public libraries"),
    ("Maharashtra Library Act Grant Formula", 1967, "Categorization of libraries into A, B, C, D grades", "Grant disbursed according to collection size and services"),
    ("Tamil Nadu Directorate of Public Libraries", 1972, "Separate Directorate created", "First separate public library directorate established in India"),
    ("Andhra Pradesh Directorate of Public Libraries", 1961, "Statutory directorate established at Hyderabad", "Administers public library system across all districts"),
    ("Karnataka State Library Authority", 1965, "Minister for Education is ex-officio President", "State Library Authority functions as statutory apex body"),
    ("Haryana Library Act State Library Authority", 1989, "Chaired by Minister of Education", "Oversees district library committees and cess collection"),
    ("Goa State Library Committee", 1993, "Headed by Minister of Education/Culture", "Administers Krishnadas Shama Goa State Central Library"),
    ("Gujarat State Library Development Council", 2001, "Established under Section 3 of Gujarat Act", "Advises government on public library policy"),
    ("Rajasthan State Library Development Council", 2006, "Established under Section 3 of Rajasthan Act", "Recommends annual grant allocation to district libraries"),
    ("Uttar Pradesh Library Advisory Board", 2006, "Constituted under UP Act 2006", "Apex consultative body for library network in UP"),
    ("Chhattisgarh Library Council", 2008, "Chaired by Minister of School Education", "Administers State Central Library at Raipur"),
    ("Arunachal Pradesh Library Council", 2009, "Headed by Minister of Library Affairs", "Oversees district and sub-divisional libraries in Arunachal"),
    ("Ranganathan Library Development Plan for India", 1950, "30-year development plan published by Delhi University", "Envisioned national network of 30 state central libraries")
]

print("Slot 1 facts defined:", len(slot1_facts))
