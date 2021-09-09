from rest_framework.routers import DefaultRouter

from .views import (
    CarView,
    ProviderView,
    ProviderCarView,
    ProviderSaleView,
)


router = DefaultRouter()
router.register('cars', CarView)
router.register('provider', ProviderView)
router.register('provider-car', ProviderCarView)
router.register('provider-sale', ProviderSaleView)

urlpatterns = router.urls
