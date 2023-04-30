chrome.runtime.onMessage.addListener((message, sender) => {
  for (const file of message.cssFiles) {
    chrome.tabs.insertCSS(sender.tab.id, { file, frameId: sender.frameId })
  }
})