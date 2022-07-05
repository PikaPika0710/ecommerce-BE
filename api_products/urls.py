from rest_framework import routers

from api_products.views.Product import ProductViewSet

api_name = 'api_products'
router = routers.SimpleRouter(trailing_slash=True)
router.register(r'', ProductViewSet, basename='account')
urlpatterns = router.urls
