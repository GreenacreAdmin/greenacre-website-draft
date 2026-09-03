(function(){
  // Dynamic base helper: when served from username.github.io/REPO/ set a <base> so root-absolute links work
  try{
    if (typeof document !== 'undefined' && !document.head.querySelector('base')){
      var host = location.hostname || '';
      if (host.endsWith('.github.io')){
        var seg = location.pathname.split('/').filter(Boolean);
        if (seg.length > 0){
          var baseHref = '/' + seg[0] + '/';
          var base = document.createElement('base');
          base.setAttribute('href', baseHref);
          document.head.insertBefore(base, document.head.firstChild);
        }
      }
    }
  } catch (e){ /* no-op */ }
})();
