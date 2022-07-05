from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from api_accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password']

    def save(self, **kwargs):
        validated_data = self.validated_data
        password = make_password(validated_data['password'])
        validated_data['password'] = password
        return super(AccountSerializer, self).save(**kwargs)
