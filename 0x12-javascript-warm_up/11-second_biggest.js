#!/usr/bin/node
let fVar = process.argv.slice(2);
const sVar = process.argv.length;

if (sVar <= 3) {
	console.log('0');
} else {
	fVar = fVar.map(Number);
	const tVar = fVar.sort(
		function (x, y) {
			return y - x;
		})[1];
	console.log(tVar);
}
