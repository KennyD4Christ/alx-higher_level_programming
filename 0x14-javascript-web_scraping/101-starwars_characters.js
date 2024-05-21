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
  const characterUrls = film.characters;

  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          reject(err);
	} else {
	  resolve(JSON.parse(body).name);
	}
      });
    });
  };

  const printCharacters = async () => {
    for (const characterUrl of characterUrls) {
      try {
        const characterName = await fetchCharacter(characterUrl);
	console.log(characterName);
      } catch (err) {
        console.error('Error:', err);
      }
    }
  };

  printCharacters();
});
