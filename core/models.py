from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django_countries.fields import CountryField


class Sale(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starts = models.DateField(blank=True)
    duration_days = models.IntegerField(validators=(MinValueValidator(limit_value=5),), default=5)
    discount = models.IntegerField(validators=(
        MinValueValidator(limit_value=5),
        MaxValueValidator(limit_value=60)
    ),
        default=5)
    cars_list = models.ManyToManyField('provider.Car')

    class Meta:
        abstract = True


class Location(models.Model):
    car_showroom = models.ForeignKey('car_showroom.CarShowroom', related_name='location', on_delete=models.CASCADE, blank=True, null=True)
    country = CountryField()
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building_number = models.CharField(max_length=10)
    index = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.country.name} - {self.city} - {self.street} - {self.building_number}'
