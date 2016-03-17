from __future__ import unicode_literals
from django.db import models

STANDARD_LENGTH = 20

class Website(models.Model):
    url = models.URLField()
    body = models.TextField()
    average_view_time = models.IntegerField(default=0)
    categories = models.ManyToManyField('Category')
    users_visited = models.ManyToManyField('Profile')


class Category(models.Model):
    name = models.CharField(max_length=STANDARD_LENGTH)
    websites = models.ManyToManyField('Website')


class Profile(models.Model):
    username = models.CharField(max_length=STANDARD_LENGTH)
    email = models.CharField(max_length=STANDARD_LENGTH)
    websites = models.ManyToManyField('Website')
    most_viewed_site = models.ForeignKey('Website',related_name='Profile.most_viewed_site+' ,on_delete=models.CASCADE)


class Rec(models.Model):
    answered = models.BooleanField()
    url = models.ForeignKey('Website', related_name='Rec.url+' ,on_delete=models.CASCADE)
    rec1 = models.ForeignKey('Website', related_name='Rec.rec1+' ,on_delete=models.CASCADE)
    rec2 = models.ForeignKey('Website', related_name='Rec.rec2+' ,on_delete=models.CASCADE)
    rec3 = models.ForeignKey('Website', related_name='Rec.rec3+' ,on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)






