from django.urls import path
from teacher import views
from teacher.models import Classroom

urlpatterns = [
    path('classrooms/<key>/students/', views.addStudent, name='ManageStudents'),
    path('classrooms/', views.addClassroom, name='AddClassroom'),
]
