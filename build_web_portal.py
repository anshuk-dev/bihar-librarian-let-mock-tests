# -*- coding: utf-8 -*-
"""
Web Portal & CBT Online Exam Generator for Bihar Librarian LET 50-Mock Series.
Generates an ultra-responsive, modern single-page portal with:
1. 50 Mock Paper Cards with one-click PDF downloads and Online CBT Test launch buttons.
2. Complete Computer-Based Test (CBT) engine capable of loading any of the 50 papers (150 Qs each).
3. 150-minute live exam timer, section filters, question palette (1-150), language toggles.
4. Comprehensive Scorecard, sectional analysis, and full bilingual review with explanations.
"""

import os
import json
from pypdf import PdfReader

# Collect metadata for all 50 mock papers
papers_data = []
for i in range(1, 51):
    fname = f"Bihar_Librarian_Bilingual_Mock_{i:02d}.pdf"
    size_kb = os.path.getsize(fname) / 1024 if os.path.exists(fname) else 220.0
    try:
        reader = PdfReader(fname)
        pages = len(reader.pages)
    except Exception:
        pages = 35
    papers_data.append({
        "num": i,
        "filename": fname,
        "pages": pages,
        "size_kb": round(size_kb, 1),
        "title_en": f"Bihar Librarian LET Mock Test Paper {i:02d}",
        "title_hi": f"बिहार पुस्तकालय पात्रता परीक्षा मॉडल पेपर {i:02d}",
        "group": (i - 1) // 10 + 1
    })

# Load Paper 01 questions for instant fallback / offline caching
with open("data/paper_01.json", "r", encoding="utf-8") as f:
    paper_01_cache = json.load(f)

print(f"Loaded {len(papers_data)} papers metadata and {len(paper_01_cache)} questions for Paper 01 cache.")

