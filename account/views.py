from multiprocessing import context
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from product.utils import cartData
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if username and password !="":
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Username or password is incorrect')
            else:
                messages.info(request, "Enter username and password")
    context = {}
    return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    current_user = request.user
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)

@login_required
def profilePage(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
        'items':items,
        'order':order,
        'cartItems':cartItems,
    }

    return render(request, 'account/profile.html', context)
