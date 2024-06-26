from django.shortcuts import render

# Create your views here.
def home(request):
    """ A home view page"""
    return render(request, 'home/home.html')
