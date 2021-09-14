from customer.models import Customer, Offer, User
from customer.api.v1.serializers import CustomerSerializer, OfferSerializer, UserSerializer
from core.views import AbstractViewSet

from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(AbstractViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OfferViewSet(AbstractViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
