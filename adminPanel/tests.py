from urllib import response
from django.test import Client, TestCase
from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User

from adminPanel.views import addCategory, adminProduct, productEdit
from product.models import Category, Product


# Create your tests here.
# class TestUrls(SimpleTestCase):
#     def test_case_products_url(self):
#         url=reverse('adminproduct')

#         self.assertEqual(resolve(url).func,adminProduct)

#     def test_case_category_url(self):
#         url=reverse('categoryAdd')

#         self.assertEqual(resolve(url).func,addCategory)

#     def test_case_prodedit_url(self):
#         url=reverse('prodEdit',args=[2])

#         self.assertEqual(resolve(url).func,productEdit)

class TestViews(TestCase):
    def test_case_prodAdd_views(self):
        user=User.objects.create(username="tomSeal")
        user.set_password('laser12')
        user.save()

        client=Client()
        logged_in=client.login(username='tomSeal',password="laser12")
        url=reverse('prodAdd')
        response=client.post(url,{
            'name':'test name',
            'price' : 0,
            'category' :"Cakes & Cupcakes",
            'description':'test desc',
            'search_tags':'test tag',
            'available': True,
            'image':'test image',
        })
        self.assertEquals(response.status_code,200)

    def test_case_deleteProdviews(self):
        user=User.objects.create(username="tomSeal")
        user.set_password('laser12')
        user.save()

        client=Client()
        print(client)

        logged_in=client.login(username='tomSeal',password="laser12")
        print(logged_in)
        
        newlyCreated=Product.objects.create(
            name='test name',
            price = 0,
            category =Category.objects.create(name="Cakes & Cupcakes"),
            description='test desc',
            search_tags='test tag',
            available= True,
            image='test image',
        )
        print(newlyCreated.id)
        url=reverse('prodDelete',args=[newlyCreated.id])
        print(url)

        response =client.delete(url)
        
        self.assertEquals(response.status_code,302)
