const DEFAULT_SETTINGS = {
  pausedRecommendedVideos: true,
  endScreenRecommendedVideos: true,
  channelWatermarks: true,
  thumbnailHoverOverlays: true,
}

chrome.storage.sync.get(DEFAULT_SETTINGS, function(storedSettings) {
  const settings = storedSettings || DEFAULT_SETTINGS
  const cssFiles = []

  if (settings.pausedRecommendedVideos) {
    cssFiles.push('css/paused-recommended-videos.css')
  }

  if (settings.endScreenRecommendedVideos) {
    cssFiles.push('css/end-screen-recommended-videos.css')
  }

  if (settings.channelWatermarks) {
    cssFiles.push('css/channel-watermarks.css')
  }

  if (settings.thumbnailHoverOverlays) {
    cssFiles.push('css/thumbnail-hover-overlays.css')
  }

  console.log('cssFiles', cssFiles)

  if (cssFiles.length > 0) {
    chrome.runtime.sendMessage({
      cssFiles,
    })
  }
})