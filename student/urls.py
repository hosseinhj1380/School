# from django.urls import URLPattern
from django.urls import path, include
from .views import Signin

urlpatterns = [
    path('signin',Signin.as_view())
]