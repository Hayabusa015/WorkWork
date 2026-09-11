import {test} from 'node:test';
import assert from 'node:assert/strict';
import {usageCost,recordCharge,balanceSummary,estimateWorkflow} from './billing.mjs';
test('Sonnet 5 charges reported input and output tokens',()=>assert.equal(usageCost('claude-sonnet-5',{input_tokens:10000,output_tokens:2000}),.04));
test('cache tokens use their own rates',()=>assert.equal(usageCost('claude-sonnet-5',{input_tokens:0,output_tokens:0,cache_creation_input_tokens:1000,cache_read_input_tokens:1000}),.0027));
test('charge recording is idempotent and balance reconciliation does not double deduct',()=>{const b={starting:5,ledger:[]},run={id:'r',model:'claude-sonnet-5'},step={role:'designer',usage:{input_tokens:10000,output_tokens:2000}};recordCharge(b,run,step,1);recordCharge(b,run,step,1);assert.equal(b.ledger.length,1);assert.equal(balanceSummary(b).remaining,4.96);b.baselineIndex=1;b.starting=4.5;assert.equal(balanceSummary(b).remaining,4.5);});
test('unknown usage and unknown models never masquerade as known free calls',()=>{assert.equal(usageCost('unknown',{input_tokens:2,output_tokens:3}),null);const b={starting:5,ledger:[]};recordCharge(b,{id:'r',model:'claude-sonnet-5'},{role:'auditor'},1);assert.equal(balanceSummary(b).uncertain,1);assert.equal(estimateWorkflow('unknown',[],{}),null);});
test('preflight prices all requested roles without deducting credit',()=>{const e=estimateWorkflow('claude-sonnet-5',['designer','auditor'],{designer:10000,auditor:8000});assert.equal(e.calls,2);assert.ok(e.low>0&&e.high>e.low);});
