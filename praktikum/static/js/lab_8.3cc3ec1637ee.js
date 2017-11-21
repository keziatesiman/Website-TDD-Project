$(document).ready(function() {
//inisiasi data tema (optional)
  var themes = [{"id":0,"text":"Red","bcgColor":"#F44336","fontColor":"#FAFAFA"},
    {"id":1,"text":"Pink","bcgColor":"#E91E63","fontColor":"#FAFAFA"},
    {"id":2,"text":"Purple","bcgColor":"#9C27B0","fontColor":"#FAFAFA"},
    {"id":3,"text":"Indigo","bcgColor":"#3F51B5","fontColor":"#FAFAFA"},
    {"id":4,"text":"Blue","bcgColor":"#2196F3","fontColor":"#212121"},
    {"id":5,"text":"Teal","bcgColor":"#009688","fontColor":"#212121"},
    {"id":6,"text":"Lime","bcgColor":"#CDDC39","fontColor":"#212121"},
    {"id":7,"text":"Yellow","bcgColor":"#FFEB3B","fontColor":"#212121"},
    {"id":8,"text":"Amber","bcgColor":"#FFC107","fontColor":"#212121"},
    {"id":9,"text":"Orange","bcgColor":"#FF5722","fontColor":"#212121"},
    {"id":10,"text":"Brown","bcgColor":"#795548","fontColor":"#FAFAFA"},
    {"id":11,"text":"White","bcgColor":"white","fontColor":"black"},
    {"id":12,"text":"Black","bcgColor":"black","fontColor":"white"},
    {"id":13,"text":"Grey","bcgColor":"grey","fontColor":"white"},
  ];
  var selectedTheme = {"White":{"bcgColor":"white","fontColor":"black"}};
  
  //simpan data tema di local storage
  localStorage.setItem('themes', JSON.stringify(themes));
  localStorage.setItem('selectedTheme', JSON.stringify(selectedTheme));
  //menload tema ke select2
  var retrievedObject = localStorage.getItem('themes');
  $('.my-select').select2({data: JSON.parse(retrievedObject)});
  
  //menerapkan selectedTheme yang ada di local storage
  var retrievedSelected = JSON.parse(localStorage.getItem('selectedTheme'));
    var key;
    var bcgColor;
    var fontColor;
  for (key in retrievedSelected) {
      if (retrievedSelected.hasOwnProperty(key)) {
          bcgColor=retrievedSelected[key].bcgColor;
          fontColor=retrievedSelected[key].fontColor;
      }
  }  
  $("body").css({"background-color": bcgColor});
  $("p:not(#footer):not(.feed p)").css({"color":fontColor});
  $("h1").css({"color":fontColor});
  $("h2").css({"color":fontColor});
  $("h3").css({"color":fontColor});



  //fungsi tombol apply
  $('.apply-button').on('click', function(){  // sesuaikan class button
    // [TODO] ambil value dari elemen select .my-select
    var valueTheme = $('.my-select').val();
    // [TODO] cocokan ID theme yang dipilih dengan daftar theme yang ada
    // [TODO] ambil object theme yang dipilih
    // [TODO] aplikasikan perubahan ke seluruh elemen HTML yang perlu diubah warnanya
    // [TODO] simpan object theme tadi ke local storage selectedTheme
    var theme;
    var a;
    var selectedTheme = {};
    //mencari tema yang sesuai dengan id
    for(a in themes){
      if(a==valueTheme){
        var bcgColor = themes[a].bcgColor;
        var fontColor = themes[a].fontColor;
        var text = themes[a].text;
        $("body").css({"background-color": bcgColor});
        $("p:not(#footer):not(.feed p)").css({"color":fontColor});
        $("h1").css({"color":fontColor});
        $("h2").css({"color":fontColor});
        $("h3").css({"color":fontColor});
        selectedTheme[text] = {"bcgColor":bcgColor,"fontColor":fontColor};
        localStorage.setItem('selectedTheme', JSON.stringify(selectedTheme));
      }
    }
});

  window.fbAsyncInit = function() {
    FB.init({
      appId      : '1756190254674727',
      cookie     : true,
      xfbml      : true,
      version    : 'v2.11'
    });
    
    // implementasilah sebuah fungsi yang melakukan cek status login (getLoginStatus)
    // dan jalankanlah fungsi render di bawah, dengan parameter true jika
    // status login terkoneksi (connected)
    FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
    // the user is logged in and has authenticated your
    // app, and response.authResponse supplies
    // the user's ID, a valid access token, a signed
    // request, and the time the access token 
    // and signed request each expire
    var uid = response.authResponse.userID;
    var accessToken = response.authResponse.accessToken;
    render(true);
    } 
     else if (response.status === 'not_authorized') {
            render(false);
    }else {
    // the user isn't logged in to Facebook.
    render(false);
    }
  });
    // Hal ini dilakukan agar ketika web dibuka dan ternyata sudah login, maka secara
    // otomatis akan ditampilkan view sudah login
  
   // FB.AppEvents.logPageView();   
      
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "https://connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));

  // Fungsi Render, menerima parameter loginFlag yang menentukan apakah harus
  // merender atau membuat tampilan html untuk yang sudah login atau belum
  // Ubah metode ini seperlunya jika kalian perlu mengganti tampilan dengan memberi
  // Class-Class Bootstrap atau CSS yang anda implementasi sendiri

  const render = loginFlag => {
    if (loginFlag) {
      // Jika yang akan dirender adalah tampilan sudah login

      // Memanggil method getUserData (lihat ke bawah) yang Anda implementasi dengan fungsi callback
      // yang menerima object user sebagai parameter.
      // Object user ini merupakan object hasil response dari pemanggilan API Facebook.
      getUserData(user => {

        // Render tampilan profil, form input post, tombol post status, dan tombol logout
        $('#lab8').html(
          '<div class="profile">' +
            '<img class="cover" src="' + user.cover.source + '" alt="cover" />' +
            '<img class="picture" src="' + user.picture.data.url + '" alt="profpic" />' +
            '<div class="data">' +
              '<h1>' + user.name + '</h1>' +
              '<h2>' + user.about + '</h2>' +
              '<h3>' + user.email + ' - ' + user.gender + '</h3>' +
            '</div>' +
          '</div>' +
          '<input id="postInput" type="text" class="post" placeholder="Ketik Status Anda" />' +
          '<button class="postStatus" onclick="postStatus()">Post ke Facebook</button>' +
          '<button class="logout" onclick="facebookLogout()">Logout</button>'
        );

        // Setelah merender tampilan di atas, dapatkan data home feed dari akun yang login
        // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
        // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
        // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
        getUserFeed(feed => {
          feed.data.map(value => {
            // Render feed, kustomisasi sesuai kebutuhan.
            if (value.message && value.story) {
              $('#lab8').append(
                '<div class="feed">' +
                  '<h1>' + value.message + '</h1>' +
                  '<h2>' + value.story + '</h2>' +
                '</div>'
              );
            } else if (value.message) {
              $('#lab8').append(
                '<div class="feed">' +
                  '<h1>' + value.message + '</h1>' +
                '</div>'
              );
            } else if (value.story) {
              $('#lab8').append(
                '<div class="feed">' +
                  '<h2>' + value.story + '</h2>' +
                '</div>'
              );
            }
          });
        });
      });
    } else {
      // Tampilan ketika belum login
      $('#lab8').html('<button class="login" onclick="facebookLogin()">Login</button>');
    }
  };

  const facebookLogin = () => {
    // TODO: Implement Method Ini
    // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan sudah login
    // ketika login sukses, serta juga fungsi ini memiliki segala permission yang dibutuhkan
    // pada scope yang ada. Anda dapat memodifikasi fungsi facebookLogin di atas.
    FB.login(function(response){
       console.log(response);
       render(true);
     }, {scope:'public_profile,user_posts,publish_actions,user_about_me'})

  };

  const facebookLogout = () => {
    // TODO: Implement Method Ini
    // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan belum login
    // ketika logout sukses. Anda dapat memodifikasi fungsi facebookLogout di atas.
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
          FB.logout();
        }
     });

  };

  // TODO: Lengkapi Method Ini
  // Method ini memodifikasi method getUserData di atas yang menerima fungsi callback bernama fun
  // lalu merequest data user dari akun yang sedang login dengan semua fields yang dibutuhkan di 
  // method render, dan memanggil fungsi callback tersebut setelah selesai melakukan request dan 
  // meneruskan response yang didapat ke fungsi callback tersebut
  // Apakah yang dimaksud dengan fungsi callback?
const getUserData = (fun) => {
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            FB.api('/me?fields=id,name,about,email,gender,cover,picture.width(168).height(168)', 'GET', function(response) {
                console.log(response);
                if (response && !response.error) {
                    fun(response);
                } else {
                    alert("Something went wrong");
                }
            });
        }
    });
};


  const getUserFeed = (fun) => {
    // TODO: Implement Method Ini
    // Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data Home Feed dari akun
    // yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
    // tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
    // tersebut
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            FB.api('/me/posts', 'GET', function(response) {
                console.log(response);
                if (response && !response.error) {
                    fun(response);
                } else {
                    alert("Something went wrong");
                }
            });
        }
    });


  };

  const postFeed = (message) => {
    // Todo: Implement method ini,
    // Pastikan method ini menerima parameter berupa string message dan melakukan Request POST ke Feed
    // Melalui API Facebook dengan message yang diterima dari parameter.
     FB.api('/me/feed', 'POST', {message:message});
     render(true)

  };

  const postStatus = () => {
    const message = $('#postInput').val();
    postFeed(message);
  };

