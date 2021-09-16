from django.db import models
from django.core.validators import MinValueValidator

from django_countries import fields

from core.models import Sale


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


class CarShowroomSale(Sale):
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)


class CarShowroomCar(models.Model):
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)
    car = models.ForeignKey('provider.Car', on_delete=models.CASCADE)
    value = models.IntegerField(default=0)


class CarShowroomCustomer(models.Model):
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    bought = models.IntegerField(default=0)
