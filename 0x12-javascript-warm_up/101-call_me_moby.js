#!/usr/bin/node
exports.callMeMoby = function (x, theFunc) {
	for (let c = 0; c < x; c++) {
		theFunc();
	}
};
