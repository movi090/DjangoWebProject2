# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-16 14:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211116_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 11, 16, 17, 7, 48, 410882), verbose_name='Опубликовано'),
        ),
    ]
