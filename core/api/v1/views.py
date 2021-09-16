from .serializers import LocationSerializer

from core.models import Location

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin


'''class LocationViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAdminOrViewOnly,)
    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer'''