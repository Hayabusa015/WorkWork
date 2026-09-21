const {contextBridge,ipcRenderer}=require('electron');
// The only bridge between the page and Electron. Every entry is a named call;
// the renderer never receives ipcRenderer, an event object or a file path.
contextBridge.exposeInMainWorld('shullDesktop',{
  openWorkspace:()=>ipcRenderer.invoke('workspace:open'),
  updates:{
    status:()=>ipcRenderer.invoke('updates:status'),
    check:()=>ipcRenderer.invoke('updates:check'),
    install:()=>ipcRenderer.invoke('updates:install'),
    // Returns its own unsubscribe, so a re-render cannot stack listeners.
    onStatus:fn=>{const handler=(_event,status)=>fn(status);ipcRenderer.on('updates:status',handler);return ()=>ipcRenderer.off('updates:status',handler);}
  }
});
