# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20170325_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='type_of_location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
