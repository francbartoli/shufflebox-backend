# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170228_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brownbag',
            old_name='user_id',
            new_name='user',
        ),
    ]