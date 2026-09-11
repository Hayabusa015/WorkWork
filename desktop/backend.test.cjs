const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
test('desktop backend uses a free port, requires its session token and persists template names',async()=>{
  process.env.SHULL_DATA_DIR=fs.mkdtempSync(path.join(os.tmpdir(),'shull-desktop-test-'));
  process.env.SHULL_DESKTOP_TOKEN='test-private-session';
  const {startServer}=await import('../app/server.mjs');
  const server=await startServer(0);
  try {
    const origin=`http://127.0.0.1:${server.address().port}`;
    assert.equal((await fetch(origin+'/api/state')).status,403);
    const headers={'X-Shull-Desktop':'test-private-session','Origin':origin,'Content-Type':'application/json'};
    const state=await (await fetch(origin+'/api/state',{headers})).json();
    assert.ok(state.templates.length>0);
    const renamed=await fetch(origin+'/api/templates/'+state.templates[0].id+'/name',{method:'POST',headers,body:JSON.stringify({name:'Desktop template test'})});
    assert.equal(renamed.status,200);
    const saved=JSON.parse(fs.readFileSync(path.join(process.env.SHULL_DATA_DIR,'state.json')));
    assert.equal(saved.templateNames[state.templates[0].id],'Desktop template test');
    assert.equal((await fetch(origin+'/api/templates/'+state.templates[0].id+'/name',{method:'POST',headers:{...headers,Origin:'https://example.com'},body:'{}'})).status,403);
    assert.match(await (await fetch(origin,{headers})).text(),/SHULL OS/);
  } finally {await new Promise(resolve=>server.close(resolve));}
});
