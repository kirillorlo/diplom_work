from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Adds an order to the database'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int)
        parser.add_argument('product_ids', nargs='+', type=int)
        parser.add_argument('total_amount', type=float)

    def handle(self, *args, **options):
        client_id = options['client_id']
        product_ids = options['product_ids']
        total_amount = options['total_amount']

        try:
            client = Client.objects.get(pk=client_id)
            products = Product.objects.filter(pk__in=product_ids)

            order = Order(client=client, total_amount=total_amount)
            order.save()
            order.products.set(products)

            self.stdout.write(self.style.SUCCESS('Order added successfully'))
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR('Client not found'))
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR('Product not found'))
