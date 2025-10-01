from django.contrib import admin
from .models import CeleryTestModel, Syllabus

# Register your models here.

class CeleryTestModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at')

class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name', 'course_url', 'course_year', 'created_at')




admin.site.register(CeleryTestModel, CeleryTestModelAdmin)
admin.site.register(Syllabus, SyllabusAdmin)

