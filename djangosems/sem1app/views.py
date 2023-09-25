from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.
logger = logging.getLogger(__name__)



def index(request):
    logger.info('Юзверь зашел на главную страницу')
    return HttpResponse("<h1>Привет, это главная страница</h1> "
                        "<h2>Инфу обо мне можно найти по маршруту /about</h2>")


def about_me(request):
    logger.info('Юзверь испытывает любопытство')
    return HttpResponse("<h1>Привет, это страница обо мне</h1>"
                        "<h2>Меня зовут Костя</h2>"
                        "<h3>На данный момент пытаюсь ковырять джангу, найти ментора и катаю контесты на стажировки</h3>")