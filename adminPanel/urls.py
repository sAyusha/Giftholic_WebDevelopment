from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("", views.adminpanelLogin, name="adminpanelLogin"),
    path("admin-dashboard", views.adminHome, name="admindashboard"),
    path("logoutAdmin", views.logoutAdmin, name="logoutAdmin"),
    path("admin-product", views.adminProduct, name="adminproduct"),
    path("productEdit/<int:prodId>", views.productEdit, name="prodEdit") ,
    path("productDelete/<int:prodId>", views.productDelete, name="prodDelete") ,
    path("productAdd", views.productAdd, name="prodAdd") ,
    path("categoryAdd", views.addCategory, name="categoryAdd") ,
    path("categoryDelete/<int:catId>", views.delCategory, name="categoryDelete") ,
    path("order_add",views.addOrder, name="order_add"),
    path("order_edit/<str:pk>/",views.orderEdit, name="order_edit"),
    path("delete_order",views.deleteOrder, name="delete_order")
]