#!/usr/bin/node
const l1 = Number(process.argv[2]);
const l2 = Number(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
if (!isNaN(l1) && !isNaN(l2)) {
  add(l1, l2);
} else {
  console.log(NaN);
}
