from django.shortcuts import render

from django.http import HttpResponse

from .models import Website

from django.core import serializers

import logging

import random

logger = logging.getLogger('django')

# Create your views here.
def index(request):
	logger.debug('index')
	return HttpResponse("SeEasy Django Index")

def api(request,url):
    logger.debug('***** url: ' + str(url))
    method = 'blank'
    json_data = 'null'
    if request.method == 'POST':
        method = 'post'
        post_to_database(url)
    elif request.method == 'GET':
        json_data = get_recommented_urls(url)
    return HttpResponse(json_data)

def similar(request, category):
    top = Website.objects.filter(category=category).order_by('-view_count')
    urls = []
    #vcount = []
    for web in top:
        urls.append(web.url)
        #vcount.append(web.view_count)

    return HttpResponse(str(urls[0:3]))


def get_recommented_urls(url):
    json_data = 'null'
    try:
        url_entry = Website.objects.get(pk=url)
        logger.debug('******* category: ' + str(url_entry.category) + '*******')
        top3_urls_in_category_list = Website.objects.filter(category=url_entry.category).order_by('-view_count')[0:3]
        json_data = serializers.serialize("json", top3_urls_in_category_list, fields = ('url','category'))
        logger.debug('*******  top 3 category: ' + str(json_data) + '*********')
    except Website.DoesNotExist:
        logger.debug('******** url does not exist in database ********')
        category = get_category()
        w = Website(url = url, view_count = 1, category=category)
        logger.debug('********* website: ' + str(w)+ 'added to database')
        w.save()
    return json_data

def post_to_database(url):
    logger.debug('post')

#TODO add function that returns the proper category
def get_category():
	sites = ['news', 'social', 'cs']
	return (random.choice(sites))

	 