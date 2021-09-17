from rest_framework.routers import DefaultRouter

from customer.api.v1.views import CustomerViewSet, OfferViewSet, UserViewSet


router = DefaultRouter()
router.register('users', UserViewSet)
router.register('customers', CustomerViewSet)
router.register('offers', OfferViewSet)

urlpatterns = router.urls
