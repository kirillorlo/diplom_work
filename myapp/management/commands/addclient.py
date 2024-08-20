from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = 'Adds a client to the database'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone_number', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **options):
        name = options['name']
        email = options['email']
        phone_number = options['phone_number']
        address = options['address']

        client = Client(name=name, email=email, phone_number=phone_number,
                        address=address)
        client.save()

        self.stdout.write(self.style.SUCCESS('Client added successfully'))
