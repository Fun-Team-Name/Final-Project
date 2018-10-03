from django.urls import path
from teacher import views
from teacher.models import Classroom

urlpatterns = [
    path('teacher/<classroom:key>/students/', views.addStudent, name='ManageStudents'),
    path('teacher/classrooms/', views.addClassroom, name='AddClassroom'),

]
