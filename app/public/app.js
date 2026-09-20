import {icon, mountLayoutEditor, isLayoutEditing} from './interface.js';

/* ------------------------------------------------------------------ *\
   State and helpers
\* ------------------------------------------------------------------ */

let state, current, gallery = null, galleryFilter = 'all';
let tab = 'Today', selectedCourse = 'chemistry', pendingTemplate = null;

const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const esc = s => String(s ?? '').replace(/[&<>"']/g,
  c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));
const usd = n => new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'}).format(n);
const title = s => String(s || '').charAt(0).toUpperCase() + String(s || '').slice(1);

async function api(p, b) {
  const r = await fetch('/api/' + p, b
    ? {method: 'POST', headers: {'content-type': 'application/json'}, body: JSON.stringify(b)}
    : {});
  const j = await r.json();
  if (!r.ok) throw Error(j.error || 'Request failed');
  return j;
}
function error(e) { $('#notice').textContent = e.message; }

const COURSE_ICON = {chemistry: 'flask', physics: 'atom', geology: 'mountain'};
const COURSE_BLURB = {
  chemistry: 'Concepts and calculations',
  physics: 'Notebook-based practice',
  geology: 'Visual learning',
};

const TABS = [
  {id: 'Today',       icon: 'home',      sub: 'Same curiosity. A more organized day.'},
  {id: 'Create',      icon: 'plus',      sub: 'Make something for your next class.'},
  {id: 'Templates',   icon: 'layers',    sub: 'Every document this system prints. Look before you pick.'},
  {id: 'Library',     icon: 'folder',    sub: 'Your locally built materials. Google Drive connection comes next.'},
  {id: 'Desk',        icon: 'inbox',     sub: 'Briefings, notices and handoffs, in one place.',
   heading: "The Secretary's desk"},
  {id: 'Assignments', icon: 'clipboard', sub: 'Paper first. Keep track of materials you hand out.'},
  {id: 'Agents',      icon: 'team',      sub: 'Your repository team, handoffs, and reports.'},
  {id: 'Standards',   icon: 'target',    sub: 'The instructions and decisions behind your materials.'},
  {id: 'Settings',    icon: 'settings',  sub: 'Connect your workspace.'},
];

const WORKING = ['Drafting', 'Building', 'Agent review'];

/* ------------------------------------------------------------------ *\
   Shell
\* ------------------------------------------------------------------ */

$('#nav').innerHTML = TABS.map(t =>
  `<button data-tab="${t.id}"><span>${icon(t.icon)}</span>${t.id}</button>`).join('');
$('#nav').onclick = e => {
  const b = e.target.closest('[data-tab]');
  if (b) { tab = b.dataset.tab; render(); }
};
$('#date').textContent = new Date().toLocaleDateString(undefined,
  {weekday: 'long', month: 'long', day: 'numeric'});
$('#close').onclick = () => $('#review').close();
$('#review').addEventListener('close', () => { current = null; refresh().catch(error); });

/* ------------------------------------------------------------------ *\
   Shared fragments
\* ------------------------------------------------------------------ */

const rows = (items, opts = {}) => items.length ? items.map(r => `
  <div class="row" data-course="${esc(r.course)}">
    <span class="document-icon">${icon(opts.icon || 'file')}</span>
    <div class="grow">
      <h3>${esc(r.title)}</h3>
      <p>${esc(title(r.course))} · ${new Date(r.created).toLocaleDateString()}${r.sample ? ' · Repository example' : ''}</p>
    </div>
    ${opts.compact ? '' : `<span class="badge ${badgeTone(r.status)}">${esc(r.status)}</span>`}
    <button data-run="${r.id}" ${opts.compact ? 'aria-label="Open document"' : ''}>${
      opts.compact ? icon('chevron') : 'Open'}</button>
  </div>`).join('')
  : `<div class="empty">${esc(opts.empty || 'Your materials will appear here when you create your first worksheet.')}</div>`;

function badgeTone(status) {
  if (['Failed', 'Interrupted', 'Agent needs attention', 'Audit needs attention'].includes(status)) return 'bad';
  if (WORKING.includes(status)) return 'warn';
  if (['Teacher approved', 'Handed out', 'Report ready'].includes(status)) return 'good';
  return '';
}

/* ------------------------------------------------------------------ *\
   Create
\* ------------------------------------------------------------------ */

