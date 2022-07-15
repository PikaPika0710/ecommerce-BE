from rest_framework import routers

from api_users.views import UserViewSet

app_name = 'api_user'
router = routers.SimpleRouter(trailing_slash=True)

router.register(r'', UserViewSet, basename='user')
urlpatterns = router.urls
