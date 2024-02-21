#!/usr/bin/node
const request = require('request');

function stat (url) {
  request(url, (error, response) => {
    if (error) {
      console.error('Error:', error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

if (process.argv.length === 3) {
  const url = process.argv[2];
  stat(url);
} else {
  console.log('Usage: script <URL>');
}
