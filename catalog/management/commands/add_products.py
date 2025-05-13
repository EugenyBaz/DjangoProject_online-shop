from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Add test product to the database "

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()


        category,_ = Category.objects.get_or_create(name = "Категория 1")

        products = [
            {"name": "отвертка ", "description": "крестовая отвертка профиль PH2", "category":category, "price": 500 },
            {"name": "ключ комбинированный ", "description": "ключ рожково-накидной 13", "category":category, "price": 800},
            {"name": "плоскогубцы ", "description": "плоскогубцы длина 200мм", "category":category, "price": 1500 }

        ]

        for products_data in products:
            product, created = Product.objects.get_or_create(**products_data)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully add product:{product.name} {product.price}'))

            else:
                self.stdout.write(self.style.WARNING(f'Product already exists:{product.name} {product.price}'))

