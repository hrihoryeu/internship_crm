from internship_crm.celery import app

from .models import Offer, Customer
from car_showroom.models import CarShowroomCar, CarShowroom, CarShowroomSale


@app.task
def customer_buy_car_showroom():
    offers = Offer.objects.filter(is_active=True)
    for offer in offers:
        cars = CarShowroomCar.objects.filter(car=offer.car,
                                             value__gt=0)
        print(cars)
        try:
            price = cars[0].price
            where_to_buy_id = cars[0].id
            for car in cars:
                sale = CarShowroomSale.objects.get(car_showroom=car.car_showroom.id,
                                                   is_active=True,
                                                   cars_list__in=(offer.car.id,))
                new_price = car.price * (1 - (sale.discount / 100))
                if new_price < price:
                    price = new_price
                    where_to_buy_id = car.id
            user = Customer.objects.get(id=offer.customer.id)
            print(price)
            if user.balance >= price:
                where_to_buy = CarShowroomCar.objects.get(id=where_to_buy_id)
                showroom = CarShowroom.objects.get(id=where_to_buy.car_showroom.id)
                showroom.balance += price
                showroom.save()
                where_to_buy.value -= 1
                where_to_buy.save()
                user.balance -= price
                user.save()
                offer.is_active = False
                offer.save()
        except IndexError:
            print('no instance found(')
