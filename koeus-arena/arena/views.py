# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'arena/index.html', {})

def arena(request, arena_name):
    return render(request, 'arena/arena.html', {
        'arena_name_json': mark_safe(json.dumps(arena_name))
    })
