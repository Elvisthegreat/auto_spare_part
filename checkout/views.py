from django.shortcuts import (render,
    redirect, reverse)
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import  bag_contents

import stripe # imported stripe
import json

# Create your views here.
def checkout(request):
    """Payment intent"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY # inside our env
    stripe_secret_key = settings.STRIPE_SECRET_KEY # inside our env

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        # Instance of the user form
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
           order = order_form.save(commit=False) # Prevent 1st save from happening
           pid = request.POST.get('client_secret').split('_secret')[0]
           order.stripe_pid = pid
           order.original_bag = json.jumps(bag)
           order.save()
           for item_id, item_data in bag.items():
                try:
                    # Get product id out from the bag
                    product = Product.objects.get(id=item_id)
                    # Then if its value is an integer we know we're working with an item that doesn't have sizes.
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                        """
                        Otherwise, if the item has sizes. we'll iterate
                        through each size and create a line item accordingly.
                        """
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                            """
                            Just in case a product isn't found we'll add an error message. 
                            Delete the empty order and return the user to the shopping bag page.
                            """
                except Product.DoesNotExist:
                    messages.error(request,(
                        "One of the products in your bag wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # whether or not the user wanted to save their profile information to the session. And then redirect them to a new page"""
            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {}) # Shopping bag
        if not bag:
            messages.error(request, 'Your bag is currently empty.')
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 300)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Since user now have profile user, users default delivery information to pre-fill the form on checkout page

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
            
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }
    return render(request, template, context)