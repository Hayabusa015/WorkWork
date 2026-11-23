import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const repo = fileURLToPath(new URL('..', import.meta.url));
const python = process.env.SHULL_PYTHON || (process.platform === 'win32' ? 'python' : 'python3');

test('a reviewed record is committed independently of records sharing its number; stale replay fails', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'workwork-decision-'));
  const git = (...args) => execFileSync('git', args, {cwd: root, encoding:'utf8'}).trim();
  try {
    const a = 'governance/proposals/SHULL-CHG-0024-physics-u1-vectors-section.md';
    const b = 'governance/proposals/SHULL-CHG-0024-validate-tokens-app-exclusion.md';
    for (const file of [a,b,'change-log/CHANGELOG.md']) {
      fs.mkdirSync(path.dirname(path.join(root,file)), {recursive:true});
      fs.copyFileSync(path.join(repo,file),path.join(root,file));
    }
    git('init','-q'); git('add','.'); git('-c','user.name=Test','-c','user.email=test@example.org','commit','-qm','fixture');
    const inputs = {record:a, decision:'approve', note:'Adopt this Physics section.', blob:git('rev-parse','HEAD:' + a)};
    const run = () => execFileSync(python,['-c',
      'import json,os; from pathlib import Path; from record_desktop_decision import apply; apply(Path.cwd(),json.loads(os.environ["DESK_INPUTS"]),"test-owner","2026-11-23")'], {
      cwd:root, env:{...process.env, PYTHONPATH:path.join(repo,'scripts'), DESK_INPUTS:JSON.stringify(inputs)},
      stdio:'pipe'
    });
    run();
    assert.match(fs.readFileSync(path.join(root,a),'utf8'),/Adopt this Physics section\..*Implementation requested via desktop/);
    assert.equal(git('diff','--',b),'');
    assert.match(fs.readFileSync(path.join(root,'change-log/CHANGELOG.md'),'utf8'),/Desktop decision \| APPROVED/);
    git('add','.'); git('-c','user.name=Test','-c','user.email=test@example.org','commit','-qm','decision');
    assert.throws(run,/proposal changed/);
    const queue = execFileSync(python,['-c',
      'from pathlib import Path; from desktop_queue import outstanding; print(*outstanding(Path.cwd(), "HEAD"))'],
      {cwd:root, env:{...process.env,PYTHONPATH:path.join(repo,'scripts')},encoding:'utf8'});
    assert.equal(queue.trim(),a);
  } finally {fs.rmSync(root,{recursive:true,force:true});}
});
