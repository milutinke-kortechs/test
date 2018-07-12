# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-12 09:24
from __future__ import unicode_literals

import annoying.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flflf', '0002_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='profile',
            field=annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='preference', serialize=False, to='flflf.Profile'),
        ),
    ]
