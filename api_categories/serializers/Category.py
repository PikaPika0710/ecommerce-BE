from rest_framework import serializers

from api_categories.models import Category
from api_products.serializers import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products"
        )
