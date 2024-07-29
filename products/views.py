from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q # To generate a search query
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect


from .models import Product, Category, Wishlist, Testimonial
from .forms import ProductForm, TestimonialForm

# Testimonials


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
                sortkey = 'category__name'

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

    """for sorting asc & desc"""
    current_sorting = f'{sort}_{direction}' # return the current sorting methodology to the template.

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/all_products.html', context)


def product_detail(request, product_id):
    """A view to display individual product"""
    product = get_object_or_404(Product, pk=product_id)
    # from testimonial
    form = TestimonialForm()
    testimonials = Testimonial.objects.filter(product=product)

    return render(request, 'products/product_detail.html', {
        'product': product,
        # from testimonial
        'form': form,
        'testimonials': testimonials,
    })


@login_required
def add_product(request):
    """Add products to store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owner can access this!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            # Redirect to that products added detail page after adding it
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Unable to add product. Please check the form for errors')
    else:
        form = ProductForm

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)

@login_required
def edit_product(request, product_id):
    """Edit a product in a store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owner can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        # instance=product. This means that if the form is valid,
        # it will update the existing product rather than creating a new one.
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated!')
            # Redirect to the product detail page using the product id
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Unable to add product. Please check the form for errors')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'

    return render(request, template, {
        'form': form,
        'product': product,
    }
)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Successfully deleted!')

    return redirect(reverse('all_products'))


@login_required
def add_to_wishlist(request, product_id):
    """Handle adding to wishlist"""
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    """Handl deleting from wishlist"""
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist')

@login_required
def wishlist(request):
    """Handle wishlist main page"""
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'products/wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def submit_testimonial(request, product_id):
    """Handling testimonials input submission"""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        testimonial_form = TestimonialForm(data=request.POST)
        if testimonial_form.is_valid(): # Check if the form is valid
            # Create a testimonial object but don't save to the database yet
            form = testimonial_form.save(commit=False)
            form.author = request.user  # Set the author of the testimonial
            form.product = product # Associate the testimonial with the current post
            form.save() # Save the testimonial to the database
            messages.success(request, "Submitted Successfully")
            return redirect('product_detail', product_id=product.id)
            
    testimonial_form = TestimonialForm()
    
    return render(request, 'submit_testimonial.html', {'form': testimonial_form})


def testimonial_edit(request, testimonial_id):
    """Edit testimonial"""
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    if request.method == 'POST':
        testimonial_form = TestimonialForm(data=request.POST, instance=testimonial)

        if testimonial_form.is_valid() and testimonial.author == request.user:
            testimonial_form.save()
            messages.success(request, 'Updated Successfully')
            return redirect('product_detail', product_id=testimonial.product.id)
        else:
            messages.error(request, 'Error updating testimonial!')

    else:
        testimonial_form = TestimonialForm(instance=testimonial)
    return HttpResponseRedirect(reverse('post_detail'))


def delete_testimonial(request, product_id, testimonial_id):
    """Handle delete testimonial"""
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    if testimonial.author == request.user:
        testimonial.delete()
        messages.add_message(request, messages.SUCCESS, 'Testimonial deleted!')
        return redirect('product_detail', product_id=product_id)
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own testimonial!')
        return redirect('product_detail', product_id=product_id)


