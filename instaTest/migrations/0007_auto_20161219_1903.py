# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-19 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaTest', '0006_auto_20161216_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(default='Images/None/No-img.jpg', upload_to='images/'),
        ),
    ]
