$(document).ready(() => {
  const el = $('#update_header');
  el.on('click', () => {
    $('header').text('New Header!!!');
  });
});
