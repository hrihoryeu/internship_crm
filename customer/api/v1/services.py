from django_filters import rest_framework as filters

from customer.models import (
    Customer,
    Offer
)


class CustomerFilter(filters.FilterSet):
    balance = filters.RangeFilter()
    class Meta:
        model = Customer
        fields = ('balance',)


class OfferFilter(filters.FilterSet):
    max_price = filters.RangeFilter()
    class Meta:
        model = Offer
        fields = ('customer', 'car')
