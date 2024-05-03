from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import  CreateUserForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')   
            

        return render(request, 'accounts/register.html', {'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = request.user
                user = form.get_user()
                login(request, user)
                return redirect('home')
            else:
                user = request.user
                if not user.is_active:
                    messages.info(request, f'Lo sentimos, estás vetado de esta página.')
                else:
                    messages.info(request, 'Usuario o contraseña incorrectos')
        return render(request, 'accounts/login.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    user = request.user
    if not user.is_active:
        banned_message = "Lo sentimos, estás vetado de esta página."
        return render(request, 'home.html', {'banned_message': banned_message})
    else: 
        return render(request, 'accounts/home.html')