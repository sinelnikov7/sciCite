import asyncio

from celery import Celery

from application.usecases.usecase_user import generate_pdf


celery = Celery('server', broker='pyamqp://admin:admin123@localhost:5672//')
celery.autodiscover_tasks(['infrastructure.celery'])


@celery.task
def user_report(user_id):
    asyncio.run(generate_pdf(user_id))

