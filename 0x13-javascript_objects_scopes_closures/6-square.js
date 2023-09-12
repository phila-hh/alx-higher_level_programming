#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let charc = c || 'X';
    for (let q = 0; q < this.height; q++) {
      console.log(charc.repeat(this.width));
    }
  }
};
