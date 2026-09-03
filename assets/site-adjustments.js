// Move testimonials block after the phases section and shorten long homepage paragraphs.
document.addEventListener('DOMContentLoaded', function(){
  try {
    var phases = document.querySelector('.phases');
    var testimonials = document.querySelector('.testimonials');
    if (phases && testimonials) {
      // Insert testimonials after phases
      phases.parentNode.insertBefore(testimonials, phases.nextSibling);
    }

    // Shorten some long paragraphs on the homepage without removing originals
    var longParas = document.querySelectorAll('.homepage-long-copy');
    longParas.forEach(function(p){
      var shortText = p.getAttribute('data-short') || 'Learn more about our approach to learning across the school.';
      var placeholder = document.createElement('p');
      placeholder.className = 'homepage-short-copy';
      placeholder.textContent = shortText;
      p.parentNode.insertBefore(placeholder, p);
    });

  } catch (e) {
    console.error('site-adjustments.js error', e);
  }
});
