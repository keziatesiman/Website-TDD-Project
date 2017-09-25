from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import index, about_me, landing_page_content
from lab_1.views import mhs_name
from .models import Message
from .forms import Message_Form
#from .views import index, message_post
from .views import index, message_post, message_table, about_me, landing_page_content


# Create your tests here.

class Lab4UnitTest(TestCase):
    def test_lab_4_url_is_exist(self):
        response = Client().get('/lab-4/')
        self.assertEqual(response.status_code, 200)

    def test_about_me_more_than_6(self):
       self.assertTrue(len(about_me) >= 6)

    def test_lab4_using_index_func(self):
        found = resolve('/lab-4/')
        self.assertEqual(found.func, index)

    def test_landing_page_is_completed(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')

        #Checking whether have Bio content
        self.assertIn(landing_page_content, html_response)

        #Chceking whether all About Me Item is rendered
        for item in about_me:
            self.assertIn(item,html_response)
    def test_model_can_create_new_message(self):
        #Creating a new activity
        new_activity = Message.objects.create(name=mhs_name,email='test@gmail.com',message='This is a test')

        #Retrieving all available activity
        counting_all_available_message= Message.objects.all().count()
        self.assertEqual(counting_all_available_message,1)

    def test_form_message_input_has_placeholder_and_css_classes(self):
        form = Message_Form()
        self.assertIn('class="form-control"', form.as_p())
        self.assertIn('<label for="id_name">Nama:</label>', form.as_p())
        self.assertIn('<label for="id_email">Email:</label>', form.as_p())
        self.assertIn('<label for="id_message">Message:</label>', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = Message_Form(data={'name': '', 'email': '', 'message': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['message'],
            ["This field is required."]
        )  
    def test_lab4_post_fail(self):
        response = Client().post('/lab-4/add_message', {'name': 'Anonymous', 'email': 'A', 'message': ''})
        self.assertEqual(response.status_code, 302)

    def test_lab4_post_success_and_render_the_result(self):
        anonymous = 'Anonymous'
        message = 'HaiHai'
        response = Client().post('/lab-4/add_message', {'name': '', 'email': '', 'message': message})
        self.assertEqual(response.status_code, 200)
        html_response = response.content.decode('utf8')
        self.assertIn(anonymous,html_response)
        self.assertIn(message,html_response)

    def test_lab_4_table_url_exist(self):
        response = Client().get('/lab-4/result_table')
        self.assertEqual(response.status_code, 200)

    def test_lab_4_table_using_message_table_func(self):
        found = resolve('/lab-4/result_table')
        self.assertEqual(found.func, message_table)

    def test_lab_4_showing_all_messages(self):

        name_budi = 'Budi'
        email_budi = 'budi@ui.ac.id'
        message_budi = 'Lanjutkan Kawan'
        data_budi = {'name': name_budi, 'email': email_budi, 'message': message_budi}
        post_data_budi = Client().post('/lab-4/add_message', data_budi)
        self.assertEqual(post_data_budi.status_code, 200)

        message_anonymous = 'Masih Jelek Nih'
        data_anonymous = {'name': '', 'email': '', 'message': message_anonymous}
        post_data_anonymous = Client().post('/lab-4/add_message', data_anonymous)
        self.assertEqual(post_data_anonymous.status_code, 200)

        response = Client().get('/lab-4/result_table')
        html_response = response.content.decode('utf8')

        for key,data in data_budi.items():
            self.assertIn(data,html_response)

        self.assertIn('Anonymous', html_response)
        self.assertIn(message_anonymous, html_response)

    #adding a new test case that covered __str__ testing
    def test_lab_4_str_is_equal_to_message(self):
        name = mhs_name
        email = 'test123@gmail.com'
        message = 'this is another test'
        test_message = Message.objects.create(name=name, email=email, message=message)
        self.assertEqual(str(test_message), message)

    def test_lab_4_navbar_and_copyright_is_here(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')
        self.assertIn('<nav class="navbar navbar-default navbar-static-top">', html_response)
        self.assertIn('&copy;', html_response)







# Create your tests here.
