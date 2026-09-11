import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const appRoot=path.dirname(fileURLToPath(import.meta.url));
const repo=path.dirname(appRoot);
const read=p=>fs.readFileSync(path.join(repo,p),'utf8');

test('repository has a usable template library for every supported course',()=>{
  const specs=fs.readdirSync(path.join(repo,'templates/worksheet/specs')).filter(x=>x.endsWith('.json'));
  assert.ok(specs.length>=4,'keep a real starter library, not an empty template directory');
  const courses=new Set(specs.map(name=>JSON.parse(read('templates/worksheet/specs/'+name)).course));
  for(const course of ['chemistry','physics','geology'])assert.ok(courses.has(course),`missing ${course} template`);
  for(const name of specs){const spec=JSON.parse(read('templates/worksheet/specs/'+name));assert.ok(Array.isArray(spec.sectionsContent)&&spec.sectionsContent.length>0,`${name} has no sections`);}
});

test('repository agent team and document workflow remain wired',()=>{
  const roles=['overseer','researcher','designer','auditor','librarian','janitor','secretary'];
  for(const role of roles){assert.ok(fs.existsSync(path.join(repo,'.claude','agents',role+'.md')),`missing ${role} agent`);}
  const source=read('app/agents.mjs');
  for(const role of ['overseer','researcher','designer','auditor'])assert.match(source,new RegExp(`agent\\(run,'${role}'`),`${role} is not in drafting flow`);
  assert.match(source,/run\.status='Draft ready'/,'draft flow has no ready state');
  assert.match(read('app/server.mjs'),/worksheet\.docx/,'server has no document build path');
});
