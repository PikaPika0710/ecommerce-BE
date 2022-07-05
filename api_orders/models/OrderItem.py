from django.db import models

from api_base.models import TimeStampedModel
from api_orders.models import Order
from api_products.models import Product


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        db_table = 'order_product'
        ordering = ['-created_at', ]
