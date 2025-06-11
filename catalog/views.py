from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


def contacts(request):
    return render(request, "catalog/contacts.html")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})  # Передаем пользователя в форму
        return kwargs

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

    def test_func(self):
        obj = self.get_object()
        return self.request.user.has_perm("catalog.can_delete_any_product") or obj.owner == self.request.user

    def handle_no_permission(self):
        raise PermissionDenied("У вас нет права удалять продукт.")


class UnpublishProductView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ["publication"]
    template_name_suffix = "_unpublish"

    def test_func(self):
        obj = self.get_object()
        return self.request.user.has_perm("catalog.can_unpublish_product") or obj.owner == self.request.user

    def handle_no_permission(self):
        raise PermissionDenied("У вас нет права отменять публикацию продукта.")

    def form_valid(self, form):
        form.instance.publication = False
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})
