from rest_framework import serializers

from api_orders.models import Order, OrderItem
from api_orders.serializers.OrderProduct import MyOrderItemSerializer, OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'zipcode', 'place', 'phone', 'stripe_token',
                  'items']

    def create(self, validated_data):
        item_datas = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in item_datas:
            OrderItem.objects.create(order=order, **item_data)
        return order


class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'zipcode', 'place', 'phone', 'stripe_token',
                  'items', 'paid_amount']
