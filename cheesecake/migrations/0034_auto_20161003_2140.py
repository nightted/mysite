# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-03 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheesecake', '0033_auto_20160927_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitortime',
            name='number',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='visitortime',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
    ]
