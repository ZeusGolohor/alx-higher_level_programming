#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let no = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      no = no + 1;
    }
    i = i + 1;
  }
  return (no);
};
