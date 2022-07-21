from urllib import request, response
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from account.models import *

# Create your tests here.
class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.username: 'ayusha'
        self.email:'ayusha@gmail.com'
        self.password1: 'doraemon67#'
        self.password2: 'doraemon67#'

    def test_signup_page_url(self):
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 301)
        self.assertTemplateUsed(response, template_name='account/register.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 301)
        self.assertTemplateUsed(response, template_name='account/register.html')

    def test_signup_form(self):
        response = self.client.post(reverse('register'), form={
            'username' : self.username,
            'email': self.email,
            'password1': self.password1,
            'password2': self.password2,
        })
        self.assertEqual(response.status_code, 301)

        users = User.objects.all()
        self.assertEqual(users.count(), 1)