from datetime import date, timedelta
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.template.loader import get_template

from django.contrib.auth.decorators import login_required
from cart.models import *
from checkout.models import ShippingAddress
from myorder.models import MyOrder

from product.models import *
from product.utils import cookieCart, cartData, guestOrder

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

# def processOrder(request):
#     data = json.loads(request.body),

#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
#     else:
#         customer,order = guestOrder(request, data)

#     total = data['form']['total']
#     if total == order.get_cart_total:
#         order.complete = True
#     order.save()

#     if order.shipping == True:
#         ShippingAddress.objects.create(
#             customer=customer,
#             order=order,
#             address=data['shipping']['address'],
#             city=data['shipping']['city'],
#             street=data['shipping']['street'],
#             wardno=data['shipping']['wardno'],
#             zipcode=data['shipping']['zipcode'],
#         )

#     return JsonResponse('Payment Successful', safe=False)
    

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
        customer = request.user.customer

        print("DATA RECEIVED")
        o_id = request.GET.get('order')
        email = request.GET.get('email')
        address =request.GET.get('address')
        city = request.GET.get('city')
        street = request.GET.get('street')
        wardno = request.GET.get('wardno')
        zipcode =request.GET.get('zipcode')
        pm = request.GET.get('pm')
        current_date = date.today()  
 
        order = Order.objects.get(customer = customer, complete=False)

        getOrder = Order.objects.get(id = o_id)

        items = getOrder.orderitem_set.all()

    dataSaved=""
    if pm == "COD":    
        getOrder.complete = True
        getOrder.payment_method = "Cash on Delivery"
        getOrder.save()

        saveData = ShippingAddress(customer=customer,order=order, email=email,address=address,city=city,street=street,wardno=wardno,zipcode=zipcode)
        saveData.save()

        saveDelivery=Delivery(o_id = getOrder, deliveryDate=getDeliveryDate(2))
        saveDelivery.save()

        delv = Delivery.objects.get(o_id=getOrder)
        adrs = ShippingAddress.objects.get(order=getOrder)

        savemyOrder=MyOrder(customer=customer, o_id = getOrder, delivery=delv, address=adrs)
        savemyOrder.save()

        dataSaved = "Saved PM: COD"    

        # htmly     = get_template('checkoutMail.html')

        # d = {
        #      'customer': customer,
        #      'o_id':o_id,
        #      'getOrderTotal':getOrder.get_cart_total,
        #      'pm':pm,
        #      'address': address,
        #      'city':city,
        #      'street':street,
        #      'items':items,
        #     }

        # subject, from_email, to = 'Order has been received', f'{settings.EMAIL_HOST_USER}', f'{email}'
        # text_content = f'Hi {customer.username}'
        # html_content = htmly.render(d)
        # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()

    return JsonResponse(dataSaved, safe=False)