# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-19 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaTest', '0008_auto_20161219_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(upload_to=b''),
        ),
    ]
