(() => {
  // Even rows: give each group the most columns that fit (up to 5, tiles 190px + 18px gap) while
  // leaving its last row at most one short, e.g. 10 = 5 + 5, 9 = 5 + 4, 7 = 4 + 3, 6 = 3 + 3.
  // The CSS centres the rows.
  const directory = document.querySelector('.staff-directory');
  const panel = document.querySelector('.staff-panel');
  if (!directory || !panel) return;
  const layout = () => {
    const style = getComputedStyle(panel);
    const width = directory.clientWidth - parseFloat(style.paddingLeft) - parseFloat(style.paddingRight);
    const fit = Math.max(1, Math.min(5, Math.floor((width + 18) / (190 + 18))));
    document.querySelectorAll('.team-grid-v2').forEach(grid => {
      const n = grid.children.length;
      const short = cols => (n % cols ? cols - n % cols : 0);
      let cols = Math.min(n, fit);
      for (let c = cols; c >= Math.min(n, 3, fit); c--) {
        if (short(c) <= 1) { cols = c; break; }
        if (short(c) < short(cols)) cols = c;
      }
      grid.style.setProperty('--team-cols', cols);
    });
  };
  layout();
  addEventListener('resize', layout);
})();

(() => {
  const items = [...document.querySelectorAll('.staff-disclosure')];
  const button = document.querySelector('.staff-tools button');
  if (!items.length || !button) return;
  const sync = () => {
    button.textContent = items.every(item => item.open) ? 'Collapse all' : 'Expand all';
  };
  button.hidden = false;
  button.addEventListener('click', () => {
    const open = !items.every(item => item.open);
    items.forEach(item => { item.open = open; });
    sync();
  });
  items.forEach(item => item.addEventListener('toggle', sync));
  // Preserve direct links to groups, including links saved before the accordion.
  const revealHash = () => {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); }
    catch { return; }
    const target = document.getElementById(id);
    if (target?.classList.contains('staff-disclosure')) {
      target.open = true;
      requestAnimationFrame(() => target.scrollIntoView());
    }
  };
  addEventListener('hashchange', revealHash);
  revealHash();
  sync();
})();

(() => {
  // Photos in closed groups would only start loading when a group is opened.
  // Once the page has finished loading, fetch them all in the background so
  // they are ready before anyone clicks to expand.
  const preload = () => {
    document.querySelectorAll('.staff-disclosure img[loading="lazy"]').forEach(img => {
      img.loading = 'eager';
    });
  };
  const start = () => ('requestIdleCallback' in window
    ? window.requestIdleCallback(preload, { timeout: 2000 })
    : window.setTimeout(preload, 200));
  if (document.readyState === 'complete') start();
  else window.addEventListener('load', start, { once: true });
})();
