# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
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
	return render(request, 'arena/mathArena.html', {
		'arena_name_json': mark_safe(json.dumps(arena_name)),
		'alias_json': mark_safe(json.dumps(alias))
	})
