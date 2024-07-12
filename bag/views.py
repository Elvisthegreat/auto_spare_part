from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.
def view_bag(request):
    """ Render bag content page """
    return render(request, 'bag/bag.html')


def add_item_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    products = get_objects_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity')) # Convert string to an integer
    redirect_url = request.POST.get('redirect_url') # redirect_url found in our form

    """ if product size is in request.post we'll set it equal to that. """
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        """first check to see if there's a bag variable in the session. And if not we'll create one."""
    bag = reuest.session.get('bag', {})

    if size:
        """If the item is already in the bag.
        Then we need to check if another item of the same id and same size already exists.
        And if so increment the quantity for that size and otherwise just set it equal to the quantity"""
        if item_id in list(bag.keys):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to shopping bag')
        else:
            """To handle maybe same item with different sizes when we add it to the bag"""
            bag[item_id] = {'items_by_size' : {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your shopping bag')

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity # Or update the quantity if it already exists.
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')
            
    request.session['bag'] = bag
    return redirect_url(redirect_url)