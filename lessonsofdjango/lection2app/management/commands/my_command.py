from django.core.management.base import BaseCommand
from lection2app.models import User

class Command(BaseCommand):
    help = 'Напишет Привет мир в консольку'

    def handle(self, *args, **kwargs):
        user = User(name='Neo', email='Neo@bk.ru', password='12345', age=22)
        user.save()
        self.stdout.write(f'{user}')
