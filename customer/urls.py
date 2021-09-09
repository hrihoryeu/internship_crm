from rest_framework.routers import DefaultRouter

from .views import (
    CustomerView,
    OfferView
)


router = DefaultRouter()
router.register('customers', CustomerView)
router.register('offers', OfferView)

urlpatterns = router.urls
