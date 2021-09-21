from .serializers import CustomerSerializer, OfferSerializer, UserSerializer
from .permissions import ReadOnly

from customer.models import (
    Customer,
    Offer,
    User,
)
from .services import (
    CustomerFilter,
    OfferFilter,
)

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin


class UserViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CustomerFilter

    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OfferViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OfferFilter

    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
