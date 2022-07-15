from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from api_accounts.models import Account
from api_accounts.serializers.Role import RoleSerializer


class AccountSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = Account
        fields = ['username', 'role']

    def save(self, **kwargs):
        validated_data = self.validated_data
        password = make_password(validated_data['password'])
        validated_data['password'] = password
        return super(AccountSerializer, self).save(**kwargs)
