# chat/views.py
from django.utils.safestring import mark_safe
from teacher.forms import questionForm
from teacher.models import Student
from django.shortcuts import render, redirect
import json

def index(request):
    return render(request, 'arena/index.html', {})

def cookie(request, arena_name, alias):
    # check if alias taken

    return render(request, 'arena/cookie.html', {
        'arena_name_json': mark_safe(json.dumps(arena_name)),
        'alias_json': mark_safe(json.dumps(alias))
    })


def arena(request, arena_name, alias):
	question = questionForm(data = request.POST or None)
	try:
		alias = request.session['name']
	except:
		print('UNAUTHORIZED: doing nothing')
	if request.method == 'POST':
		if question.is_valid():
			correct = question.cleaned_data.get('correct')
			questions = question.cleaned_data.get('questions')
			key = request.session['studentKey']
			student = Student.objects.get(key=key)
			student.numberTotal=student.numberTotal+questions
			student.numberCorrect=student.numberCorrect+correct
			student.save()
		return redirect('student')
	return render(request, 'arena/mathArena.html', {
		'arena_name_json': mark_safe(json.dumps(arena_name)),
		'alias_json': mark_safe(json.dumps(alias)),
		'question': question
	})
