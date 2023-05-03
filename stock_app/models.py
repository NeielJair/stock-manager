from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    dni = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name