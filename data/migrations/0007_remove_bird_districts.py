# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20170324_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bird',
            name='districts',
        ),
    ]