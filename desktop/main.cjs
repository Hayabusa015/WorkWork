const {app,BrowserWindow,session,dialog,Menu,shell,ipcMain}=require('electron');
const path=require('node:path');
const fs=require('node:fs');
const {pathToFileURL}=require('node:url');
const {randomBytes}=require('node:crypto');
const {autoUpdater}=require('electron-updater');
let backend,window;

// ---- Automatic updates, from this repository's GitHub releases -------------
//
// electron-builder writes latest.yml beside the installer, carrying the new
// version and the installer's SHA-512. electron-updater reads that file, and
// refuses to install anything whose hash does not match it. That check is the
// reason this replaced the hand-rolled updater, which downloaded whatever the
// URL happened to return and ran it.
//
// Nothing here asks permission: it checks shortly after launch and every six
// hours after that, downloads in the background, and stages the new version so
// Windows installs it the next time the app closes. The Settings panel shows
// what is happening and offers to restart early.
const UPDATE_EVERY=6*60*60*1000;
const AFTER_LAUNCH=8000;
let update={state:'idle',current:'',version:'',percent:0,message:''};
function report(patch){update={...update,...patch};if(window&&!window.isDestroyed())window.webContents.send('updates:status',update);}
function wireUpdates(){
  autoUpdater.autoDownload=true;
  autoUpdater.autoInstallOnAppQuit=true;
  autoUpdater.on('checking-for-update',()=>report({state:'checking',message:''}));
  autoUpdater.on('update-available',info=>report({state:'downloading',version:info.version,percent:0,message:''}));
  autoUpdater.on('update-not-available',()=>report({state:'current',percent:0,message:''}));
  autoUpdater.on('download-progress',p=>report({state:'downloading',percent:Math.round(p.percent||0)}));
  autoUpdater.on('update-downloaded',info=>report({state:'ready',version:info.version,percent:100}));
  autoUpdater.on('error',e=>report({state:'error',message:e?.message||String(e)}));
  update.current=app.getVersion();
  // Run from source and there is no installer to replace, and no app-update.yml
  // to read - checking would only produce an error the developer cannot act on.
  if(!app.isPackaged){report({state:'dev'});return;}
  const check=()=>autoUpdater.checkForUpdates().catch(e=>report({state:'error',message:e?.message||String(e)}));
  setTimeout(check,AFTER_LAUNCH).unref();
  setInterval(check,UPDATE_EVERY).unref();
}
const locked=app.requestSingleInstanceLock();
if(!locked)app.quit();
else {
  app.on('second-instance',()=>{if(window){if(window.isMinimized())window.restore();window.focus();}});
  app.whenReady().then(async()=>{
    ipcMain.handle('updates:status',()=>update);
    ipcMain.handle('updates:check',async()=>{if(!app.isPackaged)return update;await autoUpdater.checkForUpdates();return update;});
    // quitAndInstall(silent, forceRunAfter): the installer is one-click and
    // per-user, so it needs no prompts and no elevation - it closes the app,
    // swaps the files and opens the new version.
    ipcMain.handle('updates:install',()=>{if(update.state!=='ready')throw new Error('No update has finished downloading yet.');setImmediate(()=>autoUpdater.quitAndInstall(true,true));return update;});
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
    if(fs.existsSync(python))process.env.SHULL_PYTHON=python;
    // LibreOffice is not bundled - it is larger than the rest of the app put together,
    // and without it the Word document still builds and downloads; only the PDF preview
    // and the print audit are lost. So take the bundled copy if someone vendored one,
    // otherwise use an installation already on the machine.
    const offices=[path.join(vendor,'LibreOffice','program','soffice.exe'),
      ...[process.env['ProgramFiles'],process.env['ProgramFiles(x86)'],process.env.LOCALAPPDATA]
        .filter(Boolean).map(root=>path.join(root,'LibreOffice','program','soffice.exe'))];
    const office=offices.find(x=>{try{return fs.existsSync(x);}catch{return false;}});
    if(office)process.env.SHULL_SOFFICE=office;
    ipcMain.handle('workspace:open',()=>shell.openPath(data));
    const serverModule=await import(pathToFileURL(path.join(repo,'app','server.mjs')).href);
    backend=await serverModule.startServer(0);
    const origin=`http://127.0.0.1:${backend.address().port}`;
    session.defaultSession.webRequest.onBeforeSendHeaders({urls:[origin+'/*']},(details,callback)=>{
      details.requestHeaders['X-Shull-Desktop']=token;
      callback({requestHeaders:details.requestHeaders});
    });
    session.defaultSession.setPermissionRequestHandler((_wc,_permission,callback)=>callback(false));
    window=new BrowserWindow({width:1440,height:960,minWidth:900,minHeight:650,backgroundColor:'#111b20',title:'SHULL OS',show:false,autoHideMenuBar:true,webPreferences:{nodeIntegration:false,contextIsolation:true,sandbox:true,preload:path.join(__dirname,'preload.cjs')}});
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
    wireUpdates();
  }).catch(error=>{dialog.showErrorBox('SHULL OS could not start',error.message);app.quit();});
  app.on('window-all-closed',()=>app.quit());
  app.on('before-quit',()=>backend?.close());
}
