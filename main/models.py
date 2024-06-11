from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=25)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)

class Token(models.Model):
    id = models.CharField(max)
    mintSymbol = models.CharField(max_length=10)
    vsToken = models.CharField(max)
    price = models.DecimalField(max_digits=13,decimal_places=8)


