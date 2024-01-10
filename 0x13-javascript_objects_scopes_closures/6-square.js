#!/usr/bin/node
const Square2 = require('./5-square.js');

class Square extends Square2 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let str = 'c';
      str = str.repeat(this.width);
      let i = 0;
      while (i < this.height) {
        console.log(str);
        i = i + 1;
      }
    }
  }
}
module.exports = Square;
