# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-21 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('canal', models.CharField(max_length=255)),
                ('valor', models.CharField(max_length=100)),
                ('obs', models.TextField()),
            ],
        ),
    ]
