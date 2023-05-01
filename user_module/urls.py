from django.urls import path
from . import views

app_name= "user"
urlpatterns = [
    path('sign-up', views.RegisterView.as_view(), name='register'),
    path('sign-in', views.LoginView.as_view(), name='login'),
    path('user-activation/<str:activation_code>',views.UserActivateView.as_view(),name= "user_activation")
    ]