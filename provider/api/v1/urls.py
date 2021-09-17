from rest_framework.routers import DefaultRouter

from .views import (
    CarViewSet,
    ProviderViewSet,
    ProviderCarViewSet,
    ProviderSaleViewSet,
)


router = DefaultRouter()
router.register('cars', CarViewSet)
router.register('providers', ProviderViewSet)
router.register('provider-cars', ProviderCarViewSet)
router.register('provider-sales', ProviderSaleViewSet)

urlpatterns = router.urls
