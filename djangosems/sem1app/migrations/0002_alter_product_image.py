# Generated by Django 4.2.5 on 2023-10-04 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sem1app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/default.jpg', upload_to='products/'),
        ),
    ]