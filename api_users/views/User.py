from api_base.views import MyBaseViewSet
from api_users.models import User
from api_users.serializers import UserSerializer


class UserViewSet(MyBaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_map = {}
    serializer_map = {}
