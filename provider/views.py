from .models import Car, Provider, ProviderCar, ProviderSale
from .serializers import CarSerializer, ProviderSerializer, ProviderCarSerializer, ProviderSaleSerializer
from core.views import AbstractView


class CarView(AbstractView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ProviderView(AbstractView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderCarView(AbstractView):
    queryset = ProviderCar.objects.all()
    serializer_class = ProviderCarSerializer


class ProviderSaleView(AbstractView):
    queryset = ProviderSale.objects.all()
    serializer_class = ProviderSaleSerializer
