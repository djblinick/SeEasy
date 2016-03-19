// var nav = new NavigationCollector();


var allTrees = [];
var previousUrls = [];
var activeTab = 0;

chrome.tabs.onActiveChanged.addListener(function (tabId, selectInfo) {
	activeTab = tabId;
});

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {

  if (changeInfo.url) {
	var lastUrlVisitedOnThisTab = previousUrls[tabId];

	if (!lastUrlVisitedOnThisTab) {
		lastUrlVisitedOnThisTab = "null";
	}
	if (!allTrees[tabId]) {
  		allTrees[tabId] = [];
  	}

	var oppositeDirection = {"name" : lastUrlVisitedOnThisTab, "parent": changeInfo.url};
	var arrayContainsOppositeDirection = false;
	allTrees[tabId].forEach(function (node) {
		if (JSON.stringify(node) === JSON.stringify(oppositeDirection)) {
			arrayContainsOppositeDirection = true;
		}
	});

	if (!arrayContainsOppositeDirection) {
		var newVisit = {"name" : changeInfo.url, "parent": lastUrlVisitedOnThisTab};
  		allTrees[tabId].push(newVisit);
	}

  	previousUrls[tabId] = changeInfo.url;
  }
});



function onMessageListener_ (message, sender, sendResponse) {
	if (message.type === 'getJSON') {
	/*var data = [
    { "name" : "Ynet.co.il", "parent":"Google.com" },
    { "name" : "Google.com", "parent":"null" },
    { "name" : "Walla.co.il", "parent":"Ynet.co.il" },
    { "name" : "Cnn.com", "parent":"Ynet.co.il" },
    { "name" : "Gmail.com", "parent":"Google.com" }
    ];*/
      data = allTrees[activeTab];
	  sendResponse({result:data})
	}
	else 
		sendResponse({});
}

chrome.runtime.onMessage.addListener(onMessageListener_);


// function NavigationCollector() {

//   this.data_ = [];

// }

// ///////////////////////////////////////////////////////////////////////////////

// NavigationCollector.prototype = {
//   /**
//    * Returns a somewhat unique ID for a given WebNavigation request.
//    *
//    * @param {!{tabId: ?number, frameId: ?number}} data Information
//    *     about the navigation event we'd like an ID for.
//    * @return {!string} ID created by combining the source tab ID and frame ID
//    *     (or target tab/frame IDs if there's no source), as the API ensures
//    *     that these will be unique across a single navigation event.
//    * @private
//    */
//   parseId_: function(data) {
//     return data.tabId + '-' + (data.frameId ? data.frameId : 0);
//   },


//   /**
//    * Creates an empty entry in the pending array if one doesn't already exist,
//    * and prepopulates the errored and completed arrays for ease of insertion
//    * later.
//    *
//    * @param {!string} id The request's ID, as produced by parseId_.
//    * @param {!string} url The request's URL.
//    */
//   prepareDataStorage_: function(id, url) {
//     this.pending_[id] = this.pending_[id] || {
//       openedInNewTab: false,
//       source: {
//         frameId: null,
//         tabId: null
//       },
//       start: null,
//       transitionQualifiers: [],
//       transitionType: null
//     };
//     this.completed_[url] = this.completed_[url] || [];
//     this.errored_[url] = this.errored_[url] || [];
//   },


//   /**
//    * Retrieves our saved data from storage.
//    * @private
//    */
//   loadDataStorage_: function() {
//     chrome.storage.local.get({
//       "data": {},
//     }, function(storage) {
//       this.data_ = storage.data;
//     }.bind(this));
//   },


//   /**
//    * Persists our state to the storage API.
//    * @private
//    */
//   saveDataStorage_: function() {
//     chrome.storage.local.set({
//       "data": this.data_,
//     });
//   },


//   /**
//    * Resets our saved state to empty.
//    */
//   resetDataStorage: function() {
//     this.data_ = {};
//     this.saveDataStorage_();
//     // Load again, in case there is an outstanding storage.get request. This
//     // one will reload the newly-cleared data.
//     this.loadDataStorage_();
//   },
// };
