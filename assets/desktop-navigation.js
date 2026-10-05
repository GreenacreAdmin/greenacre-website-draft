(()=>{
  const desktopMQ = window.matchMedia('(min-width:981px)');
  const drops = [...document.querySelectorAll('.nav-drop')];
  // Keyboard focus alone no longer opens a menu (see the Navigation section of site.css).
  document.documentElement.classList.add('nav-js');

  const closeAll = except => {
    drops.forEach(drop => {
      if(drop === except) return;
      drop.classList.remove('nav-open');
      const trigger = drop.querySelector(':scope > button, :scope > a');
      if(trigger && trigger.hasAttribute('aria-expanded')){
        trigger.setAttribute('aria-expanded','false');
      }
    });
  };

  drops.forEach(drop => {
    const menu = drop.querySelector(':scope > .nav-menu');
    const trigger = drop.querySelector(':scope > button, :scope > a');
    if(!menu || !trigger) return;

    let closeTimer = null;

    const open = () => {
      if(!desktopMQ.matches) return;
      window.clearTimeout(closeTimer);
      closeAll(drop);
      drop.classList.remove('nav-dismissed');
      drop.classList.add('nav-open');
      trigger.setAttribute('aria-expanded','true');
    };

    const closeSoon = () => {
      if(!desktopMQ.matches) return;
      window.clearTimeout(closeTimer);
      closeTimer = window.setTimeout(() => {
        if(!drop.matches(':hover') && !drop.contains(document.activeElement)){
          drop.classList.remove('nav-open');
          trigger.setAttribute('aria-expanded','false');
        }
      },220);
    };

    drop.addEventListener('mouseenter', open);
    drop.addEventListener('mouseleave', closeSoon);
    menu.addEventListener('mouseenter', () => window.clearTimeout(closeTimer));
    menu.addEventListener('mouseleave', closeSoon);

    const close = () => {
      window.clearTimeout(closeTimer);
      drop.classList.remove('nav-open');
      trigger.setAttribute('aria-expanded','false');
    };

    trigger.addEventListener('click', e => {
      if(!desktopMQ.matches) return; // preserve existing mobile tap behaviour
      if(trigger.tagName !== 'BUTTON') return;
      e.preventDefault();
      if(e.detail === 0){
        // Enter or Space from the keyboard: show or hide the menu.
        drop.classList.contains('nav-open') ? close() : open();
        return;
      }
      // Mouse click on a section name goes to its first page.
      const firstLink = menu.querySelector('a[href]');
      if(firstLink) window.location.href = firstLink.href;
    });

    trigger.addEventListener('keydown', e => {
      if(!desktopMQ.matches || e.key !== 'ArrowDown') return;
      e.preventDefault();
      open();
      menu.querySelector('a[href]')?.focus();
    });

    menu.addEventListener('keydown', e => {
      if(!desktopMQ.matches || !['ArrowDown','ArrowUp'].includes(e.key)) return;
      const links = [...menu.querySelectorAll('a[href]')];
      const i = links.indexOf(document.activeElement);
      if(i < 0) return;
      e.preventDefault();
      links[(i + (e.key === 'ArrowDown' ? 1 : links.length - 1)) % links.length].focus();
    });

    drop.addEventListener('focusout', e => {
      if(desktopMQ.matches && !drop.contains(e.relatedTarget)){
        drop.classList.remove('nav-open');
        drop.classList.remove('nav-dismissed');
        trigger.setAttribute('aria-expanded','false');
      }
    });

    drop.addEventListener('keydown', e => {
      if(e.key === 'Escape'){
        e.preventDefault();
        window.clearTimeout(closeTimer);
        drop.classList.remove('nav-open');
        drop.classList.add('nav-dismissed');
        trigger.setAttribute('aria-expanded','false');
        trigger.focus();
      }
    });
  });

  document.addEventListener('click', e => {
    if(desktopMQ.matches && !e.target.closest('.nav-drop')){
      closeAll();
    }
  });

  desktopMQ.addEventListener?.('change', () => closeAll());
})();
