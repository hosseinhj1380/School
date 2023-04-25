# from django.urls import URLPattern
from django.urls import path, include
from .views import Signin

urlpatterns = [
    path('',Signin.as_view())
]