import {randomUUID} from 'node:crypto';

export async function deliverSuggestion({run,research,agent,suggestions,save}) {
  const sourceStep=(run.agents||[]).filter(x=>x.role==='researcher').length;
  const sourceKey=run.id+':'+sourceStep;
  if(suggestions.some(x=>x.sourceKey===sourceKey))return;
  const result=await agent(run,'secretary','Deliver a concise briefing for the teacher from the Researcher findings. Use plain language: important notices, suggested updates, and concrete to-dos. Keep evidence and uncertainties visible. Identify what the Librarian should retrieve or where it should prepare filing. Do not approve changes or claim they were implemented. This is an inbox suggestion, not an adopted governance record.',{research,course:run.course,task:run.title});
  const item={id:randomUUID(),sourceKey,sourceRun:run.id,course:run.course,title:run.title,body:result.report,findings:research.issues,source:'Researcher',deliveredBy:'Secretary',status:'new',created:new Date().toISOString()};
  suggestions.unshift(item);save();return item;
}

export function addSuggestionFocus(item,focus) {
  if(item.focusId)return item.focusId;
  const entry={id:randomUUID(),text:('Follow up: '+item.title).slice(0,200),done:false,suggestionId:item.id};
  focus.push(entry);item.focusId=entry.id;return entry.id;
}

export async function handToLibrarian({item,run,agent,save}) {
  try {
    const result=await agent(run,'librarian','The teacher sent this Secretary briefing to you. Prepare actionable retrieval and filing recommendations. Resolve course, unit, section, and content type only from the evidence; list missing information. Drive is not connected. Do not claim retrieval, filing, or changes happened. Rule changes require a separate approved Secretary proposal.',{course:item.course,notice:item.body,researchFindings:item.findings});
    item.librarianReport=result.report;item.status='response';run.status='Report ready';
  }catch(e){item.status='failed';item.error=e.message;run.status='Failed';run.error=e.message;}
  save();
}
