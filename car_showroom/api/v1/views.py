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
from core.views import AbstractViewSet


class CarShowroomViewSet(AbstractViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer


class CarShowroomCarViewSet(AbstractViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = CarShowroomCar.objects.all()
    serializer_class = CarShowroomCarSerializer


class CarShowroomSaleViewSet(AbstractViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = CarShowroomSale.objects.all()
    serializer_class = CarShowroomSaleSerializer


class CarShowroomCustomerViewSet(AbstractViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = CarShowroomCustomer.objects.all()
    serializer_class = CarShowroomCustomerSerializer
