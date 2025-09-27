"""
このファイルは tasks.pyのサンプルです。
利用する際は tasks.py にリネームしてください。
this file is a sample of tasks.py.
When you use it, please rename it to tasks.py.
"""

from celery import shared_task

# Create your tasks here

@shared_task
def store_result_test(text):
    from .models import CeleryTestModel
    instance = CeleryTestModel.objects.create(text=text)
    return f"Created CeleryTestModel instance with id: {instance.id}"

@shared_task
def add(x, y):
    return x + y