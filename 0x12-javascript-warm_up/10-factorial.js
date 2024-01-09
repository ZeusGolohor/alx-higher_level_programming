#!/usr/bin/node
const l = Number(process.argv[2]);
function f (num) {
  if (isNaN(num) || num === 0) {
    return (1);
  }
  return (num * f(num - 1));
}
if (!isNaN(l)) {
  console.log(f(l));
} else {
  console.log(1);
}
