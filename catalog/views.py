from django.shortcuts import render
from catalog.models import Product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView


# Create your views here.


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product



def contacts(request):
    return render(request, "contacts.html")


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)
