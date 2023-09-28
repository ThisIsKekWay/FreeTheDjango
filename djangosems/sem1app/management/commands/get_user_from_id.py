from django.core.management.base import BaseCommand
from sem1app.models import Client


class Command(BaseCommand):
    help = 'Get user by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User id')

    def handle(self, *args, **options):
        user = Client.objects.get(pk=options['pk'])
        print(user)
