from django.core.management.base import BaseCommand
from lection2app.models import User


class Command(BaseCommand):
    help = 'Update user'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User id')
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        name = kwargs['name']
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f'{user}')
