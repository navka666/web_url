# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('urls_short', '0008_auto_20171215_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='url_user', null=True),
        ),
    ]
