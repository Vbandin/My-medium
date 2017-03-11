# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('content', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('PUB', 'Published'), ('DFT', 'Draft')], default='DFT', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
