// var nav = new NavigationCollector();

var activeTab = 0;
var previousUrls;
var allTrees;

chrome.tabs.onActiveChanged.addListener(function (tabId, selectInfo) {
	activeTab = tabId;
});

function addVisitToTree(tabId, changeInfo) {
	if (allTrees && previousUrls) {
		var lastUrlVisitedOnThisTab = previousUrls[tabId] || "null";
		allTrees[tabId] = allTrees[tabId] || [];

		var oppositeDirection = {"name" : lastUrlVisitedOnThisTab, "parent": changeInfo.url};
		var newVisit = {"name" : changeInfo.url, "parent": lastUrlVisitedOnThisTab};

		var arrayContainsOppositeDirection = false;
		var sitePathAlreadyTraversed = false;
		allTrees[tabId].forEach(function (node) {
			if (JSON.stringify(node) === JSON.stringify(oppositeDirection)) {
				arrayContainsOppositeDirection = true;
			} else if (JSON.stringify(node) === JSON.stringify(newVisit)) {
				sitePathAlreadyTraversed = true;
			}
		});

		if (!arrayContainsOppositeDirection && !sitePathAlreadyTraversed) {
	  		allTrees[tabId].push(newVisit);
		}

	  	previousUrls[tabId] = changeInfo.url;

	    chrome.storage.sync.set({'allTrees': allTrees, 'previousUrls': previousUrls}, function() {
	          // Notify that we saved.
	          console.log('changes saved');
	    });
	}
}

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {

  if (changeInfo.url) {
  	if (!allTrees || !previousUrls) {
  		chrome.storage.sync.get({'allTrees': [],'previousUrls': []}, function (storage) {
    		previousUrls = storage.previousUrls || [];
    		allTrees = storage.allTrees || [];
    		addVisitToTree(tabId, changeInfo);
    	});
  	} else {
  		addVisitToTree(tabId, changeInfo);
  	}
  }
});



function onMessageListener_ (message, sender, sendResponse) {
	if (message.type === 'getJSON') {
		if (!allTrees) {
			chrome.storage.sync.get('allTrees', function (obj) {
			    allTrees = obj || [];
			    sendResponse({result:allTrees[activeTab]});
			});
		} else {
			sendResponse({result:allTrees[activeTab]});
		} 
	} else 
		sendResponse({});
}

chrome.runtime.onMessage.addListener(onMessageListener_);


