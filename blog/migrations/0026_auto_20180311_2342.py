# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-11 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20180311_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myplan',
            name='confirmacao_do_plano',
            field=models.CharField(choices=[('STARTUP', 'startup, apenas R$ 19,90 mensais!'), ('Business', 'business, Apenas R$ 199,00 mensais!'), ('Corporate', 'Corporate, Um preço especial, uma super oferta no seu e-mail em instantes!')], max_length=10),
        ),
    ]