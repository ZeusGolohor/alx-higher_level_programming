#!/usr/bin/node
const l = Number(process.argv[2]);
if (!isNaN(l)) {
  let i = 0;
  while (i < l) {
    const str = 'X'.repeat(l);
    console.log(str);
    i = i + 1;
  }
} else {
  console.log('Missing size');
}
