# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-11 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_myplan_tamanho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myplan',
            name='reason',
            field=models.TextField(help_text='Qual o principal motivo de voce utilizar nossos serviços?', max_length=100),
        ),
    ]