from django.db import models

from .Role import Role
from api_base.models import TimeStampedModel


class Account(TimeStampedModel):
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = 'account'
        ordering = ('-created_at',)

    def __str__(self):
        return self.username
