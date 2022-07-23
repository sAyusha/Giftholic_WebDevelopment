from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from cart.models import Delivery, Order, OrderItem
from checkout.models import ShippingAddress
from myorder.models import MyOrder
from product.models import Category
from product.utils import cartData

@login_required (login_url="login")
def orderedItems(request,order_id):
    allcategory = Category.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']

    items = OrderItem.objects.filter(order=order_id)

    context={
        'allcategory':allcategory,
        'cartItems':cartItems,
        'items':items,
        'order_id':order_id,
    }


    return render(request,'items/orderedItems.html',context)


# Create your views here.
@login_required (login_url="login")
def myOrder(request):
    allcategory = Category.objects.all()
    customer = request.user
    data = cartData(request)
    cartItems = data['cartItems']
    
    myorder = MyOrder.objects.filter()


    context={
        'allcategory':allcategory,
        'cartItems':cartItems,
        'customer':customer,
        'myorder':myorder, 
    }
    return render(request,'items/myorder.html',context)
