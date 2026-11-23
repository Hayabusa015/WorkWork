const base = 'https://github.com/Hayabusa015/WorkWork/';
const views = ['Needs Matt', 'In progress', 'Branches', 'Health', 'History'];
const waiting = r => ['PENDING', 'DEFERRED'].includes(r.status);
const progress = r => ['APPROVED', 'PARTIALLY IMPLEMENTED'].includes(r.status);

export function startRepository(api, esc, appState = () => ({})) {
  let view = views[0], data, issue = '', loading = false, local = {}, failures = [], timer, lastStart = 0;
  let active = false, notice = '', chosen = '', note = '', action = 'approve', sending = false;
  let expanded = new Set();
  const panel = () => document.querySelector('#repository-panel');
  const link = (route, label) => '<a target="_blank" rel="noopener" href="' + base + esc(route) + '">' + esc(label) + '</a>';
  const field = (name, value) => value ? '<p><strong>' + esc(name) + '</strong> ' + esc(value) + '</p>' : '';
  const details = (id, label, contents) => '<details data-key="' + esc(id) + '"' +
    (expanded.has(id) ? ' open' : '') + '><summary>' + esc(label) + '</summary>' + contents + '</details>';
  const runLink = r => link(r.commit ? 'commit/' + r.commit : 'actions/runs/' + Number(r.id), r.title + ' · ' + r.status);
  function proposal(r) {
    const idx = data.records.indexOf(r);
    const canRequest = r.status === 'APPROVED' && !r.decision.includes('Implementation requested via desktop.');
    const decide = waiting(r) || canRequest ? '<button data-pick="' + idx + '">' + (canRequest ? 'Request implementation' : 'Review decision') + '</button>' : '';
    const recent = (data.decisions || []).filter(a => a.file === r.file);
    return details(r.file, r.change_id + ' · ' + r.title + ' · ' + r.status,
      field('Current rule', r.current) + field('Proposed change', r.proposed) + field('Reason', r.summary) +
      field('Decision', r.decision) + field('Implementation', r.implemented_by) + field('Verification', r.verified) +
      recent.map(a => '<p>' + runLink(a) + '</p>').join('') +
      '<div class="actions">' + link('blob/' + data.main + '/' + r.file, 'Read full proposal and options') +
      link('commits/main/' + r.file, 'Commit history') + decide + '</div>');
  }
  function branches() {
    const localText = local.error || (local.connected ? local.root : 'Choose your local WorkWork folder to see your edits.');
    const summary = '<h3>On this computer</h3><p>' + esc(localText) + '</p>' +
      (window.shullDesktop ? '<button data-folder>Choose checkout</button>' : '') +
      (local.connected ? '<pre>' + esc(local.status) + '\n' + esc(local.branches.join('\n')) + '</pre>' : '');
    return summary + '<h3>Remote branches (' + (data.branches.length + 1) + ')</h3>' +
      '<p>' + link('tree/main', 'main · ' + data.main.slice(0, 8)) + '</p>' +
      (data.pullsError ? field('Pull requests unavailable', data.pullsError) : '') + data.branches.map(b => {
        const pull = data.pulls?.find(p => p.branch === b.name);
        const compare = 'compare/main...' + encodeURIComponent(b.name);
        return details(b.name, (b.holds || b.subject) + ' · ' + b.name,
          field('Last commit', b.date + ' · ' + b.subject) +
          field('Compared with main', b.ahead + ' ahead, ' + b.behind + ' behind') +
          field('Previous review', [b.handled, b.note].filter(Boolean).join(' · ')) +
          link(compare, 'Inspect differences') + ' · ' + (pull ? link('pull/' + pull.number, 'Review PR #' + pull.number) :
            b.ahead ? link(compare + '?expand=1', 'Open pull request on GitHub') : link('tree/' + encodeURIComponent(b.name), 'Browse branch')));
      }).join('');
  }
  function paint() {
    const root = panel();
    if (!root) return;
    const records = data?.records || [];
    const current = records.find(r => r.file === chosen);
    const list = records.filter(r => view === views[0] ? waiting(r) : view === views[1] ? progress(r) : !waiting(r) && !progress(r)).reverse();
    const health = data?.checks?.[0];
    let body = '';
    if (current) {
      body = '<h3>' + esc(current.title) + '</h3>' + field('Proposal', current.file) + field('Current rule', current.current) +
        field('Proposed change', current.proposed) + field('Reason', current.summary) +
        link('blob/' + data.main + '/' + current.file, 'Read the entire record, including open questions') +
        '<form id="repository-decision"><label>Decision<select name="action">' +
        (current.status === 'APPROVED' ? [['implement','Request implementation']] : [['approve','Approve & request implementation'],['defer','Defer'],['reject','Reject']]).map(([k,v]) =>
          '<option value="' + k + '"' + (k === action ? ' selected' : '') + '>' + esc(v) + '</option>').join('') +
        '</select></label><label>Your wording, including any options or conditions<input name="note" required maxlength="1000" value="' + esc(note) +
        '"></label><div class="actions"><button class="primary"' + (sending ? ' disabled' : '') + '>Submit decision</button><button type="button" data-cancel>Cancel</button></div></form>';
    } else if (data) {
      if (view === 'Branches') body = branches();
      else if (view === 'Health') body = '<p>GitHub activity checked ' + esc(new Date(data.activityAt || data.synced).toLocaleString()) + '</p><h3>Validation on main</h3><p>' +
        (health ? runLink(health) : esc(data.checksError || 'No validation run for this commit.')) +
        '</p><h3>Recent decision commits</h3>' + (data.decisions || []).map(r => '<p>' + runLink(r) + '</p>').join('') +
        field('Decision history', !data.decisions?.length ? 'No recorded decisions.' : '') +
        '<h3>Recent failed submissions on this computer</h3>' +
        (failures.map(f => field(f.title + ' · ' + new Date(f.time).toLocaleString(), f.status)).join('') || '<p>None recorded.</p>');
      else body = '<h3>' + esc(view) + ' (' + list.length + ')</h3>' + (list.map(proposal).join('') || '<p>No records in this view.</p>');
    }
    if (!current && data && view === 'Needs Matt') {
      const drafts = (appState()?.runs || []).filter(r => r.kind === 'maintenance')
        .flatMap(r => (r.agents || []).filter(a => a.role === 'secretary' && a.report)
          .map(a => ({id: r.id, title: r.title, body: a.report})));
      const inbox = [...(appState()?.suggestions || []), ...drafts];
      if (inbox.length) body += '<h3>Secretary drafts on this computer</h3>' +
        inbox.map(d => details(d.id, d.title, '<pre>' + esc(d.body) + '</pre>')).join('');
      if (data.branchProposals?.length) body += '<h3>Proposal changes on branches</h3>' +
        data.branchProposals.map(p => details(p.name + p.file, p.title + ' · ' + p.name,
          field('Branch status', p.status) + link('blob/' + p.tip + '/' + p.file, 'Read branch version') +
          ' · ' + link('compare/main...' + encodeURIComponent(p.name), 'Review changes for main'))).join('');
    }
    const healthSummary = data ? '<p><strong>Repository health</strong> · Main checks ' + esc(health?.status || 'unavailable') +
      ' · ' + records.filter(waiting).length + ' awaiting decision · ' + records.filter(progress).length +
      ' approved or partially implemented</p>' : '';
    root.innerHTML = healthSummary + '<div class="actions">' + views.map(v => '<button data-view="' + v + '" aria-pressed="' +
      (v === view) + '" class="' + (v === view ? 'primary' : '') + '">' + v + '</button>').join('') +
      '<button data-sync>Refresh</button></div><p class="hint">' + esc(data ? 'Last sync ' + new Date(data.synced).toLocaleString() +
      ' · main ' + data.main.slice(0,8) : 'Fetching WorkWork…') + '</p>' +
      (issue ? field('Sync unavailable', issue) : '') + (notice ? '<p role="status">' + esc(notice) + '</p>' : '') + body;
    root.querySelectorAll('details').forEach(d => d.ontoggle = () => d.open ? expanded.add(d.dataset.key) : expanded.delete(d.dataset.key));
    root.querySelectorAll('[data-view]').forEach(b => b.onclick = () => {view = b.dataset.view; chosen = ''; paint();});
    root.querySelector('[data-sync]').onclick = () => sync();
    root.querySelectorAll('[data-pick]').forEach(b => b.onclick = () => {
      const r = records[Number(b.dataset.pick)]; chosen = r.file; reviewedBlob = r.blob; note = ''; action = r.status === 'APPROVED' ? 'implement' : 'approve'; paint();
    });
    const form = root.querySelector('form');
    if (form) {
      form.elements.note.oninput = e => {note = e.target.value;};
      form.elements.action.onchange = e => {action = e.target.value;};
      root.querySelector('[data-cancel]').onclick = () => {chosen = ''; paint();};
      form.onsubmit = async e => {
        e.preventDefault();
        if (sending) return;
        sending = true;
        form.querySelector('.primary').disabled = true;
        try {
          const result = await api('repository/decision', {record: chosen, blob: reviewedBlob, decision: action, note});
          chosen = ''; view = 'Health'; notice = 'Decision recorded on main · ' + result.commit.slice(0, 8);
          await sync();
        } catch(e) {notice = e.message; await sync();} finally {sending = false; paint();}
      };
    }
    const folder = root.querySelector('[data-folder]');
    if (folder) folder.onclick = async () => {
      try { local = await window.shullDesktop.selectCheckout() || local; } catch(e) { notice = e.message; } paint();
    };
  }
  let reviewedBlob;
  async function localRefresh() {
    try {local = await api('repository/local');} catch(e) {local = {error:e.message};}
  }
  async function sync() {
    if (loading) return;
    loading = true; lastStart = Date.now();
    try {
      const [result] = await Promise.all([api('repository/sync'), localRefresh()]);
      issue = result.error || ''; failures = result.failures || [];
      if (result.snapshot) {
        const incoming = result.snapshot;
        if (data && !issue) {
          const old = new Set(data.records.filter(waiting).map(r => r.file));
          const added = incoming.records.filter(r => waiting(r) && !old.has(r.file)).length;
          const failed = incoming.records.some(r => /blocked|failed/i.test(r.verified) && data.records.some(p => p.file === r.file && r.verified !== p.verified));
          if (added || failed) window.shullDesktop?.notifyRepository(added ? added + ' new proposals need review.' : 'An implementation needs attention. Open In progress.');
        }
        data = incoming;
      }
    } catch(e) {issue = e.message;} finally { loading = false; if (!chosen) paint(); }
  }
  function observe() {
    active = true;
    if (Date.now() - lastStart >= 60000) void sync();
    if (!timer) {
      timer = setInterval(sync, 60000);
      window.addEventListener('focus', () => {if (active && Date.now() - lastStart > 2000) void sync();});
      setInterval(async () => {if (panel() && view === 'Branches') {
        const previous = JSON.stringify(local); await localRefresh(); if (JSON.stringify(local) !== previous) paint();
      }}, 5000);
    }
  }
  if (window.shullDesktop) observe();
  return {mount() {paint(); observe();}};
}
