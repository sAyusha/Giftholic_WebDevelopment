"""Giftholic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home import views
from account import views
from product import views as productView
from cart import views as cartView
from checkout import views as checkoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("accounts/", include("account.urls")),
    path("products/", include("product.urls")),
    path("cart/", include("cart.urls")),
    path("checkout/", include("checkout.urls")),
    path('myorder/', include('myorder.urls')),
    path('update_item/', cartView.updateItem, name="update_item"),
    path('searchResult',productView.searchResult,name="searched"),
    path('paymentsuccess/<int:orderID>/<int:pm>',checkoutView.paymentSuccess,name="paymentsuccess"),
    # path("process_order/", checkoutView.processOrder, name="process_order"),
    path('favoritethis/<int:p_id>', productView.favoritethis,name="favoritethis"),
    path('admin-panel/', include('adminPanel.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
