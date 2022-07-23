from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class TestViews(TestCase):
    def test_case_checkout_views(self):
        user=User.objects.create(username="tomSeal")
        user.set_password('laser12')
        user.save()

        client=Client()
        print(client)

        logged_in=client.login(username='tomSeal',password="laser12")
        print(logged_in)

        url=reverse('checkout')

        response=client.get(url)
        print(response)
     
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'items/checkout.html')