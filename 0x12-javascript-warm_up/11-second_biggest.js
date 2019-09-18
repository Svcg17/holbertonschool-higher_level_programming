#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
	let second = 0;
	let i = 0;
	const array = process.argv.slice(2).sort()
	max = Math.max.apply(Math, array)
	for (i in array) {
		if (array[i] == max) {
			i--
			console.log(array[i])
		}
	}
}
