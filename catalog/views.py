from django.shortcuts import render
from catalog.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def contacts(request):
    return render(request, "contacts.html")

def product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)

