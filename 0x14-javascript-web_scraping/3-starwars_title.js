#!/usr/bin/node
const request = require('request');

function stat (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode !== 200) {
        console.error('Failed to fetch data');
        return;
      }
      const movie = JSON.parse(body);
      console.log('Title:', movie.title);
    }
  });
}

if (process.argv.length === 3) {
  const id = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  stat(url);
} else {
  console.log('Usage: script <URL>');
}
