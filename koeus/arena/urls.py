# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<arena_name>[^/]+)/$', views.arena, name='arena'),
]
