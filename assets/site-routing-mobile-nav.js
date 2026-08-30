(()=>{
  const project=location.hostname==='greenacreadmin.github.io'?'/greenacre-website-draft/':'/';
  const links=document.querySelectorAll('[data-path]');

  links.forEach(a=>a.href=project+(a.dataset.path||''));

  const t=document.querySelector('.menu-toggle'),n=document.querySelector('.site-nav');
  if(t&&n)t.addEventListener('click',()=>{
    const o=n.classList.toggle('open');
    t.setAttribute('aria-expanded',String(o));
  });
})();
