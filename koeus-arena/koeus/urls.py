"""koeus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url #include,
from django.contrib import admin
from django.urls import path
from django.urls import include
from teacher import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
	path('teacher/', include('django.contrib.auth.urls')),
    path('', views.teacherLogin, name = 'login'),
	path('home/', views.student, name = 'student'),
	path('teacher/', views.leaderBoard, name = 'leader'),
	path('registration/', views.signup, name='signup'),
	path('student/', views.cookie, name = 'cookie'),
	path('teacher/home/', views.room, name = 'room'),

    path('arena/', include('arena.urls')),
]
