#!/usr/bin/node
const myV = process.argv[2];

if (myV === undefined || isNaN(myV)) { 
	console.log('Missing number of occurrences'); 
} else {
	let c = 0;
	while (c < myV) {
		console.log('C is fun');
		c++;
	} 
}
