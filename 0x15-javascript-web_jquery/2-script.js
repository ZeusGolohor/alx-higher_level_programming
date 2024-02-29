$(document).ready(() => {
  const el = $('#red_header');
  el.on('click', () => {
    $('header').css('color', '#FF0000');
  });
});
