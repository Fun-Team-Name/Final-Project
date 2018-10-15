from django.urls import path
from teacher import views
from teacher.models import Classroom

urlpatterns = [
    path('classrooms/<key>/students/', views.addStudents, name='badroom'),
    path('classrooms/', views.teacherHome, name='badteacher'),
]
