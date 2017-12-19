# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url_max', models.URLField()),
                ('click', models.PositiveIntegerField(default=0)),
                ('url_short', models.URLField(unique=True, max_length=25)),
                ('date_of_create', models.DateTimeField()),
            ],
        ),
    ]
