from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    context = {
        'text': 'Hello World!',
    }
    return render(request, 'index.html', context)


def products(request, category):
    if category == "All":
        product = Product.objects.all()
    else:
        a = {
            "Phones": 1,
            "Accessories": 2,
            "Others": 3,
        }
        product = Product.objects.filter(category_name=a[category])
    context = {
        "products": product,
    }
    return render(request, 'products.html', context)


def item(request, item_id):
    product = Product.objects.get(id=item_id)
    return render(request, 'item.html', {'product': product})


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')
