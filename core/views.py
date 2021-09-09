from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin


class AbstractViewSet(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = None

    def get_queryset(self):
        return self.queryset

    class Meta:
        abstract = True
