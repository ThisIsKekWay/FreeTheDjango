from random import choices

from django.core.management.base import BaseCommand
from lection3app.models import Author, Post

LONG_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et" \
            " dolore magna aliqua. At quis risus sed vulputate odio ut enim blandit volutpat. Proin fermentum leo " \
            "vel orci porta. Vitae elementum curabitur vitae nunc. Pulvinar mattis nunc sed blandit libero volutpat" \
            " sed. Praesent elementum facilisis leo vel fringilla. Faucibus turpis in eu mi bibendum neque egestas" \
            " congue quisque. Nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. Nulla aliquet " \
            "enim tortor at auctor urna nunc id cursus. Id leo in vitae turpis massa sed. In est ante in nibh. " \
            "Eget sit amet tellus cras adipiscing enim eu. Bibendum at varius vel pharetra vel turpis nunc eget " \
            "lorem. Eu turpis egestas pretium aenean pharetra magna ac. Sed elementum tempus egestas sed sed risus " \
            "pretium quam vulputate. Eu tincidunt tortor aliquam nulla facilisi cras. Ipsum dolor sit amet " \
            "consectetur. Elementum integer enim neque volutpat ac tincidunt. Sed adipiscing diam donec adipiscing " \
            "tristique risus nec. Sapien faucibus et molestie ac feugiat."


class Command(BaseCommand):
    help = 'Fills the database with some test data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of posts to create')

    def handle(self, *args, **kwargs):
        text = LONG_TEXT.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author {i}', email=f'author{i}@example.com')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),
                    author=author)
                post.save()
        self.stdout.write(self.style.SUCCESS(f'Created {count} authors and {count ** 2} posts'))
