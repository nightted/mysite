# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-03 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheesecake', '0034_auto_20161003_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='VisitorTime',
        ),
    ]
