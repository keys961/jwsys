# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-22 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicInfo', '0014_remove_classroom_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='type',
            field=models.IntegerField(default=1),
        ),
    ]