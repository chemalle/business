# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-14 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r', models.CharField(help_text='10 characters max.', max_length=10)),
            ],
        ),
    ]