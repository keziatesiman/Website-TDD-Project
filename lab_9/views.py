# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
#catatan: tidak bisa menampilkan messages jika bukan menggunakan method 'render'
from .api_enterkomputer import get_drones, get_soundcards, get_opticals

response = {}

# NOTE : untuk membantu dalam memahami tujuan dari suatu fungsi (def)
# Silahkan jelaskan menggunakan bahasa kalian masing-masing, di bagian atas
# sebelum fungsi tersebut.

# ======================================================================== #
# User Func
# Apa yang dilakukan fungsi INI? #silahkan ganti ini dengan penjelasan kalian 
#fungsi index dipanggil pertama kali saat lab-9 diakses
#fungsi ini memeriksa jika user sudah login pada session
#jika belum, akan menampilkan halaman login session
#jika sudah, di redirect ke halaman profile
def index(request):
    response['author'] = "Kezia Irene"
    print ("#==> masuk index")
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('lab-9:profile'))
    else:
        response['connected'] = False #digunakan sebagai penanda kapan header menampilkan tombol logout
        response['name'] = 'Kezia Irene'
        html = 'lab_9/session/login.html'
        return render(request, html, response)

#fungsi untuk melakukan inisiasi data yg dimunculkan pada templates
#data dimunculkan setelah login pada session

def set_data_for_session(res, request):
    response['author'] = request.session['user_login']
    response['access_token'] = request.session['access_token']
    response['kode_identitas'] = request.session['kode_identitas']
    response['role'] = request.session['role']
    response['drones'] = get_drones().json()
    response['soundcards'] = get_soundcards().json()
    response['optical'] = get_opticals().json()
    response['connected'] = True
    response['name'] = 'Kezia Irene'


    print ("#drones = ", get_drones().json(), " - response = ", response['drones'])
    ## handling agar tidak error saat pertama kali login (session kosong)
    if 'drones' in request.session.keys():
        response['fav_drones'] = request.session['drones']
    # jika tidak ditambahkan else, cache akan tetap menyimpan data
    # sebelumnya yang ada pada response, sehingga data tidak up-to-date
    else:
        response['fav_drones'] = []

    if 'soundcards' in request.session.keys():
        response['fav_soundcards'] = request.session['soundcards']
    # jika tidak ditambahkan else, cache akan tetap menyimpan data
    # sebelumnya yang ada pada response, sehingga data tidak up-to-date
    else:
        response['fav_soundcards'] = []

    if 'optical' in request.session.keys():
        response['fav_opticals'] = request.session['opticals']
    # jika tidak ditambahkan else, cache akan tetap menyimpan data
    # sebelumnya yang ada pada response, sehingga data tidak up-to-date
    else:
        response['fav_opticals'] = []



#fungsi untuk menampilkan daftar drones
def profile(request):
    print ("#==> profile")
    ## sol : bagaimana cara mencegah error, jika url profile langsung diakses
    if 'user_login' not in request.session.keys():
        return HttpResponseRedirect(reverse('lab-9:index'))
    ## end of sol

    set_data_for_session(response, request)

    html = 'lab_9/session/profile.html'
    return render(request, html, response)

# ======================================================================== #

### Drones

