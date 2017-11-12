from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
# Create your tests here.
class Lab7UnitTest(TestCase):

	def test_lab_7_url_is_exist(self):
		response = Client().get('/lab-7/')
		self.assertEqual(response.status_code, 200)

	def test_lab7_using_index_func(self):
		found = resolve('/lab-7/')
		self.assertEqual(found.func, index)

	def test_lab7_using_right_template(self):
		response = Client().get('/lab-7/')
		self.assertTemplateUsed(response, 'lab_7/lab_7.html')

# Create your tests here.
