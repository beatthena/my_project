# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-06 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_user_tuijian'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_tuijian',
            name='money',
            field=models.IntegerField(null=True),
        ),
    ]
