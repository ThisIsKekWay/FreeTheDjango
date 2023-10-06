from random import  choice, randint, uniform

from django.core.management.base import BaseCommand
from lection5app.models import Product, Category


class Command(BaseCommand):
    help = 'Генератор продуктов'

    def add_arguments(self, parser):
        parser.add_argument(
            'count', type=int, help='Количество продуктов для генерации'
        )

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(
                Product(
                    name=f'Продукт номер {i}',
                    price=uniform(0.01, 999999.99),
                    description=f'Описание продукта под номером {i}',
                    category=choice(categories),
                    quantity=randint(1, 10_000),
                    rating=uniform(0.01, 9.99),
                )
            )
        Product.objects.bulk_create(products)

