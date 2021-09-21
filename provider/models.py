from django.db import models
from django.core.validators import MinValueValidator

from car_showroom.models import CarShowroom
from core.models import Sale


class Car(models.Model):
    title = models.CharField(max_length=30)
    model = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title} {self.model}'


class Provider(models.Model):
    title = models.CharField(max_length=100)
    establishment = models.DateField(auto_created=True)
    car_list = models.ManyToManyField(Car, through='ProviderCar')
    car_showroom_list = models.ManyToManyField(CarShowroom)


class ProviderCar(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.IntegerField(validators=(
        MinValueValidator(limit_value=0),
    ))


class ProviderSale(Sale):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
