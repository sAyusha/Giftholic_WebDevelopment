from django.shortcuts import render

# Create your views here.
import json
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from cart.models import *
from product.models import *
from django.contrib.auth.models import User

from product.models import *
from product.utils import cookieCart, cartData, guestOrder

# Create your views here.
def cartPage(request):
    allcategory = Category.objects.all()

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    

    context={
        'allcategory':allcategory,
        'items':items,
        'order':order,
        'cartItems':cartItems,
    }
    return render(request,'items/cart.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'deleteItem':
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)