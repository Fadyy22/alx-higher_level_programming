#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const api = process.argv[2]

request(api, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = body;
    fs.writeFileSync(process.argv[3], content, 'utf-8');
  }
});
