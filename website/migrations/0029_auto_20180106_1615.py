# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-01-06 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_goal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='currency',
            new_name='cryptocurrency',
        ),
    ]
