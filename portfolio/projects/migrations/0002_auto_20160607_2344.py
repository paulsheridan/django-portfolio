# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 23:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='github_url',
            new_name='github',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_url',
            new_name='url',
        ),
    ]