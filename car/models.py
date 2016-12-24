from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField()


    def __str__(self):
        return "%s" %self.name
