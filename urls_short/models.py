from django.db import models

class URL(models.Model):
    url_max = models.URLField(max_length=80, null=True)
    click = models.PositiveIntegerField(default=0)
    url_short = models.CharField(blank=True, max_length=30, unique=True, null=True)
    date_of_create = models.DateTimeField(auto_now_add=True)