# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-29 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0048_auto_20180328_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting',
            name='credit',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='accounting',
            name='debit',
            field=models.CharField(max_length=30),
        ),
    ]