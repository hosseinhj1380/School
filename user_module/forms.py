from django import forms
from django.core.exceptions import ValidationError

from user_module.models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='آدرس ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'signup-form',
            'type': "email",
            'placeholder': "آدرس ایمیل",
        }))
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'signup-form',
            'type': "password",
            'placeholder': "رمـز عبـور",
        }))
    confirm_password = forms.CharField(
        label='تایید رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'signup-form',
            'type': "password",
            'placeholder': "تایید رمـز عبـور",
        }))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     user: User = User.objects.filter(username__iexact=username)
    #
    #     if user :
    #         raise ValidationError('کاربری با این نام وجود دارد')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='آدرس ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'login-form',
            'type': "email",
            'placeholder': "آدرس ایمیل",

        }))
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'login-form',
            'type': "password",
            'placeholder': "رمـز عبـور",
        }))
