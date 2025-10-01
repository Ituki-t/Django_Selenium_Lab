from django.urls import path
from . import views

app_name = 'scraper'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('collect/', views.collect_courses, name='collect_courses'),
]