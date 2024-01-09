#!/usr/bin/node
const n = Number(process.argv[2]);
if (!isNaN(n)) {
  console.log('My number: ' + Math.floor(n));
} else {
  console.log('Not a number');
}
