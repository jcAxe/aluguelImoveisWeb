# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-27 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0006_auto_20180627_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='bairro',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='cep',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='cidade',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='estado',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='pais',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='rua',
            field=models.CharField(max_length=200),
        ),
    ]
