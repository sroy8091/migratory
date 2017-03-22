# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-19 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iba_code', models.CharField(max_length=10, verbose_name='IBA Code')),
                ('species', models.CharField(max_length=30)),
                ('area', models.IntegerField(default=24000, verbose_name='Area in sq.km')),
                ('latitude_from', models.FloatField(blank=True, null=True)),
                ('latitude_to', models.FloatField(blank=True, null=True)),
                ('longitude_from', models.FloatField(blank=True, null=True)),
                ('longitude_to', models.FloatField(blank=True, null=True)),
                ('site_name', models.CharField(blank=True, choices=[('Coringa and Godaveri Estuary', 'Coringa and Godaveri Estuary'), ('Horsely Hills', 'Horsely Hills')], max_length=30, verbose_name='Site Name')),
                ('terrain', models.CharField(blank=True, choices=[('WETLANDS', 'Wetlands'), ('GALLIFORM', 'Galliform'), ('HERONARY', 'Heronary'), ('TERRESTIAL', 'Terrestial')], max_length=15)),
                ('breeding_time', models.PositiveIntegerField(blank=True, verbose_name='Breeding Time(in weeks)')),
                ('block_count', models.IntegerField(verbose_name='Block Count')),
                ('forest_type', models.CharField(blank=True, choices=[('Tropical Wet Evergreen Forest', 'Tropical Wet Evergreen Forest'), ('Tropical Semi-Evergreen Forest', 'Tropical Semi-Evergreen Forest'), ('Tropical Moist Deciduous Forest', 'Tropical Moist Deciduous Forest'), ('Littoral and Swamp Forest', ' Littoral and Swamp Forest'), ('Tropical Dry Deciduous Forest', 'Tropical Dry Deciduous Forest')], max_length=50)),
                ('districts', models.CharField(max_length=20)),
                ('state', models.CharField(choices=[('WEST BENGAL', 'WEST BENGAL'), ('PUNJAB', 'PUNJAB'), ('TAMILNADU', 'TAMIL NADU')], max_length=15)),
            ],
        ),
    ]