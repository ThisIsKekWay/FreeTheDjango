from django.urls import path
from .views import user_form, many_fields_form, add_user, upload_image

urlpatterns = [
    path('user/add/', add_user, name='user_form'),
    path('fields/', many_fields_form, name='many_fields_form'),
    path('image/', upload_image, name='upload_image'),
]