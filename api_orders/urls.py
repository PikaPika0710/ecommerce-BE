from rest_framework import routers

from api_orders.views import OrderViewSet

api_name = 'api_orders'
router = routers.SimpleRouter(trailing_slash=True)
router.register(r'', OrderViewSet, basename='order')
urlpatterns = router.urls

# from django.urls import path
#
# from api_orders import views
#
# urlpatterns = [
#     path('checkout/', views.checkout),
#     path('your_order/', views.your_order),
# ]