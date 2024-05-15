from django.shortcuts import render

from catalog.models import Product


# Create your views here.


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_info(request):
    if request.method == "POST":
        product_info = Product.objects.get(id=request.POST.get('product_id'))
    else:
        product_info = Product.objects.get(id=1)

    context = {
        'object_list': product_info
    }
    return render(request, 'catalog/product_info.html', context)


def catalog(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/catalog.html', context)