from django.contrib.auth.hashers import check_password
from django.db import transaction
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api_accounts.constants import RoleData
from api_accounts.models import Account
from api_accounts.serializers import AccountSerializer
from api_accounts.services import AccountService
from api_base.views import MyBaseViewSet
from api_users.serializers import UserSerializer


class AccountViewSet(MyBaseViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    serializer_map = {}
    permission_map = {}

    # def get_queryset(self):
    # username = self.request.query_params.get('username')
    # print(username)
    @action(methods=['post'], detail=False)
    @transaction.atomic
    def sign_up(self, request):
        user_data = request.data
        is_existed = Account.objects.filter(username=user_data.get('username'))
        if is_existed:
            return Response({"Message": "Username already exists"}, status=status.HTTP_403_FORBIDDEN)
        # account = self.serializer_class(data=data)
        # if account.is_valid(raise_exception=True):
        #     account['user_id'] = RoleData.USER.value.get('id')
        #     account.save()
        user_data["role"] = RoleData.USER.value.get("id")
        account_serializer = AccountSerializer(data=user_data)
        if account_serializer.is_valid(raise_exception=True):
            account = account_serializer.save()
            user_data['account'] = account.id.hex
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        # account = Account(username=data.get('username'), password=make_password(data.get('password')),
        #                   role_id=RoleData.USER.value.get('id'))
        # account.save()
        # return Response(self.serializer_class(account).data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False)
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        account = Account.objects.filter(username=username)
        if account.exists():
            account = account.first()
            if not account.is_activate:
                return Response({"Message": "Account has been deactivated!"}, status=status.HTTP_400_BAD_REQUEST)
            if check_password(password, account.password):
                # return Response(self.serializer_class(account).data, status=status.HTTP_200_OK)
                token = RefreshToken.for_user(account)
                response = {
                    'access_token': str(token.access_token),
                    'refreshToken': str(token),
                    'user_id': AccountService.get_user_id(account)
                }
                return Response(response, status=status.HTTP_200_OK)
        return Response({"Message": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)
