from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from teacher.forms import *
from teacher.models import Account, Student, AccountManager, Classroom
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
import re, string

def student(request):
	question = questionForm(data = request.POST or None)
	if request.method=='POST':
		if question.is_valid():
			print('asdf')
	return render(request, 'studentHome.html', {'question':question})


def teacherLogin(request):
	form = CustomAuthenticationForm(data = request.POST or None)
	studentForm = studentLoginForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			user = authenticate(username=request.POST['username'], password=request.POST['password'])
			login(request, user)
			return redirect('teacher')
		if studentForm.is_valid():
			email = studentForm.cleaned_data.get('teacherEmail')
			firstName = studentForm.cleaned_data.get('firstName')
			lastName = studentForm.cleaned_data.get('lastName')
			studentNumber = studentForm.cleaned_data.get('studentNumber')
			try:
				teacher = Account.objects.get(email=email)
				ownedClasses = Classroom.objects.filter(teacher=teacher)
				toLogin = Student.objects.filter(firstName = firstName, lastName = lastName, studentNumber = studentNumber, classroom__in = ownedClasses)
				pattern = re.compile('[\W_]+')
				request.session['studentKey'] = toLogin[0].key
				request.session['name'] = pattern.sub('', toLogin[0].getName())
				request.session['classroom'] = pattern.sub('', toLogin[0].classroom.key)
				return redirect('student')
			except:
				print("except")
	return render(request, 'registration/login.html',{'form':form, 'studentForm':studentForm})

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
		return redirect('teacher')
	return render(request, 'registration/signup.html', {'form':form})

@login_required
def deleteClassroom(request, key):
	teacher = Account.objects.get(email=request.user.email)
	classroom = Classroom.objects.get(key=key)
	ownedClasses = Classroom.objects.filter(teacher=teacher)
	if classroom in ownedClasses:
		classroom = Classroom.objects.get(key=key).delete()
	return redirect('teacher')

@login_required
def deleteStudent(request, key):
	teacher = Account.objects.get(email=request.user.email)
	student = Student.objects.get(key=key)
	ownedClasses = Classroom.objects.filter(teacher=teacher)
	classroom = student.classroom
	if classroom in ownedClasses:
		student = Student.objects.get(key=key).delete()
	return redirect('room', key=classroom.key)

@login_required
def teacherHome(request):
	form = addClassroomForm(request.POST)
	classes=request.user.classroom_set.all()
	if form.is_valid():
		name = form.cleaned_data.get('name')
		classroom = Classroom.create(name = name, user = request.user.email)
		return redirect('teacher')
	return render(request, 'teacherHome.html', {'classes':classes, 'form':form})

@login_required
def addStudents(request, key):
	classroom = get_object_or_404(Classroom, key=key)
	form = addStudentsForm(request.POST or None)
	students=Student.objects.filter(classroom=classroom)
	student=classroom.student_set.all()
	if form.is_valid():
		firstName = form.cleaned_data.get('firstName')
		lastName = form.cleaned_data.get('lastName')
		studentNumber = form.cleaned_data.get('studentNumber')
		Student.create(classroom=classroom, firstName=firstName, lastName=lastName, studentNumber=studentNumber)
		return redirect('room', key=key)
	return render(request, 'room.html', {'students':students,'form':form})