#fungsi untuk menambahkan drone ke favorit
def add_session_drones(request, id):
    ssn_key = request.session.keys()
    if not 'drones' in ssn_key:
        print ("# init drones ")
        request.session['drones'] = [id]
    else:
        drones = request.session['drones']
        print ("# existing drones => ", drones)
        if id not in drones:
            print ('# add new item, then save to session')
            drones.append(id)
            request.session['drones'] = drones

    messages.success(request, "Berhasil tambah drone favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

# fungsi untuk menghapus drone dari favorit
def del_session_drones(request, id):
    print ("# DEL drones")
    drones = request.session['drones']
    print ("before = ", drones)
    drones.remove(id) #untuk remove id tertentu dari list
    request.session['drones'] = drones
    print ("after = ", drones)

    messages.error(request, "Berhasil hapus dari favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

#fungsi untuk mengosongkan daftar favorit
#mengecek key drone pada session
#jika key drone sudah ada pada session, akan dihapus dari session
#jika belum ada, maka akan ditampilkan pesan error
def clear_session_drones(request):
    ssn_key = request.session.keys()
    print(ssn_key)
    if 'drones' in ssn_key:
        print ("# CLEAR session drones")
        print ("before 1 = ", request.session['drones'])
        del request.session['drones']

        messages.error(request, "Berhasil reset favorite drones")
        return HttpResponseRedirect(reverse('lab-9:profile'))
    else:
        messages.error(request, "Favorite drones kosong")
        return HttpResponseRedirect(reverse('lab-9:profile'))

# ======================================================================== #

### Soundcard

#fungsi untuk menambahkan soundcard ke favorit
def add_session_soundcards(request, id):
    ssn_key = request.session.keys()
    #jika soundcard belum ada pada session, buat soundcard baru
    if not 'soundcards' in ssn_key:
        print ("# init soundcard ")
        request.session['soundcards'] = [id]
    else:
        soundcards = request.session['soundcards']
        print ("# existing drones => ", soundcards)
        if id not in soundcards:
            print ('# add new item, then save to session')
            soundcards.append(id)
            request.session['soundcards'] = soundcards

    messages.success(request, "Berhasil tambah soundcard favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

# fungsi untuk menghapus soundcard dari favorit
def del_session_soundcards(request, id):
    print ("# DEL soundcards")
    soundcards = request.session['soundcards']
    print ("before = ", soundcards)
    soundcards.remove(id) #untuk remove id tertentu dari list
    request.session['soundcards'] = soundcards
    print ("after = ", soundcards)

    messages.error(request, "Berhasil hapus dari favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

#fungsi untuk mengosongkan daftar favorit
#mengecek key drone pada session
#jika key soundcard sudah ada pada session, akan dihapus dari session
#jika belum ada, maka akan ditampilkan pesan error
def clear_session_soundcards(request):
    ssn_key = request.session.keys()
    print(ssn_key)
    if 'soundcards' in ssn_key:
        print ("# CLEAR session soundcards")
        print ("before 1 = ", request.session['soundcards'])
        del request.session['soundcards']

        messages.error(request, "Berhasil reset favorite soundcards")
        return HttpResponseRedirect(reverse('lab-9:profile'))
    else:
        messages.error(request, "Favorite soundcards kosong")
        return HttpResponseRedirect(reverse('lab-9:profile'))

# ======================================================================== #

### Optical

#fungsi untuk menambahkan soundcard ke favorit
def add_session_opticals(request, id):
    ssn_key = request.session.keys()
    #jika soundcard belum ada pada session, buat soundcard baru
    if not 'opticals' in ssn_key:
        print ("# init opticals ")
        request.session['opticals'] = [id]
    else:
        opticals = request.session['opticals']
        print ("# existing drones => ", opticals)
        if id not in opticals:
            print ('# add new item, then save to session')
            opticals.append(id)
            request.session['opticals'] = opticals

    messages.success(request, "Berhasil tambah optical favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

# fungsi untuk menghapus soundcard dari favorit
def del_session_opticals(request, id):
    print ("# DEL opticals")
    opticals = request.session['opticals']
    print ("before = ", opticals)
    opticals.remove(id) #untuk remove id tertentu dari list
    request.session['opticals'] = opticals
    print ("after = ", opticals)

    messages.error(request, "Berhasil hapus dari favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

#fungsi untuk mengosongkan daftar favorit
#mengecek key drone pada session
#jika key soundcard sudah ada pada session, akan dihapus dari session
#jika belum ada, maka akan ditampilkan pesan error
def clear_session_opticals(request):
    ssn_key = request.session.keys()
    print(ssn_key)
    if 'opticals' in ssn_key:
        print ("# CLEAR session opticals")
        print ("before 1 = ", request.session['opticals'])
        del request.session['opticals']

        messages.error(request, "Berhasil reset favorite opticals")
        return HttpResponseRedirect(reverse('lab-9:profile'))
    else:
        messages.error(request, "Favorite opticals kosong")
        return HttpResponseRedirect(reverse('lab-9:profile'))

# ======================================================================== #
# COOKIES

# Apa yang dilakukan fungsi INI? #silahkan ganti ini dengan penjelasan kalian 
# fungsi menampilkan halaman login cookie jika user belum login
# jika user sudah login, di redirect ke halaman profile cookie
def cookie_login(request):
    print ("#==> masuk login")
    if is_login(request):
        return HttpResponseRedirect(reverse('lab-9:cookie_profile'))
    else:
        html = 'lab_9/cookie/login.html'
        return render(request, html, response)

# fungsi untuk memverifikasi username dan password valid
# jika tidak valid, ditampilkan error message password salah dan kembali ke halaman login cookie
# jika valid, akan berhasil untuk login
def cookie_auth_login(request):
    print ("# Auth login")
    if request.method == "POST":
        user_login = request.POST['username']
        user_password = request.POST['password']

        if my_cookie_auth(user_login, user_password):
            print ("#SET cookies")
            res = HttpResponseRedirect(reverse('lab-9:cookie_login'))

            res.set_cookie('user_login', user_login)
            res.set_cookie('user_password', user_password)

            return res
        else:
            msg = "Username atau Password Salah"
            messages.error(request, msg)
            return HttpResponseRedirect(reverse('lab-9:cookie_login'))
    else:
        return HttpResponseRedirect(reverse('lab-9:cookie_login'))

# fungsi untuk menampilkan data pada halaman profile cookie
def cookie_profile(request):
    print ("# cookie profile ")
    # method ini untuk mencegah error ketika akses URL secara langsung
    if not is_login(request):
        print ("belum login")
        return HttpResponseRedirect(reverse('lab-9:cookie_login'))
    else:
        print ("cookies => ", request.COOKIES)
        in_uname = request.COOKIES['user_login']
        in_pwd= request.COOKIES['user_password']

        # jika cookie diset secara manual (usaha hacking), distop dengan cara berikut
        # agar bisa masuk kembali, maka hapus secara manual cookies yang sudah diset
        if my_cookie_auth(in_uname, in_pwd):
            html = "lab_9/cookie/profile.html"
            response['name'] = 'Kezia Irene' #untuk header
            res =  render(request, html, response)
            return res
        else:
            print ("#login dulu")
            msg = "Kamu tidak punya akses :P "
            messages.error(request, msg)
            html = "lab_9/cookie/login.html"
            return render(request, html, response)

# fungsi untuk menghapus cookie saat logout
def cookie_clear(request):
    res = HttpResponseRedirect('/lab-9/cookie/login')
    res.delete_cookie('lang')
    res.delete_cookie('user_login')

    msg = "Anda berhasil logout. Cookies direset"
    messages.info(request, msg)
    return res

# Apa yang dilakukan fungsi ini?
def my_cookie_auth(in_uname, in_pwd):
    my_uname = "keziatesiman" #SILAHKAN ganti dengan USERNAME yang kalian inginkan
    my_pwd = "1234567890" #SILAHKAN ganti dengan PASSWORD yang kalian inginkan
    return in_uname == my_uname and in_pwd == my_pwd

#Apa yang dilakukan fungsi ini? 
def is_login(request):
    return 'user_login' in request.COOKIES and 'user_password' in request.COOKIES
