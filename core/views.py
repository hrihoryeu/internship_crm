from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin


class AbstractViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    pass
