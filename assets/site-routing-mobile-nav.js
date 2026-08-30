(()=>{
  const project=location.hostname==='greenacreadmin.github.io'?'/greenacre-website-draft/':'/';
  const links=document.querySelectorAll('[data-path]');

  links.forEach(a=>a.href=project+(a.dataset.path||''));

  let current=location.pathname;
  if(project!=='/'&&current.startsWith(project)){
    current=current.slice(project.length);
  }else{
    current=current.replace(/^\//,'');
  }

  current=current.replace(/^\/+|\/+$/g,'');
  if(current.endsWith('/index.html')){
    current=current.slice(0,-11).replace(/\/$/,'');
  }else if(current==='index.html'){
    current='';
  }

  const nav=document.querySelector('.site-nav');

  if(nav){
    nav.querySelectorAll('[data-path]').forEach(a=>{
      const target=(a.dataset.path||'').replace(/^\/+|\/+$/g,'');

      if(target===current){
        a.setAttribute('aria-current','page');

        const drop=a.closest('.nav-drop');
        const trigger=drop&&drop.querySelector(':scope > button');

        if(trigger){
          trigger.classList.add('nav-section-current');
        }
      }
    });
  }

  const t=document.querySelector('.menu-toggle'),n=document.querySelector('.site-nav');
  if(t&&n)t.addEventListener('click',()=>{
    const o=n.classList.toggle('open');
    t.setAttribute('aria-expanded',String(o));
  });
})();
