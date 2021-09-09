from rest_framework.routers import DefaultRouter

from .views import (
    CarView,
    ProviderView,
    ProviderCarView,
    ProviderSaleView,
)


router = DefaultRouter()
router.register('cars', CarView)
router.register('providers', ProviderView)
router.register('provider-cars', ProviderCarView)
router.register('provider-sales', ProviderSaleView)

urlpatterns = router.urls
