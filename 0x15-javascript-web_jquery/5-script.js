$(document).ready(() => {
  const el = $('#add_item');
  el.on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });
});
