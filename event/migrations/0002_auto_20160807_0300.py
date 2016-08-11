# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-07 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='created_date',
            new_name='event_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='post_date',
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
