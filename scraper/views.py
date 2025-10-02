from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Syllabus
from .tasks import collect_syllabus_to_db_task


# Create your views here.


def course_list(request):
    courses = Syllabus.objects.all()

    query = request.GET.get('search_query')
    if ' ' in query:
        querys = query.split(' ') # ['query1', 'query2', ...]
        # for で filter を繰り返すと AND 検索になる
        for q in querys:
            courses = courses.filter(
                Q(course_name__icontains=q) |
                Q(course_department__icontains=q)
            )
    elif query:
        courses = courses.filter(
            Q(course_name__icontains=query) |
            Q(course_department__icontains=query)
        )

    context = {
        'courses': courses
    }

    return render(request, 'scraper/course_list.html', context)


def collect_courses():
    collect_syllabus_to_db_task.delay()
    return redirect('scraper:course_list')