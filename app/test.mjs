import {test} from 'node:test';import assert from 'node:assert/strict';import {mkdtempSync} from 'node:fs';import {tmpdir} from 'node:os';import path from 'node:path';
process.env.SHULL_DATA_DIR=mkdtempSync(path.join(tmpdir(),'shull-test-'));
const {validateSpec}=await import('./server.mjs');
test('rejects file references in generated specs',()=>{assert.throws(()=>validateSpec({course:'chemistry',sectionsContent:[{imagePath:'C:/private.png'}]}));assert.throws(()=>validateSpec({course:'physics',sectionsContent:[{src:'../../secret'}]}));});
test('accepts text worksheet',()=>assert.ok(validateSpec({course:'chemistry',sectionsContent:[{title:'Moles',questions:[{prompt:'Calculate the amount.'}]}]})));
