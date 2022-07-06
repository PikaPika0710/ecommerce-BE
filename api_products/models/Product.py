import os

from django.db import models
from dotenv import load_dotenv

from api_base.models import TimeStampedModel
from api_categories.models import Category
from api_products.services import ProductService

load_dotenv()


class Product(TimeStampedModel):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
        db_table = 'product'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/product/{self.id}/'

    def get_image(self):
        if self.image:
            return os.getenv('MEDIA_URI') + self.image.url

    def get_thumbnail(self):
        if self.thumbnail:
            return os.getenv('MEDIA_URI') + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = ProductService.make_thumbnail(self.image)
                self.save()

                return os.getenv('MEDIA_URI') + self.thumbnail.url
            else:
                return ''
