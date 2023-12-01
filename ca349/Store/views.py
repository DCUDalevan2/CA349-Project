from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    context = {
        'text': 'Hello World!',
    }
    return render(request, 'index.html', context)

def products(request, catagory):
    a = {
        "Phones": 1,
        "Accessories": 2,
        "Others": 3,
    }
    product = Product.objects.filter(category_name=a[catagory])
    print(product)
    context = {
        "products": product,
    }
    return render(request, 'products.html', context)
