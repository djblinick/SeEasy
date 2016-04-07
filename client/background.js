// var nav = new NavigationCollector();

var activeTab = 0;
var previousUrls;
var currentTabTree;
var activeWindow;

chrome.tabs.onActiveChanged.addListener(function (tabId, selectInfo) {
	chrome.storage.sync.get({[activeWindow * tabId]: [],'previousUrls': {}}, function (storage) {
		previousUrls = storage.previousUrls || {};
		currentTabTree = storage[activeWindow * tabId] || [];
		activeTab = tabId;
	});
});

function addVisitToTree(tabId, changeInfo) {
	if (currentTabTree && previousUrls) {
		var lastUrlVisitedOnThisTab = previousUrls[tabId] || "null";

		var newVisit = {"name" : changeInfo.url, "parent": lastUrlVisitedOnThisTab};
		var oppositeDirection = {"name" : lastUrlVisitedOnThisTab, "parent": changeInfo.url};

		var arrayContainsOppositeDirection = false;
		var sitePathAlreadyTraversed = false;
		currentTabTree.forEach(function (record) {
			if (JSON.stringify(record) === JSON.stringify(oppositeDirection)) {
				arrayContainsOppositeDirection = true;
			} else if (JSON.stringify(record) === JSON.stringify(newVisit)) {
				sitePathAlreadyTraversed = true;
			}
		});

		if (!arrayContainsOppositeDirection && !sitePathAlreadyTraversed) {
	  		currentTabTree.push(newVisit);
		}

	  	previousUrls[tabId] = changeInfo.url;

	    chrome.storage.sync.set({[activeWindow * tabId]: currentTabTree, 'previousUrls': previousUrls}, function() {
	          // Notify that we saved.
	          console.log('changes saved');
	    });
	}
}

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {

  if (changeInfo.url) {
  	if (!currentTabTree || !previousUrls || activeTab !== tabId) {
  		chrome.storage.sync.get({[activeWindow * tabId]: [],'previousUrls': {}}, function (storage) {
    		previousUrls = storage.previousUrls || {};
    		currentTabTree = storage[activeWindow * tabId] || [];
    		activeTab = tabId;
    		addVisitToTree(tabId, changeInfo);
    	});
  	} else {
  		addVisitToTree(tabId, changeInfo);
  	}
  }
});



function onMessageListener_ (message, sender, sendResponse) {
	if (message.type === 'getJSON') {
		if (!currentTabTree) {
			chrome.storage.sync.get({[activeWindow * activeTab]: []}, function (obj) {
			    currentTabTree = obj || [];
			    sendResponse({result:currentTabTree});
			});
		} else {
			console.log(JSON.stringify({'result':currentTabTree}));
			sendResponse({'result':currentTabTree});
		} 
	} else 
		sendResponse({});
}

chrome.windows.onFocusChanged.addListener(function (windowId) {
	activeWindow = windowId;
});

chrome.runtime.onMessage.addListener(onMessageListener_);


