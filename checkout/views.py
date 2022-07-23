from datetime import date, timedelta
from re import template
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.template import Context

from django.contrib.auth.decorators import login_required
from cart.models import *
from checkout.models import ShippingAddress
from myorder.models import MyOrder

from product.models import *
from product.utils import cookieCart, cartData

# Create your views here.
def checkoutPage(request):
    allcategory = Category.objects.all()

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'allcategory': allcategory,
        'items': items,
        'order': order,
        'cartItems': cartItems,

    }
    return render(request, 'items/checkout.html', context)

def paymentSuccess(request,orderID,pm):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    getOrder = Order.objects.get(id = orderID)
    context={
        'getOrder':getOrder,
        'pm':pm,
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }

    return render(request,'items/paymentSuccess.html',context)

def getDeliveryDate(days):
    newDate = date.today() + timedelta(days=days)
    return newDate

def saveShippingData(request):
    if request.method == "GET":

        print("DATA RECEIVED")
        o_id = request.GET.get('order')
        email = request.GET.get('email')
        address =request.GET.get('address')
        city = request.GET.get('city')
        street = request.GET.get('street')
        wardno = request.GET.get('wardno')
        zipcode =request.GET.get('zipcode')
        pm = request.GET.get('pm')
        customer = request.user
        current_date = date.today()  
 
        order = Order.objects.get(user_info=customer, complete=False)

        getOrder = Order.objects.get(id = o_id)

    dataSaved=""
    if pm == "COD":    
        getOrder.complete = True
        getOrder.payment_method = "Cash on Delivery"
        getOrder.save()

        saveData = ShippingAddress(user_info = customer,order=order, email=email,address=address,city=city,street=street,wardno=wardno,zipcode=zipcode)
        saveData.save()

        saveDelivery=Delivery(o_id = getOrder, deliveryDate=getDeliveryDate(2))
        saveDelivery.save()

        delv = Delivery.objects.get(o_id=getOrder)
        adrs = ShippingAddress.objects.get(order=getOrder)

        savemyOrder=MyOrder(o_id = getOrder, delivery=delv, address=adrs)
        savemyOrder.save()

        dataSaved = "Saved PM: COD"  

        template = render_to_string('items/checkoutMail.html',{'name':request.user.username}) 

        mail = EmailMessage(
            template,
            settings.EMAIL_HOST_USER,
            ['ayushastha69@gmail.com']
            ) 

        mail.fail_silently = False
        mail.send()

    return JsonResponse(dataSaved, safe=False)