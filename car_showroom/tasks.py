from internship_crm.celery import app

from .models import CarShowroom


@app.task
def car_showroom_buy_provider():
    for car_showroom in CarShowroom.objects.all():
        specs = car_showroom.specs
        try:
            specs = specs['list']
            for spec in specs:
                pass
        except KeyError:
            print('no specs')
