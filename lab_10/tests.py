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
		
