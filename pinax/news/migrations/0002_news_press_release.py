# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-22 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='press_release',
            field=models.BooleanField(default=False),
        ),
    ]
