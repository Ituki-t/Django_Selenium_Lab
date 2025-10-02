from celery import shared_task
import os

# スクレイピング関連のインポート
from .models import Syllabus
from scraper.scraping.collect_syllabus import collect_years_url, collect_department_url, collect_lectures, record_dedup
from .utils import make_selenium_driver

from pprint import pprint # debug

# Create your tasks here

@shared_task
def store_result_test(text):
    from .models import CeleryTestModel
    instance = CeleryTestModel.objects.create(text=text)
    return f"Created CeleryTestModel instance with id: {instance.id}"

@shared_task
def add(x, y):
    return x + y


@shared_task()
def collect_syllabus_to_db_task():
    # 既存のデータを削除してから情報取得
    # 後でget_or_createに変更するかも
    Syllabus.objects.all().delete()


    driver = make_selenium_driver()

    try:
        base_url = os.getenv("SYLLABUS_URL")
        # base_url = url # debug
        years_url = collect_years_url(driver, base_url)
        department_url = collect_department_url(driver, years_url)
        syllabus_records = collect_lectures(driver, department_url)
        syllabus_records = record_dedup(syllabus_records)
        # print(syllabus_records)
        for record in syllabus_records:
            Syllabus.objects.create(
                course_name=record['lecture'],
                course_url=record['url'],
                course_year=record['year'],
                course_department=record['department']
            )

    finally:
        if driver:
            driver.quit()

