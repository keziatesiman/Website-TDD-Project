//chat box
var isSendTurn = true;


function sendMsg(msg) {
  return '<div class="msg-send"><p>' + msg + '</p></div>';
}

function receiveMsg(msg) {
  return '<div class="msg-receive"><p>' + msg + '</p></div>';
}

var chat = function(msg) {
  if (isSendTurn) {
    $('.msg-insert').append(sendMsg(msg));
    $(".chat-body").scrollTop($(".chat-body").height());
  } else {
    $('.msg-insert').append(receiveMsg(msg));
    $(".chat-body").scrollTop($(".chat-body").height());
  }
  isSendTurn = !isSendTurn;
}

// Calculator

var erase = false;

var go = function(x) {
	var print = document.getElementById('print');
	console.log(x);
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
	} else if (x === 'log'){
		print.value = Math.log10(Math.round(evil(print.value) * 10000) / 10000).toFixed(12);
		erase = true;
	} 
	 else if (x === 'sin'){
		print.value = Math.sin(Math.round(evil(print.value) * 10000) / 10000).toFixed(12);
		erase = true;
	}
	 else if (x === 'tan'){
		print.value = Math.tan(Math.round(evil(print.value) * 10000) / 10000).toFixed(12);
		erase = true;
	}
	else {
		print.value += x;
	}
};

function evil(fn) {
	return new Function('return ' + fn)();
}



//theme
function applyTheme(themeId) {
  var themes = JSON.parse(localStorage.getItem('themes'));
  selectedTheme = themes.find(theme => theme.id == themeId);
  $('body').css('background', selectedTheme.bcgColor);
  $('body').css('color', selectedTheme.fontColor);
  localStorage.setItem('selectedThemeId', JSON.stringify(themeId));
}

function loadSelectedTheme() {
  selectedThemeId = JSON.parse(localStorage.getItem('selectedThemeId'));
  applyTheme(selectedThemeId);
}

function initTheme() {
  if (localStorage.getItem('themes') === null) {
    themes = [
              {"id":0,"text":"Red","bcgColor":"#F44336","fontColor":"#ABABAB"},
              {"id":1,"text":"Pink","bcgColor":"#E91E63","fontColor":"#ABABAB"},
              {"id":2,"text":"Purple","bcgColor":"#9C27B0","fontColor":"#ABABAB"},
              {"id":3,"text":"Indigo","bcgColor":"#3F51B5","fontColor":"#ABABAB"},
              {"id":4,"text":"Blue","bcgColor":"#2196F3","fontColor":"#212121"},
              {"id":5,"text":"Teal","bcgColor":"#009688","fontColor":"#212121"},
              {"id":6,"text":"Lime","bcgColor":"#CDDC39","fontColor":"#212121"},
              {"id":7,"text":"Yellow","bcgColor":"#FFEB3B","fontColor":"#212121"},
              {"id":8,"text":"Amber","bcgColor":"#FFC107","fontColor":"#212121"},
              {"id":9,"text":"Orange","bcgColor":"#FF5722","fontColor":"#212121"},
              {"id":10,"text":"Brown","bcgColor":"#795548","fontColor":"#ABABAB"}
            ];

    localStorage.setItem('themes', JSON.stringify(themes));
  }

  if (localStorage.getItem('selectedThemeId') === null) {
  	//set indigo as default color
    localStorage.setItem('selectedThemeId', 3);
  }
}

$(document).ready(function() {
  initTheme();
  loadSelectedTheme();

  $('.my-select').select2({
    'data': JSON.parse(localStorage.getItem('themes')),
  }).select2("val", JSON.parse(localStorage.getItem('selectedThemeId')));

  $('.apply-button').on('click', function(){
    applyTheme($('.my-select').val());
  })
  //buat text chat
  $('textarea').on('keydown', function (e) {
    if (e.keyCode == 13) {//key code enter
      chat($('textarea').val());
    }
  });

  $('textarea').on('keyup', function (e) {
    if (e.keyCode == 13) {
      $('textarea').val('');
    }
  });
});
