#!/usr/bin/node
const list = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
const f = (li) => {
  const len = li.length;
  let i = 0;
  while (i < len) {
    console.log(li[i]);
    i = i + 1;
  }
};
f(list);
