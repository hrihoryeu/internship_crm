from .models import Customer, Offer
from .serializers import CustomerSerializer, OfferSerializer
from core.views import AbstractViewSet


class CustomerViewSet(AbstractViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OfferViewSet(AbstractViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
