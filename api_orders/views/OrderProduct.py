from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api_base.views import MyBaseViewSet
from api_orders.models import OrderItem
from api_orders.serializers import OrderItemSerializer


class OrderItemViewSet(MyBaseViewSet):
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderItemSerializer
    serializer_map = {

    }
    permission_map = {

    }
