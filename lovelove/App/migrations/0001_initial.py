# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-04 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('sex', models.IntegerField(default=True)),
                ('email', models.EmailField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('regtime', models.DateTimeField(auto_now_add=True)),
                ('usertype', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='User_villalist',
            fields=[
                ('tid', models.IntegerField(primary_key=True, serialize=False)),
                ('bedroom', models.IntegerField()),
                ('bedroom_photo', models.CharField(default='static/assets/img/icon/bed.png', max_length=500)),
                ('washhouse', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('garage_photo', models.CharField(default='static/assets/img/icon/cars.png', max_length=500)),
                ('bathroom', models.IntegerField()),
                ('bathroom_photo', models.CharField(default='static/assets/img/icon/shawer.png', max_length=500)),
                ('swimming', models.IntegerField()),
                ('lawn', models.IntegerField()),
                ('bikeway', models.IntegerField()),
            ],
            options={
                'db_table': 'user_villalist',
            },
        ),
        migrations.CreateModel(
            name='User_weivilla',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('money', models.IntegerField()),
                ('area', models.IntegerField()),
                ('weivilla_photo', models.CharField(default='static/assets/img/demo/property-1.jpg', max_length=500)),
            ],
            options={
                'db_table': 'user_weivilla',
            },
        ),
    ]
