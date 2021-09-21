from rest_framework.routers import DefaultRouter

from .views import (
    CarShowroomViewSet,
    CarShowroomCarViewSet,
    CarShowroomSaleViewSet,
    CarShowroomCustomerViewSet,
)


router = DefaultRouter()
router.register('car-showrooms', CarShowroomViewSet)
router.register('car-showroom-cars', CarShowroomCarViewSet)
router.register('car-showroom-sales', CarShowroomSaleViewSet)
router.register('car-showroom-customers', CarShowroomCustomerViewSet)

urlpatterns = router.urls
