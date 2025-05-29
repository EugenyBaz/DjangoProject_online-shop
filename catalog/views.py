from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def contacts(request):
    return render(request, "catalog/contacts.html")


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price")

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs = { 'pk': self.object.pk,})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")
