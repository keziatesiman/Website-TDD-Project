from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import *
from django.http import HttpRequest
import requests
from lab_9.csui_helper import *
import environ
from django.urls import reverse
from .omdb_api import get_detail_movie, create_json_from_dict, search_movie, get_api_key

# Create your tests here.
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')
# Create your tests here.
class Lab10UnitTest(TestCase):

	def test_lab_10_url_is_exist(self):
		response = Client().get('/lab-10/')
		self.assertEqual(response.status_code, 200)

	def test_lab10_using_index_func(self):
		found = resolve('/lab-10/')
		self.assertEqual(found.func, index)

	def test_lab10_using_right_template(self):
		#jika belum login
		response = self.client.get('/lab-10/')
		self.assertTemplateUsed(response, 'lab_9/session/login.html')
		#login
		session = self.client.session
		session['user_login'] = 'test'
		session['kode_identitas'] = '123'
		session.save()
		response = self.client.get('/lab-10/')
		self.assertEqual(response.status_code, 302)


	def test_profile(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")
		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
		response = self.client.get('/lab-9/profile/')
		html_response = response.content.decode('utf8')
		self.assertIn('kezia.irene',html_response)
		#test jika user belum ada pada database (pertama kali login)
		response_post = self.client.get(reverse('lab-10:dashboard'))
		self.assertTemplateUsed(response_post, 'lab_10/dashboard.html')
		#logout
		response_post = self.client.post(reverse('lab-9:auth_logout'))

	def test_add_watch_later_and_list_watch_later(self):
		#test jika id yang ditambahkan tidak valid (saat penambahan secara manual)
		response_post = self.client.get(reverse('lab-10:add_watch_later', kwargs={'id':'tidakada'}))
		self.assertEqual(response_post.status_code, 302)
		#test jika menambahkan dengan login (data disimpan di database)
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")
		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
		response_post = self.client.get(reverse('lab-10:dashboard'))
		response_post = self.client.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt1396484'}))
		self.assertEqual(response_post.status_code, 302)
		response_post = self.client.get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
		html_response = response_post.content.decode('utf8')
		self.assertIn('Berhasil tambah movie ke Watch Later',html_response)
		#test list_watch_later dengan login (data diambil dari database)
		response_post = self.client.get(reverse('lab-10:list_watch_later'))
		self.assertEqual(response_post.status_code, 200)
		self.assertTemplateUsed(response_post,"lab_10/watch_later.html")
		html_response = response_post.content.decode('utf8')
		self.assertIn('It',html_response)
		#test jika id yang sama ditambahkan kembali secara manual dengan login
		response_post = self.client.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt1396484'}))
		self.assertEqual(response_post.status_code, 302)
		response_post = self.client.get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
		html_response = response_post.content.decode('utf8')
		self.assertIn('Movie already exist on DATABASE! Hacking detected!',html_response)
		#menambahkan satu movie lagi dengan login
		response_post = self.client.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt3874544'}))
		self.assertEqual(response_post.status_code, 302)
		response_post = self.client.get(reverse('lab-10:movie_detail', kwargs={'id':'tt3874544'}))
		html_response = response_post.content.decode('utf8')
		self.assertIn('Berhasil tambah movie ke Watch Later',html_response)
		#logout
		response_post = self.client.post(reverse('lab-9:auth_logout'))
		#test jika menambahkan tanpa login (data akan disimpan di session)
		response_post = self.client.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt1396484'}))
		self.assertEqual(response_post.status_code, 302)
		response_post = self.client.get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
		html_response = response_post.content.decode('utf8')
		self.assertIn('Berhasil tambah movie ke Watch Later',html_response)
		#test list_watch_later tanpa login (data diambil dari session)
		response_post = self.client.get(reverse('lab-10:list_watch_later'))
		self.assertEqual(response_post.status_code, 200)
		self.assertTemplateUsed(response_post,"lab_10/watch_later.html")
		html_response = response_post.content.decode('utf8')
		self.assertIn('It',html_response)
		#test jika id yang sama ditambahkan kembali secara manual tanpa login
		response_post = self.client.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt1396484'}))
		self.assertEqual(response_post.status_code, 302)
		response_post = self.client.get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
		html_response = response_post.content.decode('utf8')
		self.assertIn('Movie already exist on SESSION! Hacking detected!',html_response)
		#menambahkan satu movie lagi tanpa login
		response_post = self.client.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt4649466'}))
		self.assertEqual(response_post.status_code, 302)
		response_post = self.client.get(reverse('lab-10:movie_detail', kwargs={'id':'tt4649466'}))
		html_response = response_post.content.decode('utf8')
		self.assertIn('Berhasil tambah movie ke Watch Later',html_response)
		#jika sudah menambahkan namun belum login, maka setelah login movie dari session yang belum ada di database
		#akan disimpan di dalam database
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")
		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
		response_post = self.client.get(reverse('lab-10:dashboard'))
		#logout
		response_post = self.client.post(reverse('lab-9:auth_logout'))

	def test_list_movie_page_exist(self):
		#login
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")
		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
		response_post = self.client.get(reverse('lab-10:movie_list'))
		self.assertEqual(response_post.status_code, 200)
		self.assertTemplateUsed(response_post,"lab_10/list.html")
		response_post = self.client.get(reverse('lab-10:movie_list'),{'judul':'It','tahun':'2017'})
		self.assertEqual(response_post.status_code, 200)
		self.assertTemplateUsed(response_post,"lab_10/list.html")

		#logout
		response_post = self.client.post(reverse('lab-9:auth_logout'))

	def test_detail_page(self):
		#test jika tidak login (tidak ada key 'user_login' di session)
		response_post = self.client.get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
		self.assertEqual(response_post.status_code, 200)
		self.assertTemplateUsed(response_post,"lab_10/detail.html")
		#login
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")
		response_post = self.client.post(reverse('lab-9:auth_login'), {'username': self.username, 'password': self.password})
		response_post = self.client.get(reverse('lab-10:dashboard'))
		response_post = self.client.get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
		self.assertEqual(response_post.status_code, 200)
		self.assertTemplateUsed(response_post,"lab_10/detail.html")
		#logout
		response_post = self.client.post(reverse('lab-9:auth_logout'))

	def test_search_movie_exist(self):
		response_post = self.client.get(reverse('lab-10:api_search_movie', kwargs={'tahun':'-','judul':'pooh'}))
		self.assertEqual(response_post.status_code, 200)
		response_post = self.client.get(reverse('lab-10:api_search_movie', kwargs={'judul':'-','tahun':'2017'}))
		self.assertEqual(response_post.status_code, 200)
		response_post = self.client.get(reverse('lab-10:api_search_movie', kwargs={'judul':'pooh','tahun':'2011'}))
		self.assertEqual(response_post.status_code, 200)
		response_post = self.client.get(reverse('lab-10:api_search_movie', kwargs={'judul':'-','tahun':'-'}))
		self.assertEqual(response_post.status_code, 200)

