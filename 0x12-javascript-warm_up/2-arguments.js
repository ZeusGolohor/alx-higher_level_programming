#!/usr/bin/node
const l = process.argv.length - 2;
if (l === 0) {
  console.log('No argument');
} else if (l === 1) {
  console.log('Argument found');
} else if (l > 1) {
  console.log('Arguments found');
}
