// The page, the preload and the main process each name the same channels, in
// three files that nothing type-checks against each other. Rename one and the
// app still builds, still starts, and quietly loses a button - which is exactly
// how the old `window.shullUpdater` calls outlived the bridge that served them.
// So check the three surfaces agree, without booting Electron.
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');

const read=p=>fs.readFileSync(path.join(__dirname,p),'utf8');
const preload=read('preload.cjs');
const main=read('main.cjs');
const page=read(path.join('..','app','public','app.js'));

test('every desktop call the page makes is exposed by the preload',()=>{
  const used=[...page.matchAll(/window\.shullDesktop\.([A-Za-z.]+)\s*\(/g)].map(m=>m[1]);
  assert.ok(used.length>0,'the page no longer calls the desktop bridge at all');
  for(const call of used){
    const method=call.split('.').pop();
    assert.match(preload,new RegExp(`\\b${method}\\s*:`),`preload.cjs exposes no ${call}`);
  }
});

test('every channel the preload invokes is handled in the main process',()=>{
  const channels=[...preload.matchAll(/ipcRenderer\.(?:invoke|on)\('([^']+)'/g)].map(m=>m[1]);
  assert.ok(channels.length>0,'the preload invokes nothing');
  for(const channel of channels){
    // 'updates:status' is both a handle and the push the main process sends.
    const handled=main.includes(`ipcMain.handle('${channel}'`)||main.includes(`send('${channel}'`);
    assert.ok(handled,`main.cjs neither handles nor sends ${channel}`);
  }
});

test('updates install themselves rather than waiting to be asked',()=>{
  assert.match(main,/autoUpdater\.autoDownload=true/,'a found update is not downloaded');
  assert.match(main,/autoUpdater\.autoInstallOnAppQuit=true/,'a downloaded update is never put in place');
  assert.match(main,/setInterval\(check,UPDATE_EVERY\)/,'the app checks once and then never again');
});

test('the packaged app ships the updater it depends on',()=>{
  const pkg=JSON.parse(read(path.join('..','package.json')));
  assert.ok(pkg.dependencies?.['electron-updater'],'electron-updater is not a runtime dependency');
  assert.ok(pkg.build.files.includes('node_modules/**/*'),
    'build.files lists files explicitly, so node_modules has to be named or the updater is left out');
  assert.equal(pkg.build.publish.provider,'github');
});
