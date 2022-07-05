from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_base.views import MyBaseViewSet
from api_products.models import Product
from api_products.serializers import ProductSerializer


class ProductViewSet(MyBaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
    permission_map = {

    }
    serializer_map = {

    }

    @action(methods=['post', 'get'], detail=False)
    def search(self, request):
        query = request.data.get('query', '')
        if query:
            products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            if products.exists():
                return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)
            else:
                return Response({"products": []})
