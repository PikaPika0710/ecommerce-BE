from rest_framework import routers

from api_categories.views import CategoryViewSet

api_name = 'api_categories'
router = routers.SimpleRouter(trailing_slash=True)
router.register(r'', CategoryViewSet, basename='categories')
urlpatterns = router.urls
