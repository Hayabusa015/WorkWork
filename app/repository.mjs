import fs from 'node:fs';
import path from 'node:path';
import {execFile} from 'node:child_process';
import {promisify} from 'node:util';

const exec = promisify(execFile);


export function repositoryDesk(repo, data) {
  const cache = path.join(data, 'repository-snapshot.json');
  const checkoutFile = path.join(data, 'repository-checkout.json');
  let inflight;
  let snapshot = null;
  try { snapshot = JSON.parse(fs.readFileSync(cache, 'utf8')); } catch {}
  function checkout() {
    if (fs.existsSync(checkoutFile)) return JSON.parse(fs.readFileSync(checkoutFile, 'utf8'));
    return fs.existsSync(path.join(repo, '.git')) ? repo : '';
  }
  async function read(mode, folder = checkout()) {
    const python = process.env.SHULL_PYTHON || (process.platform === 'win32' ? 'python' : 'python3');
    try {
      const {stdout} = await exec(python, [path.join(repo, 'scripts/repository_desk.py'), mode, folder,
        path.join(data, 'workwork-refs.git')], {maxBuffer: 12_000_000, timeout: 240000, windowsHide: true});
      return JSON.parse(stdout);
    } catch (e) { throw Error(e.stderr?.trim() || e.message); }
  }
  function failures() {
    const file = path.join(data, 'repository-attempts.jsonl');
    return fs.existsSync(file) ? fs.readFileSync(file, 'utf8').trim().split('\n').slice(-30).reverse().map(line => JSON.parse(line)) : [];
  }
  async function sync() {
    try {
      const fresh = await read('sync');
      fs.writeFileSync(cache + '.tmp', JSON.stringify(fresh));
      fs.renameSync(cache + '.tmp', cache);
      snapshot = fresh;
      return {snapshot, failures: failures()};
    } catch (error) { return {snapshot, failures: failures(), error: error.message}; }
  }
  return {
    sync() { return inflight ??= sync().finally(() => { inflight = null; }); },
    local: () => read('local'),
    async select(folder) {
      const info = await read('local', folder);
      if (!info.connected) throw Error('Select the root folder of your WorkWork checkout.');
      fs.writeFileSync(checkoutFile, JSON.stringify(folder));
      return info;
    },
    async decide(input) {
      const item = snapshot?.records.find(r => r.file === input.record && r.blob === input.blob);
      if (!item || !(input.decision === 'implement' ? item.status === 'APPROVED' : ['PENDING', 'DEFERRED'].includes(item.status))) throw Error('Refresh the proposal before deciding.');
      if (!['approve', 'reject', 'defer', 'implement'].includes(input.decision)) throw Error('Choose a decision.');
      if (typeof input.note !== 'string' || !input.note.trim() || /[\r\n|]/.test(input.note) || input.note.length > 1000)
        throw Error('Enter a one-line decision, including any chosen option (up to 1,000 characters, without |).');
      const python = process.env.SHULL_PYTHON || (process.platform === 'win32' ? 'python' : 'python3');
      const args = [path.join(repo, 'scripts/record_desktop_decision.py'), path.join(data, 'workwork-refs.git')];
      const attempt = {file: item.file, title: input.decision + ' · ' + item.title, time: new Date().toISOString()};
      try {
        const operation = exec(python, args, {timeout: 240000, windowsHide: true});
        operation.child.stdin.on('error', () => {});
        operation.child.stdin.end(JSON.stringify(input));
        const {stdout} = await operation;
        return {commit: stdout.trim()};
      } catch (error) {
        attempt.status = error.stderr?.trim() || error.message;
        fs.appendFileSync(path.join(data, 'repository-attempts.jsonl'), JSON.stringify(attempt) + '\n');
        throw Error(attempt.status);
      }
    }
  };
}