function create() {
  const courses = [['chemistry', 'Chemistry'], ['physics', 'Physics'], ['geology', 'Geology'], ['class', 'Class']];
  const filtered = selectedCourse === 'class'
    ? state.templates
    : state.templates.filter(t => t.course === selectedCourse);
  return `
  <section class="panel create" data-course="${esc(selectedCourse)}">
    <div class="create-intro">
      <span class="create-emblem">${icon('pen')}</span>
      <div class="create-copy">
        <h2>What are we making?</h2>
        <p>Turn your ideas into materials ready for paper.</p>
      </div>
    </div>

    <div class="course-tabs" role="tablist" aria-label="Route material to">
      <span class="route-label">Route to</span>
      ${courses.map(([id, label]) => `<button class="course-tab ${selectedCourse === id ? 'active' : ''}"
        data-course-tab="${id}" role="tab" aria-selected="${selectedCourse === id}">${label}</button>`).join('')}
    </div>

    <label for="template">Material template</label>
    <select id="template">${
      filtered.map(t => `<option value="${esc(t.id)}" ${pendingTemplate === t.id ? 'selected' : ''}>${esc(t.title)}</option>`).join('')
      || '<option value="">Choose a template after selecting a course</option>'}</select>
    <p class="route-hint">${selectedCourse === 'class'
      ? 'General class material. The selected template is used for this first build while Class routing is recorded for filing.'
      : `New work will use the ${selectedCourse} course decisions, standards, and filing route.`}</p>

    <label class="sr-only" for="prompt">What should this worksheet cover?</label>
    <textarea id="prompt" placeholder="Create a practice set for my next class…"></textarea>
    <p class="hint cost-estimate" id="cost-estimate" role="status">Calculating a planning estimate…</p>

    <div class="actions">
      <button id="sample" class="quiet">${icon('file')} Use existing worksheet</button>
      <button class="primary" id="draft">${icon('plus')} Create draft ${icon('arrow')}</button>
    </div>
    <p class="hint">${state.connected
      ? 'Anthropic connected. Drafting uses your API credits.'
      : 'Connect your Anthropic key in Settings, or explore with an existing worksheet.'}</p>
  </section>`;
}

/* ------------------------------------------------------------------ *\
   The Secretary's desk
\* ------------------------------------------------------------------ */

const suggestionLabel = {
  new: 'For you', sending: 'With Librarian', response: 'Librarian replied', failed: 'Retry available',
};

function suggestionCard(item) {
  return `
  <article class="suggestion-card" data-course="${esc(item.course)}">
    <div class="suggestion-meta">
      <span>${esc(title(item.course))} · Researcher → Secretary</span>
      <span class="badge ${item.status === 'failed' ? 'bad' : item.status === 'response' ? 'good' : ''}">${
        esc(suggestionLabel[item.status] || item.status)}</span>
    </div>
    <h3>${esc(item.title)}</h3>
    <details><summary>Read briefing &amp; to-dos</summary>
      <div class="suggestion-body">${esc(item.body)}</div>
      ${item.findings?.length ? `<ul>${item.findings.map(x => `<li>${esc(x)}</li>`).join('')}</ul>` : ''}
    </details>
    ${item.error ? `<p class="suggestion-error">${esc(item.error)}</p>` : ''}
    ${item.librarianReport ? `<details open><summary>Librarian response · not filed</summary>
      <div class="suggestion-body">${esc(item.librarianReport)}</div></details>` : ''}
    <div class="suggestion-actions">${item.dismissed
      ? `<button data-suggestion="${item.id}" data-action="restore">Restore</button>`
      : `<button data-suggestion="${item.id}" data-action="librarian" ${
            !state.connected || ['sending', 'response'].includes(item.status) ? 'disabled' : ''}>${
            item.status === 'sending' ? 'Librarian working…'
              : item.status === 'response' ? 'Response received' : 'Send to Librarian'}</button>
         <button data-suggestion="${item.id}" data-action="focus" ${item.focusId ? 'disabled' : ''}>${
            item.focusId ? 'Added to focus' : 'Add to today'}</button>
         <button data-suggestion="${item.id}" data-action="dismiss" ${
            item.status === 'sending' ? 'disabled' : ''}>Archive</button>`}
      <button data-run="${item.sourceRun}">Source report</button>
    </div>
  </article>`;
}

