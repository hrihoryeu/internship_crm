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

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin


class CarViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ProviderViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderCarViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = ProviderCar.objects.all()
    serializer_class = ProviderCarSerializer


class ProviderSaleViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = ProviderSale.objects.all()
    serializer_class = ProviderSaleSerializer