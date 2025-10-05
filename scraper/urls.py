from django.urls import path
from . import views

app_name = 'scraper'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('list_all/', views.course_list_all, name='course_list_all'),
    path('collect/', views.collect_courses, name='collect_courses'),
]