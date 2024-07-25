from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def submit_testimonial(request):
    if request.method == 'POST':
        testimonial_form = TestimonialForm(data=request.POST)
        if testimonial_form.is_valid():
            form = testimonial_form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('testimonials')
            messages.success(request, "Submitted Successfully")
    
    # Reset to blank after testimonial is submitted
    testimonial_form = TestimonialForm()
    return render(request, 'submit_testimonial.html',
     {'form': form,
      'testimonial_form': testimonial_form,
     }
     )
    

def testimonials(request):
    testimonials = Testimonial.objects.all()

    return render(request, 'testimonials.html',

     {'testimonials': testimonials
     }
     )

