#!/usr/bin/node
const fVar = process.argv[2];

function myFactorial (c) {
	if (c < 0) {
		return (-1);
	} else if (c === 0 || isNaN(c)) {
		return (1);
	} else {
		return (c * myFactorial(c - 1));
	}
}
console.log(myFactorial(parseInt(fVar)));
