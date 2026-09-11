import {test} from 'node:test';
import assert from 'node:assert/strict';
import path from 'node:path';

test('Vercel stores temporary preview state under the writable temp directory',async()=>{
  let runtime;
  try{runtime=await import('./runtime.mjs');}catch{}
  assert.equal(typeof runtime?.resolveDataDirectory,'function','runtime path resolver must exist');
  const resolved=runtime.resolveDataDirectory({vercel:true,appDirectory:'/var/task/app',temporaryDirectory:'/tmp'});
  assert.equal(resolved,path.join('/tmp','shull-os'));
});

test('local runs keep persistent state inside app/data',async()=>{
  let runtime;
  try{runtime=await import('./runtime.mjs');}catch{}
  assert.equal(typeof runtime?.resolveDataDirectory,'function','runtime path resolver must exist');
  assert.equal(runtime.resolveDataDirectory({vercel:false,appDirectory:'/workspace/app',temporaryDirectory:'/tmp'}),path.join('/workspace/app','data'));
});
