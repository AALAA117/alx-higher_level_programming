#!/usr/bin/node
const numOfArg = process.argv.length - 2;
let largest = parseInt(process.argv[2]);
let secondLargest = -Infinity;
let k;
let num;
if (numOfArg === 1 || numOfArg === 0) {
  console.log(0);
} else {
  const lastIndex = process.argv.length - 1;
  for (k = 3; k <= lastIndex; k++) {
    num = parseInt(process.argv[k]);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }
  console.log(secondLargest);
}
