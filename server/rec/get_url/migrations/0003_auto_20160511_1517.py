# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-11 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_url', '0002_auto_20160508_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='id',
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
