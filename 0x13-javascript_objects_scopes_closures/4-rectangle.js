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

  rotate () {
    if ((this.width > 1) && (this.height > 1)) {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  double () {
    if ((this.width > 1) && (this.height > 1)) {
      this.width = this.width * 2;
      this.height = this.height * 2;
    }
  }
}
module.exports = Rectangle;
