# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0002_auto_20160528_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='slug',
            field=models.SlugField(default=None, max_length=100, unique=True),
        ),
    ]
