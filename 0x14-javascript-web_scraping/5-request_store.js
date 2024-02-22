#!/usr/bin/node
const request = require('request');
const fs = require('fs');

function stat (url1, filepath1) {
  const url = url1;
  const filepath = filepath1;
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode !== 200) {
        console.error('Failed to fetch data');
        return;
      }
      try {
        fs.writeFileSync(filepath, body, 'utf8');
      } catch (error) {
        console.error(error);
      }
    }
  });
}

if (process.argv.length === 4) {
  const url = process.argv[2];
  const filepath = process.argv[3];
  stat(url, filepath);
} else {
  console.log('Usage: script <URL>');
}
