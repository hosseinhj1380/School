from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, CreateView
from .form import siginform
from .models import User
# Create your views here.
class Signin(CreateView):
    form_class = siginform
    template_name = 'student/SigninTeacher.html'

