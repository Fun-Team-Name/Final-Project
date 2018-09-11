from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
def sort_view(request):
    if request.GET.get('sort-btn'):
        return render_to_response(request, 'teacherHome.html', {})
#from django.template.response import TemplateResponse

# def my_render_callback(response):
#     # Do content-sensitive processing
#     do_post_processing()
#
# def teacher_view(request):
#     # Create a response
#     response = TemplateResponse(request, 'teacherHome.html', {})
#     # Register the callback
#     response.add_post_render_callback(my_render_callback)
#     template = 'teacherHome.html'
#     # Return the response
#     return response
# Create your views here.
#def home_view(request, *args, **kwargs):
def home_view(request):
    return render(request, 'index.html')
# def teacher_view(request):
#     return render(request, 'teacherHome.html')
# def student_view(request):
#     return render(request, 'studentHome.html')
