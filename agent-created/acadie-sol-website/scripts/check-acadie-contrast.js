// Acadie.sol computed contrast probe
// Run from ~/ExoCortex/websites/projects/acadie_sol while `python3 -m http.server 8777` is active.
// Requires puppeteer/Chrome in the local environment.

const puppeteer = require('puppeteer');

const PAGES = [
  { name: 'index', url: 'index.html', selectors: ['body', 'a[href]', '.launch-card', '.event-preview-title'] },
  { name: 'directory', url: 'directory.html', setup: () => {
      localStorage.setItem('acadie-theme', 'dark');
      document.documentElement.dataset.theme = 'dark';
      window.setDirectoryMode?.('discover', { scroll: false, focus: false });
      document.querySelector('.directory-card')?.setAttribute('open', '');
    }, selectors: ['.card-title', '.description', '.notes, .note-list, .detail-value', '.detail-link, .full-page-link', '.meta-pill'] },
  { name: 'events', url: 'events.html', selectors: ['.event-main h2', '.description', '.event-subline', '.side-note', '.event-card', '.site-dock'] },
  { name: 'entry', url: 'entry.html#big-d-drive-in', selectors: ['h1', '.entry-city', '.detail a', '.section p'] },
  { name: 'recents', url: 'recents.html', selectors: ['.card-title', '.desc', '.meta-pill', 'a[href]'] },
];

async function inspectPage(page, spec, mode) {
  await page.goto(`http://localhost:8777/${spec.url}`, { waitUntil: 'networkidle0' });
  await page.evaluate((mode) => {
    localStorage.setItem('acadie-theme', mode);
    document.documentElement.dataset.theme = mode;
  }, mode);
  if (spec.setup) await page.evaluate(spec.setup);
  await new Promise(resolve => setTimeout(resolve, 250));
  const samples = await page.evaluate((selectors) => selectors.map(selector => {
    const el = document.querySelector(selector);
    if (!el) return { selector, missing: true };
    const cs = getComputedStyle(el);
    const surface = el.closest('.event-card, .directory-card, .surface, .hero, .draft-card') || el;
    return {
      selector,
      color: cs.color,
      background: cs.backgroundColor,
      surfaceBackground: getComputedStyle(surface).backgroundColor,
      text: el.textContent.trim().replace(/\s+/g, ' ').slice(0, 90),
    };
  }), spec.selectors);
  return { page: spec.name, mode, samples };
}

(async () => {
  const browser = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome', args: ['--no-sandbox'], headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 430, height: 932 });
  const results = [];
  for (const mode of ['light', 'dark']) {
    for (const spec of PAGES) results.push(await inspectPage(page, spec, mode));
  }
  console.log(JSON.stringify(results, null, 2));
  await browser.close();
})();
