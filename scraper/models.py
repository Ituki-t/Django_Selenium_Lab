from django.db import models

# Create your models here.

class CeleryTestModel(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    class Meta:
        db_table = "celery_test_model" # テーブル名を指定
