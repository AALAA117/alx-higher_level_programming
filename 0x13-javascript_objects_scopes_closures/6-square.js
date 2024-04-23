#!/usr/bin/node
const Square = require('./5-square');
module.exports = class Square extends Square{
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.size; i++) {
        console.log('X'.repeat(this.size));
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    }
  }
};
