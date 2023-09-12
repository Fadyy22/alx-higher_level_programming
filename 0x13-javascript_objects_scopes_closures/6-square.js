#!/usr/bin/node
const ParentSquare = require('./5-square');

module.exports = class Square extends ParentSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.charPrint('X');
    }
  }
};
