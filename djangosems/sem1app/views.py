from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Привет, это главная страница</h1> "
                        "<h2>Инфу обо мне можно найти по маршруту /about</h2>")


def about_me(request):
    return HttpResponse("<h1>Привет, это страница обо мне</h1>"
                        "<h2>Меня зовут Костя</h2>"
                        "<h3>На данный момент пытаюсь ковырять джангу, найти ментора и катаю контесты на стажировки</h3>")