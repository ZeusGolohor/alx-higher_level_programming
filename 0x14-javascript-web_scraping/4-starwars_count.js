#!/usr/bin/node
const request = require('request');
const characterId = '18';

function stat (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode !== 200) {
        console.error('Failed to fetch data');
        return;
      }
      const films = JSON.parse(body).results;
      const wedge = films.filter(film =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );
      console.log(`${wedge.length}`);
    }
  });
}

if (process.argv.length === 3) {
  const url = 'https://swapi-api.alx-tools.com/api/films/';
  stat(url);
} else {
  console.log('Usage: script <URL>');
}
