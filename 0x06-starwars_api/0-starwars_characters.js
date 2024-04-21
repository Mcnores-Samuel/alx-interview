#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, async (error, response, body) => {
  const { characters } = JSON.parse(body);
  for (const character of characters) {
    request(character, (error, response, body) => {
      console.log(JSON.parse(body).name);
    });
  }
});
