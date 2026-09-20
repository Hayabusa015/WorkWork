import {test} from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {curriculum, parseCurriculum, documentTypes, documentName} from './curriculum.mjs';
import {checkScope} from './agents.mjs';

const appRoot = path.dirname(fileURLToPath(import.meta.url));
const repo = path.dirname(appRoot);
const COURSES = ['chemistry', 'physics', 'geology'];
const decisions = course => fs.readFileSync(path.join(repo, 'courses', course, 'DECISIONS.md'), 'utf8');

process.env.SHULL_DATA_DIR = fs.mkdtempSync(path.join(os.tmpdir(), 'shull-design-test-'));
const {startServer} = await import('./server.mjs');

async function withServer(run) {
  const server = await startServer(0);
  try { await run(`http://127.0.0.1:${server.address().port}`); }
  finally { await new Promise(resolve => server.close(resolve)); }
}

const post = (origin, path, body) => fetch(origin + path, {
  method: 'POST',
  headers: {'content-type': 'application/json', origin},
  body: JSON.stringify(body),
});

test('every unit parses the number of sections its own decisions file declares', () => {
  for (const course of COURSES) {
    const {units} = parseCurriculum(decisions(course), course);
    assert.ok(units.length, `${course} produced no units`);
    for (const unit of units) {
      assert.equal(unit.warning, undefined,
        `${course} U${unit.unit}: ${unit.warning}`);
      assert.ok(unit.title, `${course} U${unit.unit} has no title`);
      assert.ok(unit.sections.length, `${course} U${unit.unit} has no sections`);
    }
  }
});

test('a section the picker offers is a section the agent workflow accepts', () => {
  // The picker and checkScope read the same file. If they can ever disagree, a
  // teacher picks a section and the run dies after the money is spent.
  for (const course of COURSES) {
    const text = decisions(course);
    for (const unit of curriculum(text, course).units) {
      for (const section of unit.sections) {
        assert.doesNotThrow(
          () => checkScope({course, unit: unit.unit, sections: [section.code]}, text, course),
          `${course} ${section.code} is offered but would be refused`);
      }
    }
    // And every section belongs to the unit it is listed under.
    for (const unit of curriculum(text, course).units) {
      for (const section of unit.sections) {
        assert.equal(Number(section.code.split('.')[0]), unit.unit);
      }
    }
  }
});

test('the roadmap commentary is not read as curriculum', () => {
  // Geology's U4 note says "`4.4` covers all three convergent subtypes". A block
  // quote citing a code must not add a section, or duplicate one.
  for (const course of COURSES) {
    for (const unit of curriculum(decisions(course), course).units) {
      const codes = unit.sections.map(s => s.code);
      assert.equal(new Set(codes).size, codes.length, `${course} U${unit.unit} has a duplicate code`);
    }
  }
});

test('document types come from standards/NAMING.md, not from the app', () => {
  const naming = fs.readFileSync(path.join(repo, 'standards', 'NAMING.md'), 'utf8');
  const types = documentTypes(naming);
  for (const expected of ['Slides', 'Guided_Notes', 'Practice_Set', 'Lab', 'Activity']) {
    assert.ok(types.includes(expected), `${expected} missing from the parsed type list`);
  }
  // If NAMING.md's list changes, this parse must follow it rather than a copy here.
  assert.ok(types.length >= 10);
});

test('the filename follows the NAMING grammar, zero-padded', () => {
  assert.equal(documentName({course: 'geology', type: 'Practice_Set', unit: 4, sections: ['4.1']}),
    'SHULL_GEO_Practice_Set_U04_S04.1.docx');
  assert.equal(documentName({course: 'chemistry', type: 'Test', unit: 8, sections: ['8.4']}),
    'SHULL_CHEM_Test_U08_S08.4.docx');
  assert.equal(documentName({course: 'physics', type: 'Guided_Notes', unit: 1,
                             sections: ['1.1', '1.2', '1.3', '1.4']}),
    'SHULL_PHYS_Guided_Notes_U01_S01.1-S01.4.docx');
  assert.equal(documentName({course: 'physics', type: 'Slides', unit: 10, sections: ['10.2'],
                             extension: 'pptx'}),
    'SHULL_PHYS_Slides_U10_S10.2.pptx');
});

test('the curriculum endpoint serves each course and refuses anything else', async () => {
  await withServer(async origin => {
    for (const course of COURSES) {
      const body = await (await fetch(`${origin}/api/curriculum?course=${course}`)).json();
      assert.ok(body.units.length, `${course} returned no units`);
      assert.equal(body.source, `courses/${course}/DECISIONS.md`);
      assert.ok(body.contentTypes.length);
    }
    assert.equal((await fetch(origin + '/api/curriculum?course=biology')).status, 400);
    assert.equal((await fetch(origin + '/api/curriculum')).status, 400);
  });
});

test('only types with a builder behind them are offered as buildable', async () => {
  await withServer(async origin => {
    const {contentTypes} = await (await fetch(origin + '/api/curriculum?course=geology')).json();
    const buildable = contentTypes.filter(t => t.app).map(t => t.type).sort();
    // The worksheet builder is the only one wired into this app.
    assert.deepEqual(buildable, ['Activity', 'Practice_Set']);
    // Nothing offers a key as a choice: a key is always a second file.
    assert.ok(!contentTypes.some(t => t.type === 'Key'));
    // A type this app cannot build must say where it does build.
    for (const t of contentTypes.filter(t => !t.app && t.family)) {
      assert.ok(t.command, `${t.type} is a repository build but names no command`);
    }
  });
});

test('a design request is checked against the course decisions before anything is spent', async () => {
  await withServer(async origin => {
    const base = {course: 'geology', unit: 4, sections: ['4.1'], type: 'Practice_Set'};
    const reject = async (patch, expected) => {
      const r = await post(origin, '/api/design', {...base, ...patch});
      assert.equal(r.status, 400);
      assert.match((await r.json()).error, expected);
    };

    await reject({course: 'biology'}, /Select a course/);
    await reject({type: 'Nonsense'}, /Unknown document type/);
    // A type with no builder here names the repository command instead.
    await reject({type: 'Slides'}, /cannot build Slides yet.*templates\/slide/s);
    await reject({type: 'Quiz'}, /No template builds Quiz yet/);
    // A code that is not in the decisions file, and one from another unit.
    await reject({sections: ['4.9']}, /not in the course decisions/);
    await reject({sections: ['5.1']}, /Invalid section code/);
    await reject({sections: []}, /at least one section/);
    await reject({unit: 99}, /Invalid section code|not in/);

    // A valid selection gets all the way to the credentials check, which is the
    // last gate — the scope is proven for free, before any key is required.
    const ok = await post(origin, '/api/design', base);
    assert.equal(ok.status, 400);
    assert.match((await ok.json()).error, /Connect your Anthropic key/);
  });
});
