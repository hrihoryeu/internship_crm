import os
from celery import Celery
from celery.schedules import crontab

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_crm.settings')

app = Celery('internship_crm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'create-object-every-1-min': {
        'task': 'provider.tasks.create_beat_car',
        'schedule': crontab(),
    },
}
