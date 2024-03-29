#!/usr/bin/node
const request = require('request');

const api = process.argv[2];
let noMovies = 0;

request.get(api, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    for (const movie of results) {
      for (const character of movie.characters) {
        if (character.search('18') > 0) {
          noMovies += 1;
        }
      }
    }
  }
  console.log(noMovies);
});
