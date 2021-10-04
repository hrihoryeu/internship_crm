from celery import Celery
from celery.schedules import crontab


app = Celery('internship_crm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'print_specs_of_car_showrooms': {
        'task': 'car_showroom.tasks.car_showroom_buy_provider',
        'schedule': crontab(minute='*/5'),
    },
}
