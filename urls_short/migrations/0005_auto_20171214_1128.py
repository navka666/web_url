# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls_short', '0004_auto_20171214_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url_max',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='url_short',
            field=models.TextField(null=True),
        ),
    ]
