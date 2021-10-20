from internship_crm.celery import app

from provider.models import ProviderSale
from car_showroom.models import CarShowroomSale

import datetime
from itertools import chain


@app.task
def sale_is_active():
    """
    celery task to check if the sale is active... or not
    """
    sales = list(chain(ProviderSale.objects.all(), CarShowroomSale.objects.all()))
    for sale in sales:
        time_start = datetime.datetime(
            year=sale.starts.year,
            month=sale.starts.month,
            day=sale.starts.day
        )
        duration = datetime.timedelta(days=sale.duration_days)
        time_finish = time_start + duration
        time_now = datetime.datetime.now()
        sale.is_active = True if time_start <= time_now < time_finish else False
        sale.save()
