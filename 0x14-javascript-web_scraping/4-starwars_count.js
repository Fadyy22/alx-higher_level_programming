#!/usr/bin/node
const request = require('request');

const api = process.argv[2];
let noMovies = 0;

request.get(api, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          noMovies += 1;
        }
      }
    }
  }
  console.log(noMovies);
});
