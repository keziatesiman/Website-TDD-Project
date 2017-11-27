from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
# Create your tests here.
class Lab9UnitTest(TestCase):

	def test_lab_9_url_is_exist(self):
		response = Client().get('/lab-9/')
		self.assertEqual(response.status_code, 200)

	def test_lab9_using_index_func(self):
		found = resolve('/lab-9/')
		self.assertEqual(found.func, index)

	def test_lab9_using_right_template(self):
		#jika belum login
		response = self.client.get('/lab-9/')
		self.assertTemplateUsed(response, 'lab_9/session/login.html')
		#login
		session = self.client.session
		session['user_login'] = 'test'
		session['kode_identitas'] = '123'
		session.save()
		response = self.client.get('/lab-9/')
		self.assertEqual(response.status_code, 302)

