from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_accounts.services import AccountService
from api_base.views import MyBaseViewSet
from api_users.models import User
from api_users.serializers import UserSerializer


class UserViewSet(MyBaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_map = {}
    serializer_map = {}

    @action(methods=['get'], detail=False)
    def get_info(self, request):
        http_authorization = str(request.META.get('HTTP_AUTHORIZATION'))
        token = AccountService.get_token(http_authorization)
        account = AccountService.get_account_by_token(token)
        user = User.objects.get(account=account)
        if user:
            return Response(self.serializer_class(user).data, status=status.HTTP_200_OK)
        else:
            return Response({"message: User is not valid!"}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        http_authorization = str(request.META.get('HTTP_AUTHORIZATION'))
        token = AccountService.get_token(http_authorization)
        account = AccountService.get_account_by_token(token)
        instance = self.get_object()
        data = request.data
        data['account'] = account.id
        user = self.serializer_class(instance, data=data)
        if user.is_valid():
            self.perform_update(user)
            return Response(user.data, status=status.HTTP_200_OK)
