# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-22 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0029_candidate_has_won'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='candidates_can_commit_everywhere',
            field=models.BooleanField(default=True, help_text='Los candidatos en esta elecci\xf3n pueden comprometerse en todas las elecciones'),
        ),
    ]