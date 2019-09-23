#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  var counter = 0;
  for (let i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return counter;
};
