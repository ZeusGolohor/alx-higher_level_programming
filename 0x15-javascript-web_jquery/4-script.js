$(document).ready(() => {
  const el = $('#toggle_header');
  el.on('click', () => {
    const head = $('header');
    if (head.hasClass('green')) {
      head.removeClass('green');
      head.addClass('red');
    } else {
      head.removeClass('red');
      head.addClass('green');
    }
  });
});
