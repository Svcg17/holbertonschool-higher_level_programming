#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
let counter = 0;
request(url, function (err, request, body) {
  if (err) {
    console.log(err);
  } else {
    for (const i of JSON.parse(body)) {
      if (i.completed === true) {
        if (dict[i.userId]) {
          counter++;
          dict[i.userId] = counter;
        } else {
          counter = 1;
          dict[i.userId] = counter;
        }
      }
    }
    console.log(dict);
  }
});
