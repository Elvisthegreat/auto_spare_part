from django.shortcuts import (
    render, reverse, redirect, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_bag(request):
    """ Render bag content page """
    return render(request, 'bag/bag.html')


def add_item_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    #product_count = product.count()
    # Convert string to an integer
    quantity = int(request.POST.get('quantity'))
    # redirect_url found in our form
    redirect_url = request.POST.get('redirect_url')

    """ if product size is in request.post we'll set it equal to that. """
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        """first check to see if there's a bag variable in the
        session. And if not we'll create one."""
    bag = request.session.get('bag', {})

    if size:
        """If the item is already in the bag.
        Then we need to check if another item of the same id
        and same size already exists.
        And if so increment the quantity for that size and otherwise
         just set it equal to the quantity"""
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to '
                    f' {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your bag')
        else:
            """To handle maybe same item with different sizes
            when we add it to the bag"""
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your bag')

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity  # update quantity if it already exists.
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')
    request.session['bag'] = bag

    # Calculate the total item count
    total_items = 0

    for item in bag.values():
        if isinstance(item, dict):
            for size in item['items_by_size'].keys():
                total_items += item['items_by_size'][size]
        else:
            total_items += item

    request.session['total_items'] = total_items

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified
    product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to '
                f'{bag[item_id]["items_by_size"][size]}')  # success messages
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, "Error removing item: {e}")
        return HttpResponse(status=500)
