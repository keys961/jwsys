# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0009_auto_20170621_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='pdnum',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='xznum',
        ),
    ]