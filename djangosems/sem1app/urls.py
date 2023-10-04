from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_me, name='about'),
    path('orders/', views.orders, name='orders'),
    path('order_by_id/<int:id>/<int:time>/', views.order_by_id, name='order_by_id'),
    path('all_prods/', views.all_prods, name='all_prods'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
