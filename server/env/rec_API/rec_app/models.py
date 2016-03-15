from __future__ import unicode_literals
from django.db import models

URL_LENGTH = 100
CATEGORY_LENGTH = 20

class Website(models.Model):
    url = models.CharField(max_length=URL_LENGTH)
    body = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=CATEGORY_LENGTH)




