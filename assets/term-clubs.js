/* Filters only the fixed HTML catalogue. No document fetch or automatic refresh. */
(() => {
  const form = document.getElementById('clubs-filters');
  if (!form) return;
  const year = document.getElementById('club-year');
  const day = document.getElementById('club-day');
  const activity = document.getElementById('club-activity');
  const dayLinks = [...document.querySelectorAll('[data-day-link]')];
  const groups = [...document.querySelectorAll('.clubs-day')];
  const status = document.getElementById('club-results');
  const empty = document.getElementById('clubs-empty');
  function filterClubs() {
    let total = 0;
    groups.forEach(group => {
      let count = 0;
      group.querySelectorAll('.term-club').forEach(club => {
        const matches = (year.value === 'all' || club.dataset.years.split(',').includes(year.value)) &&
          (day.value === 'all' || group.dataset.day === day.value) &&
          (activity.value === 'all' || club.dataset.activity === activity.value);
        club.hidden = !matches;
        if (matches) count++;
      });
      group.hidden = count === 0;
      group.querySelector('.day-count').textContent = `${count} ${count === 1 ? 'club' : 'clubs'}`;
      total += count;
      const link = dayLinks.find(l => l.dataset.dayLink === group.dataset.day);
      if (link) link.hidden = count === 0;
    });
    const selection = year.value === 'all' ? '' : ` for ${year.selectedOptions[0].textContent}`;
    const selectedDay = day.value === 'all' ? '' : ` on ${day.selectedOptions[0].textContent}`;
    const selectedActivity = activity.value === 'all' ? '' : ` (${activity.selectedOptions[0].textContent})`;
    status.textContent = `${total} club ${total === 1 ? 'session' : 'sessions'}${selection}${selectedDay}${selectedActivity}`;
    empty.hidden = total !== 0;
  }
  form.hidden = false;
  form.addEventListener('change', filterClubs);
  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('reset', event => {
    event.preventDefault();
    year.value = 'all';
    day.value = 'all';
    activity.value = 'all';
    filterClubs();
  });
  filterClubs();
  // Highlight the day button for the day currently in view.
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        dayLinks.forEach(l => l.setAttribute('aria-current', String(l.dataset.dayLink === entry.target.dataset.day)));
      });
    }, { rootMargin: '-150px 0px -60% 0px' });
    groups.forEach(group => observer.observe(group));
  }
})();
