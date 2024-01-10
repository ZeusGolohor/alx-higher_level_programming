#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 1) && (h > 1)) {
      this.width = w;
      this.height = h;
    }
  }

    print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
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
