from django.db import models
from django.db.models import Max


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=100)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Name: {self.name},'
                f'e-mail: {self.email},'
                f'address: {self.address}, '
                f'phone number: {self.phone_num}, '
                f'registration date: {self.reg_date}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f'Name: {self.name},'
                f'description: {self.description}, '
                f'price: {self.price},'
                f'quantity: {self.quantity},'
                f'updated: {self.updated}')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField()

    def __str__(self):
        return (f'Client: {self.client},'
                f'product: {self.product},'
                f'total price: {self.total_price},'
                f'order date: {self.order_date}')
