from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter = models.BooleanField(default=True)
    email = models.EmailField(default="", blank=True)
    account = models.FloatField(blank=True, null=True)
