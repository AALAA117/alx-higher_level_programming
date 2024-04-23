#!/usr/bin/node
const numOfArg = process.argv.length - 2;
let largest = process.argv[2];
let secondLargest = -Infinity;
if (numOfArg === 1 || numOfArg === 0) {
  console.log(0);
} else {
  const lastIndex = process.argv.length - 1;
  for (let k = 3; k <= lastIndex; k++) {
    if (process.argv[k] > largest) {
      secondLargest = largest;
      largest = process.argv[k];
    } else if (process.argv[k] > secondLargest && process.argv[k] < largest) {
      secondLargest = process.argv[k];
    }
  }
  console.log(secondLargest);
}
