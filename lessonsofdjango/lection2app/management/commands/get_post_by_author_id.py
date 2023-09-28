from django.core.management.base import BaseCommand
from lection2app.models import Author, Post


class Command(BaseCommand):
    help = 'Get post by author id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author id')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = Author.objects.filter(pk=pk).first()
        if user is not None:
            posts = Post.objects.filter(author=user)
            intro = f'Все посты автора {user.name}:'
            text = ' '.join([post.content for post in posts])
            self.stdout.write(f'{intro}\n{text}')
