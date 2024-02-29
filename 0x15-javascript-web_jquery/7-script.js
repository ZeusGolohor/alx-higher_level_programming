$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, status) => {
    $('#character').text(data.name);
  });
});
