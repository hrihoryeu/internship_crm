from rest_framework.routers import DefaultRouter

from .views import (
    CarShowroomView,
    CarShowroomCarView,
    CarShowroomSaleView,
    CarShowroomCustomerView,
)


router = DefaultRouter()
router.register('car-showrooms', CarShowroomView)
router.register('car-showroom-cars', CarShowroomCarView)
router.register('car-showroom-sales', CarShowroomSaleView)
router.register('car-showroom-customers', CarShowroomCustomerView)

urlpatterns = router.urls
