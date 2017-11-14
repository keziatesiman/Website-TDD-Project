from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_friend, validate_npm, delete_friend, friend_list, get_friend_list, friend_description
from .models import Friend

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

	def test_lab7_using_daftar_teman_template(self):
		response = Client().get('/lab-7/friend-list/')
		self.assertTemplateUsed(response, 'lab_7/daftar_teman.html')

	def test_lab7_using_friend_list_function(self):
		found = resolve('/lab-7/friend-list/')
		self.assertEqual(found.func, friend_list)

	def test_lab7_using_get_friend_list_funct(self):
		found = resolve('/lab-7/get-friend-list/')
		self.assertEqual(found.func, get_friend_list)

	def test_lab7_using_add_friend_funct(self):
		found = resolve('/lab-7/add-friend/')
		self.assertEqual(found.func, add_friend)

	def test_model_can_create_new_friend(self):
		new_friend = Friend.objects.create(friend_name = 'Kezia Irene', npm ='1606825676')
		counting_all_object_friend = Friend.objects.all().count()
		self.assertEqual(counting_all_object_friend,1)

# Create your tests here.
