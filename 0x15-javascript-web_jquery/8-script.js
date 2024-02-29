$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, status) => {
    $('#character').text(data.name);
    for (const key in data.films) {
      console.log(data.films[key]);
      $.get(data.films[key], (data, status) => {
        const newEl = $('<li>').text(data.title);
        $('UL#list_movies').append(newEl);
      });
    }
  });
});
