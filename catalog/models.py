from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'Наименование продукта')
    description = models.TextField(verbose_name= 'Описание продукта')
    photo = models.ImageField(upload_to='catalog/foto', blank=True, null=True)
    category = models.ForeignKey("Category", on_delete= models.SET_NULL, verbose_name='Категория', null=True, related_name='products')
    price = models.IntegerField(verbose_name= 'Цена за покупку')
    created_at = models.DateTimeField(verbose_name= 'Дата создания')
    updated_at = models.DateTimeField(verbose_name= 'Дата последнего изменения')

    class Meta():
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории')

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name
