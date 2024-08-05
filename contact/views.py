from django.shortcuts import render, redirect
from django.db import IntegrityError  # Import IntegrityError
from .forms import ContactRequestForm

# Create your views here.


def contact_view(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # Attempt to save the form
                # Redirect to success page if save is successful
                return redirect('success')
            except IntegrityError:
                # Handle the error, e.g., by showing a message to the user
                form.add_error(
                    'email', 'This email address is already in use.')
    else:
        form = ContactRequestForm()
    return render(request, 'contact/contact.html', {'form': form})


def success_view(request):
    return render(request, 'contact/success.html')
