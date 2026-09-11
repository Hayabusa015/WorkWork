import {test} from 'node:test';
import assert from 'node:assert/strict';
import {createAgentRunner,draftWithAgents,checkScope,parseAgentResult} from './agents.mjs';
const example={course:'chemistry',unit:7,sections:['7.4'],sectionsContent:[{title:'Moles'}]};
test('scope fails closed for Class, absent codes and partial matches',()=>{
  assert.throws(()=>checkScope(example,'7.4 Mole','class'));
  assert.throws(()=>checkScope(example,'7.40 Other','chemistry'));
  assert.doesNotThrow(()=>checkScope(example,'7.4 Mole','chemistry'));
});
test('separate role sessions pass evidence forward and preserve independent auditor input',async()=>{
  const calls=[],reports=[],run={course:'chemistry',model:'test',prompt:'Make a worksheet'};
  const read=p=>p.endsWith('DECISIONS.md')?'7.4 Mole':p;
  const agent=createAgentRunner({read,save(){},report:(r,s)=>reports.push(s.role),request:async body=>{
    calls.push(body);const role=['overseer','researcher','designer','auditor'].find(x=>body.system.includes('SOURCE .claude/agents/'+x+'.md'));
    return {stop_reason:'end_turn',usage:{input_tokens:2,output_tokens:3},content:[{type:'text',text:JSON.stringify(role==='designer'?example:{report:role+' report',issues:[],proceed:true})}]};
  }});
  await draftWithAgents(run,{read,agent,example,validate(){},save(){}});
  assert.equal(run.status,'Draft ready');assert.deepEqual(reports,['overseer','researcher','designer','auditor']);
  assert.equal(calls.length,4);assert.ok(calls.every(c=>c.messages.length===1&&c.model==='test'));
  const auditInput=JSON.parse(calls[3].messages[0].content);
  assert.deepEqual(auditInput.spec,example);assert.equal(auditInput.research,undefined);
  assert.deepEqual(run.usage,{input_tokens:8,output_tokens:12});
});
test('overseer stop prevents downstream calls',async()=>{
  const roles=[],run={course:'chemistry'};
  await draftWithAgents(run,{read:()=> '7.4 Mole',example,save(){},validate(){},agent:async(r,role)=>{roles.push(role);return {proceed:false,report:'Scope unclear',issues:['scope']};}});
  assert.deepEqual(roles,['overseer']);assert.equal(run.status,'Agent needs attention');assert.equal(run.spec,undefined);
});
test('auditor defect blocks build-ready state and returns to overseer',async()=>{
  const roles=[],run={course:'chemistry'};
  await draftWithAgents(run,{read:()=> '7.4 Mole',example,save(){},validate(){},agent:async(r,role)=>{roles.push(role);return role==='designer'?example:{proceed:role!=='auditor',report:'Finding',issues:['incorrect calculation']};}});
  assert.equal(run.status,'Agent needs attention');assert.deepEqual(roles,['overseer','researcher','designer','auditor','overseer']);
});
test('truncated responses and malformed reports cannot pass',()=>{
  assert.throws(()=>parseAgentResult({stop_reason:'max_tokens'},'auditor'));
  assert.throws(()=>parseAgentResult({stop_reason:'end_turn',content:[{type:'text',text:'{"proceed":true}'}]},'auditor'));
});
test('API failure is recorded without retry or a completed step',async()=>{
  const run={},agent=createAgentRunner({read:()=>'',save(){},report(){assert.fail('should not persist successful report');},request:async()=>{throw Error('offline');}});
  await assert.rejects(agent(run,'overseer','plan',{}),/offline/);
  assert.equal(run.agents.length,1);assert.equal(run.agents[0].status,'failed');
});
