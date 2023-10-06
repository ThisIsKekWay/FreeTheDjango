from django.urls import path
from . import views

urlpatterns = [
    path('db/', views.total_in_db, name='db'),
    path('view/', views.total_in_view, name='view'),
    path('template/', views.total_in_template, name='templates'),
]