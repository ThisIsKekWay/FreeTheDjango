import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm, ImageForm
from .models import User

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'User {name} with email {email} is {age} years old.')
    else:
        form = UserForm()
    return render(request, 'lection4app/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            pass
            logger.info(f'Получили данные: {form.cleaned_data}')
    else:
        form = ManyFieldsForm()
    return render(request, 'lection4app/many_fields.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Got an error, repeat filling the form again'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'User {name} with email {email} is {age} years old.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Success'
    else:
        form = UserForm()
        message = 'You need to fill this form to proceed'
    return render(request, 'lection4app/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            logger.info(f'Got image: {image}')
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'lection4app/upload_image.html', {'form': form})
