from .serializers import (
    CarSerializer,
    ProviderSerializer,
    ProviderCarSerializer,
    ProviderSaleSerializer,
)
from .permissons import ReadOnly

from provider.models import (
    Car,
    Provider,
    ProviderCar,
    ProviderSale,
)

from core.api.v1.services import SaleFilter

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin


class CarViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ProviderViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderCarViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = ProviderCar.objects.all()
    serializer_class = ProviderCarSerializer


class ProviderSaleViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SaleFilter

    permission_classes = [IsAdminUser|ReadOnly]
    queryset = ProviderSale.objects.all()
    serializer_class = ProviderSaleSerializer
