"""rec_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rec_app import views
from django.conf.urls import url, include
import similar
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'website', views.WebsiteViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'rec', views.RecViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^website/$', views.WebsiteViewSet.get_all_web),
    #url(r'^website/(?P<pk>[0-9]+)/$', views.WebsiteViewSet.add_web),
    url(r'^admin/', admin.site.urls),
    url(r'^similar/', include('similar.urls')),
]

#urlpatterns = format_suffix_patterns(urlpatterns)