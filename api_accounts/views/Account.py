from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api_accounts.models import Account
from api_accounts.serializers import AccountSerializer
from api_base.views import MyBaseViewSet


class AccountViewSet(MyBaseViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    serializer_map = {}
    permission_map = {}

    # def get_queryset(self):
    # username = self.request.query_params.get('username')
    # print(username)
    @action(methods=['post'], detail=False)
    def sign_up(self, request):
        username = request.data.get('username')
        is_existed = Account.objects.filter(username=username)
        if is_existed:
            return Response({"Message": "Username already exists"}, status=status.HTTP_403_FORBIDDEN)
        account = self.serializer_class(data=request.data)
        if account.is_valid(raise_exception=True):
            account.save()
        return Response(account.data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False)
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        account = Account.objects.filter(username=username)
        print(username)
        print(password)
        if account.exists():
            account = account.first()
            if not account.is_activate:
                return Response({"Message": "Account has been deactivated!"}, status=status.HTTP_400_BAD_REQUEST)
            if check_password(password, account.password):
                # return Response(self.serializer_class(account).data, status=status.HTTP_200_OK)
                token = RefreshToken.for_user(account)
                response = {
                    'access_token': str(token.access_token),
                    'refreshToken': str(token)
                }
                return Response(response, status=status.HTTP_200_OK)
        return Response({"Message": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)
