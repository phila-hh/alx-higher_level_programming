#!/usr/bin/node
const num = parseInt(process.argv[2]);

function factorial(x) {
	if (x === 1) {
		return (1);
	} else {
		return (x + factorial(x - 1));
	}
}

if (!num) {
	console.log(1);
} else {
	const result = factorial(num);
	console.log(result);
}
