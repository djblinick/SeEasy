from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /rec/
    url(r'^$', views.index, name='index'),
    # ex: /rec/api/www.facebook.com
    url(r'^api/(?P<url>.+)/$', views.api),
    # ex: /rec/news/sim
    #url(r'^(?P<category>\w+)/$', views.similar, name='sim'),
    
    ]
