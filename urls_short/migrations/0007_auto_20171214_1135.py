# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls_short', '0006_auto_20171214_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url_short',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
