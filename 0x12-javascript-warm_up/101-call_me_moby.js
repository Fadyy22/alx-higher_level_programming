#!/usr/bin/node
exports.callMeMoby = function (number, callback) {
  for (let i = 0; i < number; i++) {
    callback();
  }
}
