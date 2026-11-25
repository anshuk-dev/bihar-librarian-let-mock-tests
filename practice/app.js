(() => {
  'use strict';

  const TOPICS = [
    { id: 't01', code: 't01_history', en: 'Library History & Thinkers', hi: 'पुस्तकालय इतिहास एवं विचारक' },
    { id: 't02', code: 't02_libtypes', en: 'Types of Libraries & Services', hi: 'पुस्तकालयों के प्रकार एवं सेवाएँ' },
    { id: 't03', code: 't03_legislation', en: 'Library Acts & Committees', hi: 'पुस्तकालय अधिनियम एवं समितियाँ' },
    { id: 't04', code: 't04_management', en: 'Library Management & Finance', hi: 'पुस्तकालय प्रबंधन एवं वित्त' },
    { id: 't05', code: 't05_ddc_udc', en: 'DDC & UDC Classification', hi: 'डीडीसी एवं यूडीसी वर्गीकरण' },
    { id: 't06', code: 't06_cc_schemes', en: 'Colon Classification & Schemes', hi: 'कोलन वर्गीकरण एवं अन्य पद्धतियाँ' },
    { id: 't07', code: 't07_cataloguing', en: 'Cataloguing, AACR2, CCC, RDA, MARC', hi: 'सूचीकरण संहिताएँ एवं मानक' },
    { id: 't08', code: 't08_reference', en: 'Information Sources & Reference', hi: 'सूचना स्रोत एवं संदर्भ सेवा' },
    { id: 't09', code: 't09_automation', en: 'Library Automation & LIS-IT', hi: 'पुस्तकालय स्वचालन एवं सूचना प्रौद्योगिकी' },
    { id: 't10', code: 't10_digital', en: 'Digital Libraries & Networks', hi: 'डिजिटल पुस्तकालय एवं नेटवर्क' },
    { id: 't11', code: 't11_biblio', en: 'Bibliometrics & Info Retrieval', hi: 'ग्रंथमितीय एवं सूचना पुनर्प्राप्ति' },
    { id: 't12', code: 't12_advanced', en: 'KO, Indexing, Standards & IPR', hi: 'ज्ञान संगठन, अनुक्रमणीकरण एवं मानक' }
  ];

  const DAYS_PLAN = [
    {
      day: 1,
      title: 'Day 1: Core Foundations & Classification Basics',
      hiTitle: 'दिन 1: मूलभूत आधार एवं वर्गीकरण के सिद्धांत',
      desc: 'Set 1 Topics T01–T06 (History, Types, Acts, Management, DDC/UDC, CC) — Highest-Yield Basics.',
      filter: { view: 'set1', topics: ['t01', 't02', 't03', 't04', 't05', 't06'] }
    },
    {
      day: 2,
      title: 'Day 2: Cataloguing, Reference & LIS-IT Core',
      hiTitle: 'दिन 2: सूचीकरण, संदर्भ सेवा एवं पुस्तकालय आईटी',
      desc: 'Set 1 Topics T07–T12 (AACR2/CCC/MARC, Info Sources, Automation, Digital, Bibliometrics, KO).',
      filter: { view: 'set1', topics: ['t07', 't08', 't09', 't10', 't11', 't12'] }
    },
    {
      day: 3,
      title: 'Day 3: Deep Core Rules & Classification/Cataloguing',
      hiTitle: 'दिन 3: गहन नियम, अधिनियम एवं वर्गीकरण-सूचीकरण',
      desc: 'Set 2 Topics T01–T06 (Detailed Acts chronology, Tables, Canons, Administration & Finance).',
      filter: { view: 'set2', topics: ['t01', 't02', 't03', 't04', 't05', 't06'] }
    },
    {
      day: 4,
      title: 'Day 4: Networks, Standards, Timeline & Bookmarks Recap',
      hiTitle: 'दिन 4: नेटवर्क, मानक, कालक्रम एवं बुकमार्क रिवीज़न',
      desc: 'Set 2 Topics T07–T12 + Full Year Timeline Review + All Bookmarked Questions.',
      filter: { view: 'set2', topics: ['t07', 't08', 't09', 't10', 't11', 't12'] }
    }
  ];

  const PAGE_SIZE = 25;
  const STORAGE_KEY = 'bihar_let_practice_v1';

  const state = {
    questions: [],
    set1Loaded: false,
    set2Loaded: false,
    view: 'set1', // set1 | set2 | all | timeline | plan
    studyMode: 'revise', // revise | recall
    lang: 'bi', // bi | hi | en
    theme: 'sepia',
    fontSize: 16,
    focusMode: false,
    showWrongs: true,
    topicFilter: 'all',
    dayTopics: null, // optional array from 4-day plan
    priorityFilter: 'all',
    statusFilter: 'all',
    searchQuery: '',
    eraFilter: 'all',
    timelineQuery: '',
    page: 1,
    focusIdx: 0,
    revealedIds: new Set(),
    userAnswers: new Map(), // globalId -> 'a'|'b'|'c'|'d'
    revisedIds: new Set(),
    bookmarkedIds: new Set()
  };

  // Load saved state
  function loadPrefs() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return;
      const saved = JSON.parse(raw);
      if (saved.theme) state.theme = saved.theme;
      if (saved.lang) state.lang = saved.lang;
      if (saved.studyMode) state.studyMode = saved.studyMode;
      if (typeof saved.fontSize === 'number') state.fontSize = Math.min(22, Math.max(13, saved.fontSize));
      if (Array.isArray(saved.revised)) state.revisedIds = new Set(saved.revised);
      if (Array.isArray(saved.bookmarked)) state.bookmarkedIds = new Set(saved.bookmarked);
    } catch (_) {}
  }

  function savePrefs() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        theme: state.theme,
        lang: state.lang,
        studyMode: state.studyMode,
        fontSize: state.fontSize,
        revised: Array.from(state.revisedIds),
        bookmarked: Array.from(state.bookmarkedIds)
      }));
    } catch (_) {}
  }

  // DOM helpers
  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  function esc(str) {
    if (str == null) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function applyAppearance() {
    document.documentElement.setAttribute('data-theme', state.theme);
    document.documentElement.setAttribute('data-lang', state.lang);
    document.documentElement.style.setProperty('--base-size', state.fontSize + 'px');

    $$('.theme-btn').forEach(b => b.classList.toggle('active', b.dataset.theme === state.theme));
    $$('.lang-btn').forEach(b => b.classList.toggle('active', b.dataset.lang === state.lang));

    const themeIcons = { light: '☀️', sepia: '📜', dark: '🌙' };
    $('#focus-theme-cycle').textContent = themeIcons[state.theme] || '📜';

    $('#btn-mode-revise').classList.toggle('active', state.studyMode === 'revise');
    $('#btn-mode-recall').classList.toggle('active', state.studyMode === 'recall');
    $('#focus-mode-revise').classList.toggle('active', state.studyMode === 'revise');
    $('#focus-mode-recall').classList.toggle('active', state.studyMode === 'recall');
  }

  function populateTopicDropdown() {
    const sel = $('#topic-select');
    sel.innerHTML = '<option value="all">All 12 Core LIS Topics (सभी विषय)</option>';
    for (const t of TOPICS) {
      const opt = document.createElement('option');
      opt.value = t.id;
      opt.textContent = `${t.en} / ${t.hi}`;
      sel.appendChild(opt);
    }
  }

  // Filter logic
  function getFilteredQuestions() {
    const qLower = state.searchQuery.trim().toLowerCase();
    return state.questions.filter(q => {
      if (state.view === 'set1' && q.set !== 1) return false;
      if (state.view === 'set2' && q.set !== 2) return false;

      if (state.dayTopics && !state.dayTopics.includes(q.topicId)) return false;
      if (state.topicFilter !== 'all' && q.topicId !== state.topicFilter) return false;

      if (state.priorityFilter === 'p1' && q.p !== 1) return false;
      if (state.priorityFilter === 'p2' && q.p !== 2) return false;
      if (state.priorityFilter === 'p3' && q.p !== 3) return false;
      if (state.priorityFilter === 'p45' && q.p < 4) return false;
      if (state.priorityFilter === 'yr' && q.yr == null) return false;

      if (state.statusFilter === 'unrevised' && state.revisedIds.has(q.gid)) return false;
      if (state.statusFilter === 'revised' && !state.revisedIds.has(q.gid)) return false;
      if (state.statusFilter === 'bookmarked' && !state.bookmarkedIds.has(q.gid)) return false;

      if (qLower) {
        const hay = q._search || '';
        if (!hay.includes(qLower)) return false;
      }
      return true;
    });
  }

  function updateStats(filteredLen) {
    const total = state.questions.length || 3000;
    const rev = state.revisedIds.size;
    const pct = total ? Math.round((rev / total) * 100) : 0;
    $('#stat-revised').textContent = rev;
    $('#stat-total').textContent = total;
    $('#stat-pct').textContent = pct + '%';
    $('#stat-bookmarked').textContent = state.bookmarkedIds.size;
    $('#stat-showing').textContent = filteredLen;
    $('#progress-bar-fill').style.width = pct + '%';

    const s1 = state.questions.filter(q => q.set === 1).length;
    const s2 = state.questions.filter(q => q.set === 2).length;
    const yrCount = state.questions.filter(q => q.yr != null).length;
    if (s1) $('#pill-set1').textContent = s1;
    if (s2) $('#pill-set2').textContent = s2;
    if (state.questions.length) $('#pill-all').textContent = state.questions.length;
    if (yrCount) $('#pill-yr').textContent = yrCount;

    const dayBadge = $('#day-filter-badge');
    if (dayBadge) {
      if (state.dayTopics) {
        dayBadge.classList.remove('hidden');
        dayBadge.textContent = `🗓️ Day Filter (${state.dayTopics.length} topics) ✕`;
      } else {
        dayBadge.classList.add('hidden');
      }
    }
  }

  function getPriorityLabel(p) {
    if (p === 1) return '<span class="badge badge-p1">⭐ P1 Must-Know</span>';
    if (p === 2) return '<span class="badge badge-p2">🔥 P2 Core</span>';
    if (p === 3) return '<span class="badge badge-p3">📘 P3 Standard</span>';
    return `<span class="badge badge-p4">🔬 P${p || 4} Deep</span>`;
  }

  function renderCardHTML(q) {
    const isRevised = state.revisedIds.has(q.gid);
    const isBookmarked = state.bookmarkedIds.has(q.gid);
    const isOpen = state.studyMode === 'revise' || state.revealedIds.has(q.gid);
    const chosen = state.userAnswers.get(q.gid);

    const topicObj = TOPICS.find(t => t.id === q.topicId);
    const topicLabel = topicObj ? topicObj.en : q.topicId;
    const yrBadge = q.yr != null ? `<button class="badge badge-year" data-year-jump="${esc(q.yr)}" title="Open Year Chronology around ${esc(q.yr)}">📅 ${esc(q.yr)}</button>` : '';

    const letters = ['a', 'b', 'c', 'd'];
    const optionsHTML = letters.map(l => {
      const opt = q[l] || ['', ''];
      let cls = 'opt-btn';
      if (isOpen && l === q.ans) cls += ' opt-correct';
      else if (chosen === l && l !== q.ans) cls += ' opt-wrong-selected';

      return `
        <button class="${cls}" data-gid="${q.gid}" data-opt="${l}">
          <span class="opt-letter">${l.toUpperCase()}</span>
          <span class="opt-body">
            <span class="opt-hi hi-only">${esc(opt[1])}</span>
            <span class="opt-en en-only">${esc(opt[0])}</span>
          </span>
        </button>
      `;
    }).join('');

    const wrongRowsHTML = letters
      .filter(l => l !== q.ans)
      .map(l => {
        const opt = q[l] || ['', ''];
        const we = (q.we && q.we[l]) || '';
        const wh = (q.wh && q.wh[l]) || '';
        return `
          <div class="wrong-item">
            <span class="wrong-key">${l.toUpperCase()}</span>
            <div>
              <div class="hi-only"><strong>${esc(opt[1])}:</strong> ${esc(wh || we)}</div>
              <div class="en-only ${state.lang === 'bi' ? 'exp-text-en' : ''}"><strong>${esc(opt[0])}:</strong> ${esc(we)}</div>
            </div>
          </div>
        `;
      }).join('');

    const yearExpHTML = q.yr != null ? `
      <div class="exp-year-box">
        <div class="exp-title">📅 Year Chronology Memory (${esc(q.yr)})</div>
        <div class="exp-text-hi hi-only">${esc(q.yrh || q.yre)}</div>
        <div class="exp-text-en en-only">${esc(q.yre || q.yrh)}</div>
      </div>
    ` : '';

    const expHTML = isOpen ? `
      <div class="exp-panel">
        <div class="exp-correct">
          <div class="exp-title">✅ Correct Answer: Option ${q.ans.toUpperCase()}</div>
          <div class="exp-text-hi hi-only">${esc(q.ch || q.ce)}</div>
          <div class="exp-text-en en-only">${esc(q.ce || q.ch)}</div>
        </div>
        ${yearExpHTML}
        ${state.showWrongs ? `
          <div class="exp-wrongs">
            <div class="exp-title">❌ Why Other 3 Options Are Incorrect</div>
            <div class="wrong-list">${wrongRowsHTML}</div>
          </div>
        ` : ''}
      </div>
    ` : `
      <div class="reveal-bar">
        <button class="reveal-btn" data-reveal="${q.gid}">👁️ Show Answer, Year &amp; All 4 Explanations</button>
      </div>
    `;

    return `
      <article class="q-card ${isRevised ? 'is-revised' : ''}" data-gid="${q.gid}">
        <div class="q-meta">
          <div class="q-badges">
            <span class="badge badge-qnum">#${q.gid}</span>
            <span class="badge">Set ${q.set}</span>
            <span class="badge">${esc(topicLabel)}</span>
            ${getPriorityLabel(q.p)}
            ${yrBadge}
          </div>
          <div class="q-actions">
            <button class="q-action-btn ${isBookmarked ? 'bookmarked' : ''}" data-bookmark="${q.gid}">
              ${isBookmarked ? '📌 Saved' : '📌 Save'}
            </button>
            <button class="q-action-btn ${isRevised ? 'revised' : ''}" data-revise="${q.gid}">
              ${isRevised ? '✅ Revised' : '⬜ Mark Done'}
            </button>
          </div>
        </div>

        <div class="q-stem">
          <div class="q-hi hi-only">${esc(q.qh)}</div>
          <div class="q-en en-only">${esc(q.qe)}</div>
        </div>

        <div class="options-grid">${optionsHTML}</div>
        ${expHTML}
      </article>
    `;
  }

  let currentFiltered = [];

  function renderPractice() {
    currentFiltered = getFilteredQuestions();
    updateStats(currentFiltered.length);

    const container = $('#questions-container');
    $('#loading-card').classList.add('hidden');

    if (currentFiltered.length === 0) {
      container.innerHTML = `
        <div class="status-card">
          <p>No questions match the current filters. Try clearing your search or changing topic/status filters.</p>
        </div>
      `;
      $('#pagination-bar').classList.add('hidden');
      $('#focus-nav-bar').classList.add('hidden');
      return;
    }

    if (state.focusMode) {
      if (state.focusIdx >= currentFiltered.length) state.focusIdx = currentFiltered.length - 1;
      if (state.focusIdx < 0) state.focusIdx = 0;

      const q = currentFiltered[state.focusIdx];
      const topicObj = TOPICS.find(t => t.id === q.topicId);
      $('#focus-counter').textContent = `Q ${state.focusIdx + 1} / ${currentFiltered.length}`;
      $('#focus-topic-chip').textContent = topicObj ? topicObj.en : '';
      container.innerHTML = renderCardHTML(q);

      $('#pagination-bar').classList.add('hidden');
      $('#focus-nav-bar').classList.remove('hidden');
      $('#focus-prev').disabled = state.focusIdx === 0;
      $('#focus-next').disabled = state.focusIdx >= currentFiltered.length - 1;
      $('#focus-bookmark').textContent = state.bookmarkedIds.has(q.gid) ? '📌 Saved' : '📌 Save';

      const isOpen = state.studyMode === 'revise' || state.revealedIds.has(q.gid);
      $('#focus-reveal').classList.toggle('hidden', isOpen);
      return;
    }

    // List mode pagination
    const totalPages = Math.max(1, Math.ceil(currentFiltered.length / PAGE_SIZE));
    if (state.page > totalPages) state.page = totalPages;
    if (state.page < 1) state.page = 1;

    const start = (state.page - 1) * PAGE_SIZE;
    const slice = currentFiltered.slice(start, start + PAGE_SIZE);

    container.innerHTML = slice.map(renderCardHTML).join('');
    $('#pagination-bar').classList.remove('hidden');
    $('#focus-nav-bar').classList.add('hidden');
    $('#page-current').textContent = state.page;
    $('#page-total').textContent = totalPages;
    $('#btn-prev-page').disabled = state.page <= 1;
    $('#btn-next-page').disabled = state.page >= totalPages;
  }

  function renderTimeline() {
    const query = state.timelineQuery.trim().toLowerCase();
    const withYears = state.questions.filter(q => typeof q.yr === 'number' && !isNaN(q.yr));

    const filtered = withYears.filter(q => {
      const y = q.yr;
      if (state.eraFilter === 'pre1900' && y >= 1900) return false;
      if (state.eraFilter === '1900_1947' && (y < 1900 || y > 1947)) return false;
      if (state.eraFilter === '1948_1975' && (y < 1948 || y > 1975)) return false;
      if (state.eraFilter === '1976_1999' && (y < 1976 || y > 1999)) return false;
      if (state.eraFilter === '2000_plus' && y < 2000) return false;

      if (query) {
        const text = `${y} ${q.yre || ''} ${q.yrh || ''} ${q.qe} ${q.qh}`.toLowerCase();
        if (!text.includes(query)) return false;
      }
      return true;
    });

    // Group by year ascending
    const byYear = new Map();
    for (const q of filtered) {
      if (!byYear.has(q.yr)) byYear.set(q.yr, []);
      byYear.get(q.yr).push(q);
    }
    const yearsSorted = Array.from(byYear.keys()).sort((a, b) => a - b);

    const cont = $('#timeline-container');
    if (yearsSorted.length === 0) {
      cont.innerHTML = '<div class="status-card"><p>No chronological milestones match this filter.</p></div>';
      return;
    }

    cont.innerHTML = yearsSorted.map(y => {
      const list = byYear.get(y);
      // Deduplicate identical year descriptions cleanly while keeping link to question
      const itemsHTML = list.map(q => `
        <div class="timeline-event-item" data-jump-gid="${q.gid}">
          <div class="hi-only"><strong>#${q.gid}:</strong> ${esc(q.yrh || q.qh)}</div>
          <div class="en-only ${state.lang === 'bi' ? 'exp-text-en' : ''}">${esc(q.yre || q.qe)}</div>
        </div>
      `).join('');

      return `
        <div class="timeline-year-group">
          <div class="timeline-year-header">
            <span class="timeline-year-pill">${y}</span>
            <span class="badge">${list.length} Milestone${list.length > 1 ? 's' : ''}</span>
          </div>
          <div class="timeline-event-list">${itemsHTML}</div>
        </div>
      `;
    }).join('');
  }

  function renderPlan() {
    const grid = $('#plan-grid');
    grid.innerHTML = DAYS_PLAN.map(d => {
      const subset = state.questions.filter(q => {
        const sNum = d.filter.view === 'set1' ? 1 : 2;
        return q.set === sNum && d.filter.topics.includes(q.topicId);
      });
      const done = subset.filter(q => state.revisedIds.has(q.gid)).length;
      const pct = subset.length ? Math.round((done / subset.length) * 100) : 0;

      return `
        <div class="day-card">
          <div>
            <span class="day-badge">DAY ${d.day} • ${subset.length} Qs</span>
            <h3 class="hi-only">${esc(d.hiTitle)}</h3>
            <h3 class="en-only">${esc(d.title)}</h3>
            <p class="day-topics">${esc(d.desc)}</p>
          </div>
          <div>
            <div class="progress-stats" style="margin-bottom:0.3rem;">
              <span>Progress</span>
              <strong>${done}/${subset.length} (${pct}%)</strong>
            </div>
            <div class="progress-bar-track" style="margin-bottom:0.65rem;">
              <div class="progress-bar-fill" style="width:${pct}%"></div>
            </div>
            <button class="day-btn" data-start-day="${d.day}">Start Day ${d.day} Revision →</button>
          </div>
        </div>
      `;
    }).join('');
  }

  function switchView(viewName) {
    state.view = viewName;
    if (viewName !== 'plan' && viewName !== 'timeline') {
      // Keep dayTopics only if triggered from Start Day; clear on manual tab click
    }
    $$('.nav-tab').forEach(b => b.classList.toggle('active', b.dataset.view === viewName));

    const isTimeline = viewName === 'timeline';
    const isPlan = viewName === 'plan';

    $('#timeline-view').classList.toggle('hidden', !isTimeline);
    $('#plan-view').classList.toggle('hidden', !isPlan);
    $('#practice-view').classList.toggle('hidden', isTimeline || isPlan);
    $('#controls-panel').classList.toggle('hidden', isTimeline || isPlan || state.focusMode);

    if (isTimeline) renderTimeline();
    else if (isPlan) renderPlan();
    else renderPractice();
  }

  function toggleFocusMode(on) {
    state.focusMode = typeof on === 'boolean' ? on : !state.focusMode;
    document.body.classList.toggle('in-focus', state.focusMode);
    $('#main-header').classList.toggle('hidden', state.focusMode);
    $('#controls-panel').classList.toggle('hidden', state.focusMode || state.view === 'timeline' || state.view === 'plan');
    $('#focus-hud').classList.toggle('hidden', !state.focusMode);

    if (state.focusMode && (state.view === 'timeline' || state.view === 'plan')) {
      switchView('set1');
      return;
    }
    renderPractice();
    window.scrollTo({ top: 0, behavior: 'instant' });
  }

  // Data Loading
  function normalizeQuestion(raw, idx) {
    const textForSearch = [
      raw.gid, raw.qe, raw.qh,
      raw.a && raw.a[0], raw.a && raw.a[1],
      raw.b && raw.b[0], raw.b && raw.b[1],
      raw.c && raw.c[0], raw.c && raw.c[1],
      raw.d && raw.d[0], raw.d && raw.d[1],
      raw.ce, raw.ch, raw.yre, raw.yrh, raw.yr
    ].filter(Boolean).join(' ').toLowerCase();
    raw._search = textForSearch;
    return raw;
  }

  async function fetchData() {
    $('#top-loader').classList.remove('hidden');
    try {
      const res1 = await fetch('data/set1.json');
      if (res1.ok) {
        const d1 = await res1.json();
        state.questions = d1.map(normalizeQuestion);
        state.set1Loaded = true;
        renderPractice();
      }
    } catch (e) {
      $('#loading-card').innerHTML = '<p>Unable to load Set 1 data. Please refresh.</p>';
    }

    try {
      const res2 = await fetch('data/set2.json');
      if (res2.ok) {
        const d2 = await res2.json();
        state.questions = state.questions.concat(d2.map(normalizeQuestion));
        state.set2Loaded = true;
        if (state.view === 'timeline') renderTimeline();
        else if (state.view === 'plan') renderPlan();
        else renderPractice();
      }
    } catch (_) {}

    $('#top-loader').classList.add('hidden');
  }

  // Event Delegation
  function bindEvents() {
    // Nav tabs
    $$('.nav-tab').forEach(btn => {
      btn.addEventListener('click', () => {
        state.dayTopics = null;
        state.page = 1;
        state.focusIdx = 0;
        switchView(btn.dataset.view);
      });
    });

    // Study mode
    const setMode = (m) => {
      state.studyMode = m;
      savePrefs();
      applyAppearance();
      renderPractice();
    };
    $('#btn-mode-revise').addEventListener('click', () => setMode('revise'));
    $('#focus-mode-revise').addEventListener('click', () => setMode('revise'));
    $('#btn-mode-recall').addEventListener('click', () => setMode('recall'));
    $('#focus-mode-recall').addEventListener('click', () => setMode('recall'));

    // Languages
    $$('.lang-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        state.lang = btn.dataset.lang;
        savePrefs();
        applyAppearance();
      });
    });

    // Themes
    $$('.theme-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        state.theme = btn.dataset.theme;
        savePrefs();
        applyAppearance();
      });
    });

    $('#focus-theme-cycle').addEventListener('click', () => {
      const order = ['sepia', 'light', 'dark'];
      state.theme = order[(order.indexOf(state.theme) + 1) % order.length];
      savePrefs();
      applyAppearance();
    });

    // Font Size
    const chgFont = (delta) => {
      state.fontSize = Math.min(22, Math.max(13, state.fontSize + delta));
      savePrefs();
      applyAppearance();
    };
    $('#btn-font-dec').addEventListener('click', () => chgFont(-1));
    $('#focus-font-dec').addEventListener('click', () => chgFont(-1));
    $('#btn-font-inc').addEventListener('click', () => chgFont(1));
    $('#focus-font-inc').addEventListener('click', () => chgFont(1));

    // Focus toggle
    $('#btn-focus-toggle').addEventListener('click', () => toggleFocusMode(true));
    $('#btn-exit-focus').addEventListener('click', () => toggleFocusMode(false));

    // Filters
    let searchTimer = null;
    $('#search-input').addEventListener('input', (e) => {
      state.searchQuery = e.target.value;
      $('#btn-clear-search').classList.toggle('hidden', !state.searchQuery);
      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => {
        state.page = 1;
        state.focusIdx = 0;
        renderPractice();
      }, 180);
    });

    $('#btn-clear-search').addEventListener('click', () => {
      $('#search-input').value = '';
      state.searchQuery = '';
      $('#btn-clear-search').classList.add('hidden');
      state.page = 1;
      renderPractice();
    });

    $('#topic-select').addEventListener('change', (e) => {
      state.dayTopics = null;
      state.topicFilter = e.target.value;
      state.page = 1;
      state.focusIdx = 0;
      renderPractice();
    });

    $('#priority-select').addEventListener('change', (e) => {
      state.priorityFilter = e.target.value;
      state.page = 1;
      state.focusIdx = 0;
      renderPractice();
    });

    $('#status-select').addEventListener('change', (e) => {
      state.statusFilter = e.target.value;
      state.page = 1;
      state.focusIdx = 0;
      renderPractice();
    });

    $('#btn-toggle-wrong').addEventListener('click', () => {
      state.showWrongs = !state.showWrongs;
      const btn = $('#btn-toggle-wrong');
      btn.classList.toggle('active', state.showWrongs);
      btn.textContent = `❌ 3 Wrong Explanations: ${state.showWrongs ? 'ON' : 'OFF'}`;
      renderPractice();
    });

    const refreshSingleOrAll = (gid) => {
      if (state.focusMode) { renderPractice(); return; }
      const qObj = currentFiltered.find(x => x.gid === gid);
      const cardEl = document.querySelector(`.q-card[data-gid="${gid}"]`);
      if (qObj && cardEl && state.statusFilter === 'all') {
        cardEl.outerHTML = renderCardHTML(qObj);
        updateStats(currentFiltered.length);
      } else {
        renderPractice();
      }
    };

    // Card interactions via delegation
    $('#questions-container').addEventListener('click', (e) => {
      const yrBtn = e.target.closest('[data-year-jump]');
      if (yrBtn) {
        const y = yrBtn.dataset.yearJump;
        state.timelineQuery = String(y);
        state.eraFilter = 'all';
        $$('.era-chip').forEach(x => x.classList.toggle('active', x.dataset.era === 'all'));
        $('#timeline-search').value = String(y);
        if (state.focusMode) toggleFocusMode(false);
        switchView('timeline');
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }

      const optBtn = e.target.closest('.opt-btn');
      if (optBtn && state.studyMode === 'recall') {
        const gid = Number(optBtn.dataset.gid);
        const opt = optBtn.dataset.opt;
        state.userAnswers.set(gid, opt);
        state.revealedIds.add(gid);
        refreshSingleOrAll(gid);
        return;
      }

      const revBtn = e.target.closest('[data-reveal]');
      if (revBtn) {
        const gid = Number(revBtn.dataset.reveal);
        state.revealedIds.add(gid);
        refreshSingleOrAll(gid);
        return;
      }

      const bmBtn = e.target.closest('[data-bookmark]');
      if (bmBtn) {
        const gid = Number(bmBtn.dataset.bookmark);
        if (state.bookmarkedIds.has(gid)) state.bookmarkedIds.delete(gid);
        else state.bookmarkedIds.add(gid);
        savePrefs();
        refreshSingleOrAll(gid);
        return;
      }

      const doneBtn = e.target.closest('[data-revise]');
      if (doneBtn) {
        const gid = Number(doneBtn.dataset.revise);
        if (state.revisedIds.has(gid)) state.revisedIds.delete(gid);
        else state.revisedIds.add(gid);
        savePrefs();
        refreshSingleOrAll(gid);
      }
    });

    $('#day-filter-badge').addEventListener('click', () => {
      state.dayTopics = null;
      state.page = 1;
      state.focusIdx = 0;
      renderPractice();
    });

    // Pagination
    $('#btn-prev-page').addEventListener('click', () => {
      state.page--;
      renderPractice();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    $('#btn-next-page').addEventListener('click', () => {
      state.page++;
      renderPractice();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    $('#btn-jump-q').addEventListener('click', () => {
      const qn = parseInt($('#jump-q-input').value, 10);
      if (!isNaN(qn) && qn >= 1) {
        const maxP = Math.max(1, Math.ceil(currentFiltered.length / PAGE_SIZE));
        const idx = currentFiltered.findIndex(q => q.gid === qn);
        if (idx >= 0) state.page = Math.floor(idx / PAGE_SIZE) + 1;
        else state.page = Math.min(maxP, Math.max(1, Math.ceil(qn / PAGE_SIZE)));
        renderPractice();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    });

    // Focus Nav Bar
    $('#focus-prev').addEventListener('click', () => {
      if (state.focusIdx > 0) { state.focusIdx--; renderPractice(); window.scrollTo(0, 0); }
    });
    $('#focus-next').addEventListener('click', () => {
      if (state.focusIdx < currentFiltered.length - 1) { state.focusIdx++; renderPractice(); window.scrollTo(0, 0); }
    });
    $('#focus-reveal').addEventListener('click', () => {
      const q = currentFiltered[state.focusIdx];
      if (q) { state.revealedIds.add(q.gid); renderPractice(); }
    });
    $('#focus-bookmark').addEventListener('click', () => {
      const q = currentFiltered[state.focusIdx];
      if (!q) return;
      if (state.bookmarkedIds.has(q.gid)) state.bookmarkedIds.delete(q.gid);
      else state.bookmarkedIds.add(q.gid);
      savePrefs();
      renderPractice();
    });
    $('#focus-revise-mark').addEventListener('click', () => {
      const q = currentFiltered[state.focusIdx];
      if (q) {
        state.revisedIds.add(q.gid);
        savePrefs();
      }
      if (state.focusIdx < currentFiltered.length - 1) state.focusIdx++;
      renderPractice();
      window.scrollTo(0, 0);
    });

    // Timeline events
    $$('.era-chip').forEach(c => {
      c.addEventListener('click', () => {
        state.eraFilter = c.dataset.era;
        $$('.era-chip').forEach(x => x.classList.toggle('active', x === c));
        renderTimeline();
      });
    });
    $('#timeline-search').addEventListener('input', (e) => {
      state.timelineQuery = e.target.value;
      renderTimeline();
    });
    $('#timeline-container').addEventListener('click', (e) => {
      const item = e.target.closest('[data-jump-gid]');
      if (!item) return;
      const gid = Number(item.dataset.jumpGid);
      state.dayTopics = null;
      state.topicFilter = 'all';
      state.priorityFilter = 'all';
      state.statusFilter = 'all';
      state.searchQuery = '';
      $('#topic-select').value = 'all';
      $('#priority-select').value = 'all';
      $('#status-select').value = 'all';
      $('#search-input').value = '';
      switchView('all');
      const idx = currentFiltered.findIndex(q => q.gid === gid);
      if (idx >= 0) {
        state.focusIdx = idx;
        state.page = Math.floor(idx / PAGE_SIZE) + 1;
        toggleFocusMode(true);
      }
    });

    // 4-Day Plan clicks
    $('#plan-grid').addEventListener('click', (e) => {
      const btn = e.target.closest('[data-start-day]');
      if (!btn) return;
      const d = DAYS_PLAN.find(x => x.day === Number(btn.dataset.startDay));
      if (!d) return;
      state.dayTopics = d.filter.topics;
      state.topicFilter = 'all';
      $('#topic-select').value = 'all';
      state.page = 1;
      state.focusIdx = 0;
      switchView(d.filter.view);
    });

    $('#btn-reset-progress').addEventListener('click', () => {
      if (confirm('Reset all revised & bookmarked tracking?')) {
        state.revisedIds.clear();
        state.bookmarkedIds.clear();
        savePrefs();
        renderPlan();
        updateStats(currentFiltered.length);
      }
    });

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
      if (['INPUT', 'SELECT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
      if (e.key === 'f' || e.key === 'F') {
        e.preventDefault();
        toggleFocusMode();
      } else if (e.key === 'Escape' && state.focusMode) {
        toggleFocusMode(false);
      } else if (state.focusMode) {
        const q = currentFiltered[state.focusIdx];
        if (e.key === 'ArrowRight' && state.focusIdx < currentFiltered.length - 1) {
          state.focusIdx++; renderPractice(); window.scrollTo(0, 0);
        } else if (e.key === 'ArrowLeft' && state.focusIdx > 0) {
          state.focusIdx--; renderPractice(); window.scrollTo(0, 0);
        } else if (e.key === ' ' && q && state.studyMode === 'recall') {
          e.preventDefault();
          state.revealedIds.add(q.gid); renderPractice();
        } else if ((e.key === 'b' || e.key === 'B') && q) {
          if (state.bookmarkedIds.has(q.gid)) state.bookmarkedIds.delete(q.gid);
          else state.bookmarkedIds.add(q.gid);
          savePrefs(); renderPractice();
        } else if ((e.key === 'r' || e.key === 'R') && q) {
          state.revisedIds.add(q.gid); savePrefs();
          if (state.focusIdx < currentFiltered.length - 1) state.focusIdx++;
          renderPractice(); window.scrollTo(0, 0);
        }
      }
    });

    // Touch swipe for Focus Mode mobile
    let touchX = null;
    document.addEventListener('touchstart', (e) => {
      if (state.focusMode && e.touches.length === 1) touchX = e.touches[0].clientX;
    }, { passive: true });
    document.addEventListener('touchend', (e) => {
      if (!state.focusMode || touchX === null || e.changedTouches.length !== 1) return;
      const dx = e.changedTouches[0].clientX - touchX;
      touchX = null;
      if (Math.abs(dx) > 65) {
        if (dx < 0 && state.focusIdx < currentFiltered.length - 1) {
          state.focusIdx++; renderPractice(); window.scrollTo(0, 0);
        } else if (dx > 0 && state.focusIdx > 0) {
          state.focusIdx--; renderPractice(); window.scrollTo(0, 0);
        }
      }
    }, { passive: true });
  }

  // Init
  loadPrefs();
  populateTopicDropdown();
  applyAppearance();
  bindEvents();
  fetchData();
})();
