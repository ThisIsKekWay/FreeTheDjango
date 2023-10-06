from django.shortcuts import render
from django.db.models import Sum

from lection5app.models import Product


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Total in DB',
        'total': total
    }
    return render(request, 'lection6app/total.html', context)


def total_in_view(request):
    prods = Product.objects.all()
    total = sum(prod.quantity for prod in prods)
    context = {
        'title': 'Total in Views',
        'total': total
    }
    return render(request, 'lection6app/total.html', context)


def total_in_template(request):
    context = {
        'title': 'Total in Template',
        'products': Product
    }
    return render(request, 'lection6app/total.html', context)
