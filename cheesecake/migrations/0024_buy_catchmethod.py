# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheesecake', '0023_auto_20160829_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='Catchmethod',
            field=models.CharField(default='', max_length=50),
        ),
    ]
