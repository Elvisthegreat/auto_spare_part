from django.shortcuts import render

# Create your views here.
def about(request):
    """Render about page"""
    return render(request, 'about/about.html')


def faq(request):
    """Render about page"""
    return render(request, 'about/faq.html')
