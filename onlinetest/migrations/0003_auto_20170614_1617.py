# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0002_department_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='department',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
    ]