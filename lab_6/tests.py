from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
# Create your tests here.
class Lab6UnitTest(TestCase):

	def test_lab_6_url_is_exist(self):
		response = Client().get('/lab-6/')
		self.assertEqual(response.status_code, 200)

	def test_lab6_using_index_func(self):
		found = resolve('/lab-6/')
		self.assertEqual(found.func, index)

	def test_lab6_using_right_template(self):
		response = Client().get('/lab-6/')
		self.assertTemplateUsed(response, 'lab_6/lab_6.html')
