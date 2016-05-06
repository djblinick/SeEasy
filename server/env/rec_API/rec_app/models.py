from __future__ import unicode_literals
from django.db import models

STANDARD_LENGTH = 20

class Website(models.Model):
    url = models.URLField()
    body = models.TextField()
    view_count = models.IntegerField(default=0, blank=True)
    average_view_time = models.IntegerField(default=0, blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    users_visited = models.ManyToManyField('Profile', blank=True)


class Category(models.Model):
    name = models.CharField(max_length=STANDARD_LENGTH)
    websites = models.ManyToManyField('Website', blank=True)


class Profile(models.Model):
    username = models.CharField(max_length=STANDARD_LENGTH)
    email = models.CharField(max_length=STANDARD_LENGTH)
    websites = models.ManyToManyField('Website', blank=True)
    most_viewed_site = models.ForeignKey('Website',related_name='Profile.most_viewed_site+' ,on_delete=models.CASCADE, blank=True)


class Rec(models.Model):
    answered = models.BooleanField(default=False)
    url = models.ForeignKey('Website', related_name='Rec.url+' ,on_delete=models.CASCADE, blank=True)
    rec1 = models.ForeignKey('Website', related_name='Rec.rec1+' ,on_delete=models.CASCADE, blank=True)
    rec2 = models.ForeignKey('Website', related_name='Rec.rec2+' ,on_delete=models.CASCADE, blank=True)
    rec3 = models.ForeignKey('Website', related_name='Rec.rec3+' ,on_delete=models.CASCADE, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)






