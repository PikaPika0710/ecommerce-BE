from rest_framework import routers

from api_orders.views import OrderViewSet

api_name = 'api_orders'
router = routers.SimpleRouter(trailing_slash=True)
router.register(r'', OrderViewSet, basename='order')
urlpatterns = router.urls