# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 12:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicInfo', '0007_auto_20170609_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=1000)),
                ('is_read', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('content', models.CharField(default='', max_length=1000)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basicInfo.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('content', models.CharField(default='', max_length=1000)),
                ('is_top', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('layer_number', models.IntegerField(default=0)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='files/')),
                ('layer', models.IntegerField()),
                ('content', models.CharField(default='', max_length=256)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Post')),
                ('replier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='reply',
            unique_together=set([('post', 'layer')]),
        ),
    ]
