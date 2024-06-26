#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, async (error, response, body) => {
  const { characters } = JSON.parse(body);
  if (error) {
    console.log(error);
  }
  const promises = characters.map((character) => new Promise((resolve, reject) => {
    request(character, (error, response, body) => {
      if (error) {
        reject(error);
      }
      resolve(JSON.parse(body).name);
    });
  }));
  const names = await Promise.all(promises);
  names.forEach((name) => console.log(name));
});
