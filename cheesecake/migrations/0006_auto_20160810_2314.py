# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 23:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheesecake', '0005_auto_20160810_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitortime',
            old_name='Visitor_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='visitortime',
            old_name='count_minutesinterval',
            new_name='time',
        ),
    ]
