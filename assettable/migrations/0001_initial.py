# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='criteria',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_code', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='criteria_iba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.criteria')),
            ],
        ),
        migrations.CreateModel(
            name='district',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='district_iba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.district')),
            ],
        ),
        migrations.CreateModel(
            name='family',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='habitat',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
                ('habitat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='habitat_iba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.habitat')),
            ],
        ),
        migrations.CreateModel(
            name='iba',
            fields=[
                ('iba_id', models.AutoField(primary_key=True, serialize=False)),
                ('iba_code', models.CharField(max_length=50)),
                ('site_name', models.CharField(max_length=50)),
                ('area', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='iba_status',
            fields=[
                ('is_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='redlist',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='specie',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('sprec_id', models.CharField(max_length=10)),
                ('sci_name', models.CharField(max_length=100)),
                ('com_name', models.CharField(max_length=100)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.family')),
                ('redlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.redlist')),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('st_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('capital', models.CharField(max_length=50)),
                ('area', models.IntegerField()),
                ('forest_area', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='iba',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.state'),
        ),
        migrations.AddField(
            model_name='iba',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.iba_status'),
        ),
        migrations.AddField(
            model_name='habitat_iba',
            name='iba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.iba'),
        ),
        migrations.AddField(
            model_name='district_iba',
            name='iba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.iba'),
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.state'),
        ),
        migrations.AddField(
            model_name='criteria_iba',
            name='iba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assettable.iba'),
        ),
    ]