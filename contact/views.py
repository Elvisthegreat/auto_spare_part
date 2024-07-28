from django.shortcuts import render, redirect
from .forms import ContactRequestForm

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactRequestForm()
    return render(request, 'contact/contact.html', {'form': form})

def success_view(request):
    return render(request, 'contact/success.html')
