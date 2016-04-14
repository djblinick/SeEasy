from django.conf.urls import url
from similar import views

urlpatterns = [
    url(r'^', views.qsimweb),
]
