# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-26 02:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211125_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 11, 26, 5, 12, 22, 282787), verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 11, 26, 5, 12, 22, 283787), verbose_name='Дата'),
        ),
    ]
