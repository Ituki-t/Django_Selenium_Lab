from django.db import models

# Create your models here.

class CeleryTestModel(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    class Meta:
        db_table = "celery_test_model" # テーブル名を指定


class Syllabus(models.Model):
    course_name = models.CharField(max_length=100)
    course_url = models.URLField(max_length=200)
    course_year = models.CharField(
        max_length=4,
        default='yet'
        )
    course_department = models.CharField(max_length=100, default='学部不明')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name
    class Meta:
        db_table = "syllabus"
