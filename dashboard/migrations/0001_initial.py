# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-10 14:43
from __future__ import unicode_literals

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=27)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(default=dashboard.models.Message.convertTimezone)),
            ],
        ),
    ]
