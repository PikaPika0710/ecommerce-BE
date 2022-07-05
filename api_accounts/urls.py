from rest_framework import routers

from api_accounts.views.Account import AccountViewSet

api_name = 'api_accounts'
router = routers.SimpleRouter(trailing_slash=True)
router.register(r'', AccountViewSet, basename='account')

urlpatterns = router.urls
