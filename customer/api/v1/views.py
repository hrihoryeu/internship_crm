from .serializers import CustomerSerializer, OfferSerializer, UserSerializer
from .permissions import IsAdminOrViewOnly

from customer.models import Customer, Offer, User
from core.views import AbstractViewSet

from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(AbstractViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OfferViewSet(AbstractViewSet):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
