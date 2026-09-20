import {test} from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const appRoot = path.dirname(fileURLToPath(import.meta.url));
const repo = path.dirname(appRoot);
const previews = path.join(appRoot, 'public', 'previews');

process.env.SHULL_DATA_DIR = fs.mkdtempSync(path.join(os.tmpdir(), 'shull-gallery-test-'));
const {startServer} = await import('./server.mjs');

async function withServer(run) {
  const server = await startServer(0);
  try { await run(`http://127.0.0.1:${server.address().port}`); }
  finally { await new Promise(resolve => server.close(resolve)); }
}

test('the app stylesheet carries no colour of its own', () => {
  const css = fs.readFileSync(path.join(appRoot, 'public', 'style.css'), 'utf8');
  assert.equal(css.match(/#[0-9a-f]{3,8}\b/gi), null,
    'style.css must take every colour from tokens.generated.css');
  assert.equal(css.match(/\brgba?\(\s*\d/g), null,
    'a numeric rgb() is a colour literal by another name');
});

test('the generated app tokens still match brand/tokens.json', () => {
  const generated = fs.readFileSync(path.join(appRoot, 'public', 'tokens.generated.css'), 'utf8');
  const tokens = JSON.parse(fs.readFileSync(path.join(repo, 'brand', 'tokens.json'), 'utf8'));
  const wanted = [
    tokens.ground.asphalt.hex, tokens.ground.graphite.hex, tokens.ground.mutedOnDark.hex,
    tokens.courses.chemistry.primary.hex, tokens.courses.physics.primary.hex,
    tokens.courses.geology.primary.hex, tokens.semantic.danger.hex,
  ];
  for (const hex of wanted) {
    assert.ok(generated.includes(hex),
      `${hex} is missing — re-run scripts/build_app_css.py after a token change`);
  }
});

test('the template gallery is served, and describes every document family', async () => {
  await withServer(async origin => {
    const gallery = await (await fetch(origin + '/api/gallery')).json();
    assert.ok(Array.isArray(gallery.families), 'gallery must always answer with a families list');
    if (!gallery.generated) return;   // previews not rendered on this machine

    const ids = gallery.families.map(f => f.id);
    for (const family of ['worksheet', 'notes', 'lab', 'practice', 'slide']) {
      assert.ok(ids.includes(family), `gallery is missing the ${family} family`);
    }
    // Only the worksheet builder is wired into this app. The gallery must not
    // claim otherwise, or a teacher will press a button that does not exist.
    const inApp = gallery.families.filter(f => f.app).map(f => f.id);
    assert.deepEqual(inApp, ['worksheet']);

    for (const family of gallery.families) {
      for (const item of family.items || []) {
        for (const image of item.images) {
          assert.ok(fs.existsSync(path.join(previews, image)), `missing preview image ${image}`);
        }
      }
    }
  });
});

test('every worksheet preview points at a template the app can actually build', async () => {
  await withServer(async origin => {
    const gallery = await (await fetch(origin + '/api/gallery')).json();
    if (!gallery.generated) return;
    const state = await (await fetch(origin + '/api/state')).json();
    const worksheet = gallery.families.find(f => f.id === 'worksheet');
    for (const item of worksheet.items) {
      assert.ok(state.templates.some(t => t.id === item.spec),
        `${item.spec} is previewed but is not in the app's template list`);
    }
  });
});

test('preview images are served, and only from the previews directory', async () => {
  await withServer(async origin => {
    const image = fs.readdirSync(previews).find(f => f.endsWith('.png'));
    if (image) {
      const ok = await fetch(`${origin}/previews/${image}`);
      assert.equal(ok.status, 200);
      assert.equal(ok.headers.get('content-type'), 'image/png');
    }
    for (const attempt of ['../state.json', '..%2Fserver.mjs', 'nope.png']) {
      assert.equal((await fetch(`${origin}/previews/${attempt}`)).status, 404);
    }
  });
});

test('the shell serves its stylesheet, tokens and icon', async () => {
  await withServer(async origin => {
    for (const [route, type] of [['/style.css', 'text/css'], ['/tokens.generated.css', 'text/css'],
                                 ['/icon.svg', 'image/svg+xml'], ['/app.js', 'text/javascript']]) {
      const response = await fetch(origin + route);
      assert.equal(response.status, 200, route);
      assert.ok(response.headers.get('content-type').startsWith(type), route);
    }
    assert.match(await (await fetch(origin + '/')).text(), /tokens\.generated\.css/);
  });
});
