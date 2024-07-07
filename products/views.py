from django.shortcuts import render, get_object_or_404


from .models import Product, Category

# Create your views here.
def all_products(request):
    """ A view to display all products, including sorting and search queries"""

    products = Product.objects.all()
    # making sure the variables are defined for it to work properly
    query = None
    categories = None

    context = {
        'products': products,
    }

    return render(request, 'products/all_products.html', context)
