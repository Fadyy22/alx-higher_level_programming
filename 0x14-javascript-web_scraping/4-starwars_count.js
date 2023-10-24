#!/usr/bin/node
const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/people/18';

request.get(api, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log((JSON.parse(body).films).length);
  }
});
