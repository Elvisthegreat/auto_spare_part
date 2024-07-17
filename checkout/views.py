from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {}) # Shopping bag
    if not bag:
        messages.error(request, 'Your bag is currently empty.')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PdLx3RuDiuKAP2V5o4QVezXXuGBo3OhuFpvY4wxmQdD0JjjWwGVLtdiBJBwbTP7i4fkfjjBcHFZ1PaiHrWdQHw000VRu4xn0L',
        'client_secret': 'sk_test_51PdLx3RuDiuKAP2VEcKp6XjfJdljV7rqbI2dwhus2D4twjxxiBzqZlty0C3zUziFrQHWAYVEPe4lNR5hTV3txF9E00MQEjboGY',
    }
    return render(request, template, context)