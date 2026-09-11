// Run with electron desktop/smoke.cjs; uses isolated data and never calls Anthropic.
const {app,BrowserWindow}=require('electron');
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
app.disableHardwareAcceleration();
app.setPath('userData',fs.mkdtempSync(path.join(os.tmpdir(),'shull-electron-smoke-')));
require('./main.cjs');
let attempts=0;
const timer=setInterval(async()=>{
  if(++attempts>60){console.error('Desktop UI timed out');clearInterval(timer);app.exit(1);return;}
  const win=BrowserWindow.getAllWindows()[0];
  if(!win||win.webContents.isLoading())return;
  try{
    const result=await win.webContents.executeJavaScript(`(async()=>{
      const state=await (await fetch('/api/state')).json();
      return {title:document.title,templates:state.templates.length,nav:document.querySelector('#nav')?.innerText};
    })()`);
    if(!result.nav?.includes('Templates'))return;
    console.log(JSON.stringify(result));
    if(!result.title.includes('SHULL')||!result.templates)throw Error('Missing desktop content');
    console.log('Electron UI and authenticated API smoke test passed');
    clearInterval(timer);app.quit();
  }catch(error){console.error(error.message);clearInterval(timer);app.exit(1);}
},500);
