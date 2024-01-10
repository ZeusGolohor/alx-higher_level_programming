#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  const len = list.length;
  let i = len - 1;
  let x = 0;
  while (i > -1) {
    newList[x] = list[i];
    x = x + 1;
    i = i - 1;
  }
  list = newList;
  return (list);
};
