from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.contrib import messages


# Create your views here.
def home(request):
    pizza = Pizza.objects.all()
    context = {
        "title": "Home",
        "pizza": pizza
    }
    return render(request, "core/home.html", context)


def login_view(request):
    if request.method == "POST":
        try:
            data = request.POST
            username = data.get("username")
            password = data.get("password")
            user_obj = User.objects.filter(username=username)

            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect("home")
            else:
                messages.error(request, "username or password is incorrect")
                return redirect("signin")
        except Exception as e:
            messages.error(request, "something went wrong")
            return redirect("signin")
    context = {
        "title": "Signin"
    }
    return render(request, "auth/login.html", context)


def signup_view(request):
    if request.method == "POST":
        try:
            data = request.POST
            username = data.get("username")
            password = data.get("password")
            email = data.get("email")
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "User name already exist")
                return redirect("signup")
            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account Creates")
            return redirect("signin")
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect("signup")
    context = {
        "title": "Register",

    }

    return render(request, "auth/register.html", context)


def add_cart(request, pizza_uid):
    user = request.user
    pizza_obj = Pizza.objects.get(uid=pizza_uid)
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    cart_items = CartItem.objects.create(
        cart=cart,
        pizza=pizza_obj
    )

    return redirect("home")
