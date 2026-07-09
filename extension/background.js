chrome.runtime.onMessage.addListener((message, sender) => {
  for (const file of message.cssFiles) {
    chrome.scripting.insertCSS({
      target: { tabId: sender.tab.id, frameIds: [sender.frameId] },
      files: [file],
    });
  }
});
