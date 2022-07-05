from django.contrib import admin

from api_orders.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)