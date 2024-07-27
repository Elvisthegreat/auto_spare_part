from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from products.models import Product
# Create your views here.


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


def edit_testimonial(request, testimonial_id):
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


def delete_testimonial(request, testimonial_id):
    """Handle delete testimonial"""
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    if testimonial.author == request.user:
        testimonial.delete()
        messages.add_message(request, messages.SUCCESS, 'Testimonial deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own testimonial!')
        return redirect(reverse('product_detail'))

