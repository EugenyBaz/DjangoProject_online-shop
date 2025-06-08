from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product


def contacts(request):
    return render(request, "catalog/contacts.html")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy(
            "catalog:product_detail",
            kwargs={
                "pk": self.object.pk,
            },
        )


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")
