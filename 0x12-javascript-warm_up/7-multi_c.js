#!/usr/bin/node
const l = Number(process.argv[2]);
if (!isNaN(l)) {
  let i = 0;
  while (i < l) {
    console.log('C is fun');
    i = i + 1;
  }
} else {
  console.log('Missing number of occurrences');
}
