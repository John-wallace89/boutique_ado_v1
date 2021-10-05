from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view to see products in a bag """
    return render(request, 'bag/bag.html')