function desk() {
  const all = state.suggestions || [];
  const live = all.filter(x => !x.dismissed);
  const archived = all.filter(x => x.dismissed);
  const waiting = state.runs.filter(r => ['Needs teacher review', 'Agent needs attention', 'Audit needs attention'].includes(r.status));
  const handoffs = state.runs.filter(r => ['handoff', 'briefing', 'maintenance'].includes(r.kind)).slice(0, 6);
  const openFocus = state.focus.filter(f => !f.done);

  const stat = (n, label, lit) =>
    `<div class="desk-stat ${lit && n ? 'lit' : ''}"><strong>${n}</strong><span>${label}</span></div>`;

  return `
  <div class="desk">
    <section class="panel desk-surface">
      <div class="nameplate">
        <span class="nameplate-seal">${icon('quill')}</span>
        <div class="grow">
          <span class="eyebrow">Your daily briefing</span>
          <h2>Secretary inbox</h2>
          <p>Research notices, suggested updates, and your next steps.</p>
        </div>
      </div>

      <div class="desk-meter">
        ${stat(live.filter(x => x.status === 'new').length, 'For you', true)}
        ${stat(live.filter(x => x.status === 'sending').length, 'With Librarian')}
        ${stat(live.filter(x => x.status === 'response').length, 'Replied')}
        ${stat(waiting.length, 'Awaiting review')}
        ${stat(openFocus.length, 'Open focus')}
      </div>

      <div class="briefing-controls">
        <label class="sr-only" for="briefing-course">Briefing course</label>
        <select id="briefing-course">${['chemistry', 'physics', 'geology'].map(c =>
          `<option value="${c}" ${selectedCourse === c ? 'selected' : ''}>${title(c)}</option>`).join('')}</select>
        <button id="request-briefing" class="primary" ${state.connected ? '' : 'disabled'}>${icon('search')} Get updates</button>
      </div>

      <div class="blotter">
        <h3>${icon('inbox')} On the blotter</h3>
        ${live.map(suggestionCard).join('') || `<div class="secretary-empty">
          <strong>You're all caught up.</strong>
          <p>Research findings arrive here through your Secretary. You can also request a course briefing above.</p>
        </div>`}
        ${archived.length ? `<details class="archived-suggestions">
          <summary>Archived notices (${archived.length})</summary>${archived.map(suggestionCard).join('')}</details>` : ''}
        <p class="hint">${state.connected
          ? 'Get updates runs Researcher and Secretary using your API credits. Sending to Librarian requests a recommendation — Drive filing is not connected.'
          : 'Connect Anthropic in Settings to receive agent updates. Drive filing is not connected.'}</p>
      </div>
    </section>

    <div class="stack">
      <section class="panel tray">
        <h3>${icon('clipboard')} Waiting on you</h3>
        ${waiting.length ? waiting.map(r => `
          <div class="tray-item" data-course="${esc(r.course)}">
            <span class="document-icon">${icon('file')}</span>
            <div class="grow"><strong>${esc(r.title)}</strong><small>${esc(r.status)}</small></div>
            <button data-run="${r.id}" aria-label="Open ${esc(r.title)}">${icon('chevron')}</button>
          </div>`).join('')
          : '<div class="empty">Nothing is waiting on your review.</div>'}
      </section>

      <section class="panel tray">
        <h3>${icon('team')} Agent handoffs</h3>
        ${handoffs.length ? handoffs.map(r => `
          <div class="tray-item" data-course="${esc(r.course)}">
            <div class="grow"><strong>${esc(r.title)}</strong><small>${esc(r.status)} · ${
              new Date(r.created).toLocaleDateString()}</small></div>
            <button data-run="${r.id}" aria-label="Open ${esc(r.title)}">${icon('chevron')}</button>
          </div>`).join('')
          : '<div class="empty">Briefings, Librarian handoffs and health reviews land here.</div>'}
      </section>

      <section class="panel tray">
        <h3>${icon('target')} Today's focus</h3>
        ${state.focus.length ? state.focus.map(f => `
          <label class="focus ${f.done ? 'done' : ''}">
            <input type="checkbox" data-focus="${f.id}" ${f.done ? 'checked' : ''}>
            <span>${esc(f.text)}</span>
          </label>`).join('')
          : '<div class="empty">A little space for what matters today.</div>'}
      </section>
    </div>
  </div>`;
}

/* A compact card for the Today dashboard that points at the desk. */
function deskCard() {
  const live = (state.suggestions || []).filter(x => !x.dismissed);
  const unread = live.filter(x => x.status === 'new').length;
  return `
  <section class="panel">
    <span class="eyebrow">Your daily briefing</span>
    <h2>${icon('quill')} Secretary</h2>
    <p>${unread
      ? `${unread} notice${unread === 1 ? '' : 's'} waiting on the desk.`
      : 'Nothing new on the desk right now.'}</p>
    ${live.slice(0, 3).map(x => `
      <div class="tray-item" data-course="${esc(x.course)}">
        <div class="grow"><strong>${esc(x.title)}</strong><small>${esc(title(x.course))} · ${
          esc(suggestionLabel[x.status] || x.status)}</small></div>
      </div>`).join('')}
    <div class="actions"><button data-goto="Desk">${icon('inbox')} Open the desk ${icon('arrow')}</button></div>
  </section>`;
}

/* ------------------------------------------------------------------ *\
   Template gallery
\* ------------------------------------------------------------------ */

const FAMILY_ICON = {worksheet: 'page', notes: 'notes', lab: 'beaker', practice: 'pen', slide: 'slides'};

function galleryView() {
  if (!gallery) return '<section class="panel"><p>Loading the template gallery…</p></section>';

  const families = gallery.families || [];
  const courses = ['all', 'chemistry', 'physics', 'geology'];
  const visible = item => galleryFilter === 'all' || item.course === galleryFilter || item.course === 'all';

  const head = `
    <section class="panel">
      <span class="eyebrow">Repository materials</span>
      <div class="templates-heading">
        <h2>Document templates</h2>
        <span class="badge neutral">${families.reduce((n, f) => n + (f.items?.length || 0), 0)} previews</span>
      </div>
      <p>Every image below is a page from the real builder's real output, not a mock-up. Pick a
      worksheet to start a draft from it; the other families build from the repository for now.</p>
      <div class="gallery-filters">${courses.map(c =>
        `<button data-gallery-filter="${c}" class="${galleryFilter === c ? 'active' : ''}">${
          c === 'all' ? 'All courses' : title(c)}</button>`).join('')}</div>
      ${gallery.generated ? '' : `<div class="empty">No previews have been generated on this computer yet.
        Run <strong>python3 scripts/build_template_previews.py</strong> from the repository to render them.</div>`}
    </section>`;

  const body = families.map(family => {
    const items = (family.items || []).filter(visible);
    if (!items.length && family.status === 'built') return '';
    return `
    <section class="family" data-course="${esc(family.course)}">
      <div class="family-head">
        <span class="family-mark">${icon(FAMILY_ICON[family.id] || 'page')}</span>
        <div class="grow">
          <h2>${esc(family.name)}</h2>
          <p>${esc(family.blurb)}</p>
        </div>
        <span class="badge ${family.app ? 'good' : 'neutral'}">${
          family.app ? 'Builds in this app' : 'Repository build'}</span>
      </div>
      ${items.length ? `<div class="gallery">${items.map(item => card(family, item)).join('')}</div>`
        : `<div class="empty">${family.status === 'unavailable'
            ? `Previews unavailable on this computer. ${esc(family.error || '')}`
            : 'No preview generated yet. Run scripts/build_template_previews.py ' + esc(family.id) + '.'}</div>`}
    </section>`;
  }).join('');

  return head + body;
}

