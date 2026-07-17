# Search surface clean-entry pattern

Session lesson: moving Dock Search to `search.html` fixed the hash/focus/keyboard trap, but the first implementation still felt like a floating version of the old directory because it rendered inside a large card container and pre-populated result cards before the visitor had expressed intent.

## Product rule
`search.html` is a primary search prompt, not a miniature directory.

Fresh entry should be quiet and non-influential:
- centered title / short guidance
- one obvious large search input
- nearby lightweight filter chips
- a clear `View all directory` escape hatch
- no preloaded result feed
- no empty-state panel
- no large container-card wrapping the whole prompt

## Render contract
On initial load, after `assets/search-index.json` finishes loading:
- result count stays blank or neutral, not “N searchable signals”
- `#results` stays empty
- no `.result-card` nodes render
- no `.empty` state renders

Results appear only after visitor intent:
- `query.trim()` is non-empty, or
- selected filter is not `all`

Pseudo-contract:
```js
const hasIntent = Boolean(query) || state.filter !== 'all';
if (!hasIntent) {
  setText('result-count', '');
  results.innerHTML = '';
  return;
}
```

## Visual direction
Avoid “container-card vibes” for the search entry state:
- prefer an unboxed `.search-surface` over `.search-card`
- pill-shaped input can carry the visual weight
- chips should be light/transparent, not dashboard controls
- when results appear, render them as a flatter list, not directory cards

## Verification probes
Use Puppeteer/text checks after starting the local server:
- initial: `document.querySelectorAll('.result-card').length === 0`
- initial: `!document.querySelector('.empty')`
- initial: `document.querySelector('#result-count').textContent.trim() === ''`
- initial: `!document.querySelector('.search-card')`
- typed query returns results
- non-`all` filter returns results

## Pitfall
Do not interpret “dedicated search page” as “directory page in a different wrapper.” The user wants the entry state to feel elegant, clean, and unsteering; the feed is reactive output, not initial content.