from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import *
from django.http import HttpRequest
import requests
from django.urls import reverse


class Dashboard(TestCase):

	def test_app_forum_url_is_exist(self):
		response = Client().get('/dashboard/')
		self.assertEqual(response.status_code, 200)

	def test_app_forum_using_index_func(self):
		found = resolve('/dashboard/')
		self.assertEqual(found.func, index)