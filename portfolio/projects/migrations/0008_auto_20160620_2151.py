# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20160620_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, max_length=50),
        ),
    ]