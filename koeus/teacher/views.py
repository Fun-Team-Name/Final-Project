from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from teacher.forms import signupForm, addStudentsForm, addClassroomForm
from teacher.models import Account, Student, AccountManager, Classroom
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def teacherHome(request):
	return render(request, 'teacherHome.html', {})

def teacherLogin(request):
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect('teacherHome')
        else:
            form = AuthenticationForm(data = request.POST)
        return render(request, 'registration/login.html',{'form':form})

def signup(request):
	form = signupForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password2')
		firstName = form.cleaned_data.get('firstName')
		lastName = form.cleaned_data.get('lastName')
		form.save()
		user = Account.objects.create_user(email=email, password=password, firstName=firstName, lastName=lastName)
		login(request, user)
		return redirect('login')
	return render(request, 'registration/signup.html', {'form':form})

@login_required
def addClassroom(request):
	form = addClassroomForm(request.POST)
	#classes=request.user.classroom_set.all()
	if form.is_valid():
		name = form.cleaned_data.get('name')
		classroom = Classroom.create(name = name, user = request.user)
		return redirect('ManageStudents', key=classroom.key)
	return render(request, 'classrooms.html', {'form':form}) #, 'classes':classes

@login_required
def addStudent(request, key):
	classroom = get_object_or_404(Classroom, key=key)
	form = addStudentsForm(request.POST or None)
	#students=Student.objects.filter(classroom__contains=request.user)
	student=classroom.student_set.all()
	if form.is_valid():
		firstName = form.cleaned_data.get('firstName')
		lastName = form.cleaned_data.get('lastName')
		studentNumber = form.cleaned_data.get('studentNumber')
		Student.create(classroom=classroom, firstName=firstName, lastName=lastName, studentNumber=studentNumber)
		return redirect('ManageStudents', key=key)
	return render(request, 'ManageStudents.html', {'students':students,'form':form})
