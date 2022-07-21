from django.urls import path
from django.urls.conf import include

from checkout import views

urlpatterns = [
    path("", views.checkoutPage, name="checkout"),
    path("saveShipping", views.saveShippingData, name="saveShipping"),
]