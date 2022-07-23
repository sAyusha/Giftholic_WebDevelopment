from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required
from cart.models import Order

from home.models import Contact
from product.models import *
from product.utils import cookieCart, cartData

# Create your views here.
def index(request):
    current_user = request.user
    popularProducts = popularProduct.objects.all()
    allcategory = Category.objects.all()

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context={
        'current_user':current_user,
        'popularProducts':popularProducts,
        'allcategory':allcategory,
        'items':items,
        'order':order,
        'cartItems':cartItems,
    }
    return render(request,'home/index.html',context)

@login_required(login_url='login')
def contact(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    if request.method=="POST":
        contact = Contact()
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.fullname = fullname
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, 'Thank You for Contacting Us!!')

        send_mail('Contact Form',
            message,
            settings.EMAIL_HOST_USER,
            ['ayushastha69@gmail.com'],
            fail_silently=False
            )
    context={
        'items':items,
        'order':order,
        'cartItems':cartItems,
    }
    return render(request, 'home/contact.html',context)
