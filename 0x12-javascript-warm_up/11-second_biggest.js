#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  let i = 0;
  const array = process.argv.slice(2).sort();
  const max = Math.max.apply(Math, array);
  for (i in array) {
    if (array[i] === String(max)) {
      i--;
      console.log(array[i]);
    }
  }
}
