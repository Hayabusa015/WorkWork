import path from 'node:path';
import os from 'node:os';

export function resolveDataDirectory({vercel=Boolean(process.env.VERCEL),appDirectory,temporaryDirectory=os.tmpdir()}={}){
  if(!appDirectory)throw Error('appDirectory is required');
  return vercel?path.join(temporaryDirectory,'shull-os'):path.join(appDirectory,'data');
}
