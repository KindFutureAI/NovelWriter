from .models import UserInfo
from rest_framework import serializers


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('username', 'password')