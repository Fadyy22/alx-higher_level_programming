#!/usr/bin/node
logs = 0;
exports.logMe = function (item) {
  console.log(logs + ': ' + item);
  logs++;
};
