from provider.models import (
    Car,
    Provider,
    ProviderCar,
    ProviderSale,
)
from .serializers import (
    CarSerializer,
    ProviderSerializer,
    ProviderCarSerializer,
    ProviderSaleSerializer,
)
from core.views import AbstractViewSet


class CarViewSet(AbstractViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ProviderViewSet(AbstractViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderCarViewSet(AbstractViewSet):
    queryset = ProviderCar.objects.all()
    serializer_class = ProviderCarSerializer


class ProviderSaleViewSet(AbstractViewSet):
    queryset = ProviderSale.objects.all()
    serializer_class = ProviderSaleSerializer
