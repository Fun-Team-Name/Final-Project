from django.urls import path

urlpatterns = [
    path('classroom/<pk>/adduser/', views.teacherAddUser, name='TeacherAddUser'),
]
