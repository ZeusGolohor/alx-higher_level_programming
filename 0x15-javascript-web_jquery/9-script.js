$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data, status) => {
    $('DIV#hello').text(data.hello);
  });
});
