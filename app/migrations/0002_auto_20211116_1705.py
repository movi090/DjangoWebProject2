# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-16 14:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 11, 16, 17, 5, 50, 435003), verbose_name='Опубликовано'),
        ),
    ]
