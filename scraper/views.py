from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Syllabus
from .tasks import collect_syllabus_to_db_task
from .utils import split_whitespace


# Create your views here.


def course_list(request):
    courses = Syllabus.objects.all()

    query = request.GET.get('search_query')
    if not query:
        # 初回アクセスや空入力は全件（ポリシーに応じて空リストでもOK）
        return render(request, 'scraper/course_list.html', {'courses': courses})

    querys = split_whitespace(query)
    # for で filter を繰り返すと AND 検索になる
    for q in querys:
        courses = courses.filter(
            Q(course_name__icontains=q) |
            Q(course_department__icontains=q)
        )

    context = {
        'courses': courses
    }

    return render(request, 'scraper/course_list.html', context)


def collect_courses():
    collect_syllabus_to_db_task.delay()
    return redirect('scraper:course_list')