/* Gentle motion: content below the fold fades up as it scrolls into view,
   and the header gains a soft shadow once the page scrolls.
   Nothing is hidden without JavaScript, and everything is skipped when the
   visitor's device asks for reduced motion. */
(() => {
  const root = document.documentElement;
  const header = document.querySelector('.site-header');
  if (header) {
    const onScroll = () => root.classList.toggle('is-scrolled', window.scrollY > 12);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // Sections with their own motion or interactive filtering are left alone.
  const skip = '.hero, .page-hero, .subhero, .testimonials, .clubs-catalogue, .clubs-day, [data-no-motion]';
  const targets = [];
  document.querySelectorAll('main section').forEach(section => {
    if (section.matches(skip) || section.closest(skip) || section.parentElement.closest('main section')) return;
    const box = section.querySelector(':scope > .wrap') || section;
    [...box.children].forEach(child => {
      const items = [...child.children].filter(el => el.nodeType === 1);
      const style = getComputedStyle(child);
      const isGrid = /grid|flex/.test(style.display) && items.length >= 3 && !child.matches('p, h2, h3');
      if (isGrid) items.forEach((el, i) => targets.push([el, i]));
      else targets.push([child, 0]);
    });
  });

  const fold = window.innerHeight * 0.92;
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      observer.unobserve(el);
      el.classList.add('is-in');
      // Hand the element back to its normal styles (hover effects, transitions).
      const done = () => { el.classList.remove('reveal', 'is-in'); el.style.removeProperty('--reveal-i'); };
      el.addEventListener('transitionend', done, { once: true });
      setTimeout(done, 1400);
    });
  }, { rootMargin: '0px 0px -8% 0px' });

  root.classList.add('motion');
  targets.forEach(([el, i]) => {
    if (el.getBoundingClientRect().top < fold) return; // already on screen: never hide it
    el.style.setProperty('--reveal-i', Math.min(i, 6));
    el.classList.add('reveal');
    observer.observe(el);
  });
})();
