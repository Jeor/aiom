(() => {
  const entries = JSON.parse(document.getElementById('guide-search-data').textContent);
  const dialog = document.createElement('dialog');
  dialog.className = 'guide-search';
  dialog.setAttribute('aria-label', 'Search all guides');
  dialog.innerHTML = '<div class="search-top"><label for="guide-query">Search all guides</label><button type="button" aria-label="Close search">Close</button></div><input id="guide-query" type="search" placeholder="Try tags, warming, profiles…" autocomplete="off"><p class="search-status" role="status"></p><div class="search-results"></div><p class="search-foot">Searches guide text only · Esc to close</p>';
  document.body.append(dialog);
  const input = dialog.querySelector('input');
  const results = dialog.querySelector('.search-results');
  const status = dialog.querySelector('.search-status');
  const normalize = text => text.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  function render() {
    results.replaceChildren();
    const query = normalize(input.value.trim());
    if (!query) { status.textContent = 'Find instructions and troubleshooting across all four guides.'; return; }
    const words = query.split(/\s+/);
    const matches = entries.map(entry => {
      const title = normalize(entry.title), guide = normalize(entry.guide), body = normalize(entry.text);
      const combined = title + ' ' + guide + ' ' + body;
      return {entry, score: words.every(word => combined.includes(word)) ? words.reduce((score, word) => score + (title.includes(word) ? 8 : 0) + (guide.includes(word) ? 3 : 0) + (body.includes(word) ? 1 : 0), 0) : 0};
    }).filter(item => item.score).sort((a,b) => b.score-a.score);
    status.textContent = matches.length ? `${matches.length} matching sections` : 'No matches. Try a shorter phrase, such as “TTL” or “tags”.';
    for (const {entry} of matches) {
      const link = document.createElement('a'); link.href = entry.url;
      const guide = document.createElement('small'); guide.textContent = entry.guide;
      const title = document.createElement('strong'); title.textContent = entry.title;
      const snippet = document.createElement('span');
      const offset = Math.max(0, normalize(entry.text).indexOf(words[0]) - 55);
      snippet.textContent = (offset ? '…' : '') + entry.text.slice(offset, offset + 190) + (entry.text.length > offset + 190 ? '…' : '');
      link.append(guide,title,snippet); link.addEventListener('click', () => dialog.close()); results.append(link);
    }
  }
  function open() { if (!dialog.open) dialog.showModal(); render(); input.focus(); }
  document.querySelectorAll('.search-trigger').forEach(button => button.addEventListener('click',open));
  dialog.querySelector('button').addEventListener('click',() => dialog.close());
  dialog.addEventListener('click',event => { if (event.target === dialog) { const r=dialog.getBoundingClientRect(); if (event.clientX<r.left || event.clientX>r.right || event.clientY<r.top || event.clientY>r.bottom) dialog.close(); }});
  input.addEventListener('input',render);
  input.addEventListener('keydown',event => { if (event.key==='ArrowDown') {event.preventDefault(); results.querySelector('a')?.focus();} if (event.key==='Enter') results.querySelector('a')?.click(); });
  document.addEventListener('keydown',event => { if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase()==='k') {event.preventDefault(); open();} });
})();
