#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (!num) {
	console.log("Missing number of occurrences");
} esle {
	for (let x = 0; num > x; x++) {
		console.log("C is fun");
	}
}
