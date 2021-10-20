from internship_crm.celery import app

from .models import CarShowroom, CarShowroomCar
from provider.models import Car, ProviderCar, ProviderSale


@app.task
def car_showroom_buy_provider():
    for car_showroom in CarShowroom.objects.all():
        if car_showroom.specs.get('where_to_buy') is not None:
            specs = specs['where_to_buy']
            for car_id, provider_id in specs.items():
                provider_car = ProviderCar.objects.get(car_id=int(car_id),
                                                       provider_id=provider_id)
                if car_showroom.balance >= provider_car.price:
                    try:
                        car_showroom_car = CarShowroomCar.objects.get(car_showroom=car_showroom,
                                                                      car=provider_car.car)
                        car_showroom_car.value += 1
                        car_showroom_car.save()
                    except CarShowroomCar.DoesNotExist:
                        CarShowroomCar.objects.create(car_showroom=car_showroom,
                                                      car=provider_car.car,
                                                      price=provider_car.price * 1.1,
                                                      value=1)
                    car_price = provider_car.price
                    try:
                        provider_sale = ProviderSale.objects.get(cars_list=int(car_id),
                                                                 provider=provider_id,
                                                                 is_active=True)
                        car_price = car_price * (1 - (provider_sale.discount / 100))
                    except ProviderSale.DoesNotExist:
                        print('sale does not exists(')
                    car_showroom.balance -= car_price
                    car_showroom.save()
                else:
                    print('not enough money, bitch!')


@app.task
def where_provider():
    for car_showroom in CarShowroom.objects.all():
        if car_showroom.specs.get('list') is not None:
            car_specs = specs['list']
            specs_list = sorted(car_specs, key=lambda k: k['sold_amount'])[::-1]
            needed_cars = []
            for specs in specs_list:
                needed_cars.append(Car.objects.get(title=specs['title'],
                                                   model=specs['model']))
            cars_json = {}
            for needed_car in needed_cars:
                cars_provider = ProviderCar.objects.filter(car=needed_car.id)
                price = cars_provider[0].price
                for car_provider in cars_provider:
                    provider_sales = ProviderSale.objects.filter(provider=car_provider.provider, is_active=True)
                    car_price = car_provider.price
                    for provider_sale in provider_sales:
                        try:
                            provider_sale.cars_list.get(id=needed_car.id)
                            car_price = car_provider.price * (1 - (provider_sale.discount / 100))
                        except Car.DoesNotExist:
                            print('no sales for that car and provider(')
                    print(f'car - {Car.objects.get(id=needed_car.id)}, price - {car_price}')
                    if car_price <= price:
                        cars_json.update({str(needed_car.id): car_provider.provider.id})  # needed_car id заменить на car_provider.car.id
                    price = car_price
            print(cars_json)
            car_showroom.specs['where_to_buy'] = cars_json
            car_showroom.save()
