#!/usr/bin/node
const request = require('request');

const moviesAPI = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(moviesAPI, async (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;

    for (const character of characters) {
      await new Promise((resolve, reject) => {
        request(character, async (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  }
});
