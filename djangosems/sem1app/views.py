import datetime

from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Client, Order, Product, Max

# Create your views here.
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Юзверь зашел на главную страницу')
    return render(request, 'sem1app/index.html')


def about_me(request):
    logger.info('Юзверь испытывает любопытство')
    return render(request, 'sem1app/about.html')


def orders(request):
    last_orders = Order.objects.values('client_id').annotate(last_order_date=Max('order_date')).order_by('client_id')

    orders = Order.objects.filter(
        order_date__in=last_orders.values('last_order_date')
    ).order_by('-order_date')

    return render(request, 'sem1app/orders.html', {'orders': orders})


def order_by_id(request, id, time):
    last_prods = (Order.objects.
                  filter(client_id=id).
                  values('product_id').
                  annotate(last_order_date=Max('order_date')).
                  order_by('product_id')
                  ).all()

    order = (Order.objects.
             filter(client_id=id,
                    order_date__in=last_prods.values('last_order_date')).
             all().
             order_by('-order_date')
             )

    if time != 0:
        order = order.filter(
            order_date__gte=datetime.datetime.now() - datetime.timedelta(days=time),
        ).order_by('-order_date').all()

    user_name = Client.objects.filter(pk=id).first()
    return render(request, 'sem1app/order_by_id.html', {'user_orders': order, 'user_name': user_name})
