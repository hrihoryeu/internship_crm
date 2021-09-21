import os
from celery import Celery


os.environ.get('DJANGO_SETTINGS_MODULE', 'settings.py')

app = Celery('internship_crm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()