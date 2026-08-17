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

    // Search Items & Recipes
    if (WIKI_DATA.items) {
      WIKI_DATA.items.forEach(item => {
        const text = `${item.name} ${item.name_vi} ${item.mod} ${item.classTags.join(' ')} ${item.category} ${item.recipe}`.toLowerCase();
        if (!query || text.includes(query)) {
          if (count++ > 15) return;
          const div = document.createElement('div');
          div.className = 'search-result-item';
          div.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <div style="display:flex; align-items:center; gap:0.5rem;">
                <img src="${item.icon}" alt="${item.name}" width="20" height="20" style="image-rendering:pixelated;" onerror="this.src='images/logo.svg'">
                <strong style="color:var(--accent-gold); font-family:var(--font-title); font-size:0.9rem;"><span class="vi-text">${item.name_vi}</span><span class="en-text">${item.name}</span></strong>
              </div>
              <span class="badge badge-cyan">${item.stage}</span>
            </div>
            <div style="font-size:0.8rem; color:var(--text-muted); margin-top:3px;">
              ${item.mod} • ${item.classTags.join(', ')} • 📜 ${item.recipe}
            </div>
          `;
          div.addEventListener('click', () => {
            window.location.href = `items.html#item-${item.id}`;
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
   Item Modal Popup Component (Bidirectional Graph Navigation)
   ========================================================================== */
let modalHistoryStack = [];

function openItemModal(itemId, isBackNav = false) {
  // Try finding in graph database first, then standard items
  let item = null;
  if (typeof ITEM_GRAPH_DATABASE !== 'undefined') {
    item = ITEM_GRAPH_DATABASE.find(i => i.id === itemId);
  }
  if (!item && WIKI_DATA.items) {
    item = WIKI_DATA.items.find(i => i.id === itemId);
  }

  if (!item) {
    console.warn(`Item not found: ${itemId}`);
    return;
  }

  if (!isBackNav) {
    modalHistoryStack.push(itemId);
  }

  let modal = document.getElementById('item-detail-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'item-detail-modal';
    modal.className = 'modal-backdrop';
    document.body.appendChild(modal);
  }

  const hasHistory = modalHistoryStack.length > 1;

  // Build ingredients interactive chips
  let ingredientsHTML = '';
  if (item.ingredients && item.ingredients.length > 0) {
    ingredientsHTML = `
      <div style="margin-top:8px;">
        <div style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:4px;"><span class="vi-text">Nguyên Liệu Cần (Nhấp để xem):</span><span class="en-text">Click Ingredients to Inspect:</span></div>
        <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
          ${item.ingredients.map(ing => `
            <button class="ingredient-chip" onclick="openItemModal('${ing.id}')" title="Xem chi tiết ${ing.name}">
              <img src="images/items/${ing.id}.png" onerror="this.src='images/logo.svg'" width="16" height="16" style="image-rendering:pixelated;">
              <span>${ing.count}x ${ing.name_vi || ing.name}</span>
            </button>
          `).join('')}
        </div>
      </div>
    `;
  }

  // Build used_in reverse crafting chips
  let usedInHTML = '';
  if (item.used_in && item.used_in.length > 0) {
    usedInHTML = `
      <div class="used-in-box">
        <div style="font-size:0.8rem; color:var(--accent-cyan); font-weight:700; margin-bottom:6px;">
          🔨 <span class="vi-text">DÙNG ĐỂ CHẾ TẠO RA (CRAFTS INTO):</span><span class="en-text">USED IN RECIPES:</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(130px, 1fr)); gap:0.5rem;">
          ${item.used_in.map(u => `
            <div class="used-in-chip" onclick="openItemModal('${u.id}')" title="Nhấp để xem công thức rèn ${u.name}">
              <img src="${u.icon}" onerror="this.src='images/logo.svg'" width="22" height="22" style="image-rendering:pixelated;">
              <div class="used-in-name">${u.name_vi || u.name}</div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  modal.innerHTML = `
    <div class="item-modal-box">
      <div class="item-modal-header">
        <div style="display:flex; align-items:center; gap:0.65rem;">
          ${hasHistory ? `<button onclick="goBackItemModal()" class="modal-back-btn" title="Quay lại item trước">←</button>` : ''}
          <div class="item-icon-frame">
            <img src="${item.icon}" alt="${item.name}" onerror="this.src='images/logo.svg'">
          </div>
          <div>
            <h3 style="margin:0; font-size:1.05rem; color:#fff;"><span class="vi-text">${item.name_vi}</span><span class="en-text">${item.name}</span></h3>
            <div style="font-size:0.75rem; color:var(--text-muted);">${item.mod} • <span class="badge badge-cyan">${item.stage} Stage</span></div>
          </div>
        </div>
        <button onclick="closeItemModal()" style="background:none; border:none; color:var(--text-muted); font-size:1.2rem; cursor:pointer;">✖</button>
      </div>

      <div class="item-modal-body">
        <!-- Class Tags -->
        <div>
          <div style="font-size:0.72rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:4px;"><span class="vi-text">Hệ Phái Tương Thích:</span><span class="en-text">Class Tags:</span></div>
          <div class="item-tag-list">
            ${item.classTags.map(tag => `<span class="tag-pill tag-${tag.toLowerCase().includes('mage') ? 'mage' : tag.toLowerCase().includes('fire') ? 'fire' : tag.toLowerCase().includes('warrior') ? 'warrior' : tag.toLowerCase().includes('paladin') ? 'paladin' : 'ranger'}">${tag}</span>`).join('')}
          </div>
        </div>

        <!-- Recipe -->
        <div class="recipe-box">
          <div style="font-size:0.78rem; color:var(--accent-gold); font-weight:700; margin-bottom:4px;">⚒️ <span class="vi-text">CÔNG THỨC CHẾ TẠO:</span><span class="en-text">CRAFTING RECIPE:</span></div>
          <div style="font-size:0.85rem; color:#fff; font-family:var(--font-title);">${item.recipe_desc_vi || item.recipe || 'Không có công thức craft'}</div>
          ${ingredientsHTML}
        </div>

        <!-- Effects -->
        <div>
          <div style="font-size:0.78rem; color:var(--accent-gold); font-weight:700; margin-bottom:4px;">✨ <span class="vi-text">HIỆU ỨNG & ĐẶC TÍNH:</span><span class="en-text">EFFECTS & TRAITS:</span></div>
          <div style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
            <span class="vi-text">${item.effects_vi || ''}</span>
            <span class="en-text">${item.effects_en || ''}</span>
          </div>
        </div>

        <!-- Used In Recipes (Reverse Graph) -->
        ${usedInHTML}

        <!-- Location Source & Breadcrumb Link -->
        <div style="background:rgba(0,0,0,0.25); padding:0.65rem 0.85rem; border-radius:6px; border:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
          <div>
            <div style="font-size:0.72rem; color:var(--text-muted);"><span class="vi-text">Vị trí / Nguồn tìm kiếm:</span><span class="en-text">Obtain Source:</span></div>
            <div style="font-size:0.82rem; color:var(--text-primary); margin-top:2px;">
              📍 <span class="vi-text">${item.source_location_vi || ''}</span><span class="en-text">${item.source_location_en || ''}</span>
            </div>
          </div>
          ${item.source_url ? `<a href="${item.source_url}" class="source-link-btn"><span class="vi-text">Xem Vùng / Boss →</span><span class="en-text">Go To Location →</span></a>` : ''}
        </div>
      </div>
    </div>
  `;

  modal.classList.add('open');
  modal.onclick = (e) => {
    if (e.target === modal) closeItemModal();
  };
}

function closeItemModal() {
  const modal = document.getElementById('item-detail-modal');
  if (modal) modal.classList.remove('open');
  modalHistoryStack = [];
}

function goBackItemModal() {
  if (modalHistoryStack.length > 1) {
    modalHistoryStack.pop(); // Remove current
    const prevId = modalHistoryStack.pop(); // Get previous
    openItemModal(prevId);
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
