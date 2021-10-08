from celery import Celery
from celery.schedules import crontab


app = Celery('internship_crm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'buy_cars': {
        'task': 'car_showroom.tasks.car_showroom_buy_provider',
        'schedule': crontab(minute='*/2'),
    },
    'choose_provider': {
        'task': 'car_showroom.tasks.where_provider',
        'schedule': crontab(minute='*/3'),
    },
    'check_if_sale': {
        'task': 'core.tasks.sale_is_active',
        'schedule': crontab(),
    }
}
