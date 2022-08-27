from django.shortcuts import render, redirect
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login
# Create your views here.

def welcome(request):
    return render(request, 'home.html')


def home(request):
    posts= Post.objects.all()
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        return render(request, 'index.html', {'post':posts})

#Registro
def register(request):
    if request.method == "POST":
        form= RegisterForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            username= form.cleaned_data['username']
            print(username)
            messages.success(request,'Usuario {username} creado')
            return redirect('home/')

    else:
        form = RegisterForm()

    context= {'form': form}
    return render(request, 'register.html', context)


def perfil(requets):
    return render(requets, 'perfil.html')

def reset_Password(request):
    return render(request, 'resetPassword.html')