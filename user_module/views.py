from django.contrib.auth import login
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import CreateView
from django.views.generic.base import View

from user_module.forms import RegisterForm, LoginForm
from user_module.models import User


# Create your views here.

class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        login_form = LoginForm()
        context = {
            "register_form": register_form
        }
        return render(request, 'user_module/register_form.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email_user = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user: bool = User.objects.filter(email__iexact=email_user).first()

            if user:
                form.add_error("email", 'حسابی با این مشخصات موجود است')
            else:
                new_user = User(email=email_user, activation_code=get_random_string(5), is_active=False,username=email_user)
                new_user.set_password(password)
                new_user.save()
                return redirect(reverse('home:home_page'))

        context = {
            "register_form": form
        }
        return render(request, 'user_module/register_form.html', context)


class UserActivateView(View):
    def get(self, request, activation_code):
        user: User = User.objects.get(activation_code__iexact=activation_code)
        if not user.is_active:
            if user:
                user.is_active = True
                user.save()
                return redirect(reverse('home:home_page'))
            raise Http404
        else:  # todo : user is already active !
            pass


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            "login_form": login_form

        }
        return render(request, 'user_module/login_form.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home:home_page'))
                    else :
                        login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'user_module/login_form.html', context)
