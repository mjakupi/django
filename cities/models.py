from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Town(models.Model):
    name = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    citizens = models.IntegerField()

    def __str__(self):
        return self.name