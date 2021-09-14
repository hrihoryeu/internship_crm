from .serializers import (
    CarShowroomSerializer,
    CarShowroomCarSerializer,
    CarShowroomSaleSerializer,
    CarShowroomCustomerSerializer,
)
from .permissions import IsAdminOrViewOnly

from car_showroom.models import (
    CarShowroom,
    CarShowroomCar,
    CarShowroomSale,
    CarShowroomCustomer,
)

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin


class CarShowroomViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer


class CarShowroomCarViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = CarShowroomCar.objects.all()
    serializer_class = CarShowroomCarSerializer


class CarShowroomSaleViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = CarShowroomSale.objects.all()
    serializer_class = CarShowroomSaleSerializer


class CarShowroomCustomerViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = CarShowroomCustomer.objects.all()
    serializer_class = CarShowroomCustomerSerializer