function card(family, item) {
  const usable = family.app && item.spec && state.templates.some(t => t.id === item.spec);
  const pages = item.images?.length || 0;
  const unit = family.id === 'slide' ? 'slide' : 'page';
  // Say "4 of 12" when the document is longer than the pages we rendered.
  const count = item.total && item.total > pages
    ? `${pages} of ${item.total} ${unit}s`
    : `${pages} ${unit}${pages === 1 ? '' : 's'}`;
  return `
  <article class="panel gallery-card" data-course="${esc(item.course)}" data-preview="${esc(item.id)}"
           tabindex="0" role="button" aria-label="Preview ${esc(item.title)}">
    ${pages ? `<figure class="gallery-figure ${family.id === 'slide' ? 'slide' : ''}">
        <img src="/previews/${esc(item.images[0])}" alt="Page one of ${esc(item.title)}" loading="lazy">
        <span class="pagecount">${count}</span>
      </figure>`
      : `<figure class="gallery-figure missing"><p>No preview rendered</p></figure>`}
    <div class="gallery-meta">
      <strong>${esc(item.title)}</strong>
      <div class="gallery-tags">
        <span class="badge">${esc(title(item.course))}</span>
        ${usable ? '' : '<span class="badge neutral">Preview</span>'}
      </div>
      <small>${esc(item.source || '')}</small>
    </div>
    ${usable
      ? `<button class="use primary" data-use-template="${esc(item.spec)}" data-use-course="${esc(item.course)}">Use this template</button>`
      : `<button class="use quiet" data-preview-open="${esc(item.id)}">${icon('eye')} Look closer</button>`}
  </article>`;
}

function openPreview(id) {
  const family = (gallery?.families || []).find(f => (f.items || []).some(i => i.id === id));
  const item = family?.items.find(i => i.id === id);
  if (!item) return;
  const usable = family.app && item.spec && state.templates.some(t => t.id === item.spec);

  let box = $('#lightbox');
  if (!box) {
    box = document.createElement('dialog');
    box.id = 'lightbox';
    document.body.append(box);
  }
  box.dataset.course = item.course;
  box.innerHTML = `
    <div class="lightbox-head">
      <span class="family-mark">${icon(FAMILY_ICON[family.id] || 'page')}</span>
      <div class="grow">
        <h2>${esc(item.title)}</h2>
        <p>${esc(family.name)} · ${esc(title(item.course))} · ${esc(item.source || '')}</p>
      </div>
      <button class="close" data-close-lightbox aria-label="Close preview">×</button>
    </div>
    <div class="lightbox-pages">${(item.images || []).map((img, i) =>
      `<img src="/previews/${esc(img)}" alt="Page ${i + 1} of ${esc(item.title)}">`).join('')}</div>
    <div class="lightbox-foot">
      <p>${family.app
        ? 'This family builds inside SHULL OS.'
        : 'Preview only. This family builds from the repository — SHULL OS does not produce it yet.'}</p>
      ${usable ? `<button class="primary" data-use-template="${esc(item.spec)}" data-use-course="${esc(item.course)}">Use this template</button>` : ''}
    </div>`;
  box.querySelector('[data-close-lightbox]').onclick = () => box.close();
  box.querySelectorAll('[data-use-template]').forEach(b => b.onclick = () => {
    box.close();
    useTemplate(b.dataset.useTemplate, b.dataset.useCourse);
  });
  box.showModal();
}

function useTemplate(specId, course) {
  pendingTemplate = specId;
  if (['chemistry', 'physics', 'geology'].includes(course)) selectedCourse = course;
  tab = 'Create';
  render();
  $('#prompt')?.focus();
}

async function loadGallery() {
  try { gallery = await api('gallery'); }
  catch (e) { gallery = {generated: false, families: [], error: e.message}; }
  if (tab === 'Templates') render();
}

/* ------------------------------------------------------------------ *\
   Other panels
\* ------------------------------------------------------------------ */

function budgetPanel() {
  const b = state.billing;
  if (!b) return '';
  return `
  <section class="panel budget-panel">
    <span class="eyebrow">Anthropic</span>
    <h2>API credits</h2>
    <strong class="credit-amount">${usd(b.remaining)}</strong>
    <p>Estimated remaining · ${usd(b.spent)} used since balance set</p>
    ${b.remaining < 1 ? '<p class="suggestion-error">Low estimated balance.</p>' : ''}
    ${b.uncertain ? '<p class="hint">Some charges are unknown. Check Anthropic before relying on this balance.</p>' : ''}
    <p class="hint">Tracks SHULL OS calls only. Other apps, top-ups and adjustments are not synced.</p>
    <a href="https://platform.claude.com/settings/billing" target="_blank" rel="noreferrer">Check Anthropic billing ↗</a>
  </section>`;
}

