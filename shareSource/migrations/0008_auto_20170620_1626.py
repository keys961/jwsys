# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareSource', '0007_auto_20170620_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment_store',
            name='file_name',
            field=models.CharField(max_length=15),
        ),
    ]
