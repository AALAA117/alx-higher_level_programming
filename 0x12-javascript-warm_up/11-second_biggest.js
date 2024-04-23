#!/usr/bin/node
const numOfArg = process.argv.length - 2;
let max;
if (numOfArg === 1 || numOfArg === 0) {
  console.log(0);
} else {
  const lastIndex = numOfArg - 1;
  for (let i = 0; i < numOfArg; i++) {
    for (let k = 2; k < lastIndex; k++) {
      if (process.argv[k + 1] > process.argv[k]) max = process.argv[k + 1];
      else continue;
    }
  }
  console.log(max);
}
