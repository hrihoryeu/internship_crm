from django_filters import rest_framework as filters

from provider.models import (
    Car,
    Provider,
    ProviderCar,
)


class CarFilter(filters.FilterSet):
    class Meta:
        model = Car
        fields = ('title', 'model')


class ProviderFilter(filters.FilterSet):
    class Meta:
        model = Provider
        fields = ('title', 'establishment')


class ProviderCarFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = ProviderCar
        fields = ('provider', 'car', 'price')
