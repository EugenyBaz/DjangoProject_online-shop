from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Load fixtures product to the database "

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'category_fixture.json')
        self.stdout.write(self.style.SUCCESS(f'Successfully load category_fixture.json'))

        call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS(f'Successfully load product_fixture.json'))





