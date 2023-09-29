from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Author, Post


def hello(request):
    return HttpResponse("Hello, world. It's a function")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world. It's a class")


def year_post(request, year):
    text = 'some text for training'
    return HttpResponse(f"All posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = 'some text for training'
        return HttpResponse(f"All posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    post = {
        'year': year,
        'month': month,
        'slug': slug,
        'title': 'Кто быстрее найдет работу в IT? Ты или гусеница?',
        'content': 'Ответ очевиден. Гусеница кнш, ты то клоун раз на курсы пошел, а гусеница лист хавает и не парится.'
    }

    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def index_view(request):
    context = {'name': 'Koha'}
    return render(request, 'lection3app/index.html', context)


class TemplIf(TemplateView):
    template_name = 'lection3app/if_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = ('Чем сильнее мерзнут ежики, тем сильнее они прижимаются друг к другу, чтобы согреться.'
                              ' Это в свою очередь делает им больно. Until we meet again')
        context['number'] = 1
        return context


def view_for(request):
    my_list = [1, 2, 3, 4]
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'lection3app/for_template.html', context)


def author_post(request, pk):
    author = get_object_or_404(Author, pk=pk)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'lection3app/author_post.html', {'author': author, 'posts': posts})


def post_full(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'lection3app/post_full.html', {'post': post})
