from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    photo = models.ImageField()

    def __str__(self):
        return self.name + ' ' + self.lname