function pipelinePanel() {
  const names = ['Draft', 'Build', 'Review', 'Print / teach'];
  const descs = ['Shape your content.', 'Make the document.', 'Polish and approve.', 'Put it in their hands.'];
  const marks = ['pen', 'file', 'search', 'printer'];
  const latest = state.runs[0];
  const index = latest ? ({'Draft ready': 0, Drafting: 0, Building: 1, 'Needs teacher review': 2,
    'Teacher approved': 3, 'Handed out': 4}[latest.status] ?? 0) : -1;
  return `
  <section class="panel" ${latest ? `data-course="${esc(latest.course)}"` : ''}>
    <span class="pipeline-count">${latest ? `${Math.max(index, 0)} of 4 complete` : 'Ready when you are'}</span>
    <h2>Assignment pipeline</h2>
    <p>From idea to classroom.</p>
    <div class="pipeline">${names.map((name, i) => `
      <div class="stage ${index > i ? 'complete' : index === i ? 'current' : ''}">
        <span class="stage-node">${icon(index > i ? 'check' : marks[i])}</span>
        <strong>${name}</strong><small>${descs[i]}</small>
      </div>`).join('')}</div>
  </section>`;
}

function classesPanel() {
  return `
  <section class="panel">
    <h2>Your classes</h2>
    <div class="courses">${['chemistry', 'physics', 'geology'].map(c => `
      <div class="course" data-course="${c}">
        <span class="course-icon">${icon(COURSE_ICON[c])}</span>
        <div><h3>${title(c)}</h3><p>${COURSE_BLURB[c]}</p></div>
      </div>`).join('')}</div>
  </section>`;
}

function focusPanel() {
  return `
  <section class="panel focus-panel">
    <h2>${icon('target')} Today's focus</h2>
    <div>${state.focus.map(f => `
      <label class="focus ${f.done ? 'done' : ''}">
        <input type="checkbox" data-focus="${f.id}" ${f.done ? 'checked' : ''}>
        <span>${esc(f.text)}</span>
      </label>`).join('') || '<div class="empty">A little space for what matters today.</div>'}</div>
    <form id="focusform">
      <label class="sr-only" for="focus">Add a focus</label>
      <input id="focus" required maxlength="200" placeholder="Prepare tomorrow's lab">
      <button aria-label="Add focus">${icon('plus')}</button>
    </form>
    <div class="focus-footnote">A little planning.<br>More room for teaching.</div>
  </section>`;
}

function templateNames() {
  return `
  <section class="panel">
    <span class="eyebrow">Display names</span>
    <h2>Rename a worksheet template</h2>
    <p>Changes the label shown in Material template. The repository file and ID stay unchanged.</p>
    ${['chemistry', 'physics', 'geology'].map(course => `
      <div class="template-group" data-course="${course}">
        <h3>${title(course)}</h3>
        ${state.templates.filter(t => t.course === course).map(t => `
          <div class="template-item">
            <div class="template-copy">
              <strong>${esc(t.title)}</strong>
              <small>Repository name: ${esc(t.originalTitle)}</small>
              <small>File: ${esc(t.id)}</small>
            </div>
            <button type="button" data-template-edit="${esc(t.id)}">Rename</button>
          </div>`).join('') || '<div class="empty">No templates yet.</div>'}
      </div>`).join('')}
  </section>`;
}

function templateRename(id) {
  const t = state.templates.find(x => x.id === id);
  if (!t) return;
  const dialog = document.createElement('dialog');
  dialog.className = 'template-rename-dialog';
  dialog.innerHTML = `<form method="dialog">
    <h2>Rename template</h2>
    <p>Change the display label used in Material template. The repository file stays unchanged.</p>
    <label for="template-name">Display name</label>
    <input id="template-name" maxlength="120" required value="${esc(t.title)}">
    <div class="actions"><button value="cancel">Cancel</button>
    <button class="primary" value="save">Save name</button></div></form>`;
  document.body.append(dialog);
  dialog.addEventListener('close', async () => {
    if (dialog.returnValue === 'save') {
      const name = dialog.querySelector('#template-name').value.trim();
      if (name.length < 2) { error(Error('Template name must be 2–120 characters')); dialog.remove(); return; }
      try { await api('templates/' + encodeURIComponent(id) + '/name', {name}); await refresh(); }
      catch (e) { error(e); }
    }
    dialog.remove();
  });
  dialog.showModal();
  dialog.querySelector('input').select();
}

/* ------------------------------------------------------------------ *\
   Render
\* ------------------------------------------------------------------ */

function render() {
  const meta = TABS.find(t => t.id === tab) || TABS[0];
  $$('[data-tab]').forEach(b => b.classList.toggle('active', b.dataset.tab === tab));
  $('#heading').textContent = meta.heading || (tab === 'Today' ? 'Good morning, Shull' : tab);
  $('#subtitle').textContent = meta.sub;

  let html = '';

  if (tab === 'Today') html = `
    <div class="grid">
      <div class="stack">
        ${create()}
        ${pipelinePanel()}
        ${classesPanel()}
        <section class="panel review-queue">
          <h2>${icon('clipboard')} In progress</h2>
          ${rows(state.runs.filter(r => r.status !== 'Handed out').slice(0, 4))}
        </section>
      </div>
      <div class="stack">
        ${budgetPanel()}
        ${deskCard()}
        ${focusPanel()}
        <section class="panel recent-panel">
          <h2>${icon('file')} Recent documents</h2>
          ${rows(state.runs.filter(r => r.docx).slice(0, 3), {compact: true})}
        </section>
      </div>
    </div>`;

  if (tab === 'Create') html = create();
  if (tab === 'Desk') html = desk();
  if (tab === 'Templates') html = galleryView() + templateNames();

  if (tab === 'Agents') html = `
    <section class="panel">
      <span class="eyebrow">Repository team</span>
      <h2>${icon('team')} Your agent team</h2>
      <p>Each role runs separately using its repository instructions. Drafting uses Overseer →
      Researcher → Designer → Auditor. Building adds artifact review, the Librarian's filing
      recommendation, and the Overseer's task report.</p>
      <div class="agent-grid">${(state.agentNames || []).map(name => `
        <div class="agent-card"><h3>${esc(name)}</h3><p>${esc(({
          overseer: 'Plans and coordinates', researcher: 'Checks content and calculations',
          designer: 'Creates worksheet specifications', auditor: 'Reviews independently',
          librarian: 'Plans filing · Drive pending', janitor: 'Reviews repository health',
          secretary: 'Drafts pending proposals'})[name] || '')}</p></div>`).join('')}</div>
      <p class="hint">Agents can read the context supplied by the app. Web research, Drive operations
      and visual inspection are not connected. Reports identify these gaps.</p>
      <div class="actions">
        <button id="maintenance" class="primary" ${state.connected ? '' : 'disabled'}>${icon('check')} Run repository health review</button>
      </div>
      <p class="hint">Runs local validators, then Janitor and Secretary. Uses two AI calls. No rules are changed.</p>
    </section>
    <section class="panel">
      <h2>Agent activity</h2>
      ${rows(state.runs.filter(r => r.agents?.length || r.kind === 'maintenance'),
        {empty: 'Agent runs will appear here once you start one.'})}
    </section>`;

  if (tab === 'Library') html = `
    <input class="search" id="search" placeholder="Search your materials" aria-label="Search materials">
    <section class="panel" id="results">${rows(state.runs.filter(r => r.docx))}</section>`;

  if (tab === 'Assignments') html = `
    <section class="panel">
      <h2>Ready for your classroom</h2>
      <p>Open an approved document to record that you handed it out. This does not send anything to students.</p>
      ${rows(state.runs.filter(r => ['Teacher approved', 'Handed out'].includes(r.status)),
        {empty: 'Approved documents appear here.'})}
    </section>`;

  if (tab === 'Standards') html = `
    <section class="panel">
      <h2>Your source of truth</h2>
      <p>The instructions your agents read before they build anything.</p>
      ${state.standards.map(s => `<div class="row">
        <span class="document-icon">${icon('target')}</span>
        <div class="grow"><h3>${esc(s.split('/').pop())}</h3><p>${esc(s)}</p></div>
        <button data-standard="${esc(s)}">Read</button></div>`).join('')}
    </section>`;

  if (tab === 'Settings') html = `
    ${budgetPanel()}
    <section class="panel">
      <h2>Update your balance</h2>
      <p>Enter the current balance from Anthropic to reconcile this local tracker. Earlier spending
      will not be deducted again.</p>
      <form id="balance-form">
        <div><label for="balance">Current balance (USD)</label>
        <input id="balance" type="number" min="0" max="100000" step="0.01" required
               value="${Math.max(0, state.billing?.remaining ?? 5).toFixed(2)}"></div>
        <button>Set current balance</button>
      </form>
    </section>
    <section class="panel">
      <h2>Anthropic connection</h2>
      <p>Your key stays in the local server's memory and is cleared when the server stops.</p>
      <form id="connect">
        <label for="key">API key</label>
        <input id="key" type="password" autocomplete="off" placeholder="Enter your Anthropic API key">
        <div class="actions">
          <button type="button" id="disconnect" class="quiet">Disconnect</button>
          <button class="primary">Connect and load models</button>
        </div>
      </form>
      <label for="model">Model</label>
      <select id="model">${state.models.map(m =>
        `<option value="${esc(m.id)}" ${m.id === state.model ? 'selected' : ''}>${esc(m.name)}</option>`).join('')}</select>
      <p class="hint">${state.connected ? 'Connected' : 'Not connected'} · Each workflow uses several
      AI calls: up to 10,000 output tokens for Designer and 4,000 per report. Actual usage appears in review.</p>
    </section>
    <section class="panel">
      <h2>Local preview release</h2>
      <p>Daily focus and requests are saved on this computer. Google Drive, cross-device hosting,
      visual agent inspection and Classroom posting are planned integrations.</p>
    </section>`;

  $('#content').innerHTML = html;
  mountLayoutEditor(tab);
  bind();
  if (tab === 'Templates' && !gallery) loadGallery();
  $('#model')?.addEventListener('change', e => api('model', {model: e.target.value}).then(refresh).catch(error));
}

async function refresh() { state = await api('state'); render(); }

/* ------------------------------------------------------------------ *\
   Wiring
\* ------------------------------------------------------------------ */

