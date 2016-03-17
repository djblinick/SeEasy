from rest_framework import serializers
from models import *



class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Website
        fields = ('url', 'body', 'categories')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'websites')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'websites', 'most_viewed_site')


class RecSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rec
        fields = ('answered','url', 'rec1', 'rec2', 'rec3', 'added', 'updated')








