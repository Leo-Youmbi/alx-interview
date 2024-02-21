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

  const getNames = async (arg) => {
    const result = await fetcher(`https://swapi-api.alx-tools.com/api/films/${arg}/`);
    const people = result.characters;
    for (const personUrl of people) {
      const res = await fetcher(personUrl);
      console.log(res.name);
    }
  };

  getNames(arg);
} else {
  console.log('Usage: ./0-starwars_characters.js number');
}
