from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Home_page(TemplateView):
    template_name = 'home_module/home_page.html'




def header_component(request):
    return render(request, 'shared/site_header_component.html', {})


def footer_component(request):
    return render(request, 'shared/site_footer-component.html', {})

