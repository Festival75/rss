# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_news', '0003_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default='2017-07-20'),
        ),
    ]
