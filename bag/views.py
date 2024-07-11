from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ Render bag content page """
    return render(request, 'bag/bag.html')
