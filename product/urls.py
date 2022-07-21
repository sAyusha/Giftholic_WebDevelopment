from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("display/", views.productPage, name="display"),
    path("productView/", views.displayPage, name="productView"),
    path("detail/<int:item_id>", views.detailPage, name="detail"),
    path("category/<int:cat_id>", views.categoryDisplay, name="category"),
    path("wishlist", views.wishlistView, name="wishlist"),
]