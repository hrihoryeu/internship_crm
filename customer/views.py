from .models import Customer, Offer
from .serializers import CustomerSerializer, OfferSerializer
from core.views import AbstractView


class CustomerView(AbstractView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OfferView(AbstractView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
