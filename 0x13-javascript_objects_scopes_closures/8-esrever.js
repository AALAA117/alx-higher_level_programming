#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  const length = list.length;
  let temp;
  const lastIndex = length - 1;
  const middleIndex = Math.round(lastIndex / 2);
  for (i = 0; i < middleIndex; i++) {
    temp = list[i];
    list[i] = list[length - 1 - i];
    list[length - 1 - i] = temp;
  }
  return (list);
};
