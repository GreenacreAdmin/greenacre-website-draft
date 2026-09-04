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
