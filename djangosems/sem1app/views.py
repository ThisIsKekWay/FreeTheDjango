import datetime

from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Client, Order, Max, Q

# Create your views here.
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Юзверь зашел на главную страницу')
    return render(request, 'sem1app/index.html')


def about_me(request):
    logger.info('Юзверь испытывает любопытство')
    return render(request, 'sem1app/about.html')


def orders(request):
    """
    Попытка получить последние заказы каждого юзера. Прошлая провалилась, т.к. при одинаковой дате заказов могли
    всплывать лишние значения, когда имя юзера есть в QuerySet в одном кортеже, а дата последнего заказа в другом.

    Идея в том, чтобы взять список юзеров, пройти по id в цикле, и получить заказы с максимальной датой внутри таблицы
    заказов по User_id. Id этих заказов заливаем в список, в итоге получаем итерируемый объект, содержащий числа int,
    который нормально обрабатывается в фильтре orm.

    Решение спорное, т.к. при большом числе юзеров это будет занимать непозволительно много времени, однако оно рабочее.
    """

    users = Client.objects.all()
    last_orders = []
    for user in users:
        last_order = Order.objects.filter(client_id=user.id).order_by('-order_date').first()
        if last_order is not None:
            last_orders.append(last_order.id)

    orders = Order.objects.filter(id__in=last_orders).order_by('-order_date')

    return render(request, 'sem1app/orders.html', {'orders': orders})


def order_by_id(request, id, time):
    last_prods = (Order.objects.
                  filter(client_id=id).
                  values('product_id').
                  annotate(last_order_date=Max('order_date')).
                  order_by('product_id')
                  )

    order = (Order.objects.
             filter(client_id=id,
                    order_date__in=last_prods.values('last_order_date'))
             .all()
             .order_by('-order_date')
             )

    if time != 0:
        order = order.filter(
            order_date__gte=datetime.datetime.now() - datetime.timedelta(days=time),
        ).order_by('-order_date').all()

    user_name = Client.objects.filter(pk=id).first()
    return render(request, 'sem1app/order_by_id.html', {'user_orders': order, 'user_name': user_name})
