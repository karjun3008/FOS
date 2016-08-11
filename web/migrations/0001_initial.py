# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-01 05:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('descr', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etitle', models.CharField(max_length=250)),
                ('short_descr', models.TextField(max_length=500)),
                ('event_image', models.TextField(max_length=200)),
                ('event_date', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=100)),
                ('descr', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('short_descr', models.TextField(max_length=500)),
                ('post_image', models.TextField(max_length=200)),
                ('post_date', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='pdetail',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Post'),
        ),
        migrations.AddField(
            model_name='edetail',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Event'),
        ),
    ]
