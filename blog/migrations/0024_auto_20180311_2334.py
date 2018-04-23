# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-11 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_myplan_confirmacao_do_plano'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myplan',
            old_name='name',
            new_name='Nome_da_Empresa',
        ),
        migrations.RenameField(
            model_name='myplan',
            old_name='socios',
            new_name='Nome_do_socio',
        ),
        migrations.RenameField(
            model_name='myplan',
            old_name='mail',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='myplan',
            name='reason',
        ),
        migrations.AddField(
            model_name='myplan',
            name='Contrato_Social',
            field=models.FileField(blank=True, help_text='Faça o upload do seu contrato social', null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='myplan',
            name='motivo',
            field=models.TextField(default='Amigo', help_text='Resumidamente diga como nos conheceu?', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myplan',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default='2018-11-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myplan',
            name='cpf',
            field=models.CharField(help_text='Qual o CPF do principal socio, preencha com pontos e traço', max_length=14),
        ),
    ]