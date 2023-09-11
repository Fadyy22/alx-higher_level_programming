#!/usr/bin/node
const args = process.argv;
const arrayNums = [];
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    arrayNums.push(parseInt(args[i]));
  }
  const maxIndex = arrayNums.indexOf(Math.max(...arrayNums));
  arrayNums.splice(maxIndex, 1);
  console.log(Math.max(...arrayNums));
}
