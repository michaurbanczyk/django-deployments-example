from django.db import models

# Create your models here.


class User(models.Model):

    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    email = models.EmailField()
