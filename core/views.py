from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from .models import *


# Create your views here.
def home(request):
    pizza = Pizza.objects.all()
    context = {
        "title": "Home",
        "pizza": pizza
    }
    return render(request, "core/home.html", context)


def login_view(request):
    return render(request, "auth/login.html")


def signup_view(request):
    return render(request, "auth/register.html")


def add_cart(request, pizza_uid):
    return render()
