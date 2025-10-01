from django.shortcuts import render, redirect
from .models import Syllabus
from .tasks import collect_syllabus_to_db_task


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


def collect_courses(request):
    collect_syllabus_to_db_task.delay()
    return redirect('scraper:course_list')