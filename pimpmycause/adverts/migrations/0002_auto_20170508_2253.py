# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-08 22:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advert',
            old_name='skill',
            new_name='skills',
        ),
    ]
