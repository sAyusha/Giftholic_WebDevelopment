from importlib.resources import contents
from itertools import product
from multiprocessing import context
from tkinter.tix import Tree
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User, Group
from django.contrib import messages

from cart.models import Order
from product.forms import categoryForm, productForm

from product.models import Category, Customer, Product
from .forms import OrderForm


# Create your views here.
def adminpanelLogin(request):
    if request.user.is_authenticated:
        return redirect('admindashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            print(user)

            if user.is_superuser:

                if username and password !="":
                    if user is not None:
                        auth_login(request,user)
                        return redirect('admindashboard')
                    else:
                        messages.info(request, "*Username or password is incorrect")
                else:
                    messages.info(request, "*Enter username and password")
            else:
                return redirect('adminpanelLogin')
    return render(request,'admin/adminLogin.html')

@login_required(login_url='adminpanelLogin')
def adminHome(request):
    # order = Order.obejcts.all()
    customer = Customer.objects.all()

    total_customer = customer.count()

    # toal_order = order.count()
    # delivered = order.filter(status='Delivered').count()
    # pending = order.filter(status='Pending').count()

    context={
        # 'order':order,
        'customer':customer,
        'total_customer': total_customer,
        # 'total_order':toal_order,
        # 'delivered':delivered,
        # 'pending':pending,
    }
    return render(request,'admin/adminHome.html',context)

def logoutAdmin(request):
    logout(request)
    return redirect('adminpanelLogin')

@login_required(login_url='adminpanelLogin')
def adminProduct(request):

    allProducts = Product.objects.all()

    context={
        'allProducts':allProducts,
    }

    return render(request,'admin/adminProduct.html',context)

def productAdd(request):
    categories = Category.objects.all()


    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print('form save')
            print('success')
            return redirect('adminproduct')
    else:
        form = productForm()

    context={
        'categories':categories,
        'form':form,
    }

    return render(request,'admin/productAdd.html',context)


def productEdit(request,prodId):
    prodDetail = Product.objects.get(id=prodId)

    categories = Category.objects.all()

    if request.method == 'GET':
        form = productForm(request.GET, request.FILES, instance=prodDetail)

        if form.is_valid():
            form.save()
            print('form save')
            return redirect('adminproduct')
    else:
        form = productForm(instance=prodDetail)

    context={
        'prodDetail':prodDetail,
        'categories':categories,
        'form':form,
    }

    return render(request,'admin/productEdit.html',context)

def productDelete(request,prodId):
    Product.objects.get(id=prodId).delete()
    return redirect('adminproduct')

def addCategory(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = categoryForm(request.POST)

        if form.is_valid():
            form.save()
            print('form save')
            return redirect('categoryAdd')
    else:
        form = categoryForm()

    context={
        'categories':categories,
        'form':form,
    }

    return render(request, 'admin/categoryAdd.html', context)

def delCategory(request,catId):
    Category.objects.filter(id=catId).delete()
    return redirect('categoryAdd')

def addOrder(request):
    form = OrderForm()

    if request.method == "POST":
        # print('printing post', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admindashboard')
    context={
        'form':form,
    }
    return render(request, 'admin/orderAdd.html',context)

def orderEdit(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        # print('printing post', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('admindashboard')

    context = {}
    return render(request, 'admin/orderAdd.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('admindashboard')

    context = {
        'item':order
    }
    return render(request, 'admin/orderDelete.html',context)