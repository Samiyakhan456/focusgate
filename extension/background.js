// ============================================================
// background.js — FocusGate v2
// ============================================================
// Much simpler than before. When you visit Instagram:
//   1. We fetch http://localhost:8000/status
//   2. Server reads tasks.json and replies locked/unlocked
//   3. If locked → redirect. If unlocked → let through.
//
// No content script. No storage sync. No permissions issues.
// ============================================================

const TASK_MANAGER = 'http://localhost:8000';
const STATUS_URL   = 'http://localhost:8000/status';

chrome.webNavigation.onBeforeNavigate.addListener(async (details) => {

  // Only intercept the main page (not iframes or sub-resources)
  if (details.frameId !== 0) return;

  console.log('[FocusGate] Instagram detected, checking status...');

  try {
    const res  = await fetch(STATUS_URL);
    const data = await res.json();

    console.log(`[FocusGate] Status: ${data.status} (${data.done}/${data.total} tasks done)`);

    if (data.status !== 'unlocked') {
      console.log('[FocusGate] LOCKED — redirecting to task manager');
      chrome.tabs.update(details.tabId, { url: TASK_MANAGER });
    } else {
      console.log('[FocusGate] UNLOCKED — enjoy Instagram! 🎉');
    }

  } catch (err) {
    // Server not running → block Instagram as a safe default
    console.warn('[FocusGate] Could not reach server, blocking Instagram');
    console.warn('[FocusGate] Make sure server.py is running!');
    chrome.tabs.update(details.tabId, { url: TASK_MANAGER });
  }

}, {
  url: [{ hostContains: 'instagram.com' }]
});

chrome.runtime.onInstalled.addListener(() => {
  console.log('[FocusGate] v2 installed — watching Instagram.');
});
