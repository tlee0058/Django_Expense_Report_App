# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-09 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_auto_20180409_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
