# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicInfo', '0003_auto_20170604_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prereq',
            name='course',
        ),
        migrations.RemoveField(
            model_name='prereq',
            name='precourse',
        ),
        migrations.RemoveField(
            model_name='teaches',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='teaches',
            name='section',
        ),
        migrations.AddField(
            model_name='course',
            name='precourse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.Course'),
        ),
        migrations.AddField(
            model_name='section',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.Instructor'),
        ),
        migrations.DeleteModel(
            name='Prereq',
        ),
        migrations.DeleteModel(
            name='Teaches',
        ),
    ]
