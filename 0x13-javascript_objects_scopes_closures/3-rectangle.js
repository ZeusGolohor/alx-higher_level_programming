#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 1) && (h > 1)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = 'X';
    str = str.repeat(this.width);
    let i = 0;
    while (i < this.height) {
      console.log(str);
      i = i + 1;
    }
  }
}
module.exports = Rectangle;
