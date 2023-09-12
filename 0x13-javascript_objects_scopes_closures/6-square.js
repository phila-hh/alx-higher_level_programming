#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    const char = c || 'X';
    for (let x = 0; x < this.height; x++) {
      console.log(char.repeat(this.width));
    }
  }
};
