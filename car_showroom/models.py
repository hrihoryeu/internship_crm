from django.db import models
from django.core.validators import MinValueValidator

from core.models import (
    Sale,
    IsActive
)


class CarShowroom(models.Model):
    title = models.CharField(max_length=30)
    specs = models.JSONField()
    car_list = models.ManyToManyField('provider.Car', through='CarShowroomCar')
    customers_list = models.ManyToManyField('customer.Customer', through='CarShowroomCustomer')
    balance = models.IntegerField(validators=(
        MinValueValidator(limit_value=0),
    ))
    unique_customers = models.JSONField()

    def __str__(self):
        return self.title


class CarShowroomSale(Sale, IsActive):
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)
    cars_list = models.ManyToManyField('provider.Car', related_name='cs_sale_car')


class CarShowroomCar(models.Model):
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)
    car = models.ForeignKey('provider.Car', on_delete=models.CASCADE)
    price = models.IntegerField(validators=(
        MinValueValidator(limit_value=0),
    ), default=0)
    value = models.IntegerField(validators=(
        MinValueValidator(limit_value=0),
    ), default=0)


class CarShowroomCustomer(models.Model):
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    bought = models.IntegerField(default=0)
