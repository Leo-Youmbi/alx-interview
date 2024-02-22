#!/usr/bin/node

const request = require('request');

const arrayOfArguments = process.argv.slice(2);

if (arrayOfArguments.length === 1) {
  const movieId = arrayOfArguments[0];

  const getCharactersForMovie = (movieId) => {
    return new Promise((resolve, reject) => {
      const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const filmData = JSON.parse(body);
          const characters = filmData.characters;
          resolve(characters);
        }
      });
    });
  };

  const fetchCharacterData = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData);
        }
      });
    });
  };

  const printCharactersForMovie = async (movieId) => {
    try {
      const characters = await getCharactersForMovie(movieId);
      for (const characterUrl of characters) {
        const characterData = await fetchCharacterData(characterUrl);
        console.log(characterData.name);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  printCharactersForMovie(movieId);
} else {
  console.log('Usage: ./0-starwars_characters.js number');
}
