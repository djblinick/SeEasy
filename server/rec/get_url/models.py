from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Website(models.Model):
    url = models.URLField()
    body = models.TextField()
    view_count = models.IntegerField(default=0, blank=True)
    average_view_time = models.FloatField(default=0, blank=True)

