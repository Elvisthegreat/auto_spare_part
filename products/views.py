from django.shortcuts import render, get_object_or_404


from .models import Product, Category

# Create your views here.
def all_product(request):
    """ A view to display all products"""

    products = Product.objects.all()

    context = {
        products: 'products',
    }

    return render(request, 'produtcs/all_product.html', context)
