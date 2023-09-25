from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world. You're at the polls index.")


def about(request):
    try:
        result = 10 / 0
    except Exception as e:
        logger.exception(f"Ошибка на странице about: {e}")
        return HttpResponse("Произошла ошибка")
    else:
        logger.debug("about page accessed")
        return HttpResponse("about")
