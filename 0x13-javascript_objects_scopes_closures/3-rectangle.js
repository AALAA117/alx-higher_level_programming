#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w = 0, h = 0) {
    if (w === 0 || w < 0 || h === 0 || h < 0) {
      return (null);
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }
};
