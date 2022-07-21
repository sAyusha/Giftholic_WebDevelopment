from multiprocessing import context
from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# pagination
from django.core.paginator import Paginator
from django.urls import reverse

from cart.models import Order

from .models import *

from .utils import cookieCart, cartData, guestOrder

# Create your views here.
def searchResult(request):
    products = Product.objects.all()
    current_user = request.user
    allcategory = Category.objects.all()

    item_name = request.GET.get('item_name')
    if item_name!= "" and item_name is not None:
        products = products.filter(search_tags__icontains=item_name)
    
    data = cartData(request)
    cartItems = data['cartItems']

    context={
        'products':products,
        'item_name':item_name,
        'current_user':current_user,
        'allcategory':allcategory,
        'cartItems':cartItems,
    }
    return render(request,'home/searchResult.html',context)

# @login_required(login_url='login')
def productPage(request):
    data = cartData(request)
    cartItems = data['cartItems']
    
    products = Product.objects.all()

    # pagination 
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'items/display.html', context)

def displayPage(request):
    allcategory = Category.objects.all()
   
    filteredProd = Product.objects.all()
    
    data = cartData(request)
    cartItems = data['cartItems']

    context = {
        'filteredProd':filteredProd,
        'allcategory':allcategory,
        'cartItems' : cartItems,
    }     
    return render (request, 'items/categoryDisplay.html',context)

def categoryDisplay(request, cat_id):
    customer = request.user.customer
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    category_name = Category.objects.get(id=cat_id)

    allcategory = Category.objects.all()
   
    filteredProd = Product.objects.all()

    if category != None:
        filteredProd = Product.objects.filter(category = cat_id)

    context = {
        'filteredProd':filteredProd,
        'category_name': category_name,
        'allcategory':allcategory,
        'customer': customer,
        'items':items,
        'order':order,
        'cartItems':cartItems,
    }  

    return render (request, 'items/categoryDisplay.html',context)

def detailPage(request,item_id):
    products = get_object_or_404(Product, pk=item_id)
    allcategory = Category.objects.all()

    productDet = get_object_or_404(Product,id=item_id)
    total_fav= productDet.total_favorite()

    favorite_status=False
    if productDet.favorite.filter(id=request.user.id).exists():
        favorite_status=True

    data = cartData(request)
    cartItems = data['cartItems']

    context={
        'products':products,
        'allcategory':allcategory,
        'cartItems':cartItems,
        'total_fav':total_fav,
        'favorite_status':favorite_status,
    }
    return render(request,'items/itemDetail.html',context)

def favoritethis(request,p_id):
    product = get_object_or_404(Product, id=request.POST.get('products.id'))
    if product.favorite.filter(id=request.user.id).exists():
        product.favorite.remove(request.user)

    else:
        product.favorite.add(request.user)

    return HttpResponseRedirect(reverse('wishlist'))

def wishlistView(request):
    current_user = request.user
    allcategory = Category.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']

    wishList = Product.objects.filter(favorite = current_user)
    countWishlist = Product.objects.filter(favorite = current_user).count()
    context={
        'cartItems':cartItems,
        'allcategory':allcategory,
        'wishList':wishList,
        'countWishlist':countWishlist,
    }
    return render(request,'home/wishlist.html',context)

