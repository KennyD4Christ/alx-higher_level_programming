#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
	return;
      }
      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
