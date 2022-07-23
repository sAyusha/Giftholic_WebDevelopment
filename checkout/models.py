from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

from cart.models import Order

# Create your models here.
class ShippingAddress(models.Model):
    user_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=150,blank=True,null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    street = models.CharField(max_length=200, null=False)
    wardno = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address