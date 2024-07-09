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
    sort = None
    direction = None

    if request.GET:

        """Sorting products and the direction either asc or desc"""
        if 'sort' in request.GET: # checking if 'sort' is there
            sortkey = request.GET['sort']
            sort = sortkey # setting sort defined to None to sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                # sort category by name instead of category id
            if sortkey == 'category':
                sortkey = 'category_name'
                
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}' # Add - which will reverse the order.
            products = products.order_by(sortkey) # order_by to sort all products

        """Handling a specific category"""
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        """Handling the search query"""
        if 'q' in request.GET: # remember the 'q' is the name in our input form in base.html
            query = request.GET['q']
            if not query:
                messages.error(request, '“Oops! It looks like you forgot to enter a search query.”')
                return redirect(reverse('home'))

            # Return match query in either the product name or the description.
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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
