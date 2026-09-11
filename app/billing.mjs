// Standard global Messages pricing, USD per million tokens. Verified 2026-09-10.
export const pricingSource='https://platform.claude.com/docs/en/about-claude/pricing';
const prices={
 'claude-sonnet-5':[2,10], 'claude-sonnet-4-6':[3,15],
 'claude-sonnet-4-5-20250929':[3,15], 'claude-haiku-4-5-20251001':[1,5],
 'claude-opus-5':[5,25], 'claude-opus-4-8':[5,25], 'claude-opus-4-7':[5,25],
 'claude-opus-4-6':[5,25], 'claude-opus-4-5-20251101':[5,25],
 'claude-fable-5':[10,50], 'claude-fable-5-1':[10,50]
};
export function usageCost(model,u){
 const p=prices[model];if(!p||!u||!Number.isFinite(u.input_tokens)||!Number.isFinite(u.output_tokens))return null;
 const writes=u.cache_creation||{};
 const hour=writes.ephemeral_1h_input_tokens||0;
 const short=writes.ephemeral_5m_input_tokens??Math.max(0,(u.cache_creation_input_tokens||0)-hour);
 return (u.input_tokens*p[0]+u.output_tokens*p[1]+short*p[0]*1.25+hour*p[0]*2+(u.cache_read_input_tokens||0)*p[0]*(model==='claude-fable-5-1'?.025:.1))/1e6;
}
export function recordCharge(billing,run,step,index){
 const id=run.id+':'+index;if(billing.ledger.some(e=>e.id===id))return;
 const amount=usageCost(run.model,step.usage);step.cost=amount;
 billing.ledger.push({id,runId:run.id,role:step.role,model:run.model,amount,at:new Date().toISOString()});
}
export function balanceSummary(b){
 const entries=b.ledger.slice(b.baselineIndex||0),spent=entries.reduce((s,e)=>s+(e.amount??0),0);
 return {starting:b.starting,spent,remaining:b.starting-spent,uncertain:entries.filter(e=>e.amount===null).length,since:b.since,source:pricingSource};
}
export function estimateWorkflow(model,roles,contextChars){
 if(!prices[model])return null;
 let low=0,high=0;
 for(const role of roles){const input=Math.ceil((contextChars[role]||0)/3)+2000;
 low+=usageCost(model,{input_tokens:input,output_tokens:role==='designer'?2000:700});
 high+=usageCost(model,{input_tokens:input*2+12000,output_tokens:role==='designer'?10000:4000});}
 return {low,high,calls:roles.length,model};
}
