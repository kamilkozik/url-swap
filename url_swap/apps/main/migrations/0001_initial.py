# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlSwap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_url', models.URLField(max_length=2048, verbose_name='Url oryginalny')),
                ('proxy_url', models.URLField(db_index=True, max_length=100, verbose_name='Proxy url')),
            ],
        ),
    ]
