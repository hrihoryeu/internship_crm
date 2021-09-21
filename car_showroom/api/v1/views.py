from .serializers import (
    CarShowroomSerializer,
    CarShowroomCarSerializer,
    CarShowroomSaleSerializer,
    CarShowroomCustomerSerializer,
)
from .permissions import ReadOnly
from .services import (
    CarShowroomFilter,
    CarShowroomCarFilter,
    CarShowroomCustomerFilter,
)

from car_showroom.models import (
    CarShowroom,
    CarShowroomCar,
    CarShowroomSale,
    CarShowroomCustomer,
)

from core.api.v1.services import SaleFilter

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAdminUser


class CarShowroomViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarShowroomFilter

    permission_classes = [IsAdminUser|ReadOnly]
    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer


class CarShowroomCarViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarShowroomCarFilter

    permission_classes = [IsAdminUser|ReadOnly]
    queryset = CarShowroomCar.objects.all()
    serializer_class = CarShowroomCarSerializer


class CarShowroomSaleViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SaleFilter

    permission_classes = [IsAdminUser|ReadOnly]
    queryset = CarShowroomSale.objects.all()
    serializer_class = CarShowroomSaleSerializer


class CarShowroomCustomerViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarShowroomCustomerFilter

    permission_classes = [IsAdminUser|ReadOnly]
    queryset = CarShowroomCustomer.objects.all()
    serializer_class = CarShowroomCustomerSerializer
