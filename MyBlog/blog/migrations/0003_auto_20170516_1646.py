# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170516_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='mod_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
