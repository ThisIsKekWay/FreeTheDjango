from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return f'Username: {self.name}, e-mail: {self.email}, age: {self.age}'
