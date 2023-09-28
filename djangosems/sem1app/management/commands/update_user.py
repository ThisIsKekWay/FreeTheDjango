from django.core.management.base import BaseCommand
from sem1app.models import Client


class Command(BaseCommand):
    help = 'Update user data'
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')
        parser.add_argument('--new_name', type=str, help='New user name')
        parser.add_argument('--new_email', type=str, help='New user email')
        parser.add_argument('--new_address', type=str, help='New user address')
        parser.add_argument('--new_phone', type=str, help='New user phone number')
        
    def handle(self, *args, **options):
        user = Client.objects.get(pk=options['pk'])
        if user is not None:
            if options['new_name'] is not None:
                user.name = options['new_name']
            if options['new_email'] is not None:
                user.email = options['new_email']
            if options['new_address'] is not None:
                user.address = options['new_address']
            if options['new_phone'] is not None:
                user.phone_num = options['new_phone']
            user.save()
    