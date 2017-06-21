# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 16:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('onlinetest', '0003_auto_20170614_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=100)),
                ('room_number', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('credits', models.IntegerField()),
                ('week_hour', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('method', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('building', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.IntegerField()),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinetest.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('event', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinetest.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('difficulty', models.CharField(choices=[('e', 'Easy'), ('m', 'Middle'), ('h', 'Hard')], max_length=1)),
                ('status', models.CharField(choices=[('o', 'open'), ('c', 'closed'), ('u', 'using')], max_length=1)),
                ('limit_time', models.IntegerField()),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinetest.Course')),
                ('instru_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinetest.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_type', models.CharField(choices=[('xz', 'C'), ('pd', 'P')], max_length=2)),
                ('title', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=400)),
                ('difficulty', models.CharField(choices=[('e', 'Easy'), ('m', 'Middle'), ('h', 'Hard')], max_length=1)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinetest.Course')),
                ('instru_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinetest.Instructor')),
                ('paper', models.ManyToManyField(to='onlinetest.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=1)),
                ('mark', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinetest.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_time', models.DateTimeField(auto_now=True)),
                ('tot_mark', models.IntegerField()),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinetest.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('tot_cred', models.IntegerField(default=0)),
                ('matriculate', models.IntegerField()),
                ('graduate', models.IntegerField(null=True)),
                ('gender', models.IntegerField()),
                ('major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinetest.Major')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinetest.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinetest.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Test_point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='timeslot',
            unique_together=set([('day', 'start_time', 'end_time')]),
        ),
        migrations.AddField(
            model_name='sheet',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinetest.Student'),
        ),
        migrations.AddField(
            model_name='reply',
            name='sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinetest.Sheet'),
        ),
        migrations.AddField(
            model_name='question',
            name='test_point',
            field=models.ManyToManyField(to='onlinetest.Test_point'),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinetest.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='precourse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinetest.Course'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='equipment',
            field=models.ManyToManyField(to='onlinetest.Equipment'),
        ),
        migrations.AlterUniqueTogether(
            name='classroom',
            unique_together=set([('building', 'room_number')]),
        ),
    ]