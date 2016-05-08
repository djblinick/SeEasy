from get_url.models import *

def all_web():
    return Website.objects.all()

def create_web_entry(url,body,category):
    web = Website(url,body,category)
    web.save()

def top_in_category(count):
