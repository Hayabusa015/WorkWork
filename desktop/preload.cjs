const {contextBridge,ipcRenderer}=require('electron');
contextBridge.exposeInMainWorld('shullUpdater',{check:()=>ipcRenderer.invoke('updates:check'),install:()=>ipcRenderer.invoke('updates:install')});
