/*
 * message consists:
 * number of windows and number of tabs opened
 * URL of all opened tabs
 * 1. send message to externally_connectable page(specified in manifest.json) 
 * 
 * 2. output in background console
 * Fired when a button is clicked on test page
 * 
 * message example:
 * "number of windows: 1
 * number of tabs of window 0: 9
 * URL of tab 0 is: https://www.html.cn/archives/6103
 * URL of tab 1 is: chrome://extensions/
 * URL of tab 2 is: https://segmentfault.com/a/1190000008518315
 * URL of tab 3 is: https://uxplanet.org/infinite-scrolling-best-practices-c7f24c9af1d#.6vfij8d11
 * URL of tab 4 is: https://www.youtube.com/
 * URL of tab 5 is: http://gpu_attack.shujiangwu.com/testpage1/
 * URL of tab 6 is: https://github.com/sxei/chrome-plugin-demo
 * URL of tab 7 is: https://crxdoc-zh.appspot.com/apps/runtime#method-getURL
 * URL of tab 8 is: http://3.221.81.120/test/new.html
 * "
 */

var url = null;
var numWindows;

chrome.runtime.onMessageExternal.addListener(function(request, sender, sendResponse) {
  chrome.windows.getAll({"populate" : true}, function getTabs(windows) {
      var MSG = '';
      numWindows = windows.length;
      MSG += 'number of windows: ' + numWindows + '\n';
      console.log('there are '+ numWindows + ' windows opening');
      for (var i = 0; i < numWindows; i++) {
        var win = windows[i];
        var Tabs = win.tabs;
        var testNumTabs = Tabs.length;
        MSG += 'number of tabs of window ' + i + ': '+ testNumTabs+ '\n';
        console.log('number of tabs of window ' + i + ': '+ testNumTabs);
        // make a sign if the window is in incognito 
        if(win.incognito){
          MSG += 'in incognito' + '\n';
          console.log('in incognito');
        }
      }
      chrome.tabs.query({}, function(Tabs){
            var numTabs = Tabs.length;
            console.log('number of all tabs: ' + numTabs);
            for (var j = 0; j<numTabs; j++){
                url = Tabs[j].url;
                MSG += 'URL of tab ' + j + ' is: ' + url + '\n';
                console.log('URL of tab ' + j + ' is: ' + url);
            }
            sendResponse({type: 'MsgFromChrome', msg: MSG});
      });
    }
);
});


/* 
 * Fired when the focused window is changed
 * output in background page console
 */
chrome.windows.onFocusChanged.addListener(function(windowId){
  console.log('focused window changed to: ' + windowId);
});



/*
 * Fired when a new tab is created
 * output in background page console
 */ 
chrome.tabs.onCreated.addListener(function(activeInfo){
  console.log('tab: ' + activeInfo.tabId + ' in window: '+ activeInfo.windowId + ' was created');
});


/*
 * Fired when the actvated tab is changed
 * output in background page console
 */ 
chrome.tabs.onActivated.addListener(function(activeInfo){
  console.log('tab ' + activeInfo.tabId + ' in window '+ activeInfo.windowId + ' was activated');
  var tab = chrome.tabs.get(activeInfo.tabId, function(tab) {
        console.log('the URL of current tab is: ' + tab.url);
    });
});


/*
 * Fired when one tab is updated
 * when the loading is complete, output in background page console
 */ 
chrome.tabs.onUpdated.addListener(function(tabId,changeInfo,tab){
  if(changeInfo.status==='complete'){  
    console.log('URL of tab ' + tabId + ' was updated to: ' + tab.url);
  }
});


