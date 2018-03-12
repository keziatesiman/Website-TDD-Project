# from django.test import TestCase
# from django.test import Client
# from django.urls import resolve
# from .views import index
# from django.http import HttpRequest
# import requests
# from .api_enterkomputer import get_drones, get_soundcards, get_opticals
# from .csui_helper import get_access_token, verify_user, get_client_id , get_data_user
# import environ
# from django.urls import reverse

# # Create your tests here.
# #setting env agar dapat diambil
# root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
# env = environ.Env(DEBUG=(bool, False),)
# environ.Env.read_env('.env')
# API_VERIFY_USER = "https://akun.cs.ui.ac.id/oauth/token/verify/"
# API_MAHASISWA = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/"


# class Lab9UnitTest(TestCase):
# 	def test_lab_9_url_is_exist(self):
# 		response = Client().get('/lab-9/')
# 		self.assertEqual(response.status_code, 200)

# 	def test_lab9_using_index_func(self):
# 		found = resolve('/lab-9/')
# 		self.assertEqual(found.func, index)

# 	def test_lab9_using_right_template(self):
# 		#jika belum login
# 		response = self.client.get('/lab-9/')
# 		self.assertTemplateUsed(response, 'lab_9/session/login.html')
# 		#login
# 		session = self.client.session
# 		session['user_login'] = 'test'
# 		session['kode_identitas'] = '123'
# 		session.save()
# 		response = self.client.get('/lab-9/')
# 		self.assertEqual(response.status_code, 302)

# 	def test_profile(self):
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')
# 		self.assertIn('kezia.irene',html_response)

# 	def test_profile_not_login(self):
# 		response = self.client.get('/lab-9/profile/')
# 		self.assertEqual(response.status_code, 302)

# # ======================================================================== #
# 	# Test api_enterkomputer.py
# 	# def test_drones_api(self):
# 	# 	response = requests.get('https://www.enterkomputer.com/api/product/drone.json')
# 	# 	self.assertEqual(response.json(),get_drones().json())

# 	# def test_soundcards_api(self):
# 	# 	response = requests.get('https://www.enterkomputer.com/api/product/soundcard.json')
# 	# 	self.assertEqual(response.json(),get_soundcards().json())

# 	# def test_opticals_api(self):
# 	# 	response = requests.get('https://www.enterkomputer.com/api/product/optical.json')
# 	# 	self.assertEqual(response.json(),get_opticals().json())
# #=============================================================================#
# 	#test custom_auth.py

# 	def test_fail_login(self):
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': 'kezia', 'password': 'kezia'})
# 		response = self.client.get('/lab-9/')
# 		html_response = response.content.decode('utf8')
# 		self.assertIn('Username atau password salah',html_response)

# 	def test_logout_auth(self):
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		response = self.client.post(reverse('lab-9:auth_logout'))
# 		response = self.client.get('/lab-9/')
# 		html_response = response.content.decode('utf8')
# 		self.assertIn('Anda berhasil logout. Semua session Anda sudah dihapus',html_response)

# #============================================================================================#
# 	#Test csui_helper
# 	def test_username_and_pass_wrong(self):
# 		username = "kezia"
# 		password = "kezia"
# 		with self.assertRaises(Exception) as context:
# 			get_access_token(username, password)
# 		self.assertIn("kezia", str(context.exception))

# 	def test_verify_function(self):
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		access_token = get_access_token(self.username,self.password)
# 		parameters = {"access_token": access_token, "client_id": get_client_id()}
# 		response = requests.get(API_VERIFY_USER, params=parameters)
# 		result = verify_user(access_token)
# 		self.assertEqual(result,response.json())

# 	def test_get_data_user_function(self):
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		self.npm = "1606825676"
# 		access_token = get_access_token(self.username,self.password)
# 		parameters = {"access_token": access_token, "client_id": get_client_id()}
# 		response = requests.get(API_MAHASISWA+self.npm, params=parameters)
# 		result = get_data_user(access_token,self.npm)
# 		self.assertEqual(result,response.json())


# #=============================================================================#
# 	#drones
# 	def test_add_favorite_drone(self):
# 		#login
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		#test tambahkan favorit drones
# 		response_post = self.client.post(reverse('lab-9:add_session_drones', kwargs={'id':107894})) #item DJI Mavic Battery
# 		response_post = self.client.post(reverse('lab-9:add_session_drones', kwargs={'id':107893})) #item DJI Phantom 3 Battery
# 		response_post = self.client.post(reverse('lab-9:profile'))

# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')

# 		self.assertIn('Hapus dari favorit', html_response)

# 	def test_delete_favorite_drone(self):
# 		#login
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		#test tambahkan favorit drones
# 		response_post = self.client.post(reverse('lab-9:add_session_drones', kwargs={'id':107894})) #item DJI Mavic Battery
# 		response_post = self.client.post(reverse('lab-9:profile'))
# 		#delete items
# 		response_post = self.client.post(reverse('lab-9:del_session_drones', kwargs={'id':107894}))
# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')
# 		self.assertIn('Favoritkan',html_response)

# 	def test_reset_favorite_drone(self):
# 		#login
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		#test tambahkan favorit drones
# 		response_post = self.client.post(reverse('lab-9:add_session_drones', kwargs={'id':107894})) #item DJI Mavic Battery
# 		response_post = self.client.post(reverse('lab-9:profile'))
# 		#reset items
# 		response_post = self.client.post(reverse('lab-9:clear_session_drones'))
# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')
# 		self.assertIn('Favoritkan',html_response)


# #=============================================================================#
# 	#soundcards
# 	def test_add_favorite_soundcard(self):
# 		#login
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		#test tambahkan favorit drones
# 		response_post = self.client.post(reverse('lab-9:add_session_soundcards', kwargs={'id':53495})) #item DJI Mavic Battery
# 		response_post = self.client.post(reverse('lab-9:add_session_soundcards', kwargs={'id':53496}))
# 		response_post = self.client.post(reverse('lab-9:profile'))

# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')

# 		self.assertIn('Hapus dari favorit', html_response)

# 	def test_delete_favorite_soundcard(self):
# 		#login
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		#test tambahkan favorit drones
# 		response_post = self.client.post(reverse('lab-9:add_session_soundcards', kwargs={'id':53495})) #item DJI Mavic Battery
# 		response_post = self.client.post(reverse('lab-9:profile'))
# 		#delete items
# 		response_post = self.client.post(reverse('lab-9:del_session_soundcards', kwargs={'id':53495}))
# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')
# 		self.assertIn('Favoritkan',html_response)

# 	def test_reset_favorite_soundcard(self):
# 		#login
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		#test tambahkan favorit drones
# 		response_post = self.client.post(reverse('lab-9:add_session_soundcards', kwargs={'id':53495})) #item DJI Mavic Battery
# 		response_post = self.client.post(reverse('lab-9:profile'))
# 		#reset items
# 		response_post = self.client.post(reverse('lab-9:clear_session_soundcards'))
# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')
# 		self.assertIn('Favoritkan',html_response)

	
# #=============================================================================#
# 	#optical
# 	def test_add_favorite_optical(self):
# 		#login
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		#test tambahkan favorit drones
# 		response_post = self.client.post(reverse('lab-9:add_session_opticals', kwargs={'id':4459})) #item DJI Mavic Battery
# 		response_post = self.client.post(reverse('lab-9:add_session_opticals', kwargs={'id':4458}))
# 		response_post = self.client.post(reverse('lab-9:profile'))

# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')

# 		self.assertIn('Hapus dari favorit', html_response)

# 	def test_delete_favorite_optical(self):
# 		#login
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		#test tambahkan favorit drones
# 		response_post = self.client.post(reverse('lab-9:add_session_opticals', kwargs={'id':4459})) #item DJI Mavic Battery
# 		response_post = self.client.post(reverse('lab-9:profile'))
# 		#delete items
# 		response_post = self.client.post(reverse('lab-9:del_session_opticals', kwargs={'id':4459}))
# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')
# 		self.assertIn('Favoritkan',html_response)

# 	def test_reset_favorite_optical(self):
# 		#login
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		#test tambahkan favorit drones
# 		response_post = self.client.post(reverse('lab-9:add_session_opticals', kwargs={'id':4459})) #item DJI Mavic Battery
# 		response_post = self.client.post(reverse('lab-9:profile'))
# 		#reset items
# 		response_post = self.client.post(reverse('lab-9:clear_session_opticals'))
# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')
# 		self.assertIn('Favoritkan',html_response)

# 	def test_clear_without_any_favourite(self):
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		response_post = self.client.post(reverse('lab-9:clear_session_opticals'))
# 		response = self.client.get('/lab-9/profile/')
# 		html_response = response.content.decode('utf8')
# 		self.assertIn('Favoritkan',html_response)

# #=================================================================================#
# #cookie

# 	def test_login_cookie_page(self):
# 		#login session
# 		self.username = env("SSO_USERNAME")
# 		self.password = env("SSO_PASSWORD")
# 		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
# 		# test template yang digunakan pada halaman login cookie
# 		response_post = self.client.get(reverse('lab-9:cookie_login'))
# 		self.assertTemplateUsed(response_post, 'lab_9/cookie/login.html')
# 		#test jika method yang digunakan pada cookie_auth_login bukan post
# 		response_post = self.client.get(reverse('lab-9:cookie_auth_login'))
# 		self.assertEqual(response_post.status_code, 302)
# 		#test jika halaman profile cookie diakses tanpa login
# 		response_post = self.client.get(reverse('lab-9:cookie_profile'))
# 		self.assertEqual(response_post.status_code, 302)
# 		#test jika username dan password salah
# 		response_post = self.client.post(reverse('lab-9:cookie_auth_login'), {'username': 'xx', 'password': 'xxx'})
# 		response_post = self.client.get(reverse('lab-9:cookie_login'))
# 		html_response = response_post.content.decode('utf8')
# 		self.assertIn('Username atau Password Salah',html_response)
# 		#test login pada halaman cookie dengan data yang valid
# 		response_post = self.client.post(reverse('lab-9:cookie_auth_login'), {'username': 'keziatesiman', 'password': '1234567890'})
# 		response_post = self.client.get(reverse('lab-9:cookie_login'))
# 		response_post = self.client.get(reverse('lab-9:cookie_profile'))
# 		self.assertTemplateUsed(response_post, 'lab_9/cookie/profile.html')
# 		#test jika cookie diset secara manual (usaha hacking)
# 		response = self.client.get(reverse('lab-9:cookie_profile'))
# 		response.client.cookies['user_login'] = 'xxsdadax'
# 		response_post = self.client.get(reverse('lab-9:cookie_profile'))
# 		self.assertTemplateUsed(response_post, 'lab_9/cookie/login.html')
# 		#test logout halaman cookie
# 		response_post = self.client.post(reverse('lab-9:cookie_auth_login'), {'username': 'keziatesiman', 'password': '1234567890'})
# 		response_post = self.client.get(reverse('lab-9:cookie_clear'))
# 		self.assertEqual(response_post.status_code, 302)

