from django.db import models
from django.db.models import ForeignKey

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание продукта")
    photo = models.ImageField(upload_to="catalog/foto", blank=True, null=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, verbose_name="Категория", null=True, related_name="products"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения", null=True)
    owner = models.ForeignKey(User, verbose_name= "Владелец", help_text= "Укажите владельца продукта", blank= True, null= True, on_delete= models.SET_NULL)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name
