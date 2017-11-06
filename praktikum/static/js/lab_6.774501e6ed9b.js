// Calculator
var print = document.getElementById('print');
var erase = false;

var go = function(x) {
	var print.value = "";

	if (erase){
		print.value ="";
		erase = false;
	}
	if (x === 'ac') {
    /* implemetnasi clear all */
    print.value = "";
	} else if (x === 'eval') {
		print.value = Math.round(evil(print.value) * 10000) / 10000;
		erase = true;
	} else {
		print.value += x;
	}
};

function evil(fn) {
	return new Function('return ' + fn)();
}
// END
