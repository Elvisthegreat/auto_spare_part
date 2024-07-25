from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm
# Create your views here.

def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
            messages.success(request, "Submitted Successfully")
    else:
        form = TestimonialForm()
    return render(request, 'submit_testimonial.html', {'form': form})
    

def testimonials(request):
    testimonials = Testimonial.objects.all()

    for testimonial in testimonials:
        print(testimonial)

    return render(request, 'testimonials.html',

     {'testimonials': testimonials
     }
     )

