# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-19 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20170119_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='districts',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]