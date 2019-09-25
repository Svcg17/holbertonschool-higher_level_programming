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
      dict[i.userId] = counter;
      counter = 0;
      for (const j of JSON.parse(body)) {
        if (j.userId === i.userId) {
          if (j.completed === true) {
            counter++;
          }
        }
      }
    }
    console.log(dict);
  }
});
