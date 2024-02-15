#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Please provide a valid movie ID as a command line argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, { json: true }, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error fetching movie information from SWAPI:', error || body);
    process.exit(1);
  }

  const characters = body.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for the provided movie ID.');
    process.exit(0);
  }

  // Fetch and print character names
  characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (error, response, characterBody) => {
      if (!error && response.statusCode === 200) {
        console.log(characterBody.name);
      } else {
        console.error('Error fetching character information from SWAPI:', error || characterBody);
      }
    });
  });
});
