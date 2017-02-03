# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 11:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_userhangout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhangout',
            name='hangout_id',
        ),
        migrations.RemoveField(
            model_name='userhangout',
            name='user_id',
        ),
        migrations.AddField(
            model_name='hangout',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserHangout',
        ),
    ]