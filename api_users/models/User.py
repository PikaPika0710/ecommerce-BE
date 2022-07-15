from django.contrib.auth.models import UserManager
from django.db import models

from api_accounts.models import Account
from api_base.models import TimeStampedModel


class User(TimeStampedModel):
    objects = UserManager()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10)
    career = models.CharField(max_length=100, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = "user"
        ordering = ('created_at',)

    def __str__(self):
        return self.name
