$(document).ready(() => {
  const el = $('#red_header');
  el.on('click', () => {
    $('header').addClass('red');
  });
});
