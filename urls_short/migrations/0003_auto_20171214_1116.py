# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls_short', '0002_auto_20171213_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url_short',
            field=models.URLField(unique=True),
        ),
    ]
