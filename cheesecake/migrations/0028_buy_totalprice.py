# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheesecake', '0027_auto_20160906_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='Totalprice',
            field=models.CharField(default='', max_length=20),
        ),
    ]
