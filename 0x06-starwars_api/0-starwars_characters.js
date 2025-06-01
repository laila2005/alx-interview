#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) process.exit();

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) return;

  const characters = JSON.parse(body).characters;

  characters.forEach(url => {
    request(url, (err, res, body) => {
      if (!err) {
        console.log(JSON.parse(body).name);
      }
    });
  });
});
