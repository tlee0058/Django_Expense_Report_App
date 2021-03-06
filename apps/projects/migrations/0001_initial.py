# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-09 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('billing_code', models.TextField(blank=True)),
                ('billing_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=100)),
                ('rate_type', models.CharField(max_length=45)),
                ('note', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='companies.Company')),
                ('users', models.ManyToManyField(related_name='staffs', to='login.Userdb')),
            ],
        ),
    ]
