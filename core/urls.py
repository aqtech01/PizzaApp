from  django.urls import path
from .views import *
urlpatterns = [
    path("",home, name="home"),
    path("signin/", login_view, name="signin"),
    path("signup/", signup_view, name="signup")
]