async function updateEstimate() {
  const target = $('#cost-estimate');
  if (!target) return;
  try {
    const result = await api('estimate?template=' + encodeURIComponent($('#template')?.value || '')
      + '&prompt=' + encodeURIComponent($('#prompt')?.value || ''));
    if (!target.isConnected) return;
    target.textContent = result.estimate
      ? `Estimated full document: ${usd(result.estimate.low)}–${usd(result.estimate.high)} with ${result.estimate.model}. `
        + 'Includes draft agents and one build review, allowing for Secretary and Overseer findings. '
        + 'Planning range, not a cap; revisions and extra builds cost more. Repository examples use no AI credits.'
      : 'Pricing unavailable for this model; cost cannot be estimated.';
  } catch (e) { target.textContent = 'Cost estimate unavailable. ' + e.message; }
}

function bind() {
  // Desktop update panel, injected by the Electron preload when present.
  if (tab === 'Settings' && window.shullUpdater) {
    const panel = document.createElement('section');
    panel.className = 'panel';
    panel.innerHTML = `<h2>SHULL OS updates</h2>
      <p>Check GitHub Releases for a newer desktop build. Your saved workspace data stays on this computer.</p>
      <div class="actions"><button id="check-updates" type="button">Check for updates</button>
      <button id="install-update" class="primary" type="button" hidden>Download and install</button></div>
      <p class="hint" id="update-status">Updates are checked only when you ask.</p>`;
    $('#content').prepend(panel);
    $('#check-updates').onclick = async () => {
      const status = $('#update-status'), install = $('#install-update');
      status.textContent = 'Checking GitHub Releases…';
      install.hidden = true;
      try {
        const r = await window.shullUpdater.check();
        if (r.available) {
          status.textContent = `Version ${r.version} is available.`;
          install.hidden = false;
          install.onclick = async () => {
            install.disabled = true;
            status.textContent = 'Downloading update…';
            try { await window.shullUpdater.install(); }
            catch (e) { install.disabled = false; status.textContent = 'Update failed. ' + e.message; }
          };
        } else status.textContent = `You are running the latest release (${r.current}).`;
      } catch (e) { status.textContent = 'Update check unavailable. ' + e.message; }
    };
  }

  $('#balance-form')?.addEventListener('submit', async e => {
    e.preventDefault();
    try { await api('billing', {balance: Number($('#balance').value)}); await refresh(); }
    catch (e) { error(e); }
  });

  updateEstimate();
  let estimateTimer;
  $('#prompt')?.addEventListener('input', () => {
    clearTimeout(estimateTimer);
    estimateTimer = setTimeout(updateEstimate, 350);
  });
  $('#template')?.addEventListener('change', () => { pendingTemplate = $('#template').value; updateEstimate(); });

  $('#request-briefing')?.addEventListener('click', async () => {
    try { const r = await api('suggestions/research', {course: $('#briefing-course').value}); await refresh(); show(r.id); }
    catch (e) { error(e); }
  });
  $$('[data-suggestion]').forEach(button => button.onclick = async () => {
    button.disabled = true;
    try { await api('suggestions/' + button.dataset.suggestion + '/' + button.dataset.action, {}); await refresh(); }
    catch (e) { button.disabled = false; error(e); }
  });
  $('#maintenance')?.addEventListener('click', async () => {
    try { const r = await api('maintenance', {}); await refresh(); show(r.id); }
    catch (e) { error(e); }
  });

  $$('[data-run]').forEach(b => b.onclick = () => show(b.dataset.run));
  $$('[data-goto]').forEach(b => b.onclick = () => { tab = b.dataset.goto; render(); });
  $$('[data-focus]').forEach(b => b.onchange = () => api('focus', {id: b.dataset.focus}).then(refresh).catch(error));
  $$('[data-course-tab]').forEach(b => b.onclick = () => {
    selectedCourse = b.dataset.courseTab;
    pendingTemplate = null;
    render();
  });
  $('#focusform')?.addEventListener('submit', e => {
    e.preventDefault();
    api('focus', {text: $('#focus').value}).then(refresh).catch(error);
  });

  for (const name of ['sample', 'draft']) $('#' + name)?.addEventListener('click', async () => {
    try {
      const r = await api('runs', {template: $('#template').value, course: selectedCourse,
        prompt: $('#prompt').value, sample: name === 'sample'});
      await refresh();
      show(r.id);
    } catch (e) { error(e); }
  });

  $('#connect')?.addEventListener('submit', async e => {
    e.preventDefault();
    try { await api('connect', {key: $('#key').value}); $('#key').value = ''; await refresh(); }
    catch (e) { error(e); }
  });
  $('#disconnect')?.addEventListener('click', () => api('disconnect', {}).then(refresh));

  $('#search')?.addEventListener('input', e => {
    const q = e.target.value.toLowerCase();
    $('#results').innerHTML = rows(state.runs.filter(r => r.docx && (r.title + ' ' + r.course).toLowerCase().includes(q)));
    $$('[data-run]').forEach(b => b.onclick = () => show(b.dataset.run));
  });

  $$('[data-standard]').forEach(b => b.onclick = async () => {
    const d = await api('standard?path=' + encodeURIComponent(b.dataset.standard));
    $('#detail').innerHTML = `<h2>${esc(b.dataset.standard)}</h2><pre>${esc(d.text)}</pre>`;
    $('#review').showModal();
  });

  // Gallery
  $$('[data-gallery-filter]').forEach(b => b.onclick = () => { galleryFilter = b.dataset.galleryFilter; render(); });
  $$('[data-use-template]').forEach(b => b.onclick = e => {
    e.stopPropagation();
    useTemplate(b.dataset.useTemplate, b.dataset.useCourse);
  });
  $$('[data-preview-open]').forEach(b => b.onclick = e => {
    e.stopPropagation();
    openPreview(b.dataset.previewOpen);
  });
  $$('[data-preview]').forEach(cardEl => {
    cardEl.onclick = () => openPreview(cardEl.dataset.preview);
    cardEl.onkeydown = e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openPreview(cardEl.dataset.preview); }
    };
  });
  $$('[data-template-edit]').forEach(b => b.onclick = () => templateRename(b.dataset.templateEdit));
}

/* ------------------------------------------------------------------ *\
   Run detail
\* ------------------------------------------------------------------ */

function agentReports(r) {
  if (!r.agents?.length) return '';
  return `<section class="agent-reports">
    <h3>Agent handoffs</h3>
    <p class="hint">Done means that agent returned a report — not that all QA or filing passed.</p>
    ${r.agents.map(step => `
      <details ${['running', 'failed', 'attention'].includes(step.status) ? 'open' : ''}>
        <summary><strong>${esc(step.role)}</strong>
        <span class="badge ${step.status === 'failed' ? 'bad' : step.status === 'running' ? 'warn' : ''}">${
          esc(step.status)}${typeof step.cost === 'number' ? ' · ' + usd(step.cost) : ''}</span></summary>
        <pre>${esc(step.error || step.report || 'Working…')}</pre>
        ${step.issues?.length ? `<ul>${step.issues.map(x => `<li>${esc(x)}</li>`).join('')}</ul>` : ''}
      </details>`).join('')}
  </section>`;
}

function show(id) {
  current = id;
  const r = state.runs.find(r => r.id === id);
  if (!r) return;
  const audit = r.audit
    ? `<div class="audit ${r.audit.status}"><strong>Repository audit: ${esc(r.audit.status)}</strong>
       <pre>${esc(r.audit.summary)}</pre></div>` : '';

  $('#detail').dataset.course = r.course || '';
  $('#detail').innerHTML = `
    <h2>${esc(r.title)}</h2>
    <p>${esc(title(r.course))} · <span class="badge ${badgeTone(r.status)}">${esc(r.status)}</span></p>
    ${r.error ? `<p class="suggestion-error">${esc(r.error)}</p>` : ''}
    <p>${esc(r.reviewNote || r.prompt || (r.sample
      ? 'Existing repository example; no AI generation used.'
      : 'Agent reports and findings are shown below.'))}</p>
    ${audit}
    <p class="hint cost-estimate">Recorded task cost estimate: ${usd(r.estimatedCost || 0)}${
      r.costUnknown ? ' + unknown charges' : ''}. ${r.sample
        ? 'Repository example: no AI calls.'
        : 'Based on returned token usage; not an Anthropic invoice.'}</p>
    ${agentReports(r)}
    <div class="actions">
      ${r.status === 'Agent needs attention' && r.spec ? '<button id="revise">Revise from agent findings</button>' : ''}
      ${r.docx ? `<a class="button" href="/files/${r.id}/worksheet.docx">Download Word</a>` : ''}
      ${r.pdf ? `<a class="button" target="_blank" href="/files/${r.id}/worksheet.pdf">Open PDF / print</a>` : ''}
      ${r.status === 'Needs teacher review' ? '<button id="approve">I reviewed this document</button>' : ''}
      ${r.status === 'Teacher approved' ? '<button id="teach">Record handed out today</button>' : ''}
      ${r.spec && ['Draft ready', 'Needs teacher review'].includes(r.status)
        ? '<button id="build" class="primary">Build Word document</button>' : ''}
    </div>
    ${r.usage ? `<p class="hint">API tokens: ${r.usage.input_tokens} input / ${r.usage.output_tokens} output</p>` : ''}
    ${r.pdf ? `<iframe title="Worksheet preview" src="/files/${r.id}/worksheet.pdf"></iframe>`
      : r.spec ? `<div class="preview">${r.spec.sectionsContent.map(s => `
          <h2>${esc(s.title)}</h2>
          <p>${esc(s.concept?.summary)}</p>
          <p>${esc(s.directions)}</p>
          <ol>${(s.questions || []).map(q => `<li>${esc(q.prompt)}${
            (q.parts || []).map(p => `<p>${esc(p)}</p>`).join('')}</li>`).join('')}</ol>
          ${s.blocks ? '<p>This activity includes visual blocks. Build the Word document to review the full layout.</p>' : ''}
        `).join('')}</div>`
      : (WORKING.includes(r.status)
        ? '<p>Your agents are working. You can close this window and return later.</p>' : '')}`;

  for (const a of ['build', 'approve', 'teach', 'revise']) $('#' + a)?.addEventListener('click', async () => {
    try { await api(`runs/${r.id}/${a}`, {}); await refresh(); show(r.id); }
    catch (e) { error(e); $('#review').close(); }
  });
  if (!$('#review').open) $('#review').showModal();
}

/* ------------------------------------------------------------------ *\
   Boot
\* ------------------------------------------------------------------ */

refresh().then(loadGallery).catch(error);

setInterval(async () => {
  if (!state?.runs.some(r => WORKING.includes(r.status))) return;
  try {
    state = await api('state');
    if ($('#review').open && current) show(current);
    else if (!isLayoutEditing() && !$('#lightbox')?.open) render();
  } catch (e) { error(e); }
}, 2500);
