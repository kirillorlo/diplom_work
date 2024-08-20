from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = 'Deletes a product from the database'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int)

    def handle(self, *args, **options):
        product_id = options['product_id']

        try:
            product = Product.objects.get(pk=product_id)
            product.delete()

            self.stdout.write(self.style.SUCCESS('Product deleted successfully'))
        except Product.DoesNotExist:
            self.stdout.write(self.style.WARNING('Product not found'))
