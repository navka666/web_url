# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls_short', '0007_auto_20171214_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url_max',
            field=models.URLField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='url_short',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
