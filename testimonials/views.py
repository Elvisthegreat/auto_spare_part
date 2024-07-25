from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib.auth.decorators import login_required

from products.models import Product
# Create your views here.


@login_required
def submit_testimonial(request, product_id):
    """Handling testimonials input submission"""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        testimonial_form = TestimonialForm(data=request.POST)
        if testimonial_form.is_valid():
            form = testimonial_form.save(commit=False)
            form.author = request.user
            form.product = product
            form.save()
            messages.success(request, "Submitted Successfully")
            return redirect('product_detail', product_id=product.id)
    
    testimonial_form = TestimonialForm()
    
    return render(request, 'submit_testimonial.html', {'form': testimonial_form})
    

def testimonials(request):
    testimonials = Testimonial.objects.all()

    return render(request, 'testimonials.html',

     {'testimonials': testimonials
     }
     )

