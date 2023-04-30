const DEFAULT_SETTINGS = {
  pausedRecommendedVideos: true,
  endScreenRecommendedVideos: true,
  channelWatermarks: true,
  thumbnailHoverOverlays: true,
}

let settings = DEFAULT_SETTINGS

for (let key in settings) {
    const checkbox = document.getElementById(key);
    checkbox.addEventListener('change', function() {
      settings[key] = this.checked
      chrome.storage.sync.set(settings)
    })
}

chrome.storage.sync.get(DEFAULT_SETTINGS, function(storedSettings) {
  settings = storedSettings || DEFAULT_SETTINGS

  for (let key in settings) {
    const checkbox = document.getElementById(key);
    checkbox.checked = settings[key]
  }
})