from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Home_page(TemplateView):
    template_name = 'home_module/home_page.html'
