# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='lobby'),
    url(r'^cookie', views.cookie, name='cookie'),
    url(r'^(?P<arena_name>[^/]+)/$', views.cookie, name='arena'),
    url(r'^(?P<arena_name>[^/]+)/(?P<alias>[^/]+)$', views.cookie, name='arena'),
    #(?P<ali>[^/]+)
]
