import uuid

from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    objects = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_activate = models.BooleanField(default=True)

    class Meta:
        abstract = True
