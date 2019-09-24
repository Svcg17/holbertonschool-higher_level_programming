#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  const newList = [];
  const newkey = dict[key];
  newDict[newkey] = newList;
  for (const k in dict) {
    if (dict[k] === dict[key]) {
      newList.push(key);
    }
  }
}
console.log(newDict);
