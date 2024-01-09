#!/usr/bin/node
const l = process.argv;
if ((l.length === 2) || (l.length === 3)) {
  console.log(0);
} else {
  const len = l.length;
  let i = 2;
  let res = 0;
  while (i < len) {
    if (l[i] > res) {
      res = l[i];
    }
    i = i + 1;
  }
  let x = 2;
  let re = 0;
  while (x < len) {
    if ((l[x] > re) && (l[x] !== res)) {
      re = l[x];
    }
    x = x + 1;
  }
  console.log(re);
}
