from urllib import request, response
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class SignUpPageTests(TestCase):
    def setUp(self):
        self.register_url=reverse('register')
        self.user={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'password1',
            'password2':'password2'
        }
        return super().setUp()

class RegisterTest(SignUpPageTests):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'account/register.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/register.html')

    def test_signup_form(self):
        response = self.client.post(reverse('register'), form={
            'username': self.username,
            'email': self.email,
            'password1': self.password1,
            'password2': self.password2
        })
        self.assertEqual(response.status_code, 200)

        users = User.objects.all()
        self.assertEqual(users.count(), 1)