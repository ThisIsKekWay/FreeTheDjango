from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_me, name='about'),
    path('orders/', views.orders, name='orders'),
    path('order_by_id/<int:id>/<int:time>/', views.order_by_id, name='order_by_id'),
]