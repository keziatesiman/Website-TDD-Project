// Calculator

var erase = false;

var go = function(x) {
	var print = document.getElementById('print');

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
//theme
$(document).ready(function() {
    $('.my-select').select2();
});
$('.apply-button-class').on('click', function(){  // sesuaikan class button
    // [TODO] ambil value dari elemen select .my-select

    // [TODO] cocokan ID theme yang dipilih dengan daftar theme yang ada

    // [TODO] ambil object theme yang dipilih

    // [TODO] aplikasikan perubahan ke seluruh elemen HTML yang perlu diubah warnanya

    // [TODO] simpan object theme tadi ke local storage selectedTheme
})
