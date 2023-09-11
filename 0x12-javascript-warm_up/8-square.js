#!/usr/bin/node
const sz = process.argv[2];

if (sz === undefined || isNaN(sz)) {
	console.log('Missing size');
} else {
	let c = 0;
	while (c < sz) {
		console.log('X'.repeat(sz));
		c++;
	}
}
