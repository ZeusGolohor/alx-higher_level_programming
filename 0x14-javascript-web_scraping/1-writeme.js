#!/usr/bin/node

const fs = require('fs');
function writeFile (filepath, content) {
  try {
    fs.writeFileSync(filepath, content, 'utf8');
  } catch (error) {
    console.error(error);
  }
}

if (process.argv.length === 4) {
  const filepath = process.argv[2];
  const content = process.argv[3];
  writeFile(filepath, content);
} else {
  console.log('Usage: script filepath content');
}
