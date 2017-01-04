# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreementGen', '0003_auto_20160130_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='one_month_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plan',
            name='one_week_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plan',
            name='one_year_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plan',
            name='three_month_price',
            field=models.IntegerField(default=0),
        ),
    ]
