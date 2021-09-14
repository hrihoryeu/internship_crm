from .serializers import (
    CarSerializer,
    ProviderSerializer,
    ProviderCarSerializer,
    ProviderSaleSerializer,
)
from .permissons import IsAdminOrViewOnly

from provider.models import (
    Car,
    Provider,
    ProviderCar,
    ProviderSale,
)
from core.views import AbstractViewSet


class CarViewSet(AbstractViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ProviderViewSet(AbstractViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderCarViewSet(AbstractViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = ProviderCar.objects.all()
    serializer_class = ProviderCarSerializer


class ProviderSaleViewSet(AbstractViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = ProviderSale.objects.all()
    serializer_class = ProviderSaleSerializer
