# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingDatum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=256, blank=True)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256, blank=True), size=None)),
            ],
        ),
    ]
