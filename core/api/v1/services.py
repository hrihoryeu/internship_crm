from django_filters import rest_framework as filters

from core.models import Sale


class SaleFilter(filters.FilterSet):
    title = filters.CharFilter()
    starts = filters.DateFilter()
    discount = filters.RangeFilter()
