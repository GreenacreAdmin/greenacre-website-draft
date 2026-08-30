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

  if(nav){
    const mobileQuery=window.matchMedia("(max-width: 980px)");
    const drops=[...nav.querySelectorAll(".nav-drop")];

    drops.forEach(drop=>{
      const button=drop.querySelector(":scope > button");
      if(!button) return;

      button.setAttribute("aria-expanded","false");

      if(mobileQuery.matches && button.classList.contains("nav-section-current")){
        drop.classList.add("nav-open");
        button.setAttribute("aria-expanded","true");
      }

      button.addEventListener("click",()=>{
        if(!mobileQuery.matches) return;

        const opening=!drop.classList.contains("nav-open");

        drops.forEach(other=>{
          other.classList.remove("nav-open");
          const otherButton=other.querySelector(":scope > button");
          if(otherButton) otherButton.setAttribute("aria-expanded","false");
        });

        if(opening){
          drop.classList.add("nav-open");
          button.setAttribute("aria-expanded","true");
        }
      });
    });
  }

  const t=document.querySelector('.menu-toggle'),n=document.querySelector('.site-nav');
  if(t&&n)t.addEventListener('click',()=>{
    const o=n.classList.toggle('open');
    t.setAttribute('aria-expanded',String(o));
  });
})();
