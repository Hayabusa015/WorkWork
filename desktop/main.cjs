const {app,BrowserWindow,session,dialog,Menu,shell,ipcMain}=require('electron');
const path=require('node:path');
const fs=require('node:fs');
const {pathToFileURL}=require('node:url');
const {randomBytes}=require('node:crypto');
const https=require('node:https');
const os=require('node:os');
const {spawn}=require('node:child_process');
let backend,window;
let pendingUpdate=null;
function fetchLatestRelease(){return new Promise((resolve,reject)=>{const req=https.get({hostname:'api.github.com',path:'/repos/Hayabusa015/WorkWork/releases/latest',headers:{'User-Agent':'SHULL-OS-Updater','Accept':'application/vnd.github+json'}},res=>{if(res.statusCode<200||res.statusCode>=300){res.resume();return reject(new Error(`GitHub returned ${res.statusCode}`));}let raw='';res.setEncoding('utf8');res.on('data',x=>raw+=x);res.on('end',()=>{try{const r=JSON.parse(raw),asset=(r.assets||[]).find(a=>/SHULL-OS-Setup-.*\.exe$/i.test(a.name));resolve({version:String(r.tag_name||'').replace(/^v/,''),name:r.name||r.tag_name||'Latest release',url:asset?.browser_download_url||null,notes:r.body||''});}catch(e){reject(e);}});});req.on('error',reject);req.setTimeout(15000,()=>req.destroy(new Error('Update check timed out')));});}
function newer(version){const a=String(app.getVersion()).split('.').map(Number),b=String(version).split('.').map(Number);for(let i=0;i<3;i++){if((b[i]||0)!==(a[i]||0))return (b[i]||0)>(a[i]||0);}return false;}
const locked=app.requestSingleInstanceLock();
if(!locked)app.quit();
else {
  app.on('second-instance',()=>{if(window){if(window.isMinimized())window.restore();window.focus();}});
  app.whenReady().then(async()=>{
    ipcMain.handle('updates:check',async()=>{const r=await fetchLatestRelease();pendingUpdate=newer(r.version)&&r.url?r:null;return {...r,current:app.getVersion(),available:!!pendingUpdate};});
    ipcMain.handle('updates:install',async()=>{if(!pendingUpdate?.url)throw new Error('No downloadable update is available.');const file=path.join(os.tmpdir(),`SHULL-OS-Setup-${pendingUpdate.version}.exe`);await new Promise((resolve,reject)=>{const get=url=>https.get(url,{headers:{'User-Agent':'SHULL-OS-Updater'}},res=>{if([301,302,307,308].includes(res.statusCode)&&res.headers.location)return get(res.headers.location);if(res.statusCode!==200)return reject(new Error(`Download failed (${res.statusCode})`));const out=fs.createWriteStream(file);res.pipe(out);out.on('finish',()=>out.close(resolve));out.on('error',reject);}).on('error',reject);get(pendingUpdate.url);});spawn(file,[],{detached:true,stdio:'ignore'}).unref();app.quit();return {started:true};});
    const repo=app.isPackaged?path.join(process.resourcesPath,'repo'):path.dirname(__dirname);
    const vendor=app.isPackaged?path.join(process.resourcesPath,'vendor'):path.join(__dirname,'vendor');
    const data=path.join(app.getPath('userData'),'data');
    fs.mkdirSync(data,{recursive:true});
    process.env.SHULL_DATA_DIR=data;
    process.env.PORT='0';
    delete process.env.VERCEL;
    const token=randomBytes(32).toString('hex');
    process.env.SHULL_DESKTOP_TOKEN=token;
    const python=path.join(vendor,'python','python.exe');
    const office=path.join(vendor,'LibreOffice','program','soffice.exe');
    if(fs.existsSync(python))process.env.SHULL_PYTHON=python;
    if(fs.existsSync(office))process.env.SHULL_SOFFICE=office;
    const serverModule=await import(pathToFileURL(path.join(repo,'app','server.mjs')).href);
    backend=await serverModule.startServer(0);
    const origin=`http://127.0.0.1:${backend.address().port}`;
    session.defaultSession.webRequest.onBeforeSendHeaders({urls:[origin+'/*']},(details,callback)=>{
      details.requestHeaders['X-Shull-Desktop']=token;
      callback({requestHeaders:details.requestHeaders});
    });
    session.defaultSession.setPermissionRequestHandler((_wc,_permission,callback)=>callback(false));
    window=new BrowserWindow({width:1440,height:960,minWidth:900,minHeight:650,backgroundColor:'#111b20',title:'SHULL OS',show:false,webPreferences:{nodeIntegration:false,contextIsolation:true,sandbox:true,preload:path.join(__dirname,'preload.cjs')}});
    window.webContents.on('will-navigate',(event,url)=>{if(new URL(url).origin!==origin)event.preventDefault();});
    window.webContents.setWindowOpenHandler(({url})=>{
      if(new URL(url).origin===origin)return {action:'allow',overrideBrowserWindowOptions:{webPreferences:{nodeIntegration:false,contextIsolation:true,sandbox:true}}};
      if(/^https:\/\/(console\.anthropic\.com|platform\.claude\.com)(\/|$)/.test(url))void shell.openExternal(url);
      return {action:'deny'};
    });
    Menu.setApplicationMenu(Menu.buildFromTemplate([
      {label:'Workspace',submenu:[{label:'Open saved documents folder',click:()=>shell.openPath(data)},{label:'Print current page',accelerator:'CmdOrCtrl+P',click:()=>BrowserWindow.getFocusedWindow()?.webContents.print({printBackground:true})},{type:'separator'},{role:'quit'}]},
      {label:'Edit',submenu:[{role:'undo'},{role:'redo'},{type:'separator'},{role:'cut'},{role:'copy'},{role:'paste'},{role:'selectAll'}]},
      {label:'View',submenu:[{role:'reload'},{role:'resetZoom'},{role:'zoomIn'},{role:'zoomOut'},{role:'togglefullscreen'}]}
    ]));
    await window.loadURL(origin);
    window.show();
  }).catch(error=>{dialog.showErrorBox('SHULL OS could not start',error.message);app.quit();});
  app.on('window-all-closed',()=>app.quit());
  app.on('before-quit',()=>backend?.close());
}
