from random import choice

from django.core.management.base import BaseCommand
from sem1app.models import Client, Order, Product


class Command(BaseCommand):
    help = 'Generate fake db data'

    def add_arguments(self, parser):
        parser.add_argument('Users_count', type=int, help='How many users you need')
        parser.add_argument('Products_count', type=int, help='How many products you need')
        parser.add_argument('Orders_count', type=int, help='How many orders you need')

    def handle(self, *args, **options):
        users_count = options['Users_count']
        products_count = options['Products_count']
        orders_count = options['Orders_count']
        for i in range(users_count):
            client = Client(
                name=f'User{i}',
                email=f'user{i}@mail.ru',
                address=f'Address{i}',
                phone_num=f'Phone{i}',
            )
            client.save()

        for j in range(1, products_count + 1):
            product = Product(
                name=f'Product{j}',
                description=f'Description{j}',
                price=j,
                quantity=j,
            )
            product.save()

        for k in range(1, orders_count + 1):
            order = Order(
                client=Client.objects.get(pk=choice(Client.objects.all()).id),
                product=Product.objects.get(pk=choice(Product.objects.all()).id),
                total_price=k,
                order_date=k,
            )
            order.save()
