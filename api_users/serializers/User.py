from rest_framework import serializers

from api_accounts.serializers import AccountSerializer
from api_users.models import User


class UserSerializer(serializers.ModelSerializer):
    # account = AccountSerializer()

    class Meta:
        model = User
        fields = ['name', 'phone', 'birthday', 'email', 'gender', 'career', 'account']

    def update(self, instance, validated_data):
        return super(UserSerializer, self).update(instance, validated_data)

