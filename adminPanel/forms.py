from django.forms import ModelForm
from cart.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('customer','product','status')