from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):
  name = models.CharField(max_length=10)
  league = models.CharField(max_length=20)

  def __str__(self):
       return self.name
