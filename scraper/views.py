from django.shortcuts import render
from .models import Syllabus


# Create your views here.


def course_list(request):
    courses = Syllabus.objects.all()
    
    query = request.GET.get('course_query')
    if query:
        courses = courses.filter(course_name__icontains=query)
    
    context = {
        'courses': courses
    }
    
    return render(request, 'scraper/course_list.html', context)
