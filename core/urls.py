from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("add_cart/<pizza_uid>/", add_cart, name="add_cart"),
    path("signin/", login_view, name="signin"),
    path("signup/", signup_view, name="signup")
]
