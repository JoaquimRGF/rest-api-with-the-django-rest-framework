# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-03 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Updates',
            new_name='Update',
        ),
    ]
