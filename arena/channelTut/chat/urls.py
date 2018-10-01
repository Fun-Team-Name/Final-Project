# channelTut/urls.py
from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    #url(r'^chat/', include('chat.urls')),
    #url(r'^admin/', admin.site.urls),
]
