# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-19 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_auto_20161219_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
    ]
