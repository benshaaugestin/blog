# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170828_0911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'News'},
        ),
    ]