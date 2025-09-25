from celery import shared_task

# Create your tasks here


@shared_task
def add(x, y):
    return x + y


# @shared_task
# def scrape_syllabus_task():
#     print("Scraping Syllabus")
#     return "Scraping Syllabus Completed"