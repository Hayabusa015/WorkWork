/* Icons and the dashboard layout editor.
   Markup lives in app.js; this file owns only the icon set and the
   drag-to-rearrange behaviour on Today. */

const paths = {
  home:      'm3 10 9-7 9 7v10H7V10m8 10v-7H9v7',
  plus:      'M12 4v16M4 12h16',
  folder:    'M3 6h7l2 3h9v11H3Z',
  clipboard: 'M9 5H5v16h14V5h-4M9 3h6v4H9ZM8 12h8M8 16h6',
  target:    'M20 12a8 8 0 1 1-8-8m0 4a4 4 0 1 0 4 4m-4 0L21 3m-5 0h5v5',
  settings:  'M9 3h6l1 3 3 1 2 5-2 5-3 1-1 3H9l-1-3-3-1-2-5 2-5 3-1ZM12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8',
  pen:       'm5 16-1 5 5-1L21 8l-5-5ZM13 6l5 5M4 21h16',
  file:      'M5 3h9l5 5v13H5ZM14 3v6h5M8 13h8M8 17h6',
  check:     'm5 12 4 4L19 6',
  search:    'M10 3a7 7 0 1 0 0 14 7 7 0 0 0 0-14m5 12 6 6',
  printer:   'M6 9V3h12v6M6 18H3V9h18v9h-3M6 14h12v7H6ZM17 12h1',
  flask:     'M9 3h6M10 3v7L4 20h16l-6-10V3M8 15h8',
  atom:      'M12 10v4m-2-2h4M4 5c-5 5 10 19 15 14S9 0 4 5m0 14C-1 14 14 0 19 5S9 24 4 19',
  mountain:  'm2 20 7-14 5 9 3-5 5 10ZM6 12l3 2 2-3',
  arrow:     'M4 12h16m-6-6 6 6-6 6',
  chevron:   'm9 5 7 7-7 7',
  // Added for the desk and the gallery.
  inbox:     'M3 13h5l1 3h6l1-3h5M3 13l3-9h12l3 9v7H3Z',
  layers:    'm12 3 9 5-9 5-9-5Zm9 9-9 5-9-5m18 4-9 5-9-5',
  team:      'M9 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6m-6 9v-1a6 6 0 0 1 12 0v1M17 6a3 3 0 0 1 0 6m4 8v-1a5 5 0 0 0-3-4.6',
  quill:     'M4 20s1-7 7-11 9-5 9-5 0 6-3 10-8 5-8 5l-3 1Zm3-1 6-6',
  slides:    'M3 4h18v11H3Zm6 15 3-4 3 4M12 4v11',
  notes:     'M6 3h12v18H6Zm4 0v18M13 8h3M13 12h3M13 16h2',
  beaker:    'M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3M7 15h10',
  page:      'M6 3h8l4 4v14H6ZM14 3v4h4M9 12h6M9 16h4',
  eye:       'M2 12s4-6 10-6 10 6 10 6-4 6-10 6-10-6-10-6m10 3a3 3 0 1 0 0-6 3 3 0 0 0 0 6',
};

export const icon = name =>
  `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" ` +
  `stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">` +
  `<path d="${paths[name] || paths.file}"/></svg>`;

/* ------------------------------------------------------------------ *\
   Dashboard layout editor
\* ------------------------------------------------------------------ */

// v2: the Today dashboard changed shape when the Secretary moved to its own
// desk, so a v1 layout no longer describes the panels on the page.
const layoutKey = 'shull-dashboard-layout-v2';
const panelIds = ['create', 'pipeline', 'classes', 'progress', 'credits', 'desk', 'focus', 'recent'];
const defaultLayout = [panelIds.slice(0, 4), panelIds.slice(4)];

let layoutEditing = false, layoutDraft = null, stopLayoutDrag = () => {};
export const isLayoutEditing = () => layoutEditing;

function readLayout() {
  try {
    const value = JSON.parse(localStorage.getItem(layoutKey));
    if (Array.isArray(value) && value.length === 2 && value.every(Array.isArray)) {
      const flat = value.flat();
      if (flat.length === panelIds.length && new Set(flat).size === panelIds.length
          && flat.every(x => panelIds.includes(x))) return value;
    }
  } catch {}
  return defaultLayout.map(c => [...c]);
}

export function mountLayoutEditor(tab) {
  stopLayoutDrag();
  document.querySelector('#layout-toolbar')?.remove();
  document.querySelector('#layout-help')?.remove();
  if (tab !== 'Today') { layoutEditing = false; layoutDraft = null; return; }

  const grid = document.querySelector('#content>.grid');
  if (!grid) return;
  const columns = [...grid.children];
  const panels = [...grid.querySelectorAll(':scope>.stack>.panel')];
  const byId = new Map(panels.map((p, i) => { p.dataset.panelId = panelIds[i]; return [panelIds[i], p]; }));
  const capture = () => columns.map(c => [...c.querySelectorAll(':scope>.panel')].map(p => p.dataset.panelId));
  const apply = layout => layout.forEach((ids, i) => ids.forEach(id => byId.get(id) && columns[i].append(byId.get(id))));
  apply(layoutEditing && layoutDraft ? layoutDraft : readLayout());

  const toolbar = document.createElement('div');
  toolbar.id = 'layout-toolbar';
  toolbar.innerHTML = '<button id="layout-toggle" type="button">Edit layout</button>' +
                      '<button id="layout-cancel" type="button">Cancel</button>' +
                      '<button id="layout-reset" type="button">Reset layout</button>';
  document.querySelector('main>header').append(toolbar);

  const help = document.createElement('p');
  help.id = 'layout-help';
  help.setAttribute('role', 'status');
  grid.before(help);
  const announce = text => { help.textContent = text; };

  function update() {
    grid.classList.toggle('layout-editing', layoutEditing);
    const toggle = toolbar.querySelector('#layout-toggle');
    toggle.textContent = layoutEditing ? 'Save layout' : 'Edit layout';
    toggle.setAttribute('aria-pressed', String(layoutEditing));
    for (const id of ['layout-cancel', 'layout-reset']) toolbar.querySelector('#' + id).hidden = !layoutEditing;
    panels.forEach(p => p.querySelector('.panel-grip').hidden = !layoutEditing);
    announce(layoutEditing
      ? 'Drag a handle to move a panel. Use arrow keys on a focused handle to move it by keyboard.'
      : '');
  }

  toolbar.querySelector('#layout-toggle').onclick = () => {
    stopLayoutDrag();
    if (layoutEditing) {
      try { localStorage.setItem(layoutKey, JSON.stringify(capture())); }
      catch { announce('Unable to save in this browser. Your layout has not been saved.'); return; }
      layoutEditing = false; layoutDraft = null; update();
      announce('Layout saved in this browser.');
    } else { layoutDraft = capture(); layoutEditing = true; update(); }
  };
  toolbar.querySelector('#layout-cancel').onclick = () => {
    stopLayoutDrag(); apply(readLayout()); layoutEditing = false; layoutDraft = null; update();
  };
  toolbar.querySelector('#layout-reset').onclick = () => {
    stopLayoutDrag(); apply(defaultLayout); layoutDraft = capture();
    announce('Default arrangement restored. Save layout to keep it, or Cancel to undo.');
  };

  for (const panel of panels) {
    const name = panel.querySelector('h2')?.textContent.trim() || 'Panel';
    const grip = document.createElement('button');
    grip.type = 'button';
    grip.className = 'panel-grip';
    grip.textContent = '⠿ Move ' + name;
    grip.setAttribute('aria-label', 'Move ' + name);
    panel.prepend(grip);

    grip.onkeydown = e => {
      if (!layoutEditing || !['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) return;
      e.preventDefault();
      const parent = panel.parentElement;
      if (e.key === 'ArrowUp' && panel.previousElementSibling) parent.insertBefore(panel, panel.previousElementSibling);
      if (e.key === 'ArrowDown' && panel.nextElementSibling) parent.insertBefore(panel.nextElementSibling, panel);
      if (e.key === 'ArrowLeft') columns[0].append(panel);
      if (e.key === 'ArrowRight') columns[1].append(panel);
      layoutDraft = capture(); grip.focus();
      announce(name + ' moved. Save layout to keep your changes.');
    };

    grip.onpointerdown = e => {
      if (!layoutEditing || e.button !== 0) return;
      e.preventDefault();
      stopLayoutDrag();
      const before = capture();
      const marker = document.createElement('div');
      marker.className = 'layout-drop-marker';
      marker.textContent = 'Place ' + name + ' here';
      panel.after(marker);
      panel.classList.add('layout-dragging');
      grip.setPointerCapture(e.pointerId);
      let target = null;

      const move = event => {
        const el = document.elementFromPoint(event.clientX, event.clientY);
        const column = el?.closest('.grid>.stack');
        if (!columns.includes(column)) { target = null; return; }
        target = column;
        const siblings = [...column.querySelectorAll(':scope>.panel')].filter(p => p !== panel);
        const next = siblings.find(p => event.clientY < p.getBoundingClientRect().top + p.getBoundingClientRect().height / 2);
        column.insertBefore(marker, next || null);
        if (event.clientY > window.innerHeight - 60) window.scrollBy(0, 24);
        else if (event.clientY < 70) window.scrollBy(0, -24);
      };
      const cleanup = () => {
        panel.classList.remove('layout-dragging');
        marker.remove();
        document.removeEventListener('pointermove', move);
        document.removeEventListener('pointerup', up);
        document.removeEventListener('pointercancel', cancel);
        document.removeEventListener('keydown', escape);
        if (grip.hasPointerCapture(e.pointerId)) grip.releasePointerCapture(e.pointerId);
        stopLayoutDrag = () => {};
      };
      const cancel = () => { cleanup(); apply(before); grip.focus(); };
      const up = () => {
        if (target) marker.before(panel);
        cleanup(); layoutDraft = capture(); grip.focus();
        announce(name + ' placed. Save layout to keep your changes.');
      };
      const escape = event => { if (event.key === 'Escape') { event.preventDefault(); cancel(); } };

      document.addEventListener('pointermove', move);
      document.addEventListener('pointerup', up);
      document.addEventListener('pointercancel', cancel);
      document.addEventListener('keydown', escape);
      stopLayoutDrag = cancel;
    };
  }
  update();
}