html_content = f'''<!DOCTYPE html>
<html lang="hi" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>बिहार विद्यालय पुस्तकालय पात्रता परीक्षा (LET) 2026 — 50 द्विभाषी मॉक टेस्ट एवं ऑनलाइन CBT टेस्ट</title>
  <meta name="description" content="बिहार विद्यालय परीक्षा समिति (BSEB) एवं BPSC द्वारा आयोजित बिहार पुस्तकालय पात्रता परीक्षा (LET/SLET) हेतु 50 संपूर्ण द्विभाषी (English & Hindi) मॉडल पेपर, लाइव ऑनलाइन CBT टेस्ट तथा पीडीएफ डाउनलोड।">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#eff6ff',
              100: '#dbeafe',
              200: '#bfdbfe',
              500: '#3b82f6',
              600: '#2563eb',
              700: '#1d4ed8',
              800: '#1e40af',
              900: '#1e3a8a',
            }}
          }},
          fontFamily: {{
            sans: ['Inter', 'Noto Sans Devanagari', 'system-ui', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>

  <!-- Google Fonts: Inter & Noto Sans Devanagari -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
    body {{
      font-family: 'Inter', 'Noto Sans Devanagari', system-ui, sans-serif;
    }}
    .cbt-palette-btn {{
      transition: all 0.15s ease-in-out;
    }}
    .cbt-palette-btn:hover {{
      transform: scale(1.08);
    }}
    /* Custom Scrollbar for Palette */
    .custom-scroll::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    .custom-scroll::-webkit-scrollbar-track {{
      background: rgba(0, 0, 0, 0.05);
    }}
    .custom-scroll::-webkit-scrollbar-thumb {{
      background: rgba(0, 0, 0, 0.2);
      border-radius: 4px;
    }}
    /* Pulsing Timer for Final Minutes */
    @keyframes timerPulse {{
      0%, 100% {{ color: #ef4444; transform: scale(1); }}
      50% {{ color: #b91c1c; transform: scale(1.05); }}
    }}
    .timer-warning {{
      animation: timerPulse 1s infinite;
    }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800 dark:bg-slate-950 dark:text-slate-100 min-h-screen flex flex-col antialiased">

  <!-- ================= TOP NAVIGATION BAR ================= -->
  <header class="sticky top-0 z-40 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 transition-colors shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      
      <!-- Brand Logo & Title -->
      <a href="#" class="flex items-center gap-3 group">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-700 via-brand-600 to-indigo-600 flex items-center justify-center text-white shadow-md shadow-brand-500/20 group-hover:scale-105 transition-transform">
          <i class="fa-solid fa-book-open-reader text-lg"></i>
        </div>
        <div>
          <div class="font-extrabold text-slate-900 dark:text-white text-base tracking-tight leading-none flex items-center gap-1.5">
            बिहार LET 2026
            <span class="text-[10px] px-1.5 py-0.5 rounded font-bold uppercase tracking-wider bg-brand-100 text-brand-800 dark:bg-brand-900/60 dark:text-brand-300">CBT Online</span>
          </div>
          <span class="text-xs text-slate-500 dark:text-slate-400 font-medium leading-none">50 Mock Tests • 7,500 MCQs</span>
        </div>
      </a>

      <!-- Navigation Links & Actions -->
      <div class="flex items-center gap-2 sm:gap-4">
        <nav class="hidden md:flex items-center gap-5 text-sm font-semibold">
          <a href="#papers-section" class="text-slate-600 hover:text-brand-600 dark:text-slate-300 dark:hover:text-brand-400 transition-colors">
            <i class="fa-solid fa-layer-group text-xs mr-1"></i> सभी 50 पेपर
          </a>
          <a href="#syllabus-section" class="text-slate-600 hover:text-brand-600 dark:text-slate-300 dark:hover:text-brand-400 transition-colors">
            <i class="fa-solid fa-list-check text-xs mr-1"></i> परीक्षा पैटर्न
          </a>
          <a href="practice/" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-amber-500 hover:bg-amber-600 text-white font-bold text-xs shadow-sm transition-all">
            <i class="fa-solid fa-book-open text-[10px]"></i> 3000 Practice Set
          </a>
          <button onclick="startOnlineTest(1)" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-md shadow-emerald-500/20 transition-all hover:scale-105">
            <i class="fa-solid fa-play text-[10px]"></i> लाइव CBT टेस्ट
          </button>
        </nav>

        <!-- Dark Mode Toggle -->
        <button id="theme-toggle" type="button" class="w-9 h-9 rounded-lg flex items-center justify-center text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors" title="Toggle Dark/Light Mode">
          <i id="theme-icon" class="fa-solid fa-moon text-base"></i>
        </button>

        <!-- GitHub Repo Link -->
        <a href="https://github.com/anshuk-dev/bihar-librarian-let-mock-tests" target="_blank" rel="noopener noreferrer" class="hidden sm:inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-lg bg-slate-900 text-white hover:bg-slate-800 dark:bg-slate-800 dark:hover:bg-slate-700 transition-colors shadow-sm">
          <i class="fa-brands fa-github text-sm"></i>
          <span>GitHub</span>
        </a>
      </div>
    </div>
  </header>

  <!-- ================= HERO SECTION ================= -->
  <section class="relative overflow-hidden bg-gradient-to-b from-blue-50/60 via-indigo-50/40 to-slate-50 dark:from-slate-900 dark:via-slate-950 dark:to-slate-950 pt-10 pb-14 border-b border-slate-200/80 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      
      <!-- Top Authority Badges -->
      <div class="inline-flex flex-wrap items-center justify-center gap-2 mb-4">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-brand-100 text-brand-800 dark:bg-brand-900/60 dark:text-brand-300 shadow-sm">
          <i class="fa-solid fa-award text-brand-600"></i> बिहार विद्यालय परीक्षा समिति (BSEB) & BPSC पैटर्न
        </span>
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 dark:bg-emerald-950/80 dark:text-emerald-300 shadow-sm">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span> 100% निःशुल्क ऑनलाइन CBT टेस्ट व पीडीएफ
        </span>
      </div>

      <!-- Main Heading -->
      <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black text-slate-900 dark:text-white tracking-tight leading-tight max-w-4xl mx-auto">
        बिहार विद्यालय पुस्तकालय पात्रता परीक्षा
        <span class="bg-gradient-to-r from-brand-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent block mt-1">
          50 संपूर्ण द्विभाषी मॉक टेस्ट सीरीज
        </span>
      </h1>

      <!-- Subtitle -->
      <p class="text-slate-600 dark:text-slate-300 text-sm sm:text-base lg:text-lg max-w-3xl mx-auto mt-4 font-medium">
        कुल <strong>7,500 अद्वितीय प्रश्न</strong> (0 दोहराव)। वास्तविक परीक्षा की भांति कंप्यूटर-आधारित ऑनलाइन टेस्ट (CBT) दें अथवा संपूर्ण व्याख्या सहित प्रिंटेबल द्विभाषी पीडीएफ बुकलेट्स डाउनलोड करें।
      </p>

      <!-- Quick Launch Online Test Box -->
      <div class="mt-8 max-w-2xl mx-auto bg-white dark:bg-slate-900 rounded-2xl p-4 sm:p-5 shadow-xl shadow-brand-500/10 border border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row gap-3 items-center justify-between">
        <div class="w-full sm:flex-1 text-left">
          <label for="hero-paper-select" class="block text-xs font-bold text-slate-500 dark:text-slate-400 mb-1">
            <i class="fa-solid fa-laptop-code text-brand-600 mr-1"></i> मॉक टेस्ट पेपर चुनें (Paper 01 to 50):
          </label>
          <select id="hero-paper-select" class="w-full bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-xl px-3 py-2 text-sm font-semibold text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-brand-500">
            {''.join([f'<option value="{p["num"]}">मॉक टेस्ट {p["num"]:02d} — {p["title_en"]} (150 MCQs)</option>' for p in papers_data])}
          </select>
        </div>
        <button onclick="startSelectedHeroPaper()" class="w-full sm:w-auto px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 via-teal-600 to-emerald-700 text-white font-extrabold text-sm shadow-lg shadow-emerald-500/25 hover:shadow-emerald-500/40 hover:scale-105 active:scale-95 transition-all flex items-center justify-center gap-2">
          <i class="fa-solid fa-play"></i>
          <span>ऑनलाइन टेस्ट शुरू करें</span>
        </button>
      </div>

      <!-- Featured Banner for 3000 Core LIS Practice Set Web App -->
      <div class="mt-4 max-w-2xl mx-auto">
        <a href="practice/" class="block bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-700/70 hover:border-amber-500 rounded-xl px-4 py-3 text-left transition-all shadow-sm hover:shadow-md flex items-center justify-between gap-3">
          <div>
            <div class="text-xs sm:text-sm font-extrabold text-amber-900 dark:text-amber-200 flex items-center gap-1.5">
              <span>📖 3,000 Core LIS Practice Set + सही/गलत व्याख्या + Year Chronology (4-Day Revision App)</span>
            </div>
            <div class="text-[11px] sm:text-xs text-amber-800/80 dark:text-amber-300/80 mt-0.5">
              केवल Core Library Science &amp; LIS-IT • चारों विकल्पों की व्याख्या • मोबाइल Focus View
            </div>
          </div>
          <span class="shrink-0 px-3 py-1.5 rounded-lg bg-amber-600 text-white text-xs font-bold">खोलें →</span>
        </a>
      </div>

      <!-- Quick Metrics Row -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-4xl mx-auto mt-10">
        <div class="bg-white dark:bg-slate-900 p-3 sm:p-4 rounded-xl border border-slate-200/80 dark:border-slate-800 shadow-sm">
          <div class="text-2xl sm:text-3xl font-black text-brand-600 dark:text-brand-400">50</div>
          <div class="text-xs font-bold text-slate-500 dark:text-slate-400 mt-0.5">फुल-लेंथ टेस्ट सेट्स</div>
        </div>
        <div class="bg-white dark:bg-slate-900 p-3 sm:p-4 rounded-xl border border-slate-200/80 dark:border-slate-800 shadow-sm">
          <div class="text-2xl sm:text-3xl font-black text-emerald-600 dark:text-emerald-400">7,500</div>
          <div class="text-xs font-bold text-slate-500 dark:text-slate-400 mt-0.5">अद्वितीय MCQs (0% Duplicate)</div>
        </div>
        <div class="bg-white dark:bg-slate-900 p-3 sm:p-4 rounded-xl border border-slate-200/80 dark:border-slate-800 shadow-sm">
          <div class="text-2xl sm:text-3xl font-black text-purple-600 dark:text-purple-400">150 Min</div>
          <div class="text-xs font-bold text-slate-500 dark:text-slate-400 mt-0.5">वास्तविक परीक्षा टाइमर</div>
        </div>
        <div class="bg-white dark:bg-slate-900 p-3 sm:p-4 rounded-xl border border-slate-200/80 dark:border-slate-800 shadow-sm">
          <div class="text-2xl sm:text-3xl font-black text-amber-600 dark:text-amber-400">English + हिन्दी</div>
          <div class="text-xs font-bold text-slate-500 dark:text-slate-400 mt-0.5">पूर्ण मानक व्याख्या सहित</div>
        </div>
      </div>

    </div>
  </section>

  <!-- ================= SYLLABUS & EXAM PATTERN SECTION ================= -->
  <section id="syllabus-section" class="py-12 bg-white dark:bg-slate-900/60 border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-8">
        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white tracking-tight">
          बिहार LET परीक्षा संरचना एवं पाठ्यक्रम (Official Pattern)
        </h2>
        <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1 max-w-2xl mx-auto">
          प्रत्येक टेस्ट पेपर में BSEB एवं BPSC के नवीनतम पाठ्यक्रम के अनुरूप 150 प्रश्न निर्धारित हैं।
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <!-- Part 1 Card -->
        <div class="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-5 border border-slate-200 dark:border-slate-700 shadow-sm">
          <div class="flex items-center justify-between mb-3 border-b border-slate-200 dark:border-slate-700 pb-2">
            <span class="font-extrabold text-sm text-brand-700 dark:text-brand-300 flex items-center gap-2">
              <i class="fa-solid fa-graduation-cap"></i> भाग 1: पुस्तकालय एवं सूचना विज्ञान (LIS)
            </span>
            <span class="px-2.5 py-0.5 bg-brand-100 dark:bg-brand-900/60 text-brand-800 dark:text-brand-200 text-xs font-extrabold rounded-full">
              100 MCQs • 100 अंक
            </span>
          </div>
          <ul class="space-y-2 text-xs sm:text-sm text-slate-700 dark:text-slate-300">
            <li class="flex items-start gap-2">
              <span class="font-bold text-brand-600">Unit 1:</span>
              <span>पुस्तकालय समाज के आधार, 5 सूत्र, पुस्तकालय कानून (बिहार 2008 सहित 19 राज्य), RRRLF, राष्ट्रीय ज्ञान आयोग (NKC)।</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="font-bold text-brand-600">Unit 2:</span>
              <span>ज्ञान संगठन, वर्गीकरण (DDC, CC, UDC), सूचीकरण (AACR-2, CCC, RDA, Dublin Core, MARC21)।</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="font-bold text-brand-600">Unit 3:</span>
              <span>पुस्तकालय प्रबंधन, वैज्ञानिक प्रबंधन, TQM, बजट निर्माण (PPBS, ZBB), परिग्रहण एवं स्टॉक सत्यापन।</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="font-bold text-brand-600">Unit 4:</span>
              <span>सूचना स्रोत एवं सेवाएं (CAS, SDI, ILL), संदर्भ सेवा, ग्रंथसूची, ई-संसाधन एवं शोध कंसोर्टिया (e-ShodhSindhu)।</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="font-bold text-brand-600">Unit 5:</span>
              <span>पुस्तकालय स्वचालन (Koha, SOUL), डिजिटल पुस्तकालय (DSpace), बारकोड/RFID, AI एवं इंटरनेट सुरक्षा।</span>
            </li>
          </ul>
        </div>

        <!-- Part 2 Card -->
        <div class="bg-slate-50 dark:bg-slate-800/60 rounded-2xl p-5 border border-slate-200 dark:border-slate-700 shadow-sm">
          <div class="flex items-center justify-between mb-3 border-b border-slate-200 dark:border-slate-700 pb-2">
            <span class="font-extrabold text-sm text-indigo-700 dark:text-indigo-300 flex items-center gap-2">
              <i class="fa-solid fa-chalkboard-user"></i> भाग 2: शिक्षण कला, सामान्य अध्ययन एवं तार्किक क्षमता
            </span>
            <span class="px-2.5 py-0.5 bg-indigo-100 dark:bg-indigo-900/60 text-indigo-800 dark:text-indigo-200 text-xs font-extrabold rounded-full">
              50 MCQs • 50 अंक
            </span>
          </div>
          <ul class="space-y-2 text-xs sm:text-sm text-slate-700 dark:text-slate-300">
            <li class="flex items-start gap-2">
              <span class="font-bold text-indigo-600">Teaching Aptitude:</span>
              <span>शिक्षण कला, बाल मनोविज्ञान, अधिगम विधियां, कक्षा प्रबंधन, मूल्यांकन एवं मूल्यपरक शिक्षा (30 प्रश्न)।</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="font-bold text-indigo-600">Bihar Special GK:</span>
              <span>बिहार का इतिहास, भूगोल, 1857 की क्रांति, चंपारण सत्याग्रह, बजट, खनिज एवं नदियां (5 प्रश्न)।</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="font-bold text-indigo-600">Indian Polity & Economy:</span>
              <span>भारतीय संविधान, मौलिक अधिकार, संसद, पंचायती राज एवं अर्थव्यवस्था (5 प्रश्न)।</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="font-bold text-indigo-600">General Science & Env:</span>
              <span>दैनिक विज्ञान, पर्यावरण, पारिस्थितिकी तंत्र एवं जलवायु परिवर्तन (5 प्रश्न)।</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="font-bold text-indigo-600">Mathematical Reasoning:</span>
              <span>अंकगणित, कोडिंग-डिकोडिंग, श्रेणी, दिशा ज्ञान एवं तार्किक क्षमता (5 प्रश्न)।</span>
            </li>
          </ul>
        </div>

      </div>

    </div>
  </section>

  <!-- ================= 50 MOCK PAPERS GRID SECTION ================= -->
  <section id="papers-section" class="py-12 bg-slate-100/60 dark:bg-slate-950 flex-1">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 mb-6">
        <div>
          <h2 class="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white tracking-tight">
            सभी 50 मॉक टेस्ट पेपर्स (Mock Tests 01 to 50)
          </h2>
          <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-0.5">
            ऑनलाइन कंप्यूटर-आधारित टेस्ट दें अथवा उच्च-गुणवत्ता वाली पीडीएफ बुकलेट डाउनलोड करें।
          </p>
        </div>

        <!-- Filter Search Bar -->
        <div class="w-full sm:w-72 relative">
          <input type="text" id="paper-search" placeholder="पेपर नंबर या विषय खोजें..." onkeyup="filterPapers()" class="w-full pl-9 pr-4 py-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-700 text-xs sm:text-sm font-semibold focus:outline-none focus:ring-2 focus:ring-brand-500 text-slate-800 dark:text-slate-200">
          <i class="fa-solid fa-magnifying-glass absolute left-3 top-2.5 text-slate-400 text-xs"></i>
        </div>
      </div>

      <!-- Set Filter Tabs -->
      <div class="flex items-center gap-1.5 overflow-x-auto pb-3 mb-6 custom-scroll">
        <button onclick="setTab('all')" id="tab-all" class="tab-btn px-4 py-1.5 rounded-xl text-xs font-bold transition-all bg-brand-600 text-white shadow-sm">सभी 50 पेपर्स</button>
        <button onclick="setTab(1)" id="tab-1" class="tab-btn px-4 py-1.5 rounded-xl text-xs font-bold transition-all bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200">सेट्स 01-10</button>
        <button onclick="setTab(2)" id="tab-2" class="tab-btn px-4 py-1.5 rounded-xl text-xs font-bold transition-all bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200">सेट्स 11-20</button>
        <button onclick="setTab(3)" id="tab-3" class="tab-btn px-4 py-1.5 rounded-xl text-xs font-bold transition-all bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200">सेट्स 21-30</button>
        <button onclick="setTab(4)" id="tab-4" class="tab-btn px-4 py-1.5 rounded-xl text-xs font-bold transition-all bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200">सेट्स 31-40</button>
        <button onclick="setTab(5)" id="tab-5" class="tab-btn px-4 py-1.5 rounded-xl text-xs font-bold transition-all bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200">सेट्स 41-50</button>
      </div>

      <!-- Papers Card Grid (50 items) -->
      <div id="papers-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        {''.join([f'''
        <div class="paper-card bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-4 shadow-sm hover:shadow-md hover:border-brand-300 dark:hover:border-brand-700 transition-all flex flex-col justify-between" data-num="{p['num']}" data-group="{p['group']}">
          <div>
            <div class="flex items-center justify-between mb-2">
              <span class="px-2 py-0.5 rounded-md text-[11px] font-extrabold bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-200 dark:border-brand-800">
                मॉक टेस्ट #{p['num']:02d}
              </span>
              <span class="text-[10px] font-semibold text-slate-400 dark:text-slate-500">
                150 Min • 150 Marks
              </span>
            </div>

            <h3 class="font-bold text-sm text-slate-900 dark:text-white leading-snug line-clamp-1">
              {p['title_en']}
            </h3>
            <p class="text-xs font-medium text-slate-500 dark:text-slate-400 leading-snug mt-0.5 line-clamp-1">
              {p['title_hi']}
            </p>

            <div class="flex flex-wrap items-center gap-1.5 my-3 text-[10px] text-slate-600 dark:text-slate-400 font-semibold">
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800"><i class="fa-solid fa-file-pdf text-red-500 mr-1"></i>{p['pages']} Pages</span>
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800"><i class="fa-solid fa-database text-blue-500 mr-1"></i>{p['size_kb']} KB</span>
              <span class="px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300"><i class="fa-solid fa-check-double mr-1"></i>Bilingual</span>
            </div>
          </div>

          <!-- Card Actions: Online Test & PDF Download -->
          <div class="flex items-center gap-2 pt-2 border-t border-slate-100 dark:border-slate-800 mt-1">
            <button onclick="startOnlineTest({p['num']})" class="flex-1 py-2 px-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white font-bold text-xs shadow-sm hover:shadow-md transition-all flex items-center justify-center gap-1.5" title="ऑनलाइन CBT टेस्ट दें">
              <i class="fa-solid fa-play text-[10px]"></i>
              <span>ऑनलाइन टेस्ट</span>
            </button>
            <a href="{p['filename']}" download="{p['filename']}" class="py-2 px-3 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 font-bold text-xs transition-colors flex items-center justify-center gap-1" title="पीडीएफ डाउनलोड करें">
              <i class="fa-solid fa-download text-xs"></i>
              <span>PDF</span>
            </a>
          </div>
        </div>
        ''' for p in papers_data])}
      </div>

    </div>
  </section>

  <!-- ================= FOOTER ================= -->
  <footer class="bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 py-8 text-center text-xs text-slate-500 dark:text-slate-400">
    <div class="max-w-7xl mx-auto px-4 space-y-2">
      <div class="font-extrabold text-slate-800 dark:text-slate-200 text-sm">
        बिहार विद्यालय पुस्तकालय पात्रता परीक्षा (LET / SLET) 2026 — निःशुल्क शिक्षा पहल
      </div>
      <p>
        प्रस्तुत 50 मॉडल पेपर एवं 7,500 बहुविकल्पीय प्रश्न (MCQs) बिहार के छात्र-छात्राओं के निःशुल्क अभ्यास हेतु पूर्ण प्रामाणिकता के साथ तैयार किए गए हैं।
      </p>
      <div class="flex items-center justify-center gap-4 pt-2 font-semibold">
        <a href="https://github.com/anshuk-dev/bihar-librarian-let-mock-tests" target="_blank" rel="noopener noreferrer" class="hover:text-brand-600 transition-colors">
          <i class="fa-brands fa-github mr-1"></i> GitHub Repository
        </a>
        <span>•</span>
        <a href="#papers-section" class="hover:text-brand-600 transition-colors">
          <i class="fa-solid fa-list-ol mr-1"></i> 50 Mock Papers
        </a>
      </div>
    </div>
  </footer>

  <!-- ================= CBT ONLINE EXAM MODAL / APPLICATION ================= -->
  <div id="cbt-modal" class="fixed inset-0 z-50 hidden bg-slate-900/90 backdrop-blur-md overflow-hidden flex flex-col">
    
    <!-- Loading State Screen -->
    <div id="cbt-view-loading" class="hidden flex-1 flex flex-col items-center justify-center p-6 text-white text-center">
      <div class="w-16 h-16 border-4 border-brand-500 border-t-transparent rounded-full animate-spin mb-4"></div>
      <h3 class="text-xl font-bold" id="loading-title">मॉक टेस्ट लोड हो रहा है...</h3>
      <p class="text-sm text-slate-400 mt-1">150 द्विभाषी प्रश्न एवं व्याख्याएं तैयार की जा रही हैं</p>
    </div>

    <!-- VIEW 1: PRE-EXAM INSTRUCTIONS SCREEN -->
    <div id="cbt-view-instructions" class="flex-1 overflow-y-auto p-4 sm:p-8 flex items-center justify-center">
      <div class="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 max-w-3xl w-full p-6 sm:p-8 shadow-2xl space-y-6">
        
        <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
          <span class="text-xs font-bold uppercase tracking-wider text-brand-600 bg-brand-50 dark:bg-brand-950 px-2.5 py-1 rounded-md">
            Computer-Based Test (CBT) Interface
          </span>
          <h2 class="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white mt-2" id="inst-paper-title">
            बिहार पुस्तकालय पात्रता परीक्षा — मॉक टेस्ट
          </h2>
          <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1">
            कृपया परीक्षा प्रारंभ करने से पूर्व निम्नलिखित सभी निर्देशों को ध्यानपूर्वक पढ़ें।
          </p>
        </div>

        <!-- Exam Scheme Specs -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
          <div class="bg-slate-50 dark:bg-slate-800/80 p-3 rounded-xl border border-slate-200/60 dark:border-slate-700">
            <div class="text-xs text-slate-400 font-semibold">कुल प्रश्न</div>
            <div class="text-lg font-black text-slate-800 dark:text-slate-100">150 MCQs</div>
          </div>
          <div class="bg-slate-50 dark:bg-slate-800/80 p-3 rounded-xl border border-slate-200/60 dark:border-slate-700">
            <div class="text-xs text-slate-400 font-semibold">कुल समय</div>
            <div class="text-lg font-black text-slate-800 dark:text-slate-100">150 मिनट</div>
          </div>
          <div class="bg-slate-50 dark:bg-slate-800/80 p-3 rounded-xl border border-slate-200/60 dark:border-slate-700">
            <div class="text-xs text-slate-400 font-semibold">पूर्णांक</div>
            <div class="text-lg font-black text-slate-800 dark:text-slate-100">150 अंक</div>
          </div>
          <div class="bg-slate-50 dark:bg-slate-800/80 p-3 rounded-xl border border-slate-200/60 dark:border-slate-700">
            <div class="text-xs text-slate-400 font-semibold">नेगेटिव मार्किंग</div>
            <div class="text-lg font-black text-emerald-600 dark:text-emerald-400">शून्य (None)</div>
          </div>
        </div>

        <!-- Palette Guide -->
        <div class="space-y-3 bg-slate-50 dark:bg-slate-800/50 p-4 rounded-xl border border-slate-200/60 dark:border-slate-700 text-xs">
          <div class="font-bold text-slate-800 dark:text-slate-200">प्रश्न पैलेट स्थिति गाइड (Question Palette Symbols):</div>
          <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
            <div class="flex items-center gap-2">
              <span class="w-5 h-5 rounded-md bg-emerald-500 text-white font-bold flex items-center justify-center text-[10px]">1</span>
              <span>उत्तर दिया (Answered)</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-5 h-5 rounded-md bg-red-500 text-white font-bold flex items-center justify-center text-[10px]">2</span>
              <span>उत्तर नहीं दिया (Not Answered)</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-5 h-5 rounded-md bg-purple-500 text-white font-bold flex items-center justify-center text-[10px]">3</span>
              <span>समीक्षा हेतु चिह्नित (Review)</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-5 h-5 rounded-md bg-slate-300 dark:bg-slate-700 text-slate-700 dark:text-slate-300 font-bold flex items-center justify-center text-[10px]">4</span>
              <span>नहीं देखा (Not Visited)</span>
            </div>
          </div>
        </div>

        <!-- Agreement Checkbox -->
        <div class="flex items-start gap-3 pt-2">
          <input type="checkbox" id="cbt-agree-chk" class="w-4 h-4 mt-0.5 text-brand-600 rounded border-slate-300 focus:ring-brand-500">
          <label for="cbt-agree-chk" class="text-xs font-semibold text-slate-700 dark:text-slate-300 select-none">
            मैंने सभी निर्देश पढ़ लिए हैं और समझ लिए हैं। मैं निष्पक्षता से 150 मिनट की समय-सीमा में यह मॉक टेस्ट देने के लिए तैयार हूँ।
          </label>
        </div>

        <!-- Action Buttons -->
        <div class="flex items-center justify-end gap-3 pt-4 border-t border-slate-200 dark:border-slate-800">
          <button onclick="closeCBTModal()" class="px-5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-300 font-bold text-xs hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">
            रद्द करें (Cancel)
          </button>
          <button onclick="startLiveCBTExam()" class="px-6 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white font-extrabold text-xs shadow-lg shadow-emerald-500/25 transition-all flex items-center gap-2">
            <span>परीक्षा प्रारंभ करें (Start Exam)</span>
            <i class="fa-solid fa-arrow-right"></i>
          </button>
        </div>

      </div>
    </div>

    <!-- VIEW 2: LIVE CBT EXAM SCREEN -->
    <div id="cbt-view-exam" class="hidden flex-1 flex flex-col bg-slate-100 dark:bg-slate-950 overflow-hidden">
      
      <!-- CBT Top Bar -->
      <div class="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 px-4 py-2.5 flex items-center justify-between gap-3 shadow-sm z-20">
        
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-brand-600 text-white font-bold flex items-center justify-center text-sm">
            <i class="fa-solid fa-laptop-code"></i>
          </div>
          <div>
            <div class="font-extrabold text-xs sm:text-sm text-slate-900 dark:text-white leading-none" id="exam-header-title">
              मॉक टेस्ट 01
            </div>
            <span class="text-[10px] text-slate-500 dark:text-slate-400 font-semibold" id="exam-header-subtitle">
              प्रश्न 1 of 150
            </span>
          </div>
        </div>

        <!-- Section Switcher Tabs -->
        <div class="hidden lg:flex items-center gap-1 bg-slate-100 dark:bg-slate-800 p-1 rounded-xl text-xs font-bold">
          <button onclick="switchSection('all')" id="sec-tab-all" class="px-3 py-1 rounded-lg bg-brand-600 text-white">सभी 150 प्रश्न</button>
          <button onclick="switchSection('lis')" id="sec-tab-lis" class="px-3 py-1 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700">भाग 1: LIS (1-100)</button>
          <button onclick="switchSection('part2')" id="sec-tab-part2" class="px-3 py-1 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700">भाग 2: शिक्षण व GS (101-150)</button>
        </div>

        <!-- Timer & Actions -->
        <div class="flex items-center gap-2 sm:gap-4">
          
          <!-- Live Countdown Timer -->
          <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
            <i class="fa-regular fa-clock text-brand-600 dark:text-brand-400 text-xs"></i>
            <span id="exam-timer-display" class="font-mono text-sm sm:text-base font-extrabold text-slate-800 dark:text-slate-100">
              02:30:00
            </span>
          </div>

          <!-- Language Toggle -->
          <select id="exam-lang-select" onchange="changeLanguageMode(this.value)" class="text-xs font-bold bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg px-2 py-1.5 text-slate-700 dark:text-slate-300">
            <option value="bilingual">द्विभाषी (EN+HI)</option>
            <option value="hi">केवल हिन्दी</option>
            <option value="en">English Only</option>
          </select>

          <!-- Mobile Palette Toggle Button -->
          <button onclick="toggleMobilePalette()" class="lg:hidden px-2.5 py-1.5 rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-200 text-xs font-bold">
            <i class="fa-solid fa-table-cells-large"></i>
          </button>

          <!-- Submit Test Button -->
          <button onclick="confirmSubmitTest()" class="px-4 py-1.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-extrabold text-xs shadow-md shadow-rose-500/20 transition-all">
            सबमिट करें
          </button>
        </div>

      </div>

      <!-- CBT Main Workspace: Question Canvas + Sidebar Palette -->
      <div class="flex-1 flex overflow-hidden relative">
        
        <!-- Left Question Panel (75% on Desktop, Full on Mobile) -->
        <div class="flex-1 overflow-y-auto p-4 sm:p-6 lg:p-8 flex flex-col justify-between">
          
          <div class="max-w-4xl w-full mx-auto space-y-6">
            
            <!-- Question Meta Header -->
            <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3">
              <div class="flex items-center gap-2">
                <span class="px-2.5 py-1 rounded-lg bg-brand-100 text-brand-800 dark:bg-brand-900/60 dark:text-brand-300 font-extrabold text-xs" id="q-number-badge">
                  Question 1
                </span>
                <span class="text-xs font-bold text-slate-500 dark:text-slate-400" id="q-section-badge">
                  Part 1: Library Science
                </span>
              </div>
              <span class="text-xs font-bold text-emerald-600 dark:text-emerald-400">
                +1 अंक • कोई नकारात्मक अंकन नहीं
              </span>
            </div>

            <!-- Question Text Box -->
            <div class="space-y-3">
              <h3 id="cbt-q-text-en" class="text-base sm:text-lg font-bold text-slate-900 dark:text-white leading-relaxed">
                Loading question...
              </h3>
              <p id="cbt-q-text-hi" class="text-sm sm:text-base font-semibold text-brand-700 dark:text-brand-300 leading-relaxed">
                प्रश्न लोड हो रहा है...
              </p>
            </div>

            <!-- 4 Options Container -->
            <div id="cbt-options-container" class="space-y-3 pt-2">
              <!-- Dynamically rendered options A, B, C, D -->
            </div>

          </div>

          <!-- Question Action Bar -->
          <div class="max-w-4xl w-full mx-auto pt-6 border-t border-slate-200 dark:border-slate-800 flex flex-wrap items-center justify-between gap-3 mt-8">
            <div class="flex items-center gap-2">
              <button onclick="clearCurrentResponse()" class="px-3.5 py-2 rounded-xl border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-slate-800 font-bold text-xs transition-colors">
                उत्तर साफ़ करें (Clear)
              </button>
              <button onclick="markForReviewAndNext()" class="px-3.5 py-2 rounded-xl bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300 hover:bg-purple-200 font-bold text-xs transition-colors">
                रिव्यू हेतु चिह्नित करें (Mark for Review)
              </button>
            </div>

            <div class="flex items-center gap-2">
              <button onclick="prevQuestion()" id="btn-prev-q" class="px-4 py-2 rounded-xl bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-300 font-bold text-xs transition-colors">
                <i class="fa-solid fa-chevron-left mr-1"></i> पिछला (Prev)
              </button>
              <button onclick="saveAndNextQuestion()" class="px-5 py-2 rounded-xl bg-brand-600 hover:bg-brand-700 text-white font-extrabold text-xs shadow-md shadow-brand-500/20 transition-all flex items-center gap-1.5">
                <span>सहेजें और अगला (Save & Next)</span>
                <i class="fa-solid fa-chevron-right ml-1"></i>
              </button>
            </div>
          </div>

        </div>

        <!-- Right Question Palette (25% on Desktop, Slide-over Drawer on Mobile) -->
        <div id="cbt-palette-sidebar" class="w-80 bg-white dark:bg-slate-900 border-l border-slate-200 dark:border-slate-800 flex flex-col z-30 transition-transform duration-300 fixed inset-y-0 right-0 lg:static translate-x-full lg:translate-x-0">
          
          <!-- Palette Header -->
          <div class="p-3 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
            <span class="font-extrabold text-xs text-slate-800 dark:text-slate-200">
              <i class="fa-solid fa-table-cells-large mr-1.5 text-brand-600"></i> प्रश्न पैलेट (1-150)
            </span>
            <button onclick="toggleMobilePalette()" class="lg:hidden text-slate-500 hover:text-slate-700">
              <i class="fa-solid fa-xmark text-sm"></i>
            </button>
          </div>

          <!-- Status Counts Summary -->
          <div class="p-3 grid grid-cols-2 gap-2 text-[10px] font-bold border-b border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40">
            <div class="flex items-center gap-1.5">
              <span class="w-3.5 h-3.5 rounded bg-emerald-500 text-white flex items-center justify-center text-[9px]" id="count-answered">0</span>
              <span>Answered</span>
            </div>
            <div class="flex items-center gap-1.5">
              <span class="w-3.5 h-3.5 rounded bg-red-500 text-white flex items-center justify-center text-[9px]" id="count-unanswered">0</span>
              <span>Not Answered</span>
            </div>
            <div class="flex items-center gap-1.5">
              <span class="w-3.5 h-3.5 rounded bg-purple-500 text-white flex items-center justify-center text-[9px]" id="count-review">0</span>
              <span>Review</span>
            </div>
            <div class="flex items-center gap-1.5">
              <span class="w-3.5 h-3.5 rounded bg-slate-300 dark:bg-slate-700 text-slate-600 dark:text-slate-300 flex items-center justify-center text-[9px]" id="count-notvisited">150</span>
              <span>Not Visited</span>
            </div>
          </div>

          <!-- Palette Buttons Grid -->
          <div class="flex-1 overflow-y-auto p-3 custom-scroll">
            <div id="cbt-palette-grid" class="grid grid-cols-5 gap-2">
              <!-- Dynamically generated 150 buttons -->
            </div>
          </div>

        </div>

      </div>

    </div>

    <!-- VIEW 3: COMPREHENSIVE SCORECARD & REVIEW SCREEN -->
    <div id="cbt-view-scorecard" class="hidden flex-1 overflow-y-auto p-4 sm:p-6 lg:p-8">
      <div class="max-w-5xl mx-auto space-y-6">
        
        <!-- Top Scorecard Banner -->
        <div class="bg-gradient-to-r from-brand-700 via-indigo-700 to-purple-800 text-white rounded-3xl p-6 sm:p-8 shadow-2xl relative overflow-hidden">
          <div class="flex flex-col sm:flex-row items-center justify-between gap-6 relative z-10">
            <div class="text-center sm:text-left space-y-1">
              <span class="px-3 py-1 rounded-full bg-white/20 text-xs font-extrabold uppercase tracking-wider">
                Exam Performance Report • परीक्षा परिणाम
              </span>
              <h2 class="text-2xl sm:text-4xl font-black" id="scorecard-paper-title">
                मॉक टेस्ट स्कोरकार्ड
              </h2>
              <p class="text-xs sm:text-sm text-blue-100" id="scorecard-timestamp">
                बिहार विद्यालय पुस्तकालय पात्रता परीक्षा
              </p>
            </div>

            <!-- Big Score Badge -->
            <div class="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl p-4 text-center min-w-[160px]">
              <div class="text-xs uppercase tracking-wider font-extrabold text-blue-200">कुल प्राप्तांक (Score)</div>
              <div class="text-4xl sm:text-5xl font-black mt-1" id="scorecard-total-marks">
                0 / 150
              </div>
              <div class="text-xs font-bold text-emerald-300 mt-1" id="scorecard-percentage">
                0%
              </div>
            </div>
          </div>
        </div>

        <!-- 4 Key Metric Cards -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
          <div class="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm text-center">
            <div class="text-xs text-slate-400 font-bold">सटीकता (Accuracy)</div>
            <div class="text-2xl sm:text-3xl font-black text-brand-600 dark:text-brand-400 mt-1" id="score-accuracy">0%</div>
          </div>
          <div class="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm text-center">
            <div class="text-xs text-slate-400 font-bold">सही उत्तर (Correct)</div>
            <div class="text-2xl sm:text-3xl font-black text-emerald-600 dark:text-emerald-400 mt-1" id="score-correct">0</div>
          </div>
          <div class="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm text-center">
            <div class="text-xs text-slate-400 font-bold">गलत उत्तर (Incorrect)</div>
            <div class="text-2xl sm:text-3xl font-black text-rose-600 dark:text-rose-400 mt-1" id="score-incorrect">0</div>
          </div>
          <div class="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm text-center">
            <div class="text-xs text-slate-400 font-bold">छोड़े गए (Skipped)</div>
            <div class="text-2xl sm:text-3xl font-black text-slate-500 dark:text-slate-400 mt-1" id="score-skipped">0</div>
          </div>
        </div>

        <!-- Sectional Performance Breakdown -->
        <div class="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-5 shadow-sm space-y-4">
          <h3 class="font-bold text-sm text-slate-800 dark:text-slate-200 border-b border-slate-200 dark:border-slate-800 pb-2">
            अनुभाग-वार प्रदर्शन विश्लेषण (Section-wise Breakdown)
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="bg-slate-50 dark:bg-slate-800/60 p-4 rounded-xl border border-slate-200/60 dark:border-slate-700">
              <div class="flex justify-between items-center text-xs font-bold mb-1">
                <span class="text-brand-700 dark:text-brand-300">भाग 1: पुस्तकालय एवं सूचना विज्ञान (1-100)</span>
                <span id="score-part1-ratio" class="text-slate-700 dark:text-slate-300 font-black">0 / 100</span>
              </div>
              <div class="w-full h-2 rounded-full bg-slate-200 dark:bg-slate-700 overflow-hidden">
                <div id="score-part1-bar" class="h-full bg-brand-600 rounded-full" style="width: 0%"></div>
              </div>
            </div>
            <div class="bg-slate-50 dark:bg-slate-800/60 p-4 rounded-xl border border-slate-200/60 dark:border-slate-700">
              <div class="flex justify-between items-center text-xs font-bold mb-1">
                <span class="text-indigo-700 dark:text-indigo-300">भाग 2: शिक्षण कला व सामान्य अध्ययन (101-150)</span>
                <span id="score-part2-ratio" class="text-slate-700 dark:text-slate-300 font-black">0 / 50</span>
              </div>
              <div class="w-full h-2 rounded-full bg-slate-200 dark:bg-slate-700 overflow-hidden">
                <div id="score-part2-bar" class="h-full bg-indigo-600 rounded-full" style="width: 0%"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Post-Exam Actions -->
        <div class="flex flex-wrap items-center justify-between gap-3 bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="flex items-center gap-2">
            <button onclick="retakeCurrentTest()" class="px-4 py-2 rounded-xl bg-brand-600 hover:bg-brand-700 text-white font-bold text-xs shadow-md transition-all flex items-center gap-1.5">
              <i class="fa-solid fa-rotate-right"></i>
              <span>पुनः टेस्ट दें (Retake)</span>
            </button>
            <button onclick="closeCBTModal()" class="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 font-bold text-xs transition-colors">
              अन्य पेपर चुनें (Choose Paper)
            </button>
          </div>
          <a id="scorecard-pdf-download" href="#" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-md transition-all flex items-center gap-1.5">
            <i class="fa-solid fa-file-pdf"></i>
            <span>इस पेपर का PDF डाउनलोड करें</span>
          </a>
        </div>

        <!-- Detailed Solutions Review Header & Filter -->
        <div class="space-y-4">
          <div class="flex flex-col sm:flex-row items-center justify-between gap-3 border-b border-slate-200 dark:border-slate-800 pb-3">
            <div>
              <h3 class="font-black text-lg text-slate-900 dark:text-white">
                विस्तृत उत्तर कुंजी एवं व्याख्या (Solutions & Explanations)
              </h3>
              <p class="text-xs text-slate-500">सभी 150 प्रश्नों के प्रामाणिक उत्तर एवं द्विभाषी व्याख्याएं</p>
            </div>
            
            <div class="flex items-center gap-1.5 text-xs font-bold">
              <button onclick="filterReviewList('all')" id="rev-tab-all" class="px-3 py-1 rounded-lg bg-brand-600 text-white">सभी (150)</button>
              <button onclick="filterReviewList('incorrect')" id="rev-tab-incorrect" class="px-3 py-1 rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">गलत उत्तर</button>
              <button onclick="filterReviewList('correct')" id="rev-tab-correct" class="px-3 py-1 rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">सही उत्तर</button>
              <button onclick="filterReviewList('unattempted')" id="rev-tab-unattempted" class="px-3 py-1 rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">छोड़े गए</button>
            </div>
          </div>

          <!-- Review Questions List -->
          <div id="review-questions-container" class="space-y-4">
            <!-- Dynamically populated review questions -->
          </div>
        </div>

      </div>
    </div>

  </div>

  <!-- ================= CLIENT JAVASCRIPT CBT ENGINE ================= -->
  <script>
    // Offline preloaded cache for Paper 01
    const OFFLINE_PAPER_01 = {json.dumps(paper_01_cache, ensure_ascii=False)};
    
    // CBT Test State
    let currentPaperNum = 1;
    let questions = [];
    let userAnswers = {{}}; // qIndex -> optionIndex (0-3)
    let questionStatus = {{}}; // qIndex -> 'not_visited' | 'not_answered' | 'answered' | 'marked_for_review'
    let currentQIdx = 0;
    let timeRemaining = 150 * 60; // 150 minutes in seconds
    let timerInterval = null;
    let activeSectionFilter = 'all'; // 'all' | 'lis' | 'part2'
    let languageMode = 'bilingual'; // 'bilingual' | 'en' | 'hi'

    // Hero Paper Select
    function startSelectedHeroPaper() {{
      const num = parseInt(document.getElementById('hero-paper-select').value) || 1;
      startOnlineTest(num);
    }}

    // Open CBT Test Modal
    async function startOnlineTest(paperNum) {{
      currentPaperNum = paperNum;
      const modal = document.getElementById('cbt-modal');
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';

      // Show Loading Screen
      showCBTView('loading');
      document.getElementById('loading-title').innerText = `मॉक टेस्ट पेपर ${{String(paperNum).padStart(2, '0')}} लोड हो रहा है...`;

      // Fetch Paper Questions
      try {{
        if (paperNum === 1 && (!window.location.protocol.startsWith('http') || window.location.protocol === 'file:')) {{
          questions = OFFLINE_PAPER_01;
        }} else {{
          const resp = await fetch(`data/paper_${{String(paperNum).padStart(2, '0')}}.json`);
          if (!resp.ok) throw new Error("Network fetch failed");
          questions = await resp.json();
        }}
      }} catch (err) {{
        console.warn("Falling back to pre-cached paper data:", err);
        questions = OFFLINE_PAPER_01;
      }}

      // Initialize State
      userAnswers = {{}};
      questionStatus = {{}};
      for (let i = 0; i < questions.length; i++) {{
        questionStatus[i] = 'not_visited';
      }}
      currentQIdx = 0;
      timeRemaining = 150 * 60;

      // Setup Instruction Screen
      document.getElementById('inst-paper-title').innerText = `बिहार पुस्तकालय पात्रता परीक्षा — मॉक टेस्ट ${{String(paperNum).padStart(2, '0')}}`;
      document.getElementById('cbt-agree-chk').checked = false;
      showCBTView('instructions');
    }}

    function showCBTView(viewName) {{
      document.getElementById('cbt-view-loading').classList.add('hidden');
      document.getElementById('cbt-view-instructions').classList.add('hidden');
      document.getElementById('cbt-view-exam').classList.add('hidden');
      document.getElementById('cbt-view-scorecard').classList.add('hidden');

      if (viewName === 'loading') document.getElementById('cbt-view-loading').classList.remove('hidden');
      if (viewName === 'instructions') document.getElementById('cbt-view-instructions').classList.remove('hidden');
      if (viewName === 'exam') document.getElementById('cbt-view-exam').classList.remove('hidden');
      if (viewName === 'scorecard') document.getElementById('cbt-view-scorecard').classList.remove('hidden');
    }}

    function closeCBTModal() {{
      if (timerInterval) clearInterval(timerInterval);
      document.getElementById('cbt-modal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }}

    // Start Live CBT Exam
    function startLiveCBTExam() {{
      const chk = document.getElementById('cbt-agree-chk');
      if (!chk.checked) {{
        alert("कृपया परीक्षा शुरू करने से पहले निर्देश पढ़ने की पुष्टि (चेकबॉक्स) पर टिक करें।");
        return;
      }}

      // Setup Exam Header
      document.getElementById('exam-header-title').innerText = `मॉक टेस्ट पेपर ${{String(currentPaperNum).padStart(2, '0')}}`;
      
      // Render Palette Grid
      renderPalette();

      // Load First Question
      jumpToQuestion(0);

      // Start Timer
      startTimer();

      // Show Exam View
      showCBTView('exam');
    }}

    // Timer Logic
    function startTimer() {{
      if (timerInterval) clearInterval(timerInterval);
      updateTimerDisplay();
      timerInterval = setInterval(() => {{
        timeRemaining--;
        updateTimerDisplay();
        if (timeRemaining <= 0) {{
          clearInterval(timerInterval);
          alert("परीक्षा की निर्धारित 150 मिनट की समय-सीमा समाप्त हो गई है! आपका टेस्ट स्वतः सबमिट हो रहा है।");
          calculateAndShowScorecard();
        }}
      }}, 1000);
    }}

    function updateTimerDisplay() {{
      const hrs = Math.floor(timeRemaining / 3600);
      const mins = Math.floor((timeRemaining % 3600) / 60);
      const secs = timeRemaining % 60;
      const display = `${{String(hrs).padStart(2, '0')}}:${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}`;
      const el = document.getElementById('exam-timer-display');
      el.innerText = display;
      if (timeRemaining < 300) {{
        el.classList.add('timer-warning');
      }} else {{
        el.classList.remove('timer-warning');
      }}
    }}

    // Jump to Question
    function jumpToQuestion(idx) {{
      if (idx < 0 || idx >= questions.length) return;
      currentQIdx = idx;

      // Mark as not_answered if was not_visited
      if (questionStatus[currentQIdx] === 'not_visited') {{
        questionStatus[currentQIdx] = 'not_answered';
      }}

      renderCurrentQuestion();
      renderPalette();
    }}

    // Render Question
    function renderCurrentQuestion() {{
      const q = questions[currentQIdx];
      document.getElementById('q-number-badge').innerText = `Question ${{currentQIdx + 1}} of ${{questions.length}}`;
      document.getElementById('q-section-badge').innerText = q.section_hi || q.section_en || (currentQIdx < 100 ? 'भाग 1: पुस्तकालय विज्ञान' : 'भाग 2: सामान्य अध्ययन');
      document.getElementById('exam-header-subtitle').innerText = `प्रश्न ${{currentQIdx + 1}} / ${{questions.length}}`;

      const qEnEl = document.getElementById('cbt-q-text-en');
      const qHiEl = document.getElementById('cbt-q-text-hi');

      qEnEl.innerText = q.q_en;
      qHiEl.innerText = q.q_hi;

      // Language visibility
      if (languageMode === 'hi') {{
        qEnEl.classList.add('hidden');
        qHiEl.classList.remove('hidden');
      }} else if (languageMode === 'en') {{
        qEnEl.classList.remove('hidden');
        qHiEl.classList.add('hidden');
      }} else {{
        qEnEl.classList.remove('hidden');
        qHiEl.classList.remove('hidden');
      }}

      // Render Options
      const container = document.getElementById('cbt-options-container');
      const selected = userAnswers[currentQIdx];
      const letters = ['A', 'B', 'C', 'D'];

      container.innerHTML = q.options_en.map((optEn, i) => {{
        const optHi = q.options_hi[i];
        const isChecked = selected === i;
        return `
          <label onclick="selectOption(${{i}})" class="flex items-start gap-3 p-3.5 rounded-xl border cursor-pointer transition-all ${{isChecked ? 'bg-brand-50 dark:bg-brand-950/70 border-brand-500 ring-2 ring-brand-500/30' : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800/60'}}">
            <div class="w-6 h-6 rounded-full border-2 flex items-center justify-center font-bold text-xs mt-0.5 ${{isChecked ? 'border-brand-600 bg-brand-600 text-white' : 'border-slate-300 dark:border-slate-600 text-slate-500'}}">
              ${{letters[i]}}
            </div>
            <div class="flex-1 space-y-0.5 text-xs sm:text-sm">
              <div class="font-bold text-slate-900 dark:text-white ${{languageMode === 'hi' ? 'hidden' : ''}}">${{optEn}}</div>
              <div class="font-medium text-slate-600 dark:text-slate-300 ${{languageMode === 'en' ? 'hidden' : ''}}">${{optHi}}</div>
            </div>
          </label>
        `;
      }}).join('');

      // Update Prev Button
      document.getElementById('btn-prev-q').disabled = currentQIdx === 0;
    }}

    function selectOption(optIdx) {{
      userAnswers[currentQIdx] = optIdx;
      questionStatus[currentQIdx] = 'answered';
      renderCurrentQuestion();
      renderPalette();
    }}

    function saveAndNextQuestion() {{
      if (currentQIdx < questions.length - 1) {{
        jumpToQuestion(currentQIdx + 1);
      }} else {{
        confirmSubmitTest();
      }}
    }}

    function markForReviewAndNext() {{
      questionStatus[currentQIdx] = 'marked_for_review';
      if (currentQIdx < questions.length - 1) {{
        jumpToQuestion(currentQIdx + 1);
      }} else {{
        renderPalette();
      }}
    }}

    function clearCurrentResponse() {{
      delete userAnswers[currentQIdx];
      questionStatus[currentQIdx] = 'not_answered';
      renderCurrentQuestion();
      renderPalette();
    }}

    function prevQuestion() {{
      if (currentQIdx > 0) {{
        jumpToQuestion(currentQIdx - 1);
      }}
    }}

    // Render Question Palette
    function renderPalette() {{
      const grid = document.getElementById('cbt-palette-grid');
      let countAns = 0, countUnans = 0, countRev = 0, countNotVis = 0;

      grid.innerHTML = questions.map((q, i) => {{
        // Filter by section
        if (activeSectionFilter === 'lis' && i >= 100) return '';
        if (activeSectionFilter === 'part2' && i < 100) return '';

        const st = questionStatus[i];
        const isCurrent = i === currentQIdx;
        let colorCls = "bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300";

        if (st === 'answered') {{
          colorCls = "bg-emerald-500 text-white";
          countAns++;
        }} else if (st === 'not_answered') {{
          colorCls = "bg-red-500 text-white";
          countUnans++;
        }} else if (st === 'marked_for_review') {{
          colorCls = "bg-purple-500 text-white";
          countRev++;
        }} else {{
          countNotVis++;
        }}

        return `
          <button onclick="jumpToQuestion(${{i}})" class="cbt-palette-btn h-8 rounded-lg font-bold text-xs flex items-center justify-center relative ${{colorCls}} ${{isCurrent ? 'ring-2 ring-blue-400 ring-offset-2' : ''}}">
            ${{i + 1}}
          </button>
        `;
      }}).join('');

      document.getElementById('count-answered').innerText = countAns;
      document.getElementById('count-unanswered').innerText = countUnans;
      document.getElementById('count-review').innerText = countRev;
      document.getElementById('count-notvisited').innerText = countNotVis;
    }}

    function switchSection(sec) {{
      activeSectionFilter = sec;
      document.getElementById('sec-tab-all').className = sec === 'all' ? 'px-3 py-1 rounded-lg bg-brand-600 text-white' : 'px-3 py-1 rounded-lg text-slate-600 dark:text-slate-300';
      document.getElementById('sec-tab-lis').className = sec === 'lis' ? 'px-3 py-1 rounded-lg bg-brand-600 text-white' : 'px-3 py-1 rounded-lg text-slate-600 dark:text-slate-300';
      document.getElementById('sec-tab-part2').className = sec === 'part2' ? 'px-3 py-1 rounded-lg bg-brand-600 text-white' : 'px-3 py-1 rounded-lg text-slate-600 dark:text-slate-300';
      renderPalette();
    }}

    function changeLanguageMode(mode) {{
      languageMode = mode;
      renderCurrentQuestion();
    }}

    function toggleMobilePalette() {{
      const pal = document.getElementById('cbt-palette-sidebar');
      pal.classList.toggle('translate-x-full');
    }}

    // Confirm Submission
    function confirmSubmitTest() {{
      let ans = Object.keys(userAnswers).length;
      let unans = questions.length - ans;
      let ok = confirm(`क्या आप वास्तव में टेस्ट सबमिट करना चाहते हैं?\\n\\n• उत्तर दिए गए प्रश्न: ${{ans}}\\n• अनुत्तरित प्रश्न: ${{unans}}\\n• कुल प्रश्न: ${{questions.length}}\\n\\nसबमिट करने के बाद आप तुरंत अपना विस्तृत स्कोरकार्ड और समाधान देख सकेंगे।`);
      if (ok) {{
        calculateAndShowScorecard();
      }}
    }}

    // Calculate Score & Display Scorecard
    function calculateAndShowScorecard() {{
      if (timerInterval) clearInterval(timerInterval);

      let correct = 0;
      let incorrect = 0;
      let part1Correct = 0;
      let part2Correct = 0;

      questions.forEach((q, i) => {{
        const correctIdx = q.answer ? (q.answer.charCodeAt(0) - 65) : (q.correct !== undefined ? q.correct : 0);
        q._correctIdx = correctIdx;
        q._userChoice = userAnswers[i];
        
        if (userAnswers[i] !== undefined) {{
          if (userAnswers[i] === correctIdx) {{
            correct++;
            if (i < 100) part1Correct++; else part2Correct++;
          }} else {{
            incorrect++;
          }}
        }}
      }});

      const totalAttempted = correct + incorrect;
      const skipped = questions.length - totalAttempted;
      const pct = ((correct / questions.length) * 100).toFixed(1);
      const accuracy = totalAttempted > 0 ? ((correct / totalAttempted) * 100).toFixed(1) : "0.0";

      // Populate Scorecard Elements
      document.getElementById('scorecard-paper-title').innerText = `मॉक टेस्ट ${{String(currentPaperNum).padStart(2, '0')}} का स्कोरकार्ड`;
      document.getElementById('scorecard-total-marks').innerText = `${{correct}} / ${{questions.length}}`;
      document.getElementById('scorecard-percentage').innerText = `${{pct}}% • ${{pct >= 50 ? 'QUALIFIED (कटऑफ उत्तीर्ण)' : 'NEEDS PRACTICE'}}`;
      document.getElementById('scorecard-timestamp').innerText = `परीक्षा पूर्ण: ${{new Date().toLocaleDateString('hi-IN')}} • कुल समय: 150 मिनट`;

      document.getElementById('score-accuracy').innerText = `${{accuracy}}%`;
      document.getElementById('score-correct').innerText = correct;
      document.getElementById('score-incorrect').innerText = incorrect;
      document.getElementById('score-skipped').innerText = skipped;

      document.getElementById('score-part1-ratio').innerText = `${{part1Correct}} / 100 (${{part1Correct}}%)`;
      document.getElementById('score-part1-bar').style.width = `${{part1Correct}}%`;

      const part2Pct = ((part2Correct / 50) * 100).toFixed(1);
      document.getElementById('score-part2-ratio').innerText = `${{part2Correct}} / 50 (${{part2Pct}}%)`;
      document.getElementById('score-part2-bar').style.width = `${{part2Pct}}%`;

      document.getElementById('scorecard-pdf-download').href = `Bihar_Librarian_Bilingual_Mock_${{String(currentPaperNum).padStart(2, '0')}}.pdf`;

      // Render Review Solutions
      renderReviewList('all');

      // Show Scorecard View
      showCBTView('scorecard');
    }}

    function retakeCurrentTest() {{
      startOnlineTest(currentPaperNum);
    }}

    // Filter and Render Solutions Review
    function filterReviewList(filterType) {{
      ['all', 'incorrect', 'correct', 'unattempted'].forEach(f => {{
        const el = document.getElementById(`rev-tab-${{f}}`);
        if (f === filterType) {{
          el.className = 'px-3 py-1 rounded-lg bg-brand-600 text-white';
        }} else {{
          el.className = 'px-3 py-1 rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300';
        }}
      }});

      const container = document.getElementById('review-questions-container');
      const letters = ['A', 'B', 'C', 'D'];

      const filtered = questions.map((q, i) => ({{ q, i }})).filter(({{ q, i }}) => {{
        const isAttempted = q._userChoice !== undefined;
        const isCorrect = isAttempted && q._userChoice === q._correctIdx;
        if (filterType === 'correct') return isCorrect;
        if (filterType === 'incorrect') return isAttempted && !isCorrect;
        if (filterType === 'unattempted') return !isAttempted;
        return true;
      }});

      if (filtered.length === 0) {{
        container.innerHTML = `<div class="p-8 text-center text-slate-500 font-bold text-sm bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800">इस श्रेणी में कोई प्रश्न नहीं है।</div>`;
        return;
      }}

      container.innerHTML = filtered.map(({{ q, i }}) => {{
        const isAttempted = q._userChoice !== undefined;
        const isCorrect = isAttempted && q._userChoice === q._correctIdx;
        
        let statusBadge = '';
        if (!isAttempted) {{
          statusBadge = `<span class="px-2.5 py-0.5 rounded text-[10px] font-bold bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300">अनुत्तरित (Skipped)</span>`;
        }} else if (isCorrect) {{
          statusBadge = `<span class="px-2.5 py-0.5 rounded text-[10px] font-bold bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300"><i class="fa-solid fa-check mr-1"></i>सही उत्तर (+1)</span>`;
        }} else {{
          statusBadge = `<span class="px-2.5 py-0.5 rounded text-[10px] font-bold bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300"><i class="fa-solid fa-xmark mr-1"></i>गलत उत्तर (0)</span>`;
        }}

        return `
          <div class="bg-white dark:bg-slate-900 p-5 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-3">
            <div class="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-2">
              <span class="font-extrabold text-xs text-brand-600 dark:text-brand-400">Question ${{i + 1}}</span>
              ${{statusBadge}}
            </div>

            <div class="space-y-1">
              <div class="font-bold text-slate-900 dark:text-white text-sm sm:text-base">${{q.q_en}}</div>
              <div class="font-semibold text-brand-700 dark:text-brand-300 text-xs sm:text-sm">${{q.q_hi}}</div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-2">
              ${{q.options_en.map((optEn, oIdx) => {{
                const optHi = q.options_hi[oIdx];
                const isCorrectOpt = oIdx === q._correctIdx;
                const isUserChoice = oIdx === q._userChoice;
                
                let optBorder = 'border-slate-200 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-800/40';
                if (isCorrectOpt) {{
                  optBorder = 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/60 ring-1 ring-emerald-500';
                }} else if (isUserChoice && !isCorrectOpt) {{
                  optBorder = 'border-rose-500 bg-rose-50 dark:bg-rose-950/60 ring-1 ring-rose-500';
                }}

                return `
                  <div class="p-2.5 rounded-xl border text-xs ${{optBorder}} flex items-start gap-2">
                    <span class="w-5 h-5 rounded-full flex items-center justify-center font-bold text-[10px] ${{isCorrectOpt ? 'bg-emerald-600 text-white' : isUserChoice ? 'bg-rose-600 text-white' : 'bg-slate-200 dark:bg-slate-700'}}">
                      ${{letters[oIdx]}}
                    </span>
                    <div class="flex-1">
                      <div class="font-bold text-slate-900 dark:text-slate-100">${{optEn}}</div>
                      <div class="text-[11px] text-slate-600 dark:text-slate-400">${{optHi}}</div>
                    </div>
                  </div>
                `;
              }}).join('')}}
            </div>

            <!-- Full Explanation Callout Box -->
            <div class="mt-3 p-3.5 rounded-xl bg-blue-50 dark:bg-slate-800/80 border border-blue-200 dark:border-slate-700 text-xs space-y-1">
              <div class="font-extrabold text-blue-900 dark:text-blue-300 flex items-center gap-1.5">
                <i class="fa-solid fa-lightbulb text-amber-500"></i> प्रामाणिक व्याख्या (Bilingual Explanation):
              </div>
              <div class="text-slate-800 dark:text-slate-200 font-medium">${{q.exp_hi}}</div>
              <div class="text-slate-600 dark:text-slate-400 italic">${{q.exp_en}}</div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    // Filter Papers by Tabs & Search
    let currentTab = 'all';
    function setTab(tab) {{
      currentTab = tab;
      document.querySelectorAll('.tab-btn').forEach(btn => {{
        btn.className = 'tab-btn px-4 py-1.5 rounded-xl text-xs font-bold transition-all bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200';
      }});
      document.getElementById(`tab-${{tab}}`).className = 'tab-btn px-4 py-1.5 rounded-xl text-xs font-bold transition-all bg-brand-600 text-white shadow-sm';
      filterPapers();
    }}

    function filterPapers() {{
      const query = (document.getElementById('paper-search').value || '').toLowerCase().trim();
      const cards = document.querySelectorAll('.paper-card');
      
      cards.forEach(card => {{
        const num = card.getAttribute('data-num');
        const grp = card.getAttribute('data-group');
        const text = card.innerText.toLowerCase();

        const matchTab = currentTab === 'all' || String(grp) === String(currentTab);
        const matchQuery = !query || text.includes(query) || num === query;

        if (matchTab && matchQuery) {{
          card.classList.remove('hidden');
        }} else {{
          card.classList.add('hidden');
        }}
      }});
    }}

    // Dark Mode Toggle Logic
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');

    if (localStorage.getItem('theme') === 'dark' || (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
      document.documentElement.classList.add('dark');
      themeIcon.className = 'fa-solid fa-sun text-amber-400';
    }} else {{
      document.documentElement.classList.remove('dark');
      themeIcon.className = 'fa-solid fa-moon text-slate-500';
    }}

    themeToggleBtn.addEventListener('click', () => {{
      if (document.documentElement.classList.contains('dark')) {{
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
        themeIcon.className = 'fa-solid fa-moon text-slate-500';
      }} else {{
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
        themeIcon.className = 'fa-solid fa-sun text-amber-400';
      }}
    }});
  </script>

</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated updated index.html with Full CBT Online Test Engine! File size: {os.path.getsize('index.html')/1024:.1f} KB")
