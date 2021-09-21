from internship_crm.celery import app

from .models import Car


@app.task
def create_car():
    Car.objects.create(title='Car', model='Model')


@app.task
def create_beat_car():
    Car.objects.create(title='Car', model='Model')