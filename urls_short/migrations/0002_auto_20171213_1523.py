# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls_short', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='date_of_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='url_short',
            field=models.URLField(unique=True, default='domain.com/OT5V3G'),
        ),
    ]
