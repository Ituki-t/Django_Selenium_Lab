from django.shortcuts import render
from .models import Syllabus


# Create your views here.


def course_list(request):
    courses = Syllabus.objects.all()
    
    context = {
        'courses': courses
    }
    
    return render(request, 'scraper/course_list.html', context)
