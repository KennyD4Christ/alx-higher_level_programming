#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const data = JSON.parse(body);
  let wedgeCount = 0;
  const wedgeCharacterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

  data.results.forEach(film => {
    if (film.characters.includes(wedgeCharacterUrl)) {
      wedgeCount++;
    }
  });

  console.log(wedgeCount);
});
