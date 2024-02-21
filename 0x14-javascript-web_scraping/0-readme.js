#!/usr/bin/node

const fs = require('fs');
function fileReader (filepath) {
  fs.readFile(filepath, 'utf8', (error, data) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(data);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: script file_path');
} else {
  const filepath = process.argv[2];
  fileReader(filepath);
}
