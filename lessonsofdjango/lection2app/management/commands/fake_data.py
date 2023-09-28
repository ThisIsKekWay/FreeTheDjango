from django.core.management.base import BaseCommand
from lection2app.models import Author, Post


class Command(BaseCommand):
    help = 'Create N fake data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User count')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            author = Author(name=f'author{i}', email=f'author{i}@gmail.com')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'title{j}',
                    content=f'content{j}',
                    author=author
                )
                post.save()
