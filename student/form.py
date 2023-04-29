
from django import forms
from .models import User
class siginform(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "نام ",
                'name': 'message',
                'type': "text"
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "نام خانوادگی  ",
                'name': 'message',
                'type': "text"
            }),
            'phonenumber': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "تلفن همراه  ",
                'name': 'message',
                'type': "tel"
            }),
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "نام کاربری ",
                'name': 'message',
                'type': "text"
            }),
            'password': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "رمز عبور ",
                'name': 'message',
                'type': "password"
            }),
            'email': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "ایمیل",
                'name': 'message',
                'type': "email"
            })

        }

        labels = {
            'first_name': 'نام',
            'last_name':'نام خانوادگی',
            'phonenumber':'تلفن همراه',
            'username':'نام کاربری',
            'password': 'رمز عبور',
            'email': 'ایمیل',
        }
        error_messages = {
            'first_name': {
                'required': 'لطفا نام رابه طورکامل وارد کنید  ',
            },
            'last_name':{
                'required':'لطفا نام خانوادگی خود را وارد کنید '
            },
            'phonenumber':{
                'required':'نلفن همراه نمی تواند خالی باشد '

            },

            'email': {
                'required': 'لطفا ایمیل خود را وارد کنید'
            },
            'username': {
                'required': 'فیلد نام کاربری نمی تواند خالی باشد  ',
            },
            'password': {
                'required': 'رمز عبور نمی تواند خالی باشد  ',
            },
        }