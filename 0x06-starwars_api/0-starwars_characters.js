#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const baseUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchCharacters (movieId) {
  request(baseUrl, { json: true }, (err, res, body) => {
    if (err) {
      console.error('Error fetching film details:', err.message);
      process.exit(1);
    }

    const characterUrls = body.characters;

    const fetchCharacterDetails = (url, callback) => {
      request(url, { json: true }, (err, res, body) => {
        if (err) {
          console.error('Error fetching character details:', err.message);
          callback(err);
        } else {
          console.log(body.name);
          callback(null);
        }
      });
    };

    let count = 0;
    const fetchNext = () => {
      if (count < characterUrls.length) {
        fetchCharacterDetails(characterUrls[count], (err) => {
          if (err) {
            process.exit(1);
          } else {
            count++;
            fetchNext();
          }
        });
      }
    };

    fetchNext();
  });
}

fetchCharacters(movieId);
