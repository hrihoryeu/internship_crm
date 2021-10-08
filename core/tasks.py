from internship_crm.celery import app

from provider.models import ProviderSale

import datetime


@app.task
def sale_is_active():
    sales = ProviderSale.objects.all()
    for sale in sales:
        year = sale.starts.year
        month = sale.starts.month
        day = sale.starts.day
        time_start = datetime.datetime(year=year, month=month, day=day)
        duration = datetime.timedelta(days=sale.duration_days)
        time_finish = time_start + duration
        time_now = datetime.datetime.now()
        if time_now < time_start:
            sale.is_active = False
            print('is active field of sale set to False')
        elif time_finish - time_now > datetime.timedelta(days=0):
            sale.is_active = True
            print('is active field of sale set to True')
        else:
            sale.is_active = False
            print('is active field of sale set to False')
        sale.save()
