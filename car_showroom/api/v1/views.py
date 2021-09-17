from .serializers import (
    CarShowroomSerializer,
    CarShowroomCarSerializer,
    CarShowroomSaleSerializer,
    CarShowroomCustomerSerializer,
)
from .permissions import ReadOnly

from car_showroom.models import (
    CarShowroom,
    CarShowroomCar,
    CarShowroomSale,
    CarShowroomCustomer,
)

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAdminUser


class CarShowroomViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer


class CarShowroomCarViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = CarShowroomCar.objects.all()
    serializer_class = CarShowroomCarSerializer


class CarShowroomSaleViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = CarShowroomSale.objects.all()
    serializer_class = CarShowroomSaleSerializer


class CarShowroomCustomerViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = CarShowroomCustomer.objects.all()
    serializer_class = CarShowroomCustomerSerializer
