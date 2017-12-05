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
