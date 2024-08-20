from django.core.management.base import BaseCommand
from myapp.models import Order


class Command(BaseCommand):
    help = 'Deletes an order from the database'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int)

    def handle(self, *args, **options):
        order_id = options['order_id']

        try:
            order = Order.objects.get(pk=order_id)
            order.delete()

            self.stdout.write(self.style.SUCCESS('Order deleted successfully'))
        except Order.DoesNotExist:
            self.stdout.write(self.style.WARNING('Order not found'))
