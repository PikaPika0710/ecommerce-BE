from django.db import models

from api_base.models import TimeStampedModel


class Role(TimeStampedModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "role"

    def __str__(self):
        return self.name
