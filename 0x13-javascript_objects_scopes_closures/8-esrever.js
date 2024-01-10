#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  const len = list.length;
  let i = 0;
  while (i < len) {
    newList.push(list[(len - (len - i))]);
    i = i + 1;
  }
  list = newList;
  return (list);
};
