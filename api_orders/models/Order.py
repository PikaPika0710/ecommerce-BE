# from django.contrib.auth.models import User
from django.db import models

from api_accounts.models import Account
from api_base.models import TimeStampedModel


class Order(TimeStampedModel):
    account = models.ForeignKey(Account, related_name='orders', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)

    class Meta:
        db_table = 'order'
        ordering = ['-created_at', ]

    def __str__(self):
        return str(self.id)
