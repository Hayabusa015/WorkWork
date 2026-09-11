import {test} from 'node:test';
import assert from 'node:assert/strict';
import {deliverSuggestion,addSuggestionFocus,handToLibrarian} from './suggestions.mjs';
test('Secretary preserves research provenance and deduplicates delivery',async()=>{
 const suggestions=[],run={id:'r1',course:'physics',title:'Unit 1',agents:[{role:'researcher'}]},research={issues:['Check units'],report:'Evidence'};
 let calls=0;
 const options={run,research,suggestions,save(){},agent:async(r,role,task,input)=>{calls++;assert.equal(role,'secretary');assert.equal(input.research,research);return {report:'Check units before filing'};}};
 await deliverSuggestion(options);await deliverSuggestion(options);
 assert.equal(calls,1);assert.equal(suggestions.length,1);assert.equal(suggestions[0].sourceRun,'r1');assert.equal(suggestions[0].status,'new');
});
test('adding a suggestion to focus is idempotent and links back to its source',()=>{
 const item={id:'s1',title:'Review units'},focus=[];
 const id=addSuggestionFocus(item,focus);assert.equal(addSuggestionFocus(item,focus),id);
 assert.equal(focus.length,1);assert.equal(focus[0].suggestionId,'s1');
});
test('Librarian receives the complete Secretary notice and returns a recommendation',async()=>{
 const item={course:'physics',body:'Retrieve the Unit 1 notes',findings:['missing notes'],status:'sending'},run={};
 await handToLibrarian({item,run,save(){},agent:async(r,role,task,input)=>{assert.equal(role,'librarian');assert.equal(input.notice,item.body);assert.match(task,/Drive is not connected/);return {report:'Need section code; not filed'};}});
 assert.equal(item.status,'response');assert.equal(run.status,'Report ready');assert.match(item.librarianReport,/not filed/);
});
test('failed handoff stays retryable and cannot claim a response',async()=>{
 const item={status:'sending'},run={};
 await handToLibrarian({item,run,save(){},agent:async()=>{throw Error('API unavailable');}});
 assert.equal(item.status,'failed');assert.equal(item.librarianReport,undefined);assert.equal(run.status,'Failed');
});
