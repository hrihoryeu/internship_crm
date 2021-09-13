from .models import Customer, Offer, User
from .serializers import CustomerSerializer, OfferSerializer, UserSerializer
from core.views import AbstractViewSet


class UserViewSet(AbstractViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(AbstractViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OfferViewSet(AbstractViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
