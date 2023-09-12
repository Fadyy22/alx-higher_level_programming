#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const newList = list.map((x) => x * list.indexOf(x));
console.log(newList);
