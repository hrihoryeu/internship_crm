from django_filters import rest_framework as filters

from car_showroom.models import (
    CarShowroom,
    CarShowroomCustomer,
    CarShowroomCar,
    CarShowroomSale,
)

from core.api.v1.services import SaleFilter


class CarShowroomFilter(filters.FilterSet):
    title = filters.CharFilter()
    balance = filters.RangeFilter()

    class Meta:
        model = CarShowroom
        fields = ('title', 'balance',)


class CarShowroomCarFilter(filters.FilterSet):
    class Meta:
        model = CarShowroomCar
        fields = ('car', 'car_showroom')


class CarShowroomCustomerFilter(filters.FilterSet):
    class Meta:
        model = CarShowroomCustomer
        fields = ('customer', 'car_showroom')
