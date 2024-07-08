from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q # To generate a search query


from .models import Product, Category

# Create your views here.
def all_products(request):
    """ A view to display all products, including sorting and search queries"""

    products = Product.objects.all()
    # making sure the variables are defined for it to work properly
    query = None
    categories = None

    if request.GET:

        """Handling the search query"""
        if 'q' in request.GET: # remember the 'q' is the name in our input form in base.html
            query = request.GET['q']
            if not query:
                messages.error(request, '“Oops! It looks like you forgot to enter a search query.”')
                return redirect(reverse('all_products'))

            # Return match query in either the product name or the description.
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
    }

    return render(request, 'products/all_products.html', context)


def product_detail(request, product_id):
    """A view to display individual product"""

    # Returning one product so we use get_object_or_404
    product = get_object_or_404(Product, pk=product_id)

    return render(
        request, 'products/product_detail.html',

    {
        'product': product,
    }
)
