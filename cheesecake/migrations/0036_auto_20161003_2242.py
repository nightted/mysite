# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-03 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheesecake', '0035_auto_20161003_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='number',
        ),
        migrations.AddField(
            model_name='visitor',
            name='onlinenumber',
            field=models.IntegerField(null=True),
        ),
    ]
