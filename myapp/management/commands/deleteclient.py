from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = 'Deletes a client from the database'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int)

    def handle(self, *args, **options):
        client_id = options['client_id']

        try:
            client = Client.objects.get(pk=client_id)
            client.delete()

            self.stdout.write(self.style.SUCCESS('Client deleted successfully'))
        except Client.DoesNotExist:
            self.stdout.write(self.style.WARNING('Client not found'))
