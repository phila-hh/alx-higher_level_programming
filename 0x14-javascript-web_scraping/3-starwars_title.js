#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
