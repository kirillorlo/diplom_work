from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = 'Adds a product to the database'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('quantity', type=int)

    def handle(self, *args, **options):
        name = options['name']
        description = options['description']
        price = options['price']
        quantity = options['quantity']

        product = Product(name=name, description=description, price=price, quantity=quantity)
        product.save()

        self.stdout.write(self.style.SUCCESS('Product added successfully'))
