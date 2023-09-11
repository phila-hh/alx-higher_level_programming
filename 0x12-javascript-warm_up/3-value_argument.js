#!/usr/bin/node
const myV = process.argv[2];

if (myV === undefined) {
	console.log('No argument');
} else {
	console.log(myV);
}
