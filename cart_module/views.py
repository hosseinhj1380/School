from django.views import View
from django.views.generic import  ListView,CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from .models import Cart
from .models import Course


class AddToCartView(CreateView):
    @login_required
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Course, pk=kwargs['pk'])
        cart = Cart.objects.create(user=request.user, product=product)
        cart.save()
        return redirect('cart')

class CartView(ListView):
    model = Cart
    template_name = 'cart.html'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class RemoveFromCartView(View):
    @login_required
    def post(self, request, *args, **kwargs):
        cart_item = get_object_or_404(Cart, pk=kwargs['pk'])
        cart_item.delete()
        return redirect('cart')
