(()=>{
  const desktopMQ = window.matchMedia('(min-width:981px)');
  const drops = [...document.querySelectorAll('.nav-drop')];

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

    trigger.addEventListener('click', e => {
      if(!desktopMQ.matches) return; // preserve existing mobile tap behaviour
      if(trigger.tagName === 'BUTTON'){
        e.preventDefault();
        const firstLink = menu.querySelector('a[href]');
        if(firstLink) window.location.href = firstLink.href;
      }
    });

    drop.addEventListener('focusin', () => {
      if(desktopMQ.matches && !drop.classList.contains('nav-dismissed')) open();
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
