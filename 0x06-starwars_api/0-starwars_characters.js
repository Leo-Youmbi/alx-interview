#!/usr/bin/node

const arrayOfArguments = process.argv.slice(2);
if (arrayOfArguments.length === 1) {
  const arg = arrayOfArguments[0];
  const fetcher = async (url = '') => {
    try {
      const res = await fetch(url);
      const result = res.json();
      return result;
    } catch (e) {
      return e.message;
    }
  };
  fetcher(`https://swapi-api.alx-tools.com/api/films/${arg}/`)
    .then((res) => {
      const people = res.characters;
      people.forEach((personUrl) => {
        fetcher(personUrl)
          .then((res) => console.log(res.name));
      });
    });
} else {
  console.log('Usage: ./0-starwars_characters.js number');
}
