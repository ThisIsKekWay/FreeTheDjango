from django.core.management.base import BaseCommand
from sem1app.models import Client


class Command(BaseCommand):
    help = 'Get user list'

    def handle(self, *args, **options):
        users = Client.objects.all()
        for user in users:
            print(user)
