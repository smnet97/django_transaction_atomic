from django.shortcuts import render
from .models import Product

def home_view(request):
    q = request.GET.get('q')
    products = Product.objects.filter(quantity__gt=0)
    if q:
        products = products.filter(name__icontains=q)

    return render(request, 'home.html', context={'products': products})
