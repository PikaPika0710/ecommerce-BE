from api_base.views import MyBaseViewSet
from api_categories.models import Category
from api_categories.serializers import CategorySerializer


class CategoryViewSet(MyBaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    serializer_map = {

    }
    permission_map = {

    }
