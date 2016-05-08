from django.shortcuts import render
from django.http import HttpResponse
from .models import Website

# Create your views here.
def index(request):
    return HttpResponse("SeEasy Django Index")

def similar(request, category):
    top = Website.objects.filter(category=category).order_by('-view_count')
    urls = []
    #vcount = []
    for web in top:
        urls.append(web.url)
        #vcount.append(web.view_count)

    return HttpResponse(str(urls[0:3]))