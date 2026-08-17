/**
 * Terramity Awakened Wiki - Core App Logic & Interactivity
 */

document.addEventListener('DOMContentLoaded', () => {
  initLanguage();
  initSearch();
  initChecklist();
  highlightActiveNav();
});

/* ==========================================================================
   Language Switcher System
   ========================================================================== */
function initLanguage() {
  const savedLang = localStorage.getItem('wiki_lang') || 'vi';
  setLanguage(savedLang);

  const langBtn = document.getElementById('lang-toggle-btn');
  if (langBtn) {
    langBtn.addEventListener('click', () => {
      const current = document.body.classList.contains('lang-en') ? 'en' : 'vi';
      const next = current === 'vi' ? 'en' : 'vi';
      setLanguage(next);
    });
  }
}

function setLanguage(lang) {
  document.body.classList.remove('lang-vi', 'lang-en');
  document.body.classList.add(`lang-${lang}`);
  localStorage.setItem('wiki_lang', lang);

  const langLabel = document.getElementById('lang-label');
  if (langLabel) {
    langLabel.textContent = lang === 'vi' ? '🇻🇳 VI' : '🇬🇧 EN';
  }
}

/* ==========================================================================
   Active Nav Indicator
   ========================================================================== */
function highlightActiveNav() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

/* ==========================================================================
   Global Search System
   ========================================================================== */
function initSearch() {
  const searchBtn = document.getElementById('btn-open-search');
  const modal = document.getElementById('search-modal');
  const searchInput = document.getElementById('global-search-input');
  const resultsContainer = document.getElementById('search-results-list');

  if (!modal || !searchInput) return;

  function openSearch() {
    modal.classList.add('open');
    searchInput.focus();
    performSearch('');
  }

  function closeSearch() {
    modal.classList.remove('open');
    searchInput.value = '';
  }

  if (searchBtn) searchBtn.addEventListener('click', openSearch);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeSearch();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {
      e.preventDefault();
      openSearch();
    }
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      closeSearch();
    }
  });

  searchInput.addEventListener('input', (e) => {
    performSearch(e.target.value.trim().toLowerCase());
  });

  function performSearch(query) {
    if (!resultsContainer) return;
    resultsContainer.innerHTML = '';

    const lang = document.body.classList.contains('lang-en') ? 'en' : 'vi';
    let count = 0;

    // Search Bosses
    if (WIKI_DATA.bosses) {
      WIKI_DATA.bosses.forEach(b => {
        const text = `${b.name} ${b.mod} ${b.dimension} ${b.location} ${b.location_vi}`.toLowerCase();
        if (!query || text.includes(query)) {
          if (count++ > 15) return;
          const div = document.createElement('div');
          div.className = 'search-result-item';
          div.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <strong style="color:var(--accent-cyan); font-family:var(--font-title); font-size:0.95rem;">🗡️ ${b.name}</strong>
              <span class="badge badge-crimson">${b.stars} (${b.hp.toLocaleString()} HP)</span>
            </div>
            <div style="font-size:0.82rem; color:var(--text-muted); margin-top:3px;">
              ${b.mod} • ${b.dimension} • ${lang === 'vi' ? b.location_vi : b.location}
            </div>
          `;
          div.addEventListener('click', () => {
            window.location.href = `bosses.html#boss-${b.id}`;
          });
          resultsContainer.appendChild(div);
        }
      });
    }

    // Search Dimensions
    if (WIKI_DATA.dimensions) {
      WIKI_DATA.dimensions.forEach(d => {
        const text = `${d.name} ${d.name_vi} ${d.portal} ${d.portal_vi}`.toLowerCase();
        if (!query || text.includes(query)) {
          if (count++ > 15) return;
          const div = document.createElement('div');
          div.className = 'search-result-item';
          div.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <strong style="color:var(--accent-purple); font-family:var(--font-title); font-size:0.95rem;">🌌 ${lang === 'vi' ? d.name_vi : d.name}</strong>
              <span class="badge badge-purple">Dimension</span>
            </div>
            <div style="font-size:0.82rem; color:var(--text-muted); margin-top:3px;">
              ${lang === 'vi' ? d.portal_vi : d.portal}
            </div>
          `;
          div.addEventListener('click', () => {
            window.location.href = `dimensions.html#dim-${d.id}`;
          });
          resultsContainer.appendChild(div);
        }
      });
    }

    if (count === 0) {
      resultsContainer.innerHTML = `
        <div style="text-align:center; padding:2rem; color:var(--text-muted);">
          ${lang === 'vi' ? 'Không tìm thấy kết quả phù hợp.' : 'No matching results found.'}
        </div>
      `;
    }
  }
}

/* ==========================================================================
   Checklist / Progress Persistence
   ========================================================================== */
function initChecklist() {
  document.querySelectorAll('.checklist-item input[type="checkbox"]').forEach(box => {
    const key = `check_${box.id || box.name || box.getAttribute('data-id')}`;
    const isDone = localStorage.getItem(key) === 'true';
    box.checked = isDone;
    if (isDone) box.parentElement.classList.add('done');

    box.addEventListener('change', (e) => {
      localStorage.setItem(key, e.target.checked);
      if (e.target.checked) {
        box.parentElement.classList.add('done');
      } else {
        box.parentElement.classList.remove('done');
      }
    });
  });
}
