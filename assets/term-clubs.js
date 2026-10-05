/* Filters only the fixed HTML catalogue. No document fetch or automatic refresh. */
(() => {
  const form = document.getElementById('clubs-filters');
  if (!form) return;
  const year = document.getElementById('club-year');
  const day = document.getElementById('club-day');
  const groups = [...document.querySelectorAll('.clubs-day')];
  const status = document.getElementById('club-results');
  const empty = document.getElementById('clubs-empty');
  function filterClubs() {
    let total = 0;
    groups.forEach(group => {
      let count = 0;
      group.querySelectorAll('.term-club').forEach(club => {
        const matches = (year.value === 'all' || club.dataset.years.split(',').includes(year.value)) &&
          (day.value === 'all' || group.dataset.day === day.value);
        club.hidden = !matches;
        if (matches) count++;
      });
      group.hidden = count === 0;
      group.querySelector('.day-count').textContent = `${count} ${count === 1 ? 'club' : 'clubs'}`;
      total += count;
    });
    const selection = year.value === 'all' ? '' : ` for ${year.selectedOptions[0].textContent}`;
    const selectedDay = day.value === 'all' ? '' : ` on ${day.selectedOptions[0].textContent}`;
    status.textContent = `${total} club ${total === 1 ? 'session' : 'sessions'}${selection}${selectedDay}`;
    empty.hidden = total !== 0;
  }
  form.hidden = false;
  form.addEventListener('change', filterClubs);
  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('reset', event => {
    event.preventDefault();
    year.value = 'all';
    day.value = 'all';
    filterClubs();
  });
  filterClubs();
})();
