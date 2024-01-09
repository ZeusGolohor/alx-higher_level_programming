#!/usr/bin/node
exports.callMeMoby = (num, func) => {
  let i = 0;
  while (i < num) {
    func();
    i = i + 1;
  }
};
