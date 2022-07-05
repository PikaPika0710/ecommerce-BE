from django.db import models

from api_base.models import TimeStampedModel


# Create your models here.
class Category(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        db_table = 'category'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category/{self.id}/'
