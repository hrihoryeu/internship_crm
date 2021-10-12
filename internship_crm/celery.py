from celery import Celery
from celery.schedules import crontab


app = Celery('internship_crm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'buy_cars_cs': {
        'task': 'car_showroom.tasks.car_showroom_buy_provider',
        'schedule': crontab(minute='*/10'),
    },
    'choose_provider': {
        'task': 'car_showroom.tasks.where_provider',
        'schedule': crontab(minute='*/5'),
    },
    'check_if_sale': {
        'task': 'core.tasks.sale_is_active',
        'schedule': crontab(),
    },
    'buy_cars_cu': {
        'task': 'customer.tasks.customer_buy_car_showroom',
        'schedule': crontab(minute='*/5'),
    },
}
