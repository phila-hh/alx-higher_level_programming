#!/usr/bin/node
const vars = process.argv.slice(2);

if (vars.length === 0) {
	console.log("No argument");
} else if (vars.length === 1) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
