#!/usr/bin/node
if (isNaN(process.argv[2])) console.log('Not a number');
else {
  const value = parseInt(process.argv[2]);
  const line = 'My number: ' + value;
  console.log(line);
}
