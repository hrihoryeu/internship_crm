from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet, OfferViewSet


router = DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('offers', OfferViewSet)

urlpatterns = router.urls
