from django.contrib import admin
from .models import CeleryTestModel

# Register your models here.

class CeleryTestModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at')

admin.site.register(CeleryTestModel, CeleryTestModelAdmin)