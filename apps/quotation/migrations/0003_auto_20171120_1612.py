# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 00:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0002_auto_20171120_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='content',
            new_name='quote',
        ),
    ]