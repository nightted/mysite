# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 19:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheesecake', '0009_comment_timepost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Nickname',
        ),
    ]
