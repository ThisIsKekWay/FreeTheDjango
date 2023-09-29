from django.urls import path
from .views import (hello, HelloView, year_post, MonthPost, post_detail, index_view, TemplIf, view_for,
                    author_post, post_full)


urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('', index_view, name='index'),
    path('if', TemplIf.as_view(), name='if'),
    path('for', view_for, name='for'),
    path('author/<int:pk>/', author_post, name='author_post'),
    path('post/<int:pk>/', post_full, name='post_full'),


]
