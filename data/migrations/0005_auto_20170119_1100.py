# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-19 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20170119_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bird',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='bird',
            name='start_date',
        ),
    ]