# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 12:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BrownBag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('status', models.CharField(choices=[('next_in_line', 'Next In Line'), ('done', 'Done'), ('not_done', 'Not Done')], default='not_done', max_length=12)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hangout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(blank=True, max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, default='', max_length=500)),
                ('brownbag', models.CharField(choices=[('next_in_line', 'Next In Line'), ('done', 'Done'), ('not_done', 'Not Done')], default='not_done', max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SecretSanta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('giftee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('santa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='santa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
