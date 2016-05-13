from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Website(models.Model):
    url = models.CharField(max_length=50,primary_key=True)
    body = models.TextField(null=True, blank=True)
    view_count = models.IntegerField(default=0, blank=True)
    average_view_time = models.FloatField(default=0, blank=True)
    category =  models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
    	return self.url