from .serializers import CustomerSerializer, OfferSerializer, UserSerializer
from .permissions import IsAdminOrViewOnly

from customer.models import Customer, Offer, User

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin


class UserViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OfferViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
