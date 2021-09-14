from car_showroom.models import (
    CarShowroom,
    CarShowroomCar,
    CarShowroomSale,
    CarShowroomCustomer,
)
from .serializers import (
    CarShowroomSerializer,
    CarShowroomCarSerializer,
    CarShowroomSaleSerializer,
    CarShowroomCustomerSerializer,
)
from core.views import AbstractViewSet


class CarShowroomViewSet(AbstractViewSet):
    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer


class CarShowroomCarViewSet(AbstractViewSet):
    queryset = CarShowroomCar.objects.all()
    serializer_class = CarShowroomCarSerializer


class CarShowroomSaleViewSet(AbstractViewSet):
    queryset = CarShowroomSale.objects.all()
    serializer_class = CarShowroomSaleSerializer


class CarShowroomCustomerViewSet(AbstractViewSet):
    queryset = CarShowroomCustomer.objects.all()
    serializer_class = CarShowroomCustomerSerializer